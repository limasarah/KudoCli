from pathlib import Path  # Para manipulação multiplataforma de caminhos
import os
import re
import requests
from dotenv import load_dotenv
from stravalib.client import Client


class StravaClient:
    # Cliente para autenticação e busca de atividades na API do Strava.
    # Usa pathlib para garantir compatibilidade multiplataforma.

    """Cliente para autenticação e busca de atividades na API do Strava.

    Esta versão tenta renovar o `access_token` automaticamente usando
    `STRAVA_REFRESH_TOKEN` + `STRAVA_CLIENT_ID`/`STRAVA_CLIENT_SECRET`. Se a
    renovação for bem-sucedida, os tokens são persistidos no arquivo `.env`.
    """

    def __init__(self):
        load_dotenv()
        client_id = os.getenv('STRAVA_CLIENT_ID')
        client_secret = os.getenv('STRAVA_CLIENT_SECRET')
        access_token = os.getenv('STRAVA_ACCESS_TOKEN') or os.getenv('ACCESS_TOKEN')
        refresh_token = os.getenv('STRAVA_REFRESH_TOKEN') or os.getenv('REFRESH_TOKEN')

        # Se houver refresh_token e credenciais do client, tente renovar
        if refresh_token and client_id and client_secret:
            try:
                refreshed = self._refresh_token(client_id, client_secret, refresh_token)
                if refreshed:
                    access_token = refreshed.get('access_token', access_token)
                    refresh_token = refreshed.get('refresh_token', refresh_token)
                    # Persistir no .env local (arquivo .env é ignorado pelo git)
                    try:
                        self._update_env({
                            'STRAVA_ACCESS_TOKEN': access_token,
                            'STRAVA_REFRESH_TOKEN': refresh_token
                        })
                    except Exception:
                        # Não falhar a inicialização se não conseguir escrever no .env
                        pass
            except Exception as e:
                print(f"Aviso: falha ao renovar token: {e}")

        if not access_token:
            raise ValueError("STRAVA_ACCESS_TOKEN (ou ACCESS_TOKEN) não encontrado no arquivo .env")

        self.client = Client(access_token=access_token)

    def _refresh_token(self, client_id: str, client_secret: str, refresh_token: str):
        url = 'https://www.strava.com/api/v3/oauth/token'
        resp = requests.post(
            url,
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token,
            },
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json()

    def _update_env(self, updates: dict):
        env_path = str(Path.cwd() / '.env')  # Caminho multiplataforma para o .env
        lines = []
        if os.path.exists(env_path):
            with open(env_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            for key, val in updates.items():
                found = False
                for i, line in enumerate(lines):
                    if line.startswith(f"{key}="):
                        lines[i] = f"{key}={val}\n"
                        found = True
                        break
                if not found:
                    lines.append(f"{key}={val}\n")
            with open(env_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
        else:
            # Cria um .env mínimo
        # Utiliza pathlib para garantir multiplataforma
            with open(env_path, 'w', encoding='utf-8') as f:  # pathlib já garante o caminho correto
                for key, val in updates.items():
                    f.write(f"{key}={val}\n")

    def resolve_athlete_id(self, athlete_ref):
        """Resolve um identificador de atleta em um athlete_id.

        Aceita um ID numérico, uma URL de perfil público (por exemplo,
        https://www.strava.com/athletes/12345) ou um username/slug.
        """
        if athlete_ref is None:
            return None
        if isinstance(athlete_ref, int):
            return athlete_ref

        value = str(athlete_ref).strip()
        if not value:
            return None

        if re.fullmatch(r'\d+', value):
            return int(value)

        if value.startswith('http://') or value.startswith('https://'):
            match = re.search(r'/athletes/(\d+)', value)
            if match:
                return int(match.group(1))
            value = value.rstrip('/').split('/')[-1]

        candidates = []
        slug = value[1:] if value.startswith('@') else value
        if slug:
            candidates.append(f'https://www.strava.com/athletes/{slug}')
            candidates.append(f'https://www.strava.com/{slug}')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/124.0 Safari/537.36'
        }
        for candidate in candidates:
            try:
                response = requests.get(candidate, headers=headers, timeout=15)
                if response.ok:
                    html = response.text
                    match = re.search(r'/athletes/(\d+)', html)
                    if match:
                        return int(match.group(1))
                    match = re.search(r'"id":(\d+)', html)
                    if match:
                        return int(match.group(1))
            except Exception:
                continue
        return None

    def get_public_activity_ids(self, profile_or_url, limit=20):
        """Tenta encontrar IDs de atividades públicas a partir de um perfil público.

        Aceita uma URL de perfil Strava (por exemplo, https://www.strava.com/athletes/12345)
        ou um identificador numérico/slug. A implementação faz uma busca simples no HTML
        da página pública e extrai links do tipo /activities/<id>.
        """
        url = profile_or_url
        if not url.startswith('http'):
            url = f'https://www.strava.com/athletes/{url}'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/124.0 Safari/537.36'
        }
        try:
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            html = response.text
            matches = re.findall(r'/activities/(\d+)', html)
            seen = []
            for activity_id in matches:
                if activity_id not in seen:
                    seen.append(activity_id)
            return seen[:limit]
        except Exception as e:
            print(f"Erro ao ler perfil público: {e}")
            return []

    def get_activities_for_athlete(self, athlete_id, limit=10):
        """Retorna atividades públicas/visíveis de outro atleta pelo athlete_id.

        Este é o endpoint oficial da API Strava para listar atividades de um atleta.
        Se o perfil não é público ou as atividades são privadas, a lista pode vir vazia.
        """
        try:
            raw = self.client.protocol.get(
                '/athletes/{id}/activities',
                id=athlete_id,
                page=1,
                per_page=limit,
            )
            return list(raw)
        except Exception as e:
            print(f"Erro ao buscar atividades de atleta {athlete_id}: {e}")
            return []

    def get_activities(self, limit=10):
        """Retorna as últimas atividades do atleta autenticado."""
        try:
            activities = self.client.get_activities(limit=limit)
            return list(activities)
        except Exception as e:
            print(f"Erro ao buscar atividades: {e}")
            return []

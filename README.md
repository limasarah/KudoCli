# KudoCli

> **Distribuição pronta para GitHub e pip:**
> Instale com `pip install --editable .` e use `kudo [comando]` no terminal.


Ferramenta de linha de comando (CLI) para análise de esforço cardíaco e inspeção básica de atividades do Strava.

## O que faz

- Autentica com a API do Strava usando um token salvo em `.env`.
- Busca atividades do atleta autenticado ou de outro atleta quando você passa um `athlete_id`/URL/slug.
- Analisa métricas de esforço cardíaco (média e máxima) e gera links de mapa quando há coordenadas.
- Exibe a saída em uma tabela formatada com `rich`.

## Requisitos

- Python 3.10+
- Dependências listadas em `requirements.txt`

## Instalação

```bash
python -m pip install -r requirements.txt
```

## Configuração do ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
STRAVA_CLIENT_ID=seu_client_id
STRAVA_CLIENT_SECRET=seu_client_secret
STRAVA_ACCESS_TOKEN=seu_access_token
STRAVA_REFRESH_TOKEN=seu_refresh_token
```

> Você também pode usar `STRAVA_OAUTH_CODE` com o exemplo em `get_token_example.py` para trocar um `code` por tokens.

## Uso

Exibir ajuda:

```bash
python main.py --help
```

Exemplos:

```bash
python main.py --limit 5
kudo analyze --limit 5 --geo
kudo search --id 1791662310 --limit 5
kudo search --id 1791662310 --limit 5
```

### Opções principais

- `--athlete`, `--athlete-id`, `--id`: ID, URL ou username/slug do atleta para buscar atividades públicas/visíveis.
- `--limit`: quantidade de atividades a buscar (padrão: 10).
- `--geo-analyze`: exibe o link de localização GPS quando disponível.

## Segurança

- O arquivo `.env` é ignorado pelo Git e não deve ser enviado ao repositório.
- O arquivo `get_token_example.py` é um exemplo seguro para trocar um `code` por tokens sem expor segredos hard-coded.
- Não compartilhe tokens, secrets ou `code` de OAuth publicamente.

## Validação rápida

```bash
python -m compileall .
kudo --help
```
# KudoCli

"""Exemplo: trocar um `code` por tokens usando variáveis de ambiente.

Coloque `STRAVA_CLIENT_ID`, `STRAVA_CLIENT_SECRET` e `STRAVA_OAUTH_CODE`
no arquivo `.env` e não comite esse arquivo no repositório.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Leitura segura das credenciais a partir do .env
CLIENT_ID = os.getenv('STRAVA_CLIENT_ID')
CLIENT_SECRET = os.getenv('STRAVA_CLIENT_SECRET')
CODE = os.getenv('STRAVA_OAUTH_CODE')

if not all([CLIENT_ID, CLIENT_SECRET, CODE]):
    print('Por favor defina STRAVA_CLIENT_ID, STRAVA_CLIENT_SECRET e STRAVA_OAUTH_CODE no .env')
    raise SystemExit(1)

response = requests.post(
    url='https://www.strava.com/api/v3/oauth/token',
    data={
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': CODE,
        'grant_type': 'authorization_code'
    }
)

print(response.json())

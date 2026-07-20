import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

STRAVA_CLIENT_ID = os.getenv('STRAVA_CLIENT_ID')
STRAVA_CLIENT_SECRET = os.getenv('STRAVA_CLIENT_SECRET')
STRAVA_ACCESS_TOKEN = os.getenv('STRAVA_ACCESS_TOKEN')
STRAVA_REFRESH_TOKEN = os.getenv('STRAVA_REFRESH_TOKEN')

# Exemplo de uso
if not all([STRAVA_CLIENT_ID, STRAVA_CLIENT_SECRET, STRAVA_ACCESS_TOKEN, STRAVA_REFRESH_TOKEN]):
    print('Preencha todas as variáveis no arquivo .env')
else:
    print('Variáveis carregadas com sucesso!')

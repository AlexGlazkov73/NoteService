from os import environ as env
from dotenv import load_dotenv

load_dotenv('.env')

DB_HOST = env.get('DB_HOST') or '0.0.0.0'
DB_PORT = env.get('DB_PORT') or 5432
DB_NAME = env.get('DB_NAME') or 'note_service'
DB_USER = env.get('DB_USER') or 'note_service'
DB_PASSWORD = env.get('DB_PWD') or 'note_service'
DB_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

DB_SCHEMA = 'note_service'

HOST = env.get('HOST') or '0.0.0.0'
PORT = env.get('PORT') or 8000

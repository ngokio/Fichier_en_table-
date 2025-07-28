# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # Charge les variables depuis le fichier .env

DB_CONFIG = {
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT'))  # attention : PORT doit être un int
}

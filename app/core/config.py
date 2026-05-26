import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_KEY: str = os.getenv("API_KEY")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    REDIS_URL: str = os.getenv("REDIS_URL")
    PROJECT_NAME: str = "Capston_project"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTE: int = 30
    MODEL_PATH: str = "app/models/model.pkl"

settings = Settings()
from pydantic import BaseSettings
import os
from dotenv import load_dotenv

# טוען את משתני הסביבה מקובץ .env (אם קיים)
load_dotenv()

class Settings(BaseSettings):
    """קובץ קונפיגורציה לניהול כל ההגדרות של המערכת"""
    
    # הגדרות מסד נתונים
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "password")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")  # ⚠️ בפרודקשן צריך להחליף בכתובת אמיתית
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_NAME: str = os.getenv("DB_NAME", "parking_db")

    # חיבור מלא למסד נתונים (PostgreSQL)
    DATABASE_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # הגדרות אבטחה (JWT)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    # הגדרות Redis (מטמון + WebSockets)
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))

    # הרשאות CORS (דומיינים מורשים)
    ALLOWED_ORIGINS: list[str] = os.getenv("ALLOWED_ORIGINS", "*").split(",")

# יצירת מופע של ההגדרות
settings = Settings()

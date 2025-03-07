from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# יצירת מנוע SQLAlchemy עם החיבור למסד הנתונים (PostgreSQL)
engine = create_engine(settings.DATABASE_URL, echo=True)  # echo=True לצורך Debugging

# יצירת SessionFactory לניהול חיבורי מסד הנתונים
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# מחלקת בסיס לכל המודלים של מסד הנתונים
Base = declarative_base()

# פונקציה שמייצרת חיבור למסד הנתונים (Session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

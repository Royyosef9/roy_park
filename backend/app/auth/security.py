from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import User
from ..config import settings
from fastapi.security import OAuth2PasswordBearer

# הגדרת הצפנת סיסמאות
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# שימוש ב-OAuth2 לצורך אימות המשתמשים עם JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# פונקציות הצפנה ובדיקת סיסמאות
def get_password_hash(password: str) -> str:
    """הצפנת סיסמה באמצעות Bcrypt"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """בדיקה אם סיסמה שהוזנה תואמת לסיסמה המוצפנת במערכת"""
    return pwd_context.verify(plain_password, hashed_password)

# יצירת טוקן JWT
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """יוצר טוקן JWT למשתמש"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

# בדיקת JWT וטעינת המשתמש המחובר
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    """טוען את המשתמש המחובר באמצעות JWT"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

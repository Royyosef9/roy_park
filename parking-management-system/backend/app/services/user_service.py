from sqlalchemy.orm import Session
from ..models.user import User
from ..auth.security import hash_password

def create_user(db: Session, username: str, email: str, password: str):
    hashed_pw = hash_password(password)
    db_user = User(username=username, email=email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

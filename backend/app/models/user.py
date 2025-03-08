from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    """מודל משתמשים - כל משתמש בבניין מוגדר כאן"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    # קשר לחניות שהמשתמש מחזיק
    parking_spots = relationship("ParkingSpot", back_populates="owner")

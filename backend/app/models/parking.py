from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class ParkingSpot(Base):
    """מודל חניה - מייצג חניה בבניין"""
    __tablename__ = "parking_spots"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)  # מספר חניה או מיקום
    is_available = Column(Boolean, default=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # קשר עם המשתמש
    owner = relationship("User", back_populates="parking_spots")

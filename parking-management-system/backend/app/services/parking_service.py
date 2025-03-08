from sqlalchemy.orm import Session
from ..models.parking import ParkingSpot

def create_parking_spot(db: Session, location: str, owner_id: int):
    spot = ParkingSpot(location=location, owner_id=owner_id)
    db.add(spot)
    db.commit()
    db.refresh(spot)
    return spot

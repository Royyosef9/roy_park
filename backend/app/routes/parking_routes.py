from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.parking import ParkingSpot
from ..models.user import User
from ..auth.security import get_current_user
from pydantic import BaseModel

router = APIRouter()

# סכמות קלט של API
class ParkingCreate(BaseModel):
    location: str

# הוספת חניה למערכת
@router.post("/add")
def add_parking(spot: ParkingCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    new_spot = ParkingSpot(location=spot.location, owner_id=user.id)
    db.add(new_spot)
    db.commit()
    db.refresh(new_spot)
    return {"message": "Parking spot added", "spot_id": new_spot.id}

# קבלת כל החניות הפנויות
@router.get("/available")
def get_available_spots(db: Session = Depends(get_db)):
    spots = db.query(ParkingSpot).filter(ParkingSpot.is_available == True).all()
    return spots

# הזמנת חניה
@router.post("/reserve/{spot_id}")
def reserve_parking(spot_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    spot = db.query(ParkingSpot).filter(ParkingSpot.id == spot_id, ParkingSpot.is_available == True).first()
    if not spot:
        raise HTTPException(status_code=404, detail="Parking spot not available")

    spot.is_available = False
    db.commit()
    return {"message": "Parking spot reserved"}

# ביטול הזמנה
@router.post("/release/{spot_id}")
def release_parking(spot_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    spot = db.query(ParkingSpot).filter(ParkingSpot.id == spot_id, ParkingSpot.is_available == False).first()
    if not spot:
        raise HTTPException(status_code=404, detail="Parking spot is not reserved")

    spot.is_available = True
    db.commit()
    return {"message": "Parking spot released"}

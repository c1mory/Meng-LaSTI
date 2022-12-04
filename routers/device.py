from typing import List
from fastapi import APIRouter, Depends, status
import schemas, database.database as database
from sqlalchemy.orm import Session
from repository import device

router = APIRouter(
    prefix="/device",
    tags=['Devices']
)

get_db = database.get_db

@router.get('/')
def all(db: Session = Depends(get_db)):
    return device.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Device, db: Session = Depends(get_db)):
    return device.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return device.destroy(id, db)

@router.get('/{id}', status_code=200)
def show(id: int, db: Session = Depends(get_db)):
    return device.show(id, db)
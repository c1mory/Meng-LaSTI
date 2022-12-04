from typing import List
from fastapi import APIRouter, Depends, status
import schemas, database.database as database
from sqlalchemy.orm import Session
from repository import library

router = APIRouter(
    prefix="/library",
    tags=['Libraries']
)

get_db = database.get_db

@router.get('/')
def all(db: Session = Depends(get_db)):
    return library.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.InputLibrary, db: Session = Depends(get_db)):
    return library.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return library.destroy(id, db)

@router.get('/{id}', status_code=200)
def show(id: int, db: Session = Depends(get_db)):
    return library.show(id, db)
from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    libraries = db.query(models.Library).all()
    return libraries

def create(request: schemas.InputLibrary, db: Session):
    new_library = models.Library(lib_name=request.libName, lib_desc=request.libDesc, device_id=request.deviceID)
    db.add(new_library)
    db.commit()
    db.refresh(new_library)
    return new_library

def destroy(id: int, db: Session):
    library = db.query(models.Library).filter(models.Library.id == id)
    if not library.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Library with id {id} not found')
    library.delete(synchronize_session=False)
    db.commit()
    return 'done'

def show(id: int, db: Session):
    library = db.query(models.Library).filter(models.Library.id == id).first()
    if not library:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Library with id {id} not available')
    return library
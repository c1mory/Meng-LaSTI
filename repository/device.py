from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    devices = db.query(models.Device).all()
    return devices

def create(request: schemas.Device, db: Session):
    new_device = models.Device(device_name=request.deviceName, device_desc=request.deviceDesc)
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return new_device

def destroy(id: int, db: Session):
    device = db.query(models.Device).filter(models.Device.id == id)
    if not device.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Device with id {id} not found')
    device.delete(synchronize_session=False)
    db.commit()
    return 'done'

def show(id: int, db: Session):
    device = db.query(models.Device).filter(models.Device.id == id).first()
    if not device:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Device with id {id} not available')
    return device
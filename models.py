from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base

class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String)
    device_desc = Column(String)

    libraries = relationship("Library", back_populates="devices")

class Library(Base):
    __tablename__ = 'libraries'
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey('devices.id'))
    lib_name = Column(String)
    lib_desc = Column(String)

    devices = relationship("Device", back_populates="libraries")
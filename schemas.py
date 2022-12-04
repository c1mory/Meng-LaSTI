from pydantic import BaseModel
from typing import List

# Base class
class DeviceBase(BaseModel):
    deviceName: str
    deviceDesc: str

class LibraryBase(BaseModel):
    libName: str
    libDesc: str

# Class
class Device(DeviceBase):
    class Config():
        orm_mode = True

class Library(LibraryBase):
    class Config():
        orm_mode = True

# Specific class
class InputLibrary(BaseModel):
    libName: str
    libDesc: str
    deviceID: int

    class Config():
        orm_mode = True

class ShowDevice(BaseModel):
    deviceName: str
    deviceDesc: str
    libraries: List[Library] = []

    class Config():
        orm_mode = True
from dataclasses import dataclass


@dataclass
class Device:
    id: str
    brand: str
    model: str
    os: str
    latitude: float
    longitude: float
    altitude_meters: float
    accuracy_meters: float

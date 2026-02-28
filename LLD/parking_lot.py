import threading
from enum import Enum
from datetime import datetime
from abc import ABC, staticmethod


class VehicleSize(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3
    
class Vehicle(ABC):
    def __init__(self, license_plate: str, size: VehicleSize):
        self.license_plate = license_plate
        self.size = size
        self.entry_time = None
        
    def set_entry_time(self):
        self.entry_time = datetime.now()
        

class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleSize.COMPACT)
        
        
class Bus(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleSize.LARGE)
        

class ParkingSpot:
    def __init__(self, spot_id: int, size: VehicleSize):
        self.id = spot_id
        self.size = size
        self.vehicle = None
        
    def is_free(self) -> bool:
        return self.vehicle is None
    
    def can_fit_vehicle(self, vehicle: Vehicle) -> bool:
        return self.is_free() and self.size.value >= vehicle.size.value
    
    def park(self, vehicle: Vehicle) -> bool:
        if self.can_fit_vehicle(vehicle):
            self.vehicle = vehicle
            self.vehicle.set_entry_time()
            return True
        return False
    
    def remove_vehicle(self):
        self.vehicle = None
        
class Level:
    def __init__(self, floor_num: int, num_spots: int):
        self.floor_num = floor_num
        # In a real app, we'd distribute spot sizes (e.g., 20% Large, 80% Compact)
        self.spots = [ParkingSpot(i, VehicleSize.COMPACT) for i in range(num_spots)]
        
    def find_available_spot(self, vehicle: Vehicle) -> ParkingSpot:
        for spot in self.spots:
            if spot.can_fit_vehicle(vehicle):
                return spot
        return None
    

# The ParkingLot is a Singleton (usually, there's only one lot instance) that manages Levels
class ParkingLot:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ParkingLot, cls).__new__(cls)
            cls._instance.levels = []
        return cls._instance
    
    def add_level(self, level: Level):
        self.levels.append(level)
        
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            spot = level.find_available_spot(vehicle)
            if spot and spot.park(vehicle):
                print(f"Parked {vehicle.license_plate} at Spot {spot.id}")
                return True
        return False
    
    
                
        
    
    
    
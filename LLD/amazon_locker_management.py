"""
The Scenario: A delivery driver arrives at an Amazon Hub. They have a package and need to be assigned a locker that fits.

1. Requirements & Constraints (Clarification)

Sizes: Small, Medium, Large.
Rule: A package can fit in a locker of its own size or any larger size.
Action: We need to assign_locker(package) and free_locker(locker_id).
"""

import threading
from enum import Enum
from typing import List
from abc import ABC, abstractmethod


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    

class Package:
    def __init__(self, package_id: str, size: Size):
        self.id = package_id
        self.size = size
        
    
class Locker:
    def __init__(self, locker_id: str, size: Size):
        self.id = locker_id
        self.sise = size
        self.is_available = True
        self._lock = threading.Lock()
        
    def book(self) -> bool:
        with self._lock:
            if self.is_available:
                self.is_available = False
                return True
            return False
        
    def release(self):
        self.is_available = True
        
        
class BaseLockerFindingStrategy(ABC):
    @abstractmethod
    def find(self, package_szie: int, lockers: List[Locker]) -> Locker:
        pass        


class StandardLockerFindingStrategy(BaseLockerFindingStrategy):
    """Finds the smallest available locker that fits the package"""
    def find(self, package_size: Size, lockers: List[Locker]) -> Locker:
        eligible_lockers = sorted(
            [locker for locker in lockers if locker.sise.value >= package_size.value],
            key=lambda x: x.size.value
        )
        return eligible_lockers[0] if eligible_lockers else None

"""
Approach 1: Thread Locking (Mutual Exclusion)
This is the most common way to handle concurrency in LLD. 
We use a Lock (Mutex) to ensure that only one thread can execute the "check and book" logic at a time.
"""
class LockerService:
    def __init__(self, lockers: List[Locker], strategy: BaseLockerFindingStrategy):
        self.lockers = lockers
        self.strategy = strategy
        self.global_lock = threading.lock() # to protect the search process
        
    def assign_locker(self, package: Package) -> str:
        with self.global_lock:
            # find a candidate
            locker = self.strategy.find(package.size, self.lockers)
            
            # try to book it
            if locker and locker.book():
                return locker.id
            
        return "No Locker Available"
    
"""
Approach 2: Thread-Safe Queue (Producer-Consumer)
Instead of locking the resource, we treat the lockers as a "pool" of available items. 
We use Python’s queue.Queue, which is thread-safe by design.
"""
from queue import Queue, Empty   


class LockerPool:
    def __init__(self):
        self.pool = {
            Size.SMALL: Queue(),
            Size.MEDIUM: Queue(),
            Size.LARGE: Queue()
        }  
        
    def add_locker(self, locker: Locker):
        self.pool[locker.size].put(locker)
        
    def get_locker(self, size: Size):
        try:
            # This is an atomic operation provided by the Queue module
            return self.pool[size].get_nowait()
        except Empty:
            return None
    
    def release_locker(self, locker: Locker):
        locker.is_available = True
        self.pool[locker.size].put(locker)
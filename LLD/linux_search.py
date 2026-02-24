from typing import List
from abc import ABC, abstractmethod


# file object
class File:
    def __init__(self, name: str, size: int, is_dir: bool=False):
        self.name = name
        self.size = size
        self.is_dir = is_dir
        
    def __repr__(self):
        return f"File({self.name}, {self.size}kb)"
        
     
# filters
class BaseFilter(ABC):
    @abstractmethod
    def isValid(self, file: File) -> bool:
        pass


class NameFilter(BaseFilter):
    def __init__(self, name: set):
        self.name = name
        
    def isValid(self, file: File) -> bool:
        return self.name in file.name
    

class MinSizeFilter(BaseFilter):
    def __init__(self, min_size: int):
        self.min_size = min_size
        
    def isValid(self, file: File) -> bool:
        return file.size >= self.min_size
    

class ExtensionFilter(BaseFilter):
    def __init__(self, extension: str):
        self.extension = extension
    
    def isValid(self, file: File) -> bool:
        return file.name.endswith(self.extension)
        

class AndFilter(BaseFilter):
    def __init__(self, filters: List[BaseFilter]) -> bool:
        self.filters = filters
        
    def isValid(self, file: File) -> bool:
        return all(filter.isValid(file) for filter in self.filters)
    
# search engine
class FileSearcher:
    def search(self, files: List[File], filter: BaseFilter) -> List[File]:
        return [file for file in files if filter.isValid(file)]
    

    


from abc import ABC, abstractmethod

class Figure(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
from dataclasses import dataclass
from datetime import datetime


@dataclass
class State:
    id:str
    Name:str
    Capital:str
    Lat:float
    Lng:float
    Area:int
    Population:int
    Neighbors:str

    def __hash__(self):
        return hash(self.id)
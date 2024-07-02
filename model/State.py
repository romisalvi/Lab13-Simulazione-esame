from dataclasses import dataclass
@dataclass
class State:
    id:str
    Name:str
    Capital:str
    Lat:float
    Lng:float
    Area:int
    Population:int
    Neighbors:int
    Sightings:int
    def __hash__(self):
        return hash(self.id)
from pydantic import BaseModel

class ItemBase(BaseModel):
    id: int
    name: str

class Position(ItemBase):
    description: str

    class Config:
        orm_mode = True


class Team(ItemBase):
    description: str

    class Config:
        orm_mode = True 

class Player(ItemBase):
    age: int
    avegare_points: float
    tshirt_number: int
    position: Position
    team : Team

    class Config:
        orm_mode = True

class NewPlayer(BaseModel):
    name: str
    age: int
    avegare_points: float
    tshirt_number: int
    position: int
    team : int

class TeamPlayers(Team):
    players: list[Player]

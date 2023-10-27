from pydantic import BaseModel
from datetime import datetime

class ItemBase(BaseModel):
    id: int

class Gabba(ItemBase):
    name: str
    description: str
    url: str

class UserKani(ItemBase):
    name: str
    phone_number: str
    create_date: datetime
    password_hash: str
    gabba_id: int

class NewUserKani(ItemBase):
    name: str
    phone_number: str
    
class Improve(ItemBase):
    improvement: str

class UserImprove(ItemBase):
    user_id: int
    improve_id: int

class Interests(ItemBase):
    interest: str
    user_id: int

class UserInterests(ItemBase):
    user_id: int
    interests_id: int

class Diario(ItemBase):
    user_id: int

class Note(ItemBase):
    title: str
    text: str
    diary_id: int

class Emotions(ItemBase):
    name: str
    description: str

class UserEmotions(ItemBase):
    user_id: int
    emotion_id: int
    date: datetime

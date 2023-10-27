from pydantic import BaseModel
from datetime import datetime

class ItemBase(BaseModel):
    id: int

class Gabba(ItemBase):
    name: str
    description: str
    url: str

    class Config:
        orm_mode = True

class UserKani(ItemBase):
    name: str
    phone_number: str
    create_date: datetime
    password_hash: str
    gabba_id: int

    class Config:
        orm_mode = True

class NewUserKani(ItemBase):
    name: str
    phone_number: str

class NewDiaryNote(ItemBase):
    user_id: int
    note_title: str
    note_text: str

class Improve(ItemBase):
    improvement: str

    class Config:
        orm_mode = True

class UserImprove(ItemBase):
    user_id: int
    improve_id: int

    class Config:
        orm_mode = True

class Interests(ItemBase):
    interest: str
    user_id: int

    class Config:
        orm_mode = True
class UserInterests(ItemBase):
    user_id: int
    interests_id: int
    class Config:
        orm_mode = True

class Diary(ItemBase):
    user_id: int
    class Config:
        orm_mode = True

class Note(ItemBase):
    title: str
    text: str
    diary_id: int
    class Config:
        orm_mode = True

class Emotions(ItemBase):
    name: str
    description: str
    class Config:
        orm_mode = True

class UserEmotions(ItemBase):
    user_id: int
    emotion_id: int
    date: datetime
    class Config:
        from_attributes = True

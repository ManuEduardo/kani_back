from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from typing import List

from .schemas import NewDiaryNoteResponse, UserKani,NewDiaryNote, NewUserKani, Improve, UserImprove, Interests, UserInterests, Diary, Note, Emotions, UserEmotions
from .services import userkani_services, diary_services

router = APIRouter(
    prefix='/api',
    tags=['kani'],
    
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/usuarios/', response_model=NewUserKani)
def crear_usuario(nuevo_usuario: NewUserKani, db: Session = Depends(get_db)):
    db_user = userkani_services.create_user_kani(db, nuevo_usuario)
    return db_user

@router.post('/diario/', response_model= NewDiaryNoteResponse)
def crear_elemento_diario(nuevo_diario: NewDiaryNote, db: Session = Depends(get_db)):
    NewDiary = diary_services.create_diary_entry(db, nuevo_diario)
    return NewDiary

@router.get('/diario/{user_id}', response_model= List[Note])
def get_notas_usuario(user_id: int, db: Session = Depends(get_db)):
    db_Notes = diary_services.get_notas_usuario(db, user_id)
    return db_Notes


@router.get('/user/{user_id}', response_model=UserKani)
def get_user_kani(user_id: int, db: Session = Depends(get_db)):
    db_user = userkani_services.get_user_kani(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get('/userDate/{user_id}', response_model=int)
def get_user_kani(user_id: int, db: Session = Depends(get_db)):
    db_userDay = userkani_services.get_days_used(db, user_id)
    return db_userDay

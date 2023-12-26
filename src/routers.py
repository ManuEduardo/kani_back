from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from typing import List, Annotated

from .schemas import NewDiaryNoteResponse, UserKani,NewDiaryNote, NewUserKani, Improve, UserImprove, Interests, UserInterests, Diary, Note, Emotions, UserEmotions
from .services import userkani_services, diary_services
from .auth import get_current_user

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

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.post('/diario/', response_model= NewDiaryNoteResponse)
async def crear_elemento_diario(user: user_dependency, nuevo_diario: NewDiaryNote, db: Session = Depends(get_db)):
    
    if user is None:
        raise HTTPException(status_code=401, detail= 'Authentication Failed')
    
    NewDiary = diary_services.create_diary_entry(db, nuevo_diario)
    return NewDiary

@router.get('/diario/{user_id}', response_model= List[Note])
async def get_notas_usuario(user: user_dependency, user_id: int, db: Session = Depends(get_db)):
    
    if user is None:
        raise HTTPException(status_code=401, detail= 'Authentication Failed')
    
    db_Notes = diary_services.get_notas_usuario(db, user_id)
    return db_Notes


@router.get('/user/{user_id}', response_model=UserKani)
async def get_user_kani(user: user_dependency, user_id: int, db: Session = Depends(get_db)):

    if user is None:
        raise HTTPException(status_code=401, detail= 'Authentication Failed')

    db_user = userkani_services.get_user_kani(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get('/userDate/{user_id}', response_model=int)
async def get_user_kani(user: user_dependency, user_id: int, db: Session = Depends(get_db)):
    
    if user is None:
        raise HTTPException(status_code=401, detail= 'Authentication Failed')
    
    db_userDay = userkani_services.get_days_used(db, user_id)
    return db_userDay

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal

from .schemas import Gabba, UserKani, NewUserKani, Improve, UserImprove, Interests, UserInterests, Diario, Note, Emotions, UserEmotions
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


@router.post('/diario/', response_model=Diario)
def crear_elemento_diario(nuevo_diario: Diario, db: Session = Depends(get_db)):
    user_id = nuevo_diario.user_id
    diary_text = nuevo_diario.diary_text
    note_title = nuevo_diario.note_title
    note_text = nuevo_diario.note_text

    diario_entry, note = diary_services.create_diary_entry(db, user_id, diary_text, note_title, note_text)
    return diario_entry, note

@router.get('/user/{user_id}', response_model=UserKani)
def get_user_kani(user_id: int, db: Session = Depends(get_db)):
    db_user = userkani_services.get_user_kani(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
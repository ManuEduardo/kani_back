from sqlalchemy.orm import Session
from src import models, schemas
from datetime import datetime

from src import models

def create_diary_entry(
    db: Session,
    nuevo_diario: schemas.NewDiaryNote
):
    user_id = nuevo_diario.user_id
    note_title = nuevo_diario.note_title
    note_text = nuevo_diario.note_text
    current_datetime = datetime.now()
    # Verificar si ya existe un diario para el usuario
    existing_diary = db.query(models.Diary).filter(models.Diary.user_id == user_id).first()

    if existing_diary:
        # Si ya existe un diario, simplemente crear una nueva nota
        new_note = models.Note(
            title = note_title, 
            text = note_text, 
            diary_id = existing_diary.id,
            date =  current_datetime
        )
        db.add(new_note)
        db.commit()
        db.refresh(new_note)
        return existing_diary, new_note
    else:
        # Si no existe un diario, crear uno y luego una nueva nota
        new_diary_entry = models.Diary(
            user_id = user_id
            )
        db.add(new_diary_entry)
        db.commit()
        db.refresh(new_diary_entry)

        new_note = models.Note(
            title = note_title, 
            text = note_text, 
            diary_id = new_diary_entry.id,
            date = current_datetime
            )
        db.add(new_note)
        db.commit()
        db.refresh(new_note)

        return new_diary_entry, new_note

def get_notas_usuario(db: Session, user_id: int):
    return db.query(models.Note).join(models.Diary).filter(models.Diary.user_id == user_id).all()

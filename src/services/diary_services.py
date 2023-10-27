from sqlalchemy.orm import Session

from src import models

def create_diary_entry(
    db: Session,
    user_id: int,
    diary_text: str,
    note_title: str,
    note_text: str
):
    # Verificar si ya existe un diario para el usuario
    existing_diary = db.query(models.Diario).filter(models.Diario.user_id == user_id).first()

    if existing_diary:
        # Si ya existe un diario, simplemente crear una nueva nota
        new_note = models.Note(title=note_title, text=note_text, diary_id=existing_diary.id)
        db.add(new_note)
        db.commit()
        db.refresh(new_note)
        return existing_diary, new_note
    else:
        # Si no existe un diario, crear uno y luego una nueva nota
        new_diary_entry = models.Diario(user_id=user_id)
        db.add(new_diary_entry)
        db.commit()
        db.refresh(new_diary_entry)

        new_note = models.Note(title=note_title, text=note_text, diary_id=new_diary_entry.id)
        db.add(new_note)
        db.commit()
        db.refresh(new_note)

        return new_diary_entry, new_note
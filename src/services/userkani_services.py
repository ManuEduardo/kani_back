from sqlalchemy.orm import Session

from src import models, schemas
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError


def get_user_kani(db: Session, user_id: int):
    return db.query(models.UserKani).filter(models.UserKani.id == user_id).first()


def create_user_kani(db: Session, new_user: schemas.NewUserKani):
    try:
        current_time = datetime.utcnow()
        db_user_kani = models.UserKani(
            name=new_user.name,
            phone_number=new_user.phone_number,
            password_hash= "",
            create_date=current_time
        )
        db.add(db_user_kani)
        db.commit()
        db.refresh(db_user_kani)
        return db_user_kani
    except SQLAlchemyError as e:
        # Imprimir información de error o registrarla en un archivo de registro
        print(f"Error al crear usuario: {str(e)}")
        db.rollback()
        return None

def get_users_by_phone_number(db: Session, phone_number: str):
    return db.query(models.UserKani).filter(models.UserKani.phone_number == phone_number).all()

from sqlalchemy.orm import Session

from src import models, schemas
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
import bcrypt


def get_user_kani(db: Session, user_id: int):
    return db.query(models.UserKani).filter(models.UserKani.id == user_id).first()

def create_user_kani(db: Session, new_user: schemas.NewUserKani):
    try:

        # Genera un hash seguro de la contraseña
        hashed_password = bcrypt.hashpw(new_user.password_hash.encode('utf-8'), bcrypt.gensalt())

        current_time = datetime.utcnow()
        db_user_kani = models.UserKani(
            name = new_user.name,
            phone_number = "",
            password_hash = hashed_password,
            create_date = current_time,
            gabba_id = 1
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

def get_days_used(db: Session, id_user: int):
    user = db.query(models.UserKani).filter(models.UserKani.id == id_user).first()
    if user:
        create_date = user.create_date
        current_date = datetime.now().date()
        
        # Asegúrate de que ambas fechas sean de tipo datetime.date
        create_date = create_date.date()  # Convierte a datetime.date
        
        days_used = (current_date - create_date).days
        return days_used 
    else:
        return None
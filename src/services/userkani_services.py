from sqlalchemy.orm import Session

from src import models, schemas
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
import bcrypt
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

SECRET_KEY = 'asdasdasdasfasfoeiro12oi312i73u128o3j1o231238u2319od23jo2'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_user_kani(db: Session, user_id: int):
    return db.query(models.UserKani).filter(models.UserKani.id == user_id).first()

def authenticate_user(username: str, password: str, db):
    user = db.query(models.UserKani).filter(models.UserKani.name == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.password_hash):
        return False
    return user

def create_user_kani(db: Session, new_user: schemas.NewUserKani):
    try:

        # Genera un hash seguro de la contraseña
        hashed_password = bcrypt_context.hash(new_user.password_hash)

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
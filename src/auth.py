from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from typing import List, Annotated
from starlette import status
from datetime import timedelta, datetime

from .schemas import NewDiaryNoteResponse, UserKani,NewDiaryNote, NewUserKani, Improve, UserImprove, Interests, UserInterests, Diary, Note, Emotions, UserEmotions, Token
from .services import userkani_services, diary_services

router = APIRouter(
    prefix='/Auth',
    tags=['Auth']
    )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SECRET_KEY = 'asdasdasdasfasfoeiro12oi312i73u128o3j1o231238u2319od23jo2'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='Auth/token')

db_dependency = Annotated[Session, Depends(get_db)]

@router.post('/', status_code=status.HTTP_201_CREATED)
def crear_usuario(nuevo_usuario: NewUserKani, db: Session = Depends(get_db)):
    db_user = userkani_services.create_user_kani(db, nuevo_usuario)
    return db_user

 

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
    user = userkani_services.authenticate_user(form_data.username, form_data.password, db)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
    
    token = create_access_token(user.name, user.id, timedelta(minutes=120))

    return {'access_token': token, 'token_type': 'bearer'}


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub':username, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token:Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username : str = payload.get('sub')
        user_id: int = payload.get('id')

        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user.')
        return {'username':username, 'id':user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could no validate user.')
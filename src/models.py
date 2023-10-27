from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base

class Gabba(Base):
    __tablename__ = 'gabba'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    url = Column(String)

class UserKani(Base):
    __tablename__ = 'user_kani'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    create_date = Column(Date)
    password_hash = Column(String)
    gabba_id = Column(Integer, ForeignKey('gabba.id'))


class Improve(Base):
    __tablename__ = 'improve'

    id = Column(Integer, primary_key=True)
    improvement = Column(String)

class UserImprove(Base):
    __tablename__ = 'user_improve'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_kani.id'))
    improve_id = Column(Integer, ForeignKey('improve.id'))

class Interests(Base):
    __tablename__ = 'interests'

    id = Column(Integer, primary_key=True)
    interest = Column(String)
    user_id = Column(Integer, ForeignKey('user_kani.id'))

class UserInterests(Base):
    __tablename__ = 'user_interests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_kani.id'))
    interests_id = Column(Integer, ForeignKey('interests.id'))

class Diario(Base):
    __tablename__ = 'diario'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_kani.id'))

class Note(Base):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)
    diary_id = Column(Integer, ForeignKey('diario.id'))

class Emotions(Base):
    __tablename__ = 'emotions'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class UserEmotions(Base):
    __tablename__ = 'user_emotions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_kani.id'))
    emotion_id = Column(Integer, ForeignKey('emotions.id'))
    date = Column(Date)
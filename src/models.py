from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Gabba(Base):
    __tablename__ = 'gabba'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    url = Column(String)
    users = relationship("UserKani", back_populates="gabba")

class UserKani(Base):
    __tablename__ = 'user_kani'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    create_date = Column(DateTime)
    password_hash = Column(String)
    gabba_id = Column(Integer, ForeignKey('gabba.id'))
    gabba = relationship("Gabba", back_populates="users")
    improves = relationship("Improve", secondary="user_improve")
    interests = relationship("Interest", secondary="user_interests")
    diaries = relationship("Diary", back_populates="user")
    emotions = relationship("Emotion", secondary="user_emotions")

class Improve(Base):
    __tablename__ = 'improve'

    id = Column(Integer, primary_key=True)
    improvement = Column(String)

class UserImprove(Base):
    __tablename__ = 'user_improve'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_kani.id'))
    improve_id = Column(Integer, ForeignKey('improve.id'))

class Interest(Base):
    __tablename__ = 'interests'

    id = Column(Integer, primary_key=True)
    interest = Column(String)

class UserInterest(Base):
    __tablename__ = 'user_interests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_kani.id'))
    interest_id = Column(Integer, ForeignKey('interests.id'))

class Diary(Base):
    __tablename__ = 'diary'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_kani.id'))
    
    user = relationship("UserKani", back_populates="diaries")
    notes = relationship("Note", back_populates="diary")

class Note(Base):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)
    diary_id = Column(Integer, ForeignKey('diary.id'))
    
    diary = relationship("Diary", back_populates="notes")


class Emotion(Base):
    __tablename__ = 'emotions'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class UserEmotion(Base):
    __tablename__ = 'user_emotions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_kani.id'))
    emotion_id = Column(Integer, ForeignKey('emotions.id'))
    date = Column(DateTime)
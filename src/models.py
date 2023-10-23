from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from src.database import Base

class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    players = relationship("Player", back_populates="position")  # Corregir esta línea

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    players = relationship("Player", back_populates="team")  # Corregir esta línea

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    position_id = Column(Integer, ForeignKey("positions.id"))
    team_id = Column(Integer, ForeignKey("teams.id"))
    age = Column(Integer, index=True)
    avegare_points = Column(Float, index=True)
    tshirt_number = Column(Integer, index=True)

    position = relationship("Position", back_populates="players")
    team = relationship("Team", back_populates="players")

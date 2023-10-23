from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal

import schemas
from services import player_services, team_services

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

@router.get('/player/{player_id}', response_model=schemas.Player)
def get_player(player_id: int, db: SessionLocal = Depends(get_db)):
    db_player = player_services.get_player(db, player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player


@router.post('/player/', response_model=schemas.Player)
def post_player(new_player: schemas.NewPlayer, db: Session = Depends(get_db)):
    db_player = player_services.post_player(db, new_player)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Players not found")
    return db_player


@router.get('/players/tshirt/{player_tshirt}', response_model=list[schemas.Player])
def get_players_tshirt(player_tshirt: int, db: Session = Depends(get_db)):
    db_players = player_services.get_players_tshirt(db, player_tshirt)
    if db_players is None:
        raise HTTPException(status_code=406, detail="Players no accepted")
    return db_players


@router.get('/team/{team_id}', response_model=schemas.TeamPlayers)
def get_team_players(team_id: int, db: Session = Depends(get_db)):
    db_team_players = team_services.get_team_players(db, team_id)
    if db_team_players is None:
        raise HTTPException(status_code=404, detail="Players not found")
    return db_team_players
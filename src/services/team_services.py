from sqlalchemy.orm import Session

from src import models

def get_team_players(db: Session, team_id: int):
    return db.query(models.Team).filter_by(id = team_id).first()


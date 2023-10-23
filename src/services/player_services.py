from sqlalchemy.orm import Session

from src import models, schemas


def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()


def post_player(db: Session, new_player: schemas.NewPlayer):
    db_player = models.Player(name=new_player.name,
                              position_id=new_player.position,
                              team_id=new_player.team,
                              age=new_player.age,
                              avegare_points=new_player.avegare_points,
                              tshirt_number=new_player.tshirt_number)
    db.add(db_player)   
    db.commit()
    db.refresh(db_player)
    return db_player

def get_players_tshirt(db: Session, player_tshirt: int):
    return db.query(models.Player).filter(models.Player.tshirt_number == player_tshirt).all()

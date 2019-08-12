# from app import db
from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

# Create our classes, one for each table
# One to many - Each player belongs to 1 team. Each team has many players
# One to one - Each team has 1 captain. Each captain can only belong to 1 team.

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    rank = Column(Integer, nullable=False)
    players = relationship('Player', backref='team_name', lazy=True)
    
    def __repr__(self):
        return '<Team %r>' % self.name


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    position = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    
    def __repr__(self):
        return '<Player %r>' % self.name


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    level = Column(String(30), nullable=False)
    child_id = Column(Integer, ForeignKey('games.id'), nullable=True)
    winner_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    loser_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    child = relationship('Game', remote_side=[id])

    def __repr__(self):
        return '<Game %r>' % self.winner_id
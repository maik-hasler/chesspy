from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)

    moves = relationship('Move', back_populates='game')

class Move(Base):
    __tablename__ = 'moves'

    id = Column(Integer, primary_key=True)
    start_pos_row = Column(Integer)
    start_pos_col = Column(Integer)
    end_pos_row = Column(Integer)
    end_pos_col = Column(Integer)

    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship('Game', back_populates='moves')

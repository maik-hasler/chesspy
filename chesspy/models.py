from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

    games = relationship('Game', back_populates='user')

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    winner_id = Column(Integer, ForeignKey('users.id'))

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='games')

    moves = relationship('Move', back_populates='game')

class Move(Base):
    __tablename__ = 'moves'

    id = Column(Integer, primary_key=True)
    chess_piece = Column(String)
    origin = Column(String)
    destination = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')

    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship('Game', back_populates='moves')

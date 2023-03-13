from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True)
    games = relationship(Game, back_populates='user')

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship(User, back_populates='game')

class Move(Base):
    __tablename__ = 'moves'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))

    game = relationship(Game)
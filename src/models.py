from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True)

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship(User)

class Move(Base):
    __tablename__ = 'moves'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))

    game = relationship(Game)
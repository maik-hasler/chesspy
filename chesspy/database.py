from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from chesspy.models import Base, Game, Move


class Database:

    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///chesspy.db', connect_args={"check_same_thread": False})
        Base.metadata.create_all(self.engine)
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        self.connection = self.engine.connect()

    def insert_new_game(self) -> int:
        Session = sessionmaker(bind=self.engine)
        session = Session()
        game = Game()
        session.add(game)
        session.commit()
        game_id = game.id
        session.close_all()
        return game_id

    def insert_new_move(self, move) -> None:
        Session = sessionmaker(bind=self.engine)
        session = Session()
        move = Move(
            start_pos_row = move.start_position[0],
            start_pos_col = move.start_position[1],
            end_pos_row = move.end_position[0],
            end_pos_col = move.end_position[1]
        )
        session.add(move)
        session.commit()
        session.close_all()

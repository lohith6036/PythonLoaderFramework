import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from dataloader_library.database_manager import Athlete, Team, Event, Game, Participation, get_engine, get_session
from dataloader_library.metadata_logger import MetadataLogger

class DataLoader:
    def __init__(self, db_url, metadata_logger: MetadataLogger):
        self.engine = get_engine(db_url)
        self.session = get_session(self.engine)
        self.metadata_logger = metadata_logger

    def load_data(self, csv_file):
        df = pd.read_csv(csv_file)

        for index, row in df.iterrows():
            try:
                athlete_id = self.get_or_create_athlete(row)
                team_id = self.get_or_create_team(row)
                event_id = self.get_or_create_event(row)
                game_id = self.get_or_create_game(row)
                self.create_participation(row, athlete_id, team_id, event_id, game_id)
                self.metadata_logger.log_success(csv_file, row['ID'])
            except SQLAlchemyError as e:
                self.session.rollback()
                self.metadata_logger.log_error(csv_file, row['ID'], str(e))
            except Exception as e:
                self.metadata_logger.log_error(csv_file, row['ID'], str(e))

    def get_or_create_athlete(self, row):
        athlete = self.session.query(Athlete).filter_by(Name=row['Name'], Sex=row['Sex'], Age=row['Age']).first()
        if athlete is None:
            athlete = Athlete(Name=row['Name'], Sex=row['Sex'], Age=row['Age'])
            self.session.add(athlete)
            self.session.commit()
        return athlete.AthleteID

    def get_or_create_team(self, row):
        team = self.session.query(Team).filter_by(TeamName=row['Team'], NOC=row['NOC']).first()
        if team is None:
            team = Team(TeamName=row['Team'], NOC=row['NOC'])
            self.session.add(team)
            self.session.commit()
        return team.TeamID

    def get_or_create_event(self, row):
        event = self.session.query(Event).filter_by(Sport=row['Sport'], EventName=row['Event']).first()
        if event is None:
            event = Event(Sport=row['Sport'], EventName=row['Event'])
            self.session.add(event)
            self.session.commit()
        return event.EventID

    def get_or_create_game(self, row):
        game = self.session.query(Game).filter_by(Games=row['Games'], Year=row['Year'], Season=row['Season'], City=row['City']).first()
        if game is None:
            game = Game(Games=row['Games'], Year=row['Year'], Season=row['Season'], City=row['City'])
            self.session.add(game)
            self.session.commit()
        return game.GameID

    def create_participation(self, row, athlete_id, team_id, event_id, game_id):
        participation = Participation(
            AthleteID=athlete_id,
            TeamID=team_id,
            EventID=event_id,
            GameID=game_id,
            Medal=row['Medal']
        )
        self.session.add(participation)
        self.session.commit()
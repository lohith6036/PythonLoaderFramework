from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Athlete(Base):
    __tablename__ = 'Athlete'
    
    AthleteID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(255), nullable=False)
    Sex = Column(String(10), nullable=False)
    Age = Column(Integer)

class Team(Base):
    __tablename__ = 'Team'
    
    TeamID = Column(Integer, primary_key=True, autoincrement=True)
    TeamName = Column(String(255), nullable=False)
    NOC = Column(String(10), nullable=False)
    __table_args__ = (UniqueConstraint('TeamName', 'NOC', name='idx_team_noc'),)

class Event(Base):
    __tablename__ = 'Event'
    
    EventID = Column(Integer, primary_key=True, autoincrement=True)
    Sport = Column(String(255), nullable=False)
    EventName = Column(String(255), nullable=False)
    __table_args__ = (UniqueConstraint('Sport', 'EventName', name='idx_sport_event'),)

class Game(Base):
    __tablename__ = 'Game'
    
    GameID = Column(Integer, primary_key=True, autoincrement=True)
    Games = Column(String(255), nullable=False)
    Year = Column(Integer, nullable=False)
    Season = Column(String(20), nullable=False)
    City = Column(String(255), nullable=False)
    __table_args__ = (UniqueConstraint('Games', 'Year', 'Season', 'City', name='idx_game_year_season_city'),)

class Participation(Base):
    __tablename__ = 'Participation'
    
    ParticipationID = Column(Integer, primary_key=True, autoincrement=True)
    AthleteID = Column(Integer, nullable=False)
    TeamID = Column(Integer, nullable=False)
    EventID = Column(Integer, nullable=False)
    GameID = Column(Integer, nullable=False)
    Medal = Column(String(50))

class LoadMetadata(Base):
    __tablename__ = 'LoadMetadata'
    
    LoadID = Column(Integer, primary_key=True, autoincrement=True)
    SourceFile = Column(String(255), nullable=False)
    Timestamp = Column(DateTime, nullable=False)
    RecordID = Column(Integer, nullable=False)
    Status = Column(String(20), nullable=False)
    ErrorMessage = Column(Text)

# Database setup
def get_engine(db_url):
    return create_engine(db_url)

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
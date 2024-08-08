


USE olympics_db;

CREATE TABLE Athlete (
    AthleteID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Sex VARCHAR(10) NOT NULL,
    Age INT
);

CREATE TABLE Team (
    TeamID INT AUTO_INCREMENT PRIMARY KEY,
    TeamName VARCHAR(255) NOT NULL,
    NOC VARCHAR(10) NOT NULL,
    UNIQUE (TeamName, NOC)
);

CREATE TABLE Event (
    EventID INT AUTO_INCREMENT PRIMARY KEY,
    Sport VARCHAR(255) NOT NULL,
    EventName VARCHAR(255) NOT NULL,
    UNIQUE (Sport, EventName)
);

CREATE TABLE Game (
    GameID INT AUTO_INCREMENT PRIMARY KEY,
    Games VARCHAR(255) NOT NULL,
    Year INT NOT NULL,
    Season VARCHAR(20) NOT NULL,
    City VARCHAR(255) NOT NULL,
    UNIQUE (Games, Year, Season, City)
);

CREATE TABLE Participation (
    ParticipationID INT AUTO_INCREMENT PRIMARY KEY,
    AthleteID INT NOT NULL,
    TeamID INT NOT NULL,
    EventID INT NOT NULL,
    GameID INT NOT NULL,
    Medal VARCHAR(50),
    FOREIGN KEY (AthleteID) REFERENCES Athlete(AthleteID),
    FOREIGN KEY (TeamID) REFERENCES Team(TeamID),
    FOREIGN KEY (EventID) REFERENCES Event(EventID),
    FOREIGN KEY (GameID) REFERENCES Game(GameID)
);

CREATE TABLE LoadMetadata (
    LoadID INT AUTO_INCREMENT PRIMARY KEY,
    SourceFile VARCHAR(255) NOT NULL,
    Timestamp DATETIME NOT NULL,
    RecordID INT NOT NULL,
    Status VARCHAR(20) NOT NULL,
    ErrorMessage TEXT
);

CREATE INDEX idx_name ON Athlete (Name);
CREATE UNIQUE INDEX idx_team_noc ON Team (TeamName, NOC);
CREATE UNIQUE INDEX idx_sport_event ON Event (Sport, EventName);
CREATE UNIQUE INDEX idx_game_year_season_city ON Game (Games, Year, Season, City);
CREATE INDEX idx_athlete_id ON Participation (AthleteID);
CREATE INDEX idx_team_id ON Participation (TeamID);
CREATE INDEX idx_event_id ON Participation (EventID);
CREATE INDEX idx_game_id ON Participation (GameID);
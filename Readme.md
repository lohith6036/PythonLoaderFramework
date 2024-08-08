Overview

This project provides a Python library for loading data from a CSV file into a MySQL database. The library is modularized into different classes for handling database operations, logging metadata, and loading data. The database schema includes tables for athletes, teams, events, games, and participations, with a metadata table to track load operations.

Database Entities

	1.	Athlete
		AthleteID: Unique identifier for the athlete.
		Name: Name of the athlete.
		Sex: Sex of the athlete.
		Age: Age of the athlete.
	2.	Team
		TeamID: Unique identifier for the team.
		TeamName: Name of the team.
		NOC: National Olympic Committee code.
		Unique Constraint: Combination of TeamName and NOC must be unique.
	3.	Event
		EventID: Unique identifier for the event.
		Sport: Name of the sport.
		EventName: Name of the event.
		Unique Constraint: Combination of Sport and EventName must be unique.
	4.	Game
		GameID: Unique identifier for the game.
		Games: Name of the games (e.g., “Olympic Games”).
		Year: Year of the games.
		Season: Season of the games (e.g., “Winter”).
		City: City where the games were held.
		Unique Constraint: Combination of Games, Year, Season, and City must be unique.
	5.	Participation
		ParticipationID: Unique identifier for the participation record.
		AthleteID: ID of the athlete (foreign key).
		TeamID: ID of the team (foreign key).
		EventID: ID of the event (foreign key).
		GameID: ID of the game (foreign key).
		Medal: Medal won (if any).
	6.	LoadMetadata
		LoadID: Unique identifier for the load operation.
		SourceFile: Name of the source file.
		Timestamp: Timestamp of the load operation.
		RecordID: ID of the record being loaded.
		Status: Status of the load operation (e.g., “Success” or “Error”).
		ErrorMessage: Error message (if any).

Requirements:

	•	Python 3.6+
	•	MySQL database
	•	Required Python packages (can be installed using requirements.txt)
Setup
1. Unzip and copy the code to required folder. 

2. Install Required Packages

pip install -r requirements.txt

3. Database Setup

Create the MySQL database and tables using the following DDL script.

schema.sql

4. To run the data loader package, 

    1. Update the startup.py with username, password details for the database db_url
    2. Update the startup.py with updated csv_file_1 and csv_file_2
    3. To run, run command python run.py. this invokes the dataloader project and loads the data . 
For the dump, 

mysqldump -u username -p olympics_db > olympics_dump.sql

Enter the password prompted and dump will be created. 
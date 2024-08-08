from dataloader_library.database_manager import get_engine,get_session
from dataloader_library.metadata_logger import MetadataLogger
from dataloader_library.data_loader import DataLoader
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    print("Started...")
    db_url = 'mysql+pymysql://user:password@localhost/olympics_db'
    engine = get_engine(db_url)
    session = get_session(engine)

    
    metadata_logger = MetadataLogger(session)
    data_loader = DataLoader(db_url, metadata_logger)

    csv_file_1 = '..path/archive/Athletes_summer_games.csv'
    csv_file_2 = '..path/archive/Athletes_winter_games.csv'
    data_loader.load_data(csv_file_1)
    data_loader.load_data(csv_file_2)

    print("... Data Loaded Succesfully...")

if __name__ == "__main__":
    main()
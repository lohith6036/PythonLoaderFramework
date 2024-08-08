from datetime import datetime
from sqlalchemy.orm import Session
from dataloader_library.database_manager import LoadMetadata

class MetadataLogger:
    def __init__(self, session: Session):
        self.session = session

    def log_success(self, source_file, record_id):
        metadata_record = LoadMetadata(
            SourceFile=source_file,
            Timestamp=datetime.now(),
            RecordID=record_id,
            Status='Success',
            ErrorMessage=None
        )
        self.session.add(metadata_record)
        self.session.commit()

    def log_error(self, source_file, record_id, error_message):
        metadata_record = LoadMetadata(
            SourceFile=source_file,
            Timestamp=datetime.now(),
            RecordID=record_id,
            Status='Error',
            ErrorMessage=error_message
        )
        self.session.add(metadata_record)
        self.session.commit()
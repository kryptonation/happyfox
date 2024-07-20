# models.py

import logging

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base = declarative_base()

class Email(Base):
    """
    Email model representing the emails table in the database.
    """
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    from_address = Column(String)
    subject = Column(String)
    message = Column(Text)
    received_date = Column(DateTime)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def store_email(email_data):
    """
    Stores an email in the database.

    Args:
        email_data: Dictionary containing email details.
    """
    try:
        new_email = Email(
            from_address=email_data.get('from', 'unknown'),
            subject=email_data.get('subject', 'No Subject'),
            message=email_data.get('message', ''),
            received_date=email_data.get('received_date')
        )
        session.add(new_email)
        session.commit()
        logger.info(f"Stored email from {new_email.from_address}")
    except Exception as e:
        logger.error(f"Error storing email: {e}")
        session.rollback()

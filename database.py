from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = "postgresql://username:password@localhost/dbname"

# Create a new database engine instance
engine = create_engine(DATABASE_URL)

# Base class for declarative models
Base = declarative_base()

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()
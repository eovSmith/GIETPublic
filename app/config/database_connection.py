# Imports the database engine creator from sqlalchemy
from sqlalchemy import create_engine
# Import the base declarative method from sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
# Import the session creator from sqlachemy
from sqlalchemy.orm import sessionmaker
# Import the loggins module to generate info of the running process 
import logging
# Import the os to get access to the path methods and the getenv methos
import os
# Import from dotnev the load_dotenv method to load the .env file 
from dotenv import load_dotenv

# Loads the .env file and gives the dinamic url using the join() method from os.path
load_dotenv(os.path.join("config",".env"))
# Creates a engine with the provided direction from the env file
engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URL")) 
# Creates a database Session with the created engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Session that 
# Creates an instance of the declarative base
Base = declarative_base()


def db_session() -> None:
    """_Generator for the local session conection to the database_"""
    try:
        # Create the instance of the Local Session from sqlalchemy
        session = SessionLocal()
        # Generates the session 
        yield session
    finally:
        # Finally it closes the session
        session.close()


async def init_db() -> None:
    """_Method that inits the database wend the system startup _"""
    try:       
        # Use the create_all to create the tables (args: engine)
        Base.metadata.create_all(engine)
    except Exception as e:
        # If there is any exception returns a log with the error description
        logging.error(f" An error has ocurred on the database {str(e)}")

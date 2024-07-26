# Import the drivers table
from models.driver_models import DriverDB
# Import the vecycles table
from models.vecycles_models import VecyclesDB 
# Import the vecycle pydantic schema
from schemas.vecycle_schemas import VecycleCreate, VecycleSearch
# Import the database Session
from config.database_connection import db_session
# Import the Session from sqlalchemy for parameter validations
from sqlalchemy.orm import Session
# Import the search method conditioners
from sqlalchemy import (and_ , or_)
# Import the type return data
from typing import List , Union
# Import jsonable_encoder to convert the data to json
from fastapi.encoders import jsonable_encoder

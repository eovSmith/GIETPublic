# Import the vecycle table
from models.vecycles_models import VecyclesDB
# Import the driver table
from models.driver_models import DriverDB
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
# Import Integrity Error for the validation
from sqlalchemy.exc import IntegrityError
# Import the DriverDB model
from models.driver_models import DriverDB


"-----------------------------------------------------------------------VECYCLE_SERVICES-----------------------------------------------------------------------"


def create_new_vecycle(vecycle: VecycleCreate, db_session: Session) -> dict:
    
    
    """_The create new vecycle method_
    
    Args:
        vecycle (VecycleCreate): _The vecycle data_
        db_session (Session): _The database session_
    Returns:
        dict: _The response of the vecycle created_
        or
        dict: _The response of the  error with the system exception_
    
    """
    
    
    try:
        # Create the new vecycle instance
        new_vecycle = VecyclesDB(**vecycle.model_dump())
        # Add the new vecycle to the database
        db_session.add(new_vecycle)
        # Commit the changes to the database
        db_session.commit()
        # Refresh the new vecycle instance
        db_session.refresh(new_vecycle)
        # Return the response of the vecycle created
        return {"success": "Vecycle created successfully"}
    except IntegrityError:
        # If there is any integrity error during the process
        return {"error": "Vecycle already exists"}
    # If there is any excetion during the process
    except Exception as e:
        # Return the response of the  error with the system exception
        return {"error": str(e)}


def search_vecycle_in_db(search: VecycleSearch, db_session: Session) -> dict:
    
    
    """_The search vecycle method_

    Args:
        search (VecycleSearch): _The vecycle data_
        db_session (Session): _The database session_
    Returns:
        dict: _The response of the vecycle found or the error with the system exception_

    """
    
    
    try:
        fields = []
        # Iterate in the dict obtained from the schema with the method model_dump
        for key, value in search.model_dump(exclude_none=True).items():
            if value:
                # With the geattr() method obtains the field in the db model and add the condition with ilike() method
                fields.append(getattr(VecyclesDB, key).ilike(f"%{value}%"))
        if fields:
            # Search the match in the database with the filter method and the fields list
            results = db_session.query(VecyclesDB).filter(and_(*fields)).all()
            # If there is any match
            if results:
                # Returns it
                return  {"results": results}
            # If not
            else:
                # Returns a not found response
                return {"not_found": "Dont match any"}
    # If there is any exceptions
    except Exception as e:
        # Returns a dict with the exception description
        return {"error": str(e)}
    

def delete_existent_vecycle(vecyclePlate: str, db_session: Session) -> dict:
    
    
    """_Delete an existent vecycle in the database_
    Args:
        vecyclePlate (str): The plate of the vecycle
        db_session (Session): The database session
    Returns:
        dict: A dict with the response
        or 
        dict: A dict with the exception description
    """
    
    
    try:
        # Search the vecycle in the database with the filter method and the plate
        vecycle = db_session.query(VecyclesDB).get(vecyclePlate)
        # If the vecycle exists
        if vecycle:
            # Delete it
            db_session.delete(vecycle)
            # Commit the changes
            db_session.commit()
            # Returns a dict with the vecycle plate
            return {"success": "vecycle deleted"}
        # If not
        else:
            # Returns a not found response
            return {"not_found": "Dont match any"}
    # If there is any exceptions
    except Exception as e:
        # Returns a dict with the exception description
        return {"error": str(e)}


def vecycle_assign_driver(vecyclePlate: str, driverCid: str, db_session: Session) -> dict:
    
    
    """_Assign a driver to the desired vecycle_
    Args:
        vecyclePlate (str): The plate of the vecycle
        driverCid (str): The cid of the driver
        db_session (Session): The database session
    Returns:
        dict: A dict with the vecycle plate and the driver cid
        or
        dict: A with the exception description
    """
    
    
    try:
        # Search the vecycle in the database with the filter method and the plate
        vecycle = db_session.query(VecyclesDB).get(vecyclePlate)
        # Search the driver in the database with the filter method and the cid
        driver = db_session.query(DriverDB).get(driverCid)
        # If the vecycle and the driver exists
        if vecycle and driver:
            # Assign the driver to the vecycle
            vecycle.driver = driver
            # Commit the changes
            db_session.commit()
            # Returns a dict with the vecycle plate
            return {"success": "Driver assigned to vecycle"}
        # If not
        else:
            # Returns a not found response
            return {"error": "Vecycle or driver not found"}
    # If an exception is raised
    except Exception as e:
        # Returns a dict with the exception description
        return {"error": str(e)}


def delete_all_existent_vecycles(db_session: Session) -> dict:
    
    
    """_Delete all the existent vecycles in the database _

     Args:
        db_session (Session): _The database session_

    Returns:
        dict: _The Response message_
    """
    
    
    try:
        # Delete all the vecycles in the database
        db_session.query(VecyclesDB).delete()
        # Commit the changes
        db_session.commit()
        # Returns a dict with the success message
        return {"success": "All vecycles deleted"}
    # If an exception is raised
    except Exception as e:
        # Returns a dict with the exception description
        return {"error": str(e)}


def list_existent_vecycles(db_session: Session) -> dict:
    """_List the existent vecycles in the database_

    Args:
        db_session (Session): _The database session_

    Returns:
        List[UsersDB] or dict: _The list of data_
    """
    try:
        # Gets the list of elements in the database
        respond = db_session.query(VecyclesDB).all()
        # If there is data
        if respond:
            # Returns the list of elements
            return {"data": respond}
        # If not
        else:
            # Returns a message with the information
            return {"message": "The data is empty"}
    # If there is any exception during the process
    except Exception as e:
        # Returns a dict with the exception description
        return {"error": str(e)}


def vecycle_get_driver(vecyclePlate: str, db_session: Session) -> dict:
    """_Gets the assigned driver to the especified vecyle_

    Args:
        vecyclePlate (str): _The vecycle licence Plate_
        db_session (Session): _The database session_

    Returns:
        DriverDB: _Driver instance in the vecycle_
    """
    
    try:
        # Gets the desired vecycle 
        vecycle = db_session.query(VecyclesDB).get(vecyclePlate)
        # Gets the driver assigned to the selected vecycle
        assignedDriver = vecycle.driver
        # Returns the driver
        return {"driver": assignedDriver}
    # If there is any exception during the process
    except Exception as e:
        # Returns a dict with the exception descriptiom
        return {"error": str(e)}
    
    
"-----------------------------------------------------------------------VECYCLE_SERVICES-----------------------------------------------------------------------"
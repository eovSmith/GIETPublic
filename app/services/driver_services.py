# Import the drivers table
from models.driver_models import DriverDB
# Import the Driver database model
from models.driver_models import DriverDB
# Import the driver Schemas
from schemas.driver_schemas import DriverCreate, DriverSearch
# import the Session class
from sqlalchemy.orm import Session
from sqlalchemy.sql import and_
from sqlalchemy.exc import IntegrityError


"------------------------------------------------------------------------DRIVER SERVICES--------------------------------------------------------------------------------------------------------------------------------------------------"


def create_new_driver(newdriver: DriverCreate, db_session: Session) -> dict:
    
    
    """_The create new driver method_
    
    Args:
        newdriver (DriverCreate): _The driver data_
        db_session (Session): _The database session_
    Returns:
        dict: _The response of the vecycle created_
        or
        dict: _The response of the  error with the system exception_
    
    """
    
    
    try:
        # Create the new driver instance
        new_driver = DriverDB(**newdriver.model_dump())
        # Add the new driver to the database
        db_session.add(new_driver)
        # Commit the changes to the database
        db_session.commit()
        # Refresh the new driver instance
        db_session.refresh(new_driver)
        # Return the response of the driver created
        return {"success": "Driver created successfully"}
    # If there is any excetion during the process
    except IntegrityError :
        # Return the response of the  error with the system exception
        return {"error": "Driver already exists"}
    except Exception as e:
        # Return the response of the  error with the system exception
        return {"error": str(e)}


def search_driver_in_db(search: DriverSearch, db_session: Session) -> dict:
    
    
    """_The search vecycle method_

    Args:
        search (DriverSearch): _The driver data_
        db_session (Session): _The database session_
    Returns:
        dict: _The response of the found driver or the error with the system exception_

    """
    
    
    try:
        fields = []
        # Iterate in the dict obtained from the schema with the method model_dump
        for key, value in search.model_dump(exclude_none=True).items():
            if value:
                # With the geattr() method obtains the field in the db model and add the condition with ilike() method
                fields.append(getattr(DriverDB, key).ilike(f"%{value}%"))
        if fields:
            # Search the match in the database with the filter method and the fields list
            results = db_session.query(DriverDB).filter(and_(*fields)).all()
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
    

def delete_existent_driver(driverCid: str, db_session: Session) -> dict:
    
    
    """_Delete an existent driver in the database_
    Args:
        driverCid (str): The driver's cid
        db_session (Session): The database session
    Returns:
        dict: A dict with the response
        or 
        dict: A dict with the exception description
    """
    
    
    try:
        # Search for the driver in the database with the filter method and the plate
        driver = db_session.query(DriverDB).get(driverCid)
        # If the driver exists
        if driver:
            # Delete it
            db_session.delete(driver)
            # Commit the changes
            db_session.commit()
            # Returns a dict with the vecycle plate
            return {"success": "Driver deleted"}
        # If not
        else:
            # Returns a not found response
            return {"not_found": "Dont match any"}
    # If there is any exceptions
    except Exception as e:
        # Returns a dict with the exception description
        return {"error": str(e)}



def delete_all_existent_drivers(db_session: Session) -> dict:
    
    
    """_Delete all the existent drivers in the database _

     Args:
        db_session (Session): _The database session_

    Returns:
        dict: _The Response message_
    """
    
    
    try:
        # Delete all the drivers in the database
        db_session.query(DriverDB).delete()
        # Commit the changes
        db_session.commit()
        # Returns a dict with the success message
        return {"success": "All drivers deleted"}
    # If an exception is raised
    except Exception as e:
        # Returns a dict with the exception description
        return {"error": str(e)}


def list_existent_drivers(db_session: Session) -> dict:
    """_List the existent drviers in the database_

    Args:
        db_session (Session): _The database session_

    Returns:
        List[UsersDB] or dict: _The list of data_
    """
    try:
        # Gets the list of elements in the database
        respond = db_session.query(DriverDB).all()
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



"------------------------------------------------------------------------DRIVER SERVICES--------------------------------------------------------------------------------------------------------------------------------------------------"
# Import the users table
from models.users_models import UsersDB
# Import the users pydantic schema
from schemas.primary_schemas import UserCreate, UserSearch, UserChangePassword
# Import the database Session
from config.database_connection import db_session
# Import the Session from sqlalchemy for parameter validations
from sqlalchemy.orm import Session
# Import the search method conditioners
from sqlalchemy import (and_ , or_)
# Import the type return data
from typing import List , Union
# Import bcrypt to encrypt the passwordsS
import bcrypt
# Import jsonable_encoder to convert the data to json
from fastapi.encoders import jsonable_encoder


"------------------------------------------------------------------------USER SERVICES--------------------------------------------------------------------------------------------------------------------------------------------------"
def create_new_user(newUser: UserCreate, db_session: Session) -> dict:
    """_The create new user method_

    Args:
        newUser (UserCreate): _The schema of the new user_
        db_session (Session): _The sqlalchemy session_

    Returns:
        dict: _ The success or error description of the action _
    """
    try:
        # First search if the user existe in the database 
        dummyUser = UserSearch(id=newUser.id)
        check = search_user_in_db(search=dummyUser, db_session=db_session)
        # If the search gets any resutls
        if check.get("results"):
            # Returns the error that the user already exist in the database
            return {"error": " User already exist in database"}
        # Gets a dict of the UserCreate schema using the model_dump() method
        newData = newUser.model_dump()
        # Generate a salt for the encryptation
        salt = bcrypt.gensalt()
        # Encrypt the existent password using bcrypt.hashpw() method
        hashedPassword = bcrypt.hashpw(newData.get("password").encode("utf-8"),salt)
        # Updates the existent dict
        newData.update({"password": hashedPassword})
        # Create a new instance of the UserDB model using the deconstruct of the created dict
        new = UsersDB(**newData)
        # Add the new instance to the desired table with the add() method
        db_session.add(new)
        # Commit the changes
        db_session.commit()
        # And refresh the data
        db_session.refresh(new)
        # Finally it returns a dict message with the name of the new user
        return {"success": f"{newUser.firstName} {newUser.lastName}"}
    # If there is any exceptions
    except Exception as e:
        # Returns a dict with the exception description
        return {"error": str(e)}


def search_user_in_db(search: UserSearch, db_session: Session) -> dict:
    """_Search an user into the database making a filter with parameters and returns it_

    Args:
        search (UserSearch): _An search squeme with the fields and the values to filter_
        db_session (Session): _The sqlalchemy session_

    Returns:
        UsersDB or List[UsersDB]: _Returns a UserDB object or a list of UserDB objects if there are more than one match_
    """
    try:
        fields = []
        # Iterate in the dict obtained from the schema with the method model_dump
        for key, value in search.model_dump(exclude_none=True).items():
            if value:
                # With the geattr() method obtains the field in the db model and add the condition with ilike() method
                fields.append(getattr(UsersDB, key).ilike(f"%{value}%"))
        if fields:
            # Search the match in the database with the filter method and the fields list
            results = db_session.query(UsersDB).filter(and_(*fields)).all()
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
    

def delete_existent_user(userId: str, db_session: Session) -> dict:
    """_Delete an especific existetent instnace of the UserDB database model _

    Args:
        userId (str): _The id of the instance to delete_
        db_session (Session): _The sqlalchemy session_

    Returns:
        dict: _description_
    """
    try:
        # Finds the desired user to delete with the get() method that takes the id
        userToDelete = db_session.query(UsersDB).get(userId)
        # If the user exist in the database
        if userToDelete:
            # Deletes the instance in the database with the delete method
            db_session.delete(userToDelete)
            # Commit the changes
            db_session.commit()
            # Return a dict confirmation message
            return {"success": "User Deleted"}
        # If not exist in the database
        else:
            # Returns the not exist error
            return {"error": "User dont exist in the database"}
     # If there is any exceptions
    except Exception as e:
        # Returns a dict with the exception description
        return {"error": str(e)}


def change_existent_password(passwords: UserChangePassword, id: str, db_session: Session) -> dict:
    """_Updates the existen password of an especific user_

    Args:
        passwords (UserChangePassword): _The user schema with the new password_
        id (str): _the user cid_
        db_session (Session): _Te database session_

    Returns:
        dict: _success messages or errors messages_
    """
    try:
        # User the shema method check to check if the passwords in the schema are equals
        check = passwords.check()
        # If are equals
        if check:
            # Gets the user with the id
            userToCHange = db_session.query(UsersDB).filter(UsersDB.id == id).first()
            # If the user exist
            if userToCHange:
                # Generates a salt for the encrypting method
                salt = bcrypt.gensalt()
                # Encripts the new password
                hashedNew = bcrypt.hashpw(passwords.planePassword.encode("utf-8"),salt)
                # Changes the existen password
                userToCHange.password = hashedNew
                # Commits the changes
                db_session.commit()
                # Returns the success respond
                return {"success": "Password Changed"}
            # If the user dont exist in the database
            else:
                # Returns a non existent message
                return {"not_exystent": "User not in the database"}
        # If the passwords are not equals
        else: 
            # Returns a error response
            return {"error": "Not equal passwords"}
    # If there is any exception during the process
    except Exception as e:
       # Returns a dict with the exception description
        return {"error": str(e)}


def list_existent_users(db_session: Session) -> dict:
    """_List the existent users in the database_

    Args:
        db_session (Session): _The database session_

    Returns:
        List[UsersDB] or dict: _The list of data_
    """
    try:
        # Gets the list of elements in the database
        respond = db_session.query(UsersDB).all()
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


def delete_all_existent_users(db_session: Session) -> dict:
    """_Delete all the existent users in the database_

    Args:
        db_session (Session): _The database session_

    Returns:
        dict: _The Response message_
    """
    try:
        # Execute the delete query
        db_session.query(UsersDB).delete()
        # Commit the changes in the database
        db_session.commit()
        # Returns a success message
        return {"success": "Data cleaned"}
    # If there is any exception during the process
    except Exception as e:
        # Returns a dict with the exception description
        return {"error": str(e)}
        
"------------------------------------------------------------------------USER SERVICES--------------------------------------------------------------------------------------------------------------------------------------------------"
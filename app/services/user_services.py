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
# Import bcrypt to encrypt the passwords
import bcrypt


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
        dummyUser = UserSearch(id= newUser.id)
        check = search_user_in_db(search=dummyUser, db_session= db_session)
        if check:
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
    except Exception as e:
        # If there is any exceptions returns a dict with the exception description
        return {"error": str(e)}


def search_user_in_db(search: UserSearch, db_session: Session) -> UsersDB or List[UserCreate] :
    """_Search an user into the database making a filter with parameters and returns it_

    Args:
        search (UserSearch): _An search squeme with the fields and the values to filter_
        db_session (Session): _The sqlalchemy session_

    Returns:
        UsersDB or List[UsersDB]: _Returns a UserDB object or a list of UserDB objects if there are more than one match_
    """
    fields = []
    try:
        # Iterate in the dict obtained from the schema with the method model_dump
        for key, value in search.model_dump(exclude=None):
            if value and value.strip():
                # With the geattr() method obtains the field in the db model and add the condition with ilike() method
                fields.append(getattr(UsersDB, key).ilike(f"%{value}%"))
        if fields:
            # Search the match in the database with the filter method and the fields list
            results = db_session.query(UsersDB).filter(and_(*fields)).all()
            if results:
                # If there is any match returns it
                return results
            else:
                # If there is no match returns all the data
                return db_session.query(UsersDB).all()
    except Exception as e:
        # If there is any exceptions returns a dict with the exception description
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
        # Deletes the instance in the database with the delete method
        db_session.delete(userToDelete)
        # Commit the changes
        db_session.commit()
        # And refresh the data
        db_session.refresh(userToDelete)
        # Return a dict confirmation message
        return {"succes": "User Deleted"}
    except Exception as e:
        # If there is any exceptions returns a dict with the exception description
        return {"error": str(e)}


def change_existent_password(passwords: UserChangePassword, id: str, db_session: Session) -> dict:
    try:
        check = passwords.check()
        if check:
            userToCHange = db_session.query(UsersDB).filter(UsersDB.id == id).first()
            if userToCHange:
                salt = bcrypt.gensalt()
                hashedNew = bcrypt.hashpw(passwords.planePassword.encode("utf-8"),salt)
                userToCHange.password = hashedNew
                db_session.commit()
                return {"succes": "Password Changed"}
            else:
                return {"not_exystent": "User not in the database"}
        else: 
            return {"error": "Not equal passwords"}
    except Exception as e:
        return {"error": str(e)}


def list_existent_users(db_session: Session) -> List[UsersDB] or dict:
    try:
        respond = db_session.query(UsersDB).all()
        return respond
    except Exception as e:
        return {"error": str(e)}
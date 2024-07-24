# Import the Base model class for the creation of the schemes and the Field class for validations
from pydantic import (BaseModel, Field, field_validator, validator)
# Import the Optional class for the definition of opcional fields
from typing import Optional
# Import the re python module for the match of regular expressions
import re


# Clase Constants
VALID_ROLES = ("U", "T", "A")

class UserCreate(BaseModel):
    """_The User Schema for validation and the creation of a new instance _
    
    id: The users CID and Primary key for the users table (example "71061412256")
    firstName: The users first name (example "John")
    lastName: The users last name (example "Doe")
    password: The hashed user password in the system 
    email: The email direction of the user (example "example@gmail.com")
    role: The user role im the system (U(for "User"), T(for "Tecnic") and A( for "Admin"))
    isActive: The status of the user in the system (active "True" and inactive "False") 
    
    
    """
    
    
    id: str = Field(..., description="The CID for the users, and they primary key", max_length=11, min_length=11, examples=["00020621212", "99030188921", "73072381233"])
    firstName: str = Field(..., description="The users primary name", max_length=255, min_length=1, examples=["Juan", "Pedro", "Carlos"])
    lastName: str = Field(..., description="The users last name", max_length=255, min_length=1, examples=["García", "Perales", "Smith"])
    password: str = Field(...,description="The user password", max_length=255, min_length=8)
    email: str = Field(..., description="The users email dir", max_length=255, min_length=1, examples=["ejemplo@gmail.com", "otroejemplo@gmail.com"], )
    role: str = Field(..., description="The users category", max_length=1)
    isActive: bool = Field(..., description="The status of the user")
    
    
    @field_validator("id")
    def validate_cid_data(cls, v: str) -> str:
        """_Validator for the users id_"""
        # Delete the whitespaces
        data = v.strip()
        # Validate that the id must have only 11 numbers
        if not len(data) == 11 or not data.isdigit():
            # Raises a Value error wen it does not satisfaces the conditions
            raise ValueError(" The id can only contain 11 numbers")
        else:
            # If the data is valid returns the data without the whitespaces
            return data
    
    
    @field_validator("role")
    def validate_role_data(cls, v: str) -> str:
        """_Validator for the role_"""
        # Validates that the data is a valid role
        if not v in VALID_ROLES:
            # Raises a Value error wen it does not satisfaces the conditions
            raise ValueError(" The user must have a valid role ")
        else:
            # If the data is valid returns the data
            return v
    
    
    @field_validator("firstName")
    def validate_firtsName_data(cls, v: str) -> str:
        """_Validator for the users first name_"""
        # Delete the whitespaces
        data = v.strip()
        # Validate the format of the name
        if not isinstance(data, str) or not bool(re.fullmatch(r'^[a-zA-Z]+$', v)):
            # Raises a Value error wen it does not satisfaces the conditions
            raise ValueError(" The first name must be in a correct format")
        else : 
            # If the data is valid returns the data
            return v
        
        
    @field_validator("lastName")
    def validate_lastName_data(cls, v: str) -> str:
        """__Validator for the users last name__"""
        # Delete the whitespaces
        data = v.strip()
        # Validate the format of the name
        if not isinstance(data, str) or not bool(re.fullmatch(r'^[a-zA-Z]+$', v)):
            # Raises a Value error wen it does not satisfaces the conditions
            raise ValueError(" The last name must be in a correct format")
        else : 
            # If the data is valid returns the data
            return v
     
     
    @field_validator("password")
    def validate_password_data(cls, v: str) -> str:
        """_Validator for the user password_"""
        # Validate that the length of the password must be longer than 8
        if len(v)<8:
            # Raises a Value error wen it does not satisfaces the conditions
            raise ValueError(" The password must be with at least 8 characters")
        else: 
            # If the data is valid returns the data
            return v   


    @field_validator("email")
    def validate_email_data(cls, v: str) -> str:
        """__Validator for the users email__"""
        # Delete the whitespaces
        data = v.strip()
        # Validate that the email must be in a valid format
        if not isinstance(data, str) or not bool(re.fullmatch(r'^[\w\.-]+@[\w\.-]+\.\w+$', data)):
            # Raises a Value error wen it does not satisfaces the conditions
            raise ValueError(" The email must be in a valid format ")
        else:
            # If the data is valid returns the data
            return data
        
        
class UserSearch(BaseModel):
    """_The user schema for search an instance in the database_
    
    
    id: The users CID and Primary key for the users table (example "71061412256")
    firstName: The users first name (example "John")
    lastName: The users last name (example "Doe")
    email: The email direction of the user (example "example@gmail.com")
    
    
    """
    id: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None 
    email: Optional[str] = None


class UserLogin(BaseModel):
    """
    
    _The user schema for system authentication_
    
    email: The email direction of the user (example "example@gmail.com")
    planePassword: The known user only password
    
    
    """
    
    email: Optional[str] = None
    planePassword: Optional[str] = None


class UserChangePassword(BaseModel):
    """_The user schema for changing the current password in the system_
    
    planePassword: The known user only password
    planePasswordRepeat: The known user only password confirmation
    """
    
    planePassword: str
    planePasswordRepeat: str
    
    @classmethod
    def check(self) -> bool:
        """_Checks if the passwords are equals_"""
        # returns the value of the bool condition
        return self.planePassword == self.planePasswordRepeat
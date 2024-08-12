# Import the Base model class for the creation of the schemes and the Field class for validations
from pydantic import (BaseModel, Field, field_validator)
# Import the Optional class for the definition of opcional fields
from typing import Optional
# Import datemtime.date for date parameters
from datetime import date
# Import re for regular expressions
import re


"-------------------------------------------------------------------------------DRIVER_SCHEMAS----------------------------------------------------------------------------------------------------------------------------------------------"


class DriverCreate(BaseModel):
    """_Schema for create new Drivers _


    cid : The driver id (example: 88031088523)
    firstName: The driver first name (example: Juan)
    lastName: The driver last name (example: Perez)
    licenceNumber: The driver licence number (example: 1234567890)
    jobPosition: The driver job position (example: Reparter)
    
    
    """
    cid: str = Field(..., description="The user cid", min_length=11, max_length=11)
    firstName: str = Field(..., description="The user first name", min_length=2, max_length=255)
    lastName: str = Field(..., description="The user last name", min_length=2, max_length=255)
    licenceNumber: str = Field(..., description="The user licence number", min_length=8, max_length=8)
    jobPosition: str = Field(..., description="The user job position", min_length=2, max_length=255)
    
    
    @field_validator('cid')
    def validate_cid(cls, v: str)  -> str:
        """_The cid validator_"""
       # Check if the cid is empty
        if not v.strip():
            # If empty raise an error
            raise ValueError('cid is required')
        # Check if the cid is a 11 digits number
        if not re.match(r'^\d{11}$', v):
            # If not raise an error
            raise ValueError('cid must be a 11 digits number')
        # If everything is ok return the cid
        return v
    
    @field_validator("firstName")
    def validate_firstName(cls, v: str):
        """_The firtsName validator_"""
        # Check if the firstName is empty
        if not v.strip():
            # If empty raise an error
            raise ValueError('firstName is required')
        # Check if the firstName is text only
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$', v):
            # If not raise an error
            raise ValueError('firstName must be text only')
        # If everything is ok return the firstName
        return v
    
    
    @field_validator("lastName")
    def validate_lastName(cls, v: str)  -> str:
        """_THe lastName Validator_"""
        # Check if the lastName is empty
        if not v.strip():
            # If empty raise an error
            raise ValueError("lastName required")
        # Check if the lastName is text only
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$', v):
            # If not raise an error
            raise ValueError("lastName must be text only")
        # If everything is ok return the lastName
        return v
    
    
    @field_validator("licenceNumber")
    def validate_licenceNumber(cls, v: str) -> str:
        """_The licenceNumber Validator_"""
        # Check if the licenceNumber is empty
        if not v.strip():
            # If empty raise an error
            raise ValueError("licenceNumber is required")
        # Check if the licenceNumber is alphanumeric only
        if not re.match(r'^[a-zA-Z0-9]*$', v):
            # If not raise an error
            raise ValueError("licenceNumber must be alphanumeric only")
        # If everything is ok return the licenceNumber
        return v


class DriverSearch(BaseModel):
    
    
    """_The schema for search drivers in the db_
    
    cid : The driver id (example: 88031088523)
    firstName: The driver first name (example: Juan)
    lastName: The driver last name (example: Perez)
    licenceNumber: The driver licence number (example: 1234567890)
    jobPosition: The driver job position (example: Reparter)
    vecycle: The assigned driver vecycle (example: 1234567890)
    
    
    """
    cid: str
    firstName: str
    lastName: str 
    licenceNumber: str
    jobPosition: str 
    vecycle: str
    
    
    
"-------------------------------------------------------------------------------DRIVER_SCHEMAS----------------------------------------------------------------------------------------------------------------------------------------------"
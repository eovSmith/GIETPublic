# Import the Base model class for the creation of the schemes and the Field class for validations
from pydantic import (BaseModel, Field, field_validator)
# Import the Optional class for the definition of opcional fields
from typing import Optional
# Import datemtime.date for date parameters
from datetime import date
# Import re for regular expressions
import re


"-------------------------------------------------------------------------------VECYCLE_SCHEMAS----------------------------------------------------------------------------------------------------------------------------------------------"
class VecycleCreate(BaseModel):
    """_The schema for create new vecycles_


    licencePlate: The licence plate of the vecycle (example: B234123)
    vecycleType: The type of the vecycle (example: Van)
    brand: The brand of the vecycle (example: Peugeot)
    model: The model of the vecycle (example: Partner)
    countryOfOrigin: The vecycle country of origin (example: France)
    ficav: The date of the technical revision validity of the vecycle (example: 15-07-2024)
    lot: The date of the operating license validity of the vecycle (example: 06-10-2024) 
    
      
    """
    licencePlate: str = Field(..., description="The vecycle licence plate and its id",min_length=8)
    vecycleType: str = Field(..., description=" The type of vecycle", max_length=12)
    brand: str = Field(..., description="The brand of the vecycle", max_length=255)
    model: str = Field(..., description="The model of the vecycle", max_length=255)
    countryOfOrigin: str = Field(..., description="The vecycle country of origin", max_length=255)
    ficav: date = Field(..., description="The date of the technical revision validity of the vecycle")
    lot: date = Field(..., description="The date of the operating license validity of the vecycle ")
    
    
    @field_validator("ficav", "lot")
    def validate_dates(cls, value: date) -> date:
        """_Validator for the ficav and the operative licence _"""
        # Check if the date is empty
        if not value:
            # if empty raise an Value error
            raise ValueError("Date field cannot be empty")
        # If everything is ok
        else:
            # return value
            return value
        
    
    @field_validator("licencePlate")
    def validate_licence_plate(cls, value: str):
        """_Validator for the licence Plate _"""
        # Check if the licence plate is empty
        if not value.strip():
            # if empty raise an Value error
            raise ValueError("Licence plate field cannot be empty")
        # Check if the licence plate is in the correct format
        if not re.match(r"\d{8}", value):
            # If is not in the correct format raise an Value error
            raise ValueError("Invalid licence plate format. Please use 8 digits")
        # If everything is ok
        else:
            # return value
            return value
    
    
    @field_validator("countryOfOrigin")
    def validate_country_of_origin(cls, value: str) -> str:
        """_Validator for the country of origin_"""
        # Check if the country of origin is empty
        if not value.strip():
            # if empty raise an Value error
            raise ValueError("Country of origin field cannot be empty")
        # Check if the country of origin is in the correct format
        if not re.match(r"^[a-zA-Z\s]*$", value):
            # If is not in the correct format raise an Value error
            raise ValueError("Invalid country of origin format. Please use letters and spaces only")
        # If everything is ok
        else:
            # return value
            return value
        
    
    @field_validator("vecycleType")
    def validate_type_of_vehicle(cls, value: str) -> str:
        """_Validator for the vecicle type _"""
        # Check if the type of vehicle is empty
        if not value.strip():
            # if empty raise an Value error
            raise ValueError("Type of vehicle field cannot be empty")
        # Check if the type of vehicle is in the correct format
        if not re.match(r"^[a-zA-Z\s]*$", value):
            # If is not in the correct format raise an Value error
            raise ValueError("Invalid type of vehicle format. Please use letters and spaces only")
        # If everything is ok
        else:
            # return value
            return value


    @field_validator("model")
    def validate_model(cls, value: str) -> str:
        """_Validator for the vecycle model_"""
        # Check if the model is empty
        if not value.strip():
            # if empty raise an Value error
            raise ValueError("Model field cannot be empty")
        # if everything is ok
        else:
            # return value
            return value
    
    
    @field_validator("brand")
    def validate_brand(cls, value: str) -> str:
        """_Validator for the vecycle brand_"""
        # Check if the brand is empty
        if not value.strip():
            # if empty raise an Value error
            raise ValueError("Brand field cannot be empty")
        # if everything is ok
        else:
            # return value
            return value
        
class VecycleSearch(BaseModel):
    """ _Schema for the vecycle search_
    
    
    licensePlate: The licence plate of the vecycle (example: B234123)
    vecycleType: The type of the vecycle (example: Van)
    model: The model of the vecycle (example: Transit)
    brand: The brand of the vecycle (example: Ford)
    countryOfOrigin: The country of origin of the vecycle (example: USA)
    
    
    """
    licencePlate: Optional[str] = None
    vecycleType: Optional[str] = None
    model: Optional[str] = None
    brand: Optional[str] = None
    countryOfOrigin: Optional[str] = None
    
    
"-------------------------------------------------------------------------------VECYCLE_SCHEMAS----------------------------------------------------------------------------------------------------------------------------------------------"
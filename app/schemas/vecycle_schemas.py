# Import the Base model class for the creation of the schemes and the Field class for validations
from pydantic import (BaseModel, Field)
# Import the Optional class for the definition of opcional fields
from typing import Optional
# Import datemtime.date for date parameters
from datetime import date



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
    
    
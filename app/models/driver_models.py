# Imports the Base from the database config file
from config.database_connection import Base
# Imports the sql types to use in the database model
from sqlalchemy.types import (String, Boolean, Integer, VARCHAR, Date)
# Imports the Mapped class and the mapped_column method to define the atribute propertys, also the relationship() method to specify the relationships
from sqlalchemy.orm import (Mapped, mapped_column, relationship)
# Imports the ForeignKey class for the relationships id 
from sqlalchemy import ForeignKey



class DriverDB(Base):
    
    """_The Drivers model in the datbase_

   
    cid : The driver id (example: 88031088523)
    firstName: The driver first name (example: Juan)
    lastName: The driver last name (example: Perez)
    licenceNumber: The driver licence number (example: 1234567890)
    jobPosition: The driver job position (example: Reparter)
    vecycle: The assigned driver vecycle (example: B123123)
    
    
    """
    
    
    __tablename__ = "drivers_table"
    cid: Mapped[str] = mapped_column(String(11), primary_key=True)
    firstName: Mapped[str] = mapped_column(String(255), nullable=False)
    lastName: Mapped[str] = mapped_column(String(255), nullable=False)
    licenceNumber: Mapped[str] = mapped_column(String(8), nullable=False)
    jobPosition:  Mapped[str] = mapped_column(String(255), nullable=False)
    vecycle = relationship("VecyclesDB", back_populates="driver", uselist= False)
    
    
    def __repr__(self) -> str:
        # Visual friendly representation for the database data
        return f"< Driver: cid={self.cid} >"
    
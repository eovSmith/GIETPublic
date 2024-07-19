# Imports the Base from the database config file
from config.database_connection import Base
# Imports the sql types to use in the database model
from sqlalchemy.types import (String, Boolean, Integer, VARCHAR, Date)
# Imports the Mapped class and the mapped_column method to define the atribute propertys, also the relationship() method to specify the relationships
from sqlalchemy.orm import (Mapped, mapped_column, relationship)
from sqlalchemy import ForeignKey


class VecyclesDB(Base):
    """_The Vecycles model in the database_
    
    
    licencePlate: The licence plate of the vecycle (example: B234123)
    vecycleType: The type of the vecycle (example: Van)
    brand: The brand of the vecycle (example: Peugeot)
    model: The model of the vecycle (example: Partner)
    countryOfOrigin: The vecycle country of origin (example: France)
    ficav: The date of the technical revision validity of the vecycle (example: 15-07-2024)
    lot: The date of the operating license validity of the vecycle (example: 06-10-2024)
    driver_id: The cid of the driver assigned to the vecycle 
    driver: Is the relationship between the tables
    
    
    """
    __tablename__ = "vecycles_table"
    licencePlate: Mapped[str] = mapped_column(String(8), primary_key=True)
    vecycleType: Mapped[str] = mapped_column(String(12), nullable=False)
    brand: Mapped[str] = mapped_column(String(255), nullable=False)
    model: Mapped[str] = mapped_column(String(255), nullable=False)
    countryOfOrigin: Mapped[str] = mapped_column(String(255), nullable=False)
    ficav: Mapped[Date] = mapped_column(Date(), nullable=False)
    lot: Mapped[Date] = mapped_column(Date(), nullable=False)
    driver_id: Mapped[String] = mapped_column(String(11), ForeignKey("drivers_table.cid"), nullable=True,)
    driver = None
    
    def __repr__ (self) -> str:
        # Visual friendly representation for the database data
        return f"< Vecycle: licPlate={self.licencePlate} >"
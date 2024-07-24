# Imports the Base from the database config file
from config.database_connection import Base
# Imports the sql types to use in the database model
from sqlalchemy.types import (String, Boolean, Integer, VARCHAR, Date)
# Imports the Mapped class and the mapped_column method to define the atribute propertys, also the relationship() method to specify the relationships
from sqlalchemy.orm import (Mapped, mapped_column, relationship)
from sqlalchemy import ForeignKey



class DriverDB(Base):
    
    
    __tablename__ = "drivers_table"
    cid: Mapped[str] = mapped_column(String(11), primary_key=True)
    firstName: Mapped[str] = mapped_column(String(255), nullable=False)
    lastName: Mapped[str] = mapped_column(String(255), nullable=False)
    licenceNumber: Mapped[str] = mapped_column(String(8), nullable=False)
    jobPosition:  Mapped[str] = mapped_column(String(255), nullable=False)
    vecycle_id : Mapped[str] = mapped_column(String(8), ForeignKey("vecycles_table.licencePlate") , nullable=True)
    vecycle = relationship("VecycleDB", back_populates="driver", uselist= False)
    
    
    def __repr__(self) -> str:
        # Visual friendly representation for the database data
        return f"< Driver: cid={self.cid} >"
    
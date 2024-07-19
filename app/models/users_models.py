# Imports the base from de database confirm file
from config.database_connection import Base
# Imports the sql types to use in the model
from sqlalchemy import  (String, BOOLEAN)
# Imports the Mapped class and the mapped_column method to define the atribute propertys, also the relationship() method to specify the relationships
from sqlalchemy.orm import (Mapped, mapped_column, relationship)


class UsersDB(Base):
    """_The user database model_
    
    id: The users CID and Primary key for the users table (example "71061412256")
    firstName: The users first name (example "John")
    lastName: The users last name (example "Doe")
    password: The hashed user password in the system 
    email: The email direction of the user (example "example@gmail.com")
    role: The user role im the system (U(for "User"), T(for "Tecnic") and A( for "Admin"))
    isActive: The status of the user in the system (active "True" and inactive "False") 
     
    """
    __tablename__= "users"
    id : Mapped[str] = mapped_column(String(11), primary_key=True)
    firstName: Mapped[str] = mapped_column(String(255), nullable=False)
    lastName: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False)
    role: Mapped[str] = mapped_column(String(1), nullable=False)
    isActive: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    
    
    def __repr__(self) -> str:
        # Visual friendly representation for the database data
        return f"< User: cid={self.id} name={self.firstName} {self.lasName} email={self.email} >"
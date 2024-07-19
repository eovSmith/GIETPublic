# Import the database Models to relate
from .driver_models import DriverDB
from .vecycles_models import VecyclesDB
# Import the relationship method
from sqlalchemy.orm import relationship


# Models Relationships declarations
DriverDB.vecycle = relationship(VecyclesDB, back_populates="driver", foreign_keys=[DriverDB.vecycle_id], uselist=True)
VecyclesDB.driver = relationship(DriverDB, back_populates="vecycle", foreign_keys=[VecyclesDB.driver_id], uselist=True)
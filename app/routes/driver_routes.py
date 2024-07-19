# Import the API Router class to create the router instance
from fastapi.routing import APIRouter
# Import the fastapi Http request class
from fastapi.requests import Request
# Import the fastapi Jinjatemplate engine for the html template responses
from fastapi.templating import Jinja2Templates
# Import the Driver database model
from models.driver_models import DriverDB


# Create the name of the instance
driver_Router = APIRouter(prefix="/Drivers")

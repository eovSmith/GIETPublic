# Import the API Router class to create the router instance
from fastapi.routing import APIRouter
# Import the fastapi Http request class
from fastapi.requests import Request
# Import the fastapi Jinjatemplate engine for the html template responses
from fastapi.templating import Jinja2Templates
# Import the Vecycle database model
from models.vecycles_models import VecyclesDB


# Create the name of the instance
vecycle_Router = APIRouter(prefix="/Vecycles")
# Import the API Router class to create the router instance
from fastapi.routing import APIRouter
# Import the fastapi Http request class
from fastapi.requests import Request
# Import the fastapi Jinjatemplate engine for the html template responses
from fastapi.templating import Jinja2Templates
# Import the created User Schema
from schemas.primary_schemas import (UserCreate, UserChangePassword, UserLogin, UserSearch)
# Import the User database model
from models.users_models import UsersDB
# Import the HTML response for the html returns and JSONResponse for the dict data
from fastapi.responses import HTMLResponse ,JSONResponse
# Import the services
from services.user_services import (create_new_user, delete_existent_user, search_user_in_db)
# Import the database methods
from fastapi import Depends
from config.database_connection import db_session
from sqlalchemy.orm import Session


# Create the name of the instance
user_Router = APIRouter(prefix="/Users")


@user_Router.get("/login", status_code=200, tags=["User Router"])
async def user_render_login(request: Request) ->None:
    """_Login the user into the system_

    Args:
        request (Request): _The Http Request_
    """
    raise NotImplementedError("Method not implemented yet")


@user_Router.post("/login/post", status_code=200, tags=["User Router"])
async def user_render_login_post(request: Request) ->None:
    """_Get the post of the user and makes an authentication_

    Args:
        request (Request): _The Http Request_
    """
    raise NotImplementedError("Method not implemented yet")


@user_Router.get("/Page", status_code=200, tags=["User Router"])
async def user_render_index_page(request: Request) ->HTMLResponse:
    """_Render the Users main page_

    Args:
        request (Request): _The Http request_

    Raises:
        NotImplementedError: _description_

    Returns:
        Jinja2Templates.TemplateResponse: __
    """
    raise NotImplementedError("Method not implemented yet")


@user_Router.get("/new", status_code=200, tags=["User Router"])
async def user_render_newUserPage(request: Request) ->HTMLResponse:
    """_Render the new User creation page_

    Args:
        request (Request): _The Http Request_

    Returns:
        Jinja2Templates.TemplateResponse: _description_
    """
    raise NotImplementedError("Method not implemented yet")


@user_Router.post("/new", status_code=200, tags=["User Router"])
async def user_render_newUserPage_post(request: Request, newUser: UserCreate, session: Session = Depends(db_session)) ->HTMLResponse:
    
    
    """_Manage the new user creation post_

    Args:
        request (Request): _The Http Request_

    Returns:
        Jinja2Templates.TemplateResponse: _description_
    """
    
    
    try: 
        respond = create_new_user(newUser=newUser, db_session=session)
        if respond["error"]:
            return JSONResponse(content=respond, status_code=401)
        else:
            return JSONResponse(content={"success": "Sucess Operations"}, status_code=401)
    except Exception as e:
        raise JSONResponse(content={"System Exception": str(e)}, status_code=401)
    
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
from services.user_services import (create_new_user, delete_existent_user, search_user_in_db, change_existent_password, list_existent_users, delete_all_existent_users)
# Import the database methods and the session
from fastapi.param_functions import Depends
from config.database_connection import db_session
from sqlalchemy.orm import Session
# Import the jsonable_encoder method to encode in a jsonable readeble text the database data
from fastapi.encoders import jsonable_encoder


# Create the name of the instance
user_Router = APIRouter(prefix="/Users")

"-------------------------------------------------------------------------------USER_ROUTES----------------------------------------------------------------------------------------------------------------------------------------------"
@user_Router.get("/login", status_code=200, tags=["User Router"], response_class=JSONResponse)
async def user_render_login(request: Request) -> None:
    """_Login the user into the system_

    Args:
        request (Request): _The Http Request_
    """
    raise NotImplementedError("Method not implemented yet")


@user_Router.post("/login/post", status_code=200, tags=["User Router"], response_class=JSONResponse)
async def user_render_login_post(request: Request) -> None:
    """_Get the post of the user and makes an authentication_

    Args:
        request (Request): _The Http Request_
    """
    raise NotImplementedError("Method not implemented yet")


@user_Router.get("/Page", status_code=200, tags=["User Router"], response_class=JSONResponse )
async def user_render_index_page(request: Request, session: Session = Depends(db_session) ) -> HTMLResponse:
    """_Render the Users main page_

    Args:
        request (Request): _The Http request_

    Raises:
        NotImplementedError: _description_

    Returns:
        Jinja2Templates.TemplateResponse: __
    """
    try:
        # Calls and Gets the data from the list_existent_users() method that gets all the users in the database
        data = list_existent_users(db_session=session)
        # If there is data
        if data.get("data"):
            # Returns the template with the data
            return jsonable_encoder(data["data"])
        # If not
        else:
            # Returns the template without the data
            return data
        # If there is any exception during the process
    except Exception as e:
        # Returns the system exception response with the exception description
        return {"system_exception": str(e)}
        

@user_Router.get("/searchUser",status_code=200, tags=["User Router"], response_class=HTMLResponse)
async def user_render_search_page(request: Request) -> HTMLResponse:
    """_Search a especific user in the database_

    Args:
        request (Request): _The HTTP request_

    Raises:
        NotADirectoryError: _description_

    Returns:
        HTMLResponse: __
    """
    
    raise NotImplementedError("Method not implemented yet")


@user_Router.post("/searchUser",status_code=200, tags=["User Router"])
async def user_render_search_page_post(request: Request, search: UserSearch, session: Session = Depends(db_session)):
    """_Get the post to search a especific user in the database_

    Args:
        request (Request): _The HTTP request_
        search ( UserSearch): _The user search squema_
        session (Session, optional): _The database session_. Defaults to Depends(db_session).

    Raises:
        NotADirectoryError: _description_

    Returns:
        HTMLResponse: __
    """
    try:
        respond = search_user_in_db(search=search, db_session=session)
        if respond.get("results"):
            return JSONResponse(content={"data": jsonable_encoder(respond["results"])}, status_code=200)
        else:
            return JSONResponse(content=respond, status_code=500)
    except Exception as e:
        return JSONResponse(content={"System Exception": str(e)}, status_code=500)


@user_Router.get("/new", status_code=200, tags=["User Router"], response_class=JSONResponse)
async def user_render_newUserPage(request: Request) -> HTMLResponse:
    """_Render the new User creation page_

    Args:
        request (Request): _The Http Request_

    Returns:
        Jinja2Templates.TemplateResponse: _description_
    """
    raise NotImplementedError("Method not implemented yet")


@user_Router.post("/new", status_code=200, tags=["User Router"], response_class=JSONResponse)
async def user_render_newUserPage_post(request: Request, newUser: UserCreate, session: Session = Depends(db_session)) -> HTMLResponse:
    
    
    """_Manage the new user creation post_

    Args:
        request (Request): _The Http Request_

    Returns:
        Jinja2Templates.TemplateResponse: _description_
    """
    
    
    try: 
        # Call and Gets the response of the create_new_user() method that creates the new user
        respond = create_new_user(newUser=newUser, db_session=session)
        # If there is a error in the operation
        if respond.get("error"):
            # Returns the error response
            return JSONResponse(content=respond, status_code=500)
        # If not
        else:
            # Returns the successfull response
            return JSONResponse(content={"success": "Sucess Operations"}, status_code=200)
    # If there was any exception
    except Exception as e:
        # Returns the system exception response with the exception description
        return JSONResponse(content={"system_except": str(e)}, status_code=500)
    

@user_Router.get("/changePassword", status_code=200, tags=["User Router"], response_class=JSONResponse)
async def user_render_change_password_page(request: Request) -> HTMLResponse:
    """
    
    _Render the change user password page_

    Args:
        request (Request): _The HTTP request_

    Returns:
        HTMLResponse: _The desired template_
    
    
    """
    raise NotImplemented("Method not implemented yet")


@user_Router.post("/changePassword/{cid: str}", status_code=200, tags=["User Router"], response_class=JSONResponse)
async def user_render_change_password_post(request: Request, data: UserChangePassword, cid: str, session: Session = Depends(db_session)) -> JSONResponse:
    
    
    """_Get the post of the change password page and make the changes_

    Args:
        request (Request): _The HTTP request_
        data (UserChangePassword): _The schema with the new password_
        cid (str): _The cid of the user_
        session (Session): _The database session_. Defaults to Depends(db_session).

    Returns:
        JSONResponse: _description_
    """
    
    
    try:
        # Calls and Gets the response of the change_existent_password() method that change the desired user password
        respond = change_existent_password(passwords=data, id=cid, db_session=session)
        # If the operation was a success
        if respond.get("success"):
            # Returns the successfull response
            return JSONResponse(content=respond, status_code=200)
        else:
            # If not returns the exception or error
            return JSONResponse(content=respond, status_code=500)
    # If there is any exception during the operations
    except Exception as e:
        # Returns the system exception response with the exception description
        return JSONResponse(content={"system_exception": str(e)}, status_code=500)


@user_Router.delete("/deleteExistentUser/{cid: str}", status_code=200, tags=["User Router"], response_class=JSONResponse)
async def user_delete_existent_user(request: Request, cid: str, session: Session = Depends(db_session)) -> JSONResponse:
    
    """_Delete an existent user in the database_

    Args:
        request (Request): _The HTTP request_
        cid (str): _The cid of the desired user_
        session (Session, optional): _The database session_. Defaults to Depends(db_session).

    Returns:
        JSONResponse: _description_
    """
    
    
    try:
        # Calls and Gets the response of the delete_existent_user() method
        respond = delete_existent_user(userId=cid, db_session=session)
        # If the response is success
        if respond["success"]:
            # Returns the success message
            return JSONResponse(content=respond, status_code=200)
        # If not
        else:
            # Returns the error description
            return JSONResponse(content=respond, status_code=500)
    # If there is any exception during the operations
    except Exception as e:
        # Returns the system exception response with the exception description
        return JSONResponse(content={"system_exception": str(e)}, status_code=500)
    

@user_Router.delete("/deleteAll", status_code=200, tags=["User Router"], response_class=JSONResponse)
async def user_delete_all_exixtent_users(request: Request, session: Session = Depends(db_session)) -> JSONResponse:
    """_Delete all the users in the db_

    Args:
        request (Request): _description_
        session (Session, optional): _description_. Defaults to Depends(db_session).

    Returns:
        JSONResponse: _description_
    """
    
    try:
        # Calls and Gets the response of the delete_all_existent_users() method
        respond = delete_all_existent_users(db_session=session)
        # If the response is success
        if respond["success"]:
            # Returns the success message
            return JSONResponse(content=respond, status_code=200)
        # If not
        else:
            # Returns the error description
            return JSONResponse(content=respond, status_code=500)
     # If there is any exception during the operations
    except Exception as e:
        # Returns the system exception response with the exception description
        return JSONResponse(content={"system_exception": str(e)}, status_code=500)
    
    
"-------------------------------------------------------------------------------USER_ROUTES----------------------------------------------------------------------------------------------------------------------------------------------"
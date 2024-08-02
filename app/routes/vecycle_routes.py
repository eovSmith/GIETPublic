# Import the API Router class to create the router instance
from fastapi.routing import APIRouter
# Import the fastapi Http request class
from fastapi.requests import Request
# Import the fastapi Jinjatemplate engine for the html template responses
from fastapi.templating import Jinja2Templates
# Import the Vecycle database model
from models.vecycles_models import VecyclesDB
# Import the HTML response class
from fastapi.responses import HTMLResponse
# Import the schemas
from schemas.vecycle_schemas import (VecycleCreate, VecycleSearch)
# Import the vecycle services
from services.vecycle_services import (create_new_vecycle, delete_all_existent_vecycles, delete_existent_vecycle, search_vecycle_in_db, vecycle_assign_driver)
# Import the database connection
from config.database_connection import db_session
# Import the database session class
from sqlalchemy.orm import Session
# Import the Depends class
from fastapi import Depends
# Import the JSOnResponse class
from fastapi.responses import JSONResponse
# Import the jsonable_encoder method
from fastapi.encoders import jsonable_encoder


# Create the name of the instance
vecycle_Router = APIRouter(prefix="/Vecycles")


"-----------------------------------------------------------------------Vecycles Routes-----------------------------------------------------------------------"


@vecycle_Router.get("/Page", tags=["Vecycle Router"], status_code=200)
async def vecylce_render_main_page(request: Request) -> HTMLResponse:
    """_Render the vecycle main page_

    Args:
        request (Request): _The Http Request_

    Raises:
        NotImplementedError: _description_
    """
    
    raise NotImplementedError("Method not implemented yet")


@vecycle_Router.get("/new", tags=["Vecycle Router"], status_code=200, response_class= HTMLResponse)
async def vecylce_render_new_page(request: Request) -> HTMLResponse:
    """_Render the vecycle new page_

    Args:
        request (Request): _The Http Request_

    Raises:
        NotImplementedError: _description_
    """

    raise NotImplementedError("Method not implemented yet")


@vecycle_Router.post("/new", tags=["Vecycle Router"], status_code=200, response_class= HTMLResponse)
async def vecylce_render_new_page_post(request: Request, new: VecycleCreate, db: Session = Depends(db_session)) -> JSONResponse:
    
    
    """_Manage the new vecycle creation post_

    Args:
        request (Request): _the HTTP request_
        new (VecycleCreate): _The new vecycle schema_
        db (Session, optional): _The database session_. Defaults to Depends(db_session).

    Returns:
        _JSONResponse_: _system error_
        _JSONResponse_: _Successfull response_
        _JSONResponse_: _system exception_
    """
    
    
    try:
        # Call and Gets the response of the create_new_vecycle() method that creates the new vecycle
        respond = create_new_vecycle(vecycle=new, db_session=db)
        # If there is a error in the operation
        if respond.get("error"):
            # # Returns the error response
            return JSONResponse(content=respond, status_code=500)
        # If not
        else:
            # Returns the successfull response
            return JSONResponse(content=respond, status_code=200)
    # If there was any exception
    except Exception as e:
        # Returns the system exception response with the exception description
        return JSONResponse(content={"system_exception": str(e)}, status_code=500)
        

@vecycle_Router.get("/search", tags=["Vecycle Router"], status_code=200, response_class=HTMLResponse)
async def vecycle_render_search_page(request: Request) -> HTMLResponse:
    """_Search for a vecycle by its name_


    Args:
        vecycle (VecycleSearch): _The vecycle to search_
        db (Session, optional): _The database session_. Defaults to Depends(db_session).

    Returns:
    """
    raise NotImplementedError("Method not implemented yet")


@vecycle_Router.post("/search", tags=["Vecycle Router"], status_code=200, response_class=JSONResponse)
async def vecycle_render_search_page_post(request: Request ,search: VecycleSearch, db: Session = Depends(db_session)) -> JSONResponse:
    """_Search for a vecycle by its name_


    Args:
        vecycle (VecycleSearch): _The vecycle to search_
        db (Session, optional): _The database session_. Defaults to Depends(db_session).

    Returns:
    """


    try:
        # Call and Gets the response of the create_new_vecycle() method that creates the new vecycle
        respond = search_vecycle_in_db(search=search, db_session=db)
        # If got resulsts
        if respond.get("results"):
            # Returns the results
            return JSONResponse(content={"data": jsonable_encoder(respond["results"])}, status_code=200)
        # If got not found
        if respond.get("not_found"):
            # Returns the not found
            return JSONResponse(content=respond, status_code=200)
        # If got error
        else:
            # Returns the error description
            return JSONResponse(content=respond, status_code=501)
    # If there was a exception 
    except Exception as e:
        # Returns the exception description
        return JSONResponse(content={"System Exception": str(e)}, status_code=501)

@vecycle_Router.delete("/vecycle/delete/all", tags=["Vecycle Router"], status_code=200, response_class=JSONResponse)
async def delete_all_vecycles(request: Request, db: Session = Depends(db_session)) -> JSONResponse:
    """


    """
    try:
        respond = delete_all_existent_vecycles(db_session=db)
        # If the response is success
        if respond.get("success"):
            # Returns the success message
            return JSONResponse(content=respond, status_code=200)
        # If not
        else:   
            # Returns the error description
            return JSONResponse(content=respond, status_code=501)
    except Exception as e:
        # Returns the system exception response with the exception description  
        return JSONResponse(content={"system_exception": str(e)}, status_code=501)


@vecycle_Router.delete("/vecycle/delete/{vecycle_id}", tags=["Vecycle Router"], status_code=200, response_class=JSONResponse)
async def delete_vecycle(request: Request ,vecycle_id: str, db: Session = Depends(db_session)) -> JSONResponse:
    """


    Args:
        vecycle_id (int): _The vecycle id to delete_
    """
    
    
    try:
        respond = delete_existent_vecycle(vecyclePlate=vecycle_id, db_session=db)
        # If the response is success
        if respond.get("success"):
            # Returns the success message
            return JSONResponse(content=respond, status_code=200)
        # If not
        else:
            # Returns the error description
            return JSONResponse(content=respond, status_code=501)
    # If there is any exception during the operations
    except Exception as e:
        # Returns the system exception response with the exception description
        return JSONResponse(content={"system_exception": str(e)}, status_code=501)





@vecycle_Router.get("/assign_driver/{vecycle_id}", tags=["Vecycle Router"], status_code=200, response_class=HTMLResponse)
async def vecycle_render_assign_driver_get(request: Request) -> HTMLResponse:
    """"""
    
    raise NotImplementedError("Method not implemented yet")



@vecycle_Router.post("/assign_driver/{vecycle_id}", tags=["Vecycle Router"], status_code=200, response_class=JSONResponse )
async def vecycle_render_assign_driver_post(request: Request, vecycle_id: str, driver: str , db: Session = Depends(db_session)) -> JSONResponse:
    """


    """


    try:
        respond = vecycle_assign_driver(vecycle_id=vecycle_id, driverCid=driver , db=db)
        # If the response is success
        if respond.get("success"):
            # Returns the success message
            return JSONResponse(content=respond, status_code=200)
        # If not
        else:   
            # Returns the error description
            return JSONResponse(content=respond, status_code=501)
    except Exception as e:
        # Returns the system exception response with the exception description  
        return JSONResponse(content={"system_exception": str(e)}, status_code=501)
    
"-----------------------------------------------------------------------Vecycles Routes-----------------------------------------------------------------------"
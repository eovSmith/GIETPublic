# Import the API Router class to create the router instance
from fastapi.routing import APIRouter
# Import the fastapi Http request class
from fastapi.requests import Request
# Import the fastapi Jinjatemplate engine for the html template responses
from fastapi.templating import Jinja2Templates
# Import the Driver database model
from models.driver_models import DriverDB
# Import the driver Schemas
from schemas.driver_schemas import DriverCreate, DriverSearch
# Import the drivers services
from services.driver_services import create_new_driver, delete_all_existent_drivers, delete_existent_driver, list_existent_drivers, search_driver_in_db
# import the Session class
from sqlalchemy.orm import Session
# import the HTML response class
from fastapi.responses import HTMLResponse, JSONResponse
# import the database connection
from config.database_connection import db_session 
# Import the Depends class for dependency injection
from fastapi import Depends
# Import the jsonable encoder
from fastapi.encoders import jsonable_encoder


# Create the name of the instance
driver_Router = APIRouter(prefix="/Drivers")


"-----------------------------------------------------------------------DRIVER_ROUTES-----------------------------------------------------------------------"


@driver_Router.get("/Page", tags=["Driver Router"], status_code=200)
async def driver_render_main_page(request: Request) -> HTMLResponse:
    """_Render the driver main page_

    Args:
        request (Request): _The Http Request_

    Raises:
        NotImplementedError: _description_
    """
    
    raise NotImplementedError("Method not implemented yet")


@driver_Router.get("/new", tags=["Driver Router"], status_code=200, response_class= HTMLResponse)
async def driver_render_new_page(request: Request) -> HTMLResponse:
    """_Render the driver new page_

    Args:
        request (Request): _The Http Request_

    Raises:
        NotImplementedError: _description_
    """

    raise NotImplementedError("Method not implemented yet")


@driver_Router.post("/new", tags=["Driver Router"], status_code=200, response_class= HTMLResponse)
async def driver_render_new_page_post(request: Request, new: DriverCreate, db: Session = Depends(db_session)) -> JSONResponse:
    
    
    """_Manage the new driver creation post_

    Args:
        request (Request): _the HTTP request_
        new (DriverCreate): _The new driver schema_
        db (Session, optional): _The database session_. Defaults to Depends(db_session).

    Returns:
        _JSONResponse_: _system error_
        _JSONResponse_: _Successfull response_
        _JSONResponse_: _system exception_
    """
    
    
    try:
        # Call and Gets the response of the create_new_vecycle() method that creates the new vecycle
        respond = create_new_driver(newdriver=new, db_session=db)
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
        

@driver_Router.get("/search", tags=["Driver Router"], status_code=200, response_class=HTMLResponse)
async def driver_render_search_page(request: Request) -> HTMLResponse:
    """_Search for a vecycle by its name_

    """
    raise NotImplementedError("Method not implemented yet")


@driver_Router.post("/search", tags=["Driver Router"], status_code=200, response_class=JSONResponse)
async def driver_render_search_page_post(request: Request ,search: DriverSearch, db: Session = Depends(db_session)) -> JSONResponse:
    """_Search for a driver in the database_


    Args:
        search (DriverSearch): _The driver to search_
        db (Session, optional): _The database session_. Defaults to Depends(db_session).

    Returns:
    """


    try:
        # Call and Gets the response of the search_driver_in_db method that filters the existents drivers in the database
        respond = search_driver_in_db(search=search, db_session=db)
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

@driver_Router.delete("/driver/delete/all", tags=["Driver Router"], status_code=200, response_class=JSONResponse)
async def delete_all_drivers(request: Request, db: Session = Depends(db_session)) -> JSONResponse:
    """


    """
    try:
        respond = delete_all_existent_drivers(db_session=db)
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


@driver_Router.delete("/driver/delete/{driver_id}", tags=["Driver Router"], status_code=200, response_class=JSONResponse)
async def delete_driver(request: Request ,driver_id: str, db: Session = Depends(db_session)) -> JSONResponse:
    """


    Args:
        driver_id (str): _The driver id to delete_
    """
    
    
    try:
        respond = delete_existent_driver(driverCid=driver_id, db_session=db)
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



"-----------------------------------------------------------------------DRIVER_ROUTES-----------------------------------------------------------------------"
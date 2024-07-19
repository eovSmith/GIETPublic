# Import fastapi and the http request
# from fastapi_offline import FastAPIOffline
from fastapi import (FastAPI,Request)
# Import the JsonResponse
from fastapi.responses import JSONResponse
# Import the Routers
from routes.user_routes import user_Router
from routes.vecycle_routes import vecycle_Router
from routes.driver_routes import driver_Router
# Import the db init method
from config.database_connection import init_db 
from fastapi.middleware.cors import CORSMiddleware


# Declares the instance
app = FastAPI()
# Start the database
app.add_event_handler("startup", init_db)
# Include the routers to the main app
app.include_router(user_Router)
app.include_router(vecycle_Router)
app.include_router(driver_Router)
app.add_middleware(
     CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Main endpoint
@app.get("/", status_code=200, tags=["Main"])
def main_endpoint(request: Request) -> JSONResponse:
    return JSONResponse({"message": "System init"})
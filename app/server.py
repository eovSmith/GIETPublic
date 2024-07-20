 # Import the uvicorn server and the created Fastapi instance
import uvicorn
# Import the fastapi app instance
from main import app
# Import the load_dotenv method from dotenv for load the enviorement variables
from dotenv import load_dotenv
# Import the logging module for make console messages
import logging
# Import os to use the path an env methods
import os




def main() -> None:
    """_The Main method that runs the uvicorn server and loads the dotenv_"""
    try:
        # Search the dinamic route of the system .env
        env_dir = os.path.join("config",".env")
        # Loads the .env using the env_dir directory
        load_dotenv(dotenv_path=env_dir)
        # Runs the uvicorn server with the app the HOST and the PORT
        uvicorn.run("main:app", host=os.getenv("HOST"), port=int(os.getenv("PORT")), reload=True)
    except Exception as e:
        logging.warning(f"A error has ocurred {str(e)}")

# The main run
if __name__ == "__main__":
    main()
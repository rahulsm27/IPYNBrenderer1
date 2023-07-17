import os
from pathlib import Path
import logging

logging.basicConfig( level=  10,
                    format ='[%(asctime)s : %(levelname)s] : %(message)s')

while True:
    project_name = input("Enter the proejct name")
    if project_name!= " ":
        break

logging.info(f"Creating project by name : {project_name}")

# List of files

list_of_files = [".github/workflows/.gitkeep", f"src/{project_name}/__init__.py",
                 "init_setup.sh","requirements.txt","requriements_dev.txt","setup.py",
                 "pyproject.toml","setup.cfg","txo.ini",
                 "tests/__init__.py",
                 "tests/unit/__init__.py",
                 "tests/integration/__init__.py"]

for filepath in list_of_files:
    filepath = Path(filepath) # To make it OS independent
    filedir, filename = os.path.split(Path(filepath))
    if filedir != '': # If in given list of files thre is a directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at :{filedir} for file :{filename}")

    if (not os.path.exists(filepath)) or(os.path.getsize(filepath) ==0 ): # If the file is not there
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating a new file : {filename} at path : {filepath}")

    else :
        logging.info(f"File {filename} already exists ")



import os
# to make file operating system independent
import pathlib
import logging
from time import time

# set logging level
logging.basicConfig(level= logging.INFO, 
                    format="[%(asctime)s: %(levelname)s]: %(message)s"
                    )


while True:
    project_name = input("Input Project Name : ")
    if project_name !='':
        break

logging.info(f"Creating Project {project_name}")

# list of files we want to create

list_of_files =[ ".github/workflows/.gitkeep",
                 f"src/{project_name}/__init__.py", # basic project source directory
                 f"tests/__init__.py",
                 f"tests/unit/__init__.py",
                 f"tests/integration/__init__.py",
                 "init_setup.sh",# basic environ set up
                "requirements.txt",# Production requirement txt
                "requirements_dev.txt",# developer and Testing requirements.txt
                "setup.py",
                "pyproject.toml",
                'setup.cfg',
                "tox.ini"# Tested should be on various environemnt
]


for filepath in list_of_files:
    filepath = pathlib.Path(filepath)
    filedir,filename = os.path.split(filepath)

    # if file directory is not exists
    if filedir != "":
        # if directory already exists don't create any error
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating dir at {filedir} for file : {filename}")

    # if file path is not present or fiepath present but file size is 0 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")

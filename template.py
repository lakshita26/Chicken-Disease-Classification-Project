import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"

list_of_files =[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    # because windows use backward slash instead of forward slash
    # so this will specify the path as it a windows path
    
    filedir, filename = os.path.split(filepath)
    # this will split filepath from filname and storing then in filedir and filename
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # getsize will return some number showing it has some bytes of data
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
            
    else:
        logging.info(f"{filepath} is already exits.")
        
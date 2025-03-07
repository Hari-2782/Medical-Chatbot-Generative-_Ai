import os
from pathlib import Path
import logging
# //modular approach
logging.basicConfig(level=logging.INFO, format='[%(acstime)s]: %(message)s:')
list_of_files =[
    "src/_init_.py", #constructor
    "src/helper.py",
    "src/prompt.py",
    ".env",
    # "requirements.txt",
    "setup.py",
    "app.py",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir,filename = os.path.split(file_path)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}") 
    
    if(not os.path.exists(filepath)) or(os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty  file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")
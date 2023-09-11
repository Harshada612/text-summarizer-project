import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name='textsummarizer'

list_of_files=[
    '.github/workflows/.gitkeep',
    f'scr/{project_name}/__init__.py',
    f'scr/{project_name}/components/__init__.py',
    f'scr/{project_name}/components/data_ingestion.py',
    f'scr/{project_name}/components/data_transformation.py',
    f'scr/{project_name}/components/model_trainer.py',
    f'scr/{project_name}/components/model_monitering.py',
    f'scr/{project_name}/utils/__init__.py',
    f'scr/{project_name}/utils/common.py',
    f'scr/{project_name}/logging/__init__.py',
    f'scr/{project_name}/config/__init__.py',
    f'scr/{project_name}/config/configuration.py',
    f'scr/{project_name}/pipeline/__init__.py',
    f'scr/{project_name}/pipeline/training_pipeline.py',
    f'scr/{project_name}/pipeline/prediction_pipeline.py',
    f'scr/{project_name}/entity/__init__.py',
    f'scr/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'creating directory : {filedir} for the file {filename}')

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open (filepath,'w') as f:
            pass
        logging.info(f'creating empty file:{filepath}')

    else:
        logging.info(f'{file}is already exists')
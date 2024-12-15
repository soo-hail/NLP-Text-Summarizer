# To create Project-Template(Structure) in Pythonic way.
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

files_list = [
    '.github/workflow/.gitkeep',
    
    'src/__init__.py',
    'src/utils.py',
    'src/logger.py',
    'src/exception.py',
    
    'src/components/data_ingestion.py',
    'src/components/data_trasformation.py',
    'src/components/model_trainer.py',
    
    'src/pipeline/__init__.py',
    'src/pipeline/predict_pipeline.py',
    'src/pipeline/train_pipeline.py',
    
    'notebook/',
    
    'app.py',
    'main.py',
    'setup.py',
    'Dockerfile',
    'requirements.txt',
    'config/config.yaml',
    'params.yaml'
    
]

# Create Folders and Files.
for file_path in files_list:
    file_path = Path(file_path)
    dir_name, file_name = os.path.split(file_path)
    
    # If file present inside a Directory(create folder then create file).
    if dir_name != '':
        os.makedirs(dir_name, exist_ok=True)
        logging.info(f'{dir_name} directory created.')
        
    if (not os.path.exists(file_path) or os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            
        logging.info(f'{file_path} empty file created.')
        
    else:
        logging.info(f'{file_path} already exists.')
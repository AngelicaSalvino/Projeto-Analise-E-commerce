# Módulo configurar as crendenciais do kaggle

import os
import json
from dotenv import load_dotenv

def save_kaggle_config():
    load_dotenv()

    kaggle_config = {
        "username": os.getenv('USER'),
        "key": os.getenv('KEY')
    }

    os.makedirs(os.path.join(os.path.expanduser("~"), ".kaggle"), exist_ok=True)

    with open(os.path.join(os.path.expanduser("~"), ".kaggle/kaggle.json"), "w") as file:
        json.dump(kaggle_config, file)

    os.chmod(os.path.join(os.path.expanduser("~"), ".kaggle/kaggle.json"), 0o600)
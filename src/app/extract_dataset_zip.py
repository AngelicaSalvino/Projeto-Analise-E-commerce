# Módulo para extrair o dataset

import zipfile

def extract_dataset(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)
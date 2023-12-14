# Módulo para baixar o dataset

import subprocess

def download_kaggle_dataset(dataset, path="./data"):
    subprocess.run(["kaggle", "datasets", "download", "-d", dataset, "--path", path])
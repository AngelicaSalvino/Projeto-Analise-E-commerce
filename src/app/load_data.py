# Módulo para carregar dados de um arquivo csv

import pandas as pd

def load_data(file_path):
    # Criação de uma lista para identificar valores ausentes
    lista_labels_valores_ausentes = ["n/a", "na", "undefined"]

    # Carregamento dos dados
    return pd.read_csv(file_path, na_values = lista_labels_valores_ausentes)
    
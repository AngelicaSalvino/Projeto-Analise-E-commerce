from app.load_config import save_kaggle_config
from app.download_dataset import download_kaggle_dataset
from app.extract_dataset_zip import extract_dataset
from app.load_data import load_data
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Configurando Kaggle
save_kaggle_config()

# Download e extração do conjunto de dados
download_kaggle_dataset("olistbr/brazilian-ecommerce")
extract_dataset("./data/brazilian-ecommerce.zip", "./data/brazilian_ecommerce")

# Carregamento dos datasets
customers = load_data("data/brazilian_ecommerce/olist_customers_dataset.csv")
geolocation = load_data("data/brazilian_ecommerce/olist_geolocation_dataset.csv") 
order_items = load_data("data/brazilian_ecommerce/olist_order_items_dataset.csv")
payments = load_data("data/brazilian_ecommerce/olist_order_payments_dataset.csv")
reviews = load_data("data/brazilian_ecommerce/olist_order_reviews_dataset.csv")
orders = load_data("data/brazilian_ecommerce/olist_orders_dataset.csv")
products = load_data("data/brazilian_ecommerce/olist_products_dataset.csv") 
sellers = load_data("data/brazilian_ecommerce/olist_sellers_dataset.csv")
category = load_data("data/brazilian_ecommerce/product_category_name_translation.csv")

# Reagrupamento das categorias
moda_acessorios = ['fashion_bolsas_e_acessorios', 'fashion_calcados', 'fashion_roupa_masculina',
                   'fashion_roupa_feminina', 'fashion_underwear_e_moda_praia', 'fashion_esporte', 'relogios_presentes','malas_acessorios', 'fashion_roupa_infanto_juvenil']

casa_decoracao = ['cama_mesa_banho', 'moveis_decoracao', 'moveis_escritorio', 'moveis_sala', 'moveis_quarto',
                  'moveis_cozinha_area_de_servico_jantar_e_jardim', 'moveis_colchao_e_estofado', 
                  'casa_conforto', 'casa_conforto_2', 'la_cuisine', 'utilidades_domesticas','eletroportateis', 'portateis_casa_forno_e_cafe','cool_stuff', 'eletrodomesticos', 'eletrodomesticos_2','artes_e_artesanato','ferramentas_jardim', 'climatizacao', 'moveis_colchao_e_estofado', 'portateis_cozinha_e_preparadores_de_alimentos','flores','artigos_de_natal', 'artigos_de_festas']

casa_construcao = ['construcao_ferramentas_construcao', 'casa_construcao', 'construcao_ferramentas_seguranca', 
                   'construcao_ferramentas_jardim', 'construcao_ferramentas_iluminacao', 'construcao_ferramentas_ferramentas','sinalizacao_e_seguranca']

eletronicos_tecnologia = ['informatica_acessorios', 'eletronicos', 'tablets_impressao_imagem', 'pcs','consoles_games', 'audio', 
                          'telefonia', 'telefonia_fixa', 'pc_gamer']

infantil = ['bebes']

automotivo = ['automotivo']

hobbies_entretenimento = ['esporte_lazer', 'brinquedos', 'instrumentos_musicais', 'cds_dvds_musicais', 'dvds_blu_ray',
                          'musica', 'cine_foto', 'artes', 'brinquedos', 'audio']

pet_shop = ['pet_shop']

livros_papelaria = ['livros_interesse_geral', 'livros_tecnicos ', 'livros_importados', 'papelaria']

saude_higiene = ['beleza_saude','perfumaria', 'fraldas_higiene']

alimentos_bebidas = ['alimentos_bebidas', 'alimentos', 'bebidas']

agro_ind_comercio = ['agro_industria_e_comercio','industria_comercio_e_negocios']

outros = ['seguros_e_servicos', 'market_place']

# Criando uma nova coluna 'categoria_agrupada' com valor padrão 'Outros'
products['categoria_agrupada'] = 'Outros'

# Aplicando os agrupamentos
products.loc[products['product_category_name'].isin(moda_acessorios), 'categoria_agrupada'] = 'Moda e Acessórios'
products.loc[products['product_category_name'].isin(casa_decoracao), 'categoria_agrupada'] = 'Casa e Decoração'
products.loc[products['product_category_name'].isin(casa_construcao), 'categoria_agrupada'] = 'Casa e Construção'
products.loc[products['product_category_name'].isin(eletronicos_tecnologia), 'categoria_agrupada'] = 'Eletrônicos e Tecnologia'
products.loc[products['product_category_name'].isin(hobbies_entretenimento), 'categoria_agrupada'] = 'Hobbies e Entretenimento'
products.loc[products['product_category_name'].isin(saude_higiene), 'categoria_agrupada'] = 'Saúde e Higiene'
products.loc[products['product_category_name'].isin(infantil), 'categoria_agrupada'] = 'Infantil'
products.loc[products['product_category_name'].isin(automotivo), 'categoria_agrupada'] = 'Automotivo'
products.loc[products['product_category_name'].isin(pet_shop), 'categoria_agrupada'] = 'Pet-Shop'
products.loc[products['product_category_name'].isin(livros_papelaria), 'categoria_agrupada'] = 'Livros e Papelaria'
products.loc[products['product_category_name'].isin(alimentos_bebidas), 'categoria_agrupada'] = 'Alimentos e Bebidas'
products.loc[products['product_category_name'].isin(agro_ind_comercio), 'categoria_agrupada'] = 'Agro, Ind. e Comércio'
products.loc[products['product_category_name'].isin(outros), 'categoria_agrupada'] = 'Outros'



def run_app():
    st.write("Resumo da tabela 'customers'")
   
    # Criando um gráfico de barras
    plt.figure(figsize=(12, 6))  # Ajuste o tamanho conforme necessário

    # Contar a frequência de cada categoria agrupada
    contagem_categorias = products['categoria_agrupada'].value_counts()

    # Plotar o gráfico de barras
    contagem_categorias.plot(kind='bar', color='skyblue')
    plt.title('Contagem de Produtos por Categoria Agrupada')
    plt.xlabel('Categoria Agrupada')
    plt.ylabel('Contagem de Produtos')
    plt.xticks(rotation=45, ha='right')  # Rotacionar os rótulos no eixo x para melhor legibilidade

    # Exibe o gráfico no Streamlit
    st.pyplot(plt)




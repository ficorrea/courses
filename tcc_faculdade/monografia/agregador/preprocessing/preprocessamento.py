import pandas as pd
from unicodedata import normalize


class Preprocessamento():
    """Preprocessamento dos dados"""

    def ler_csv(self, nome_arquivo):
        nome_arquivo = 'datasets/' + nome_arquivo
        return pd.read_csv(nome_arquivo)

    def concatenar_datasets(self, lista_datasets):
        """Retorna a concatenação dos datasets"""
        dataset = pd.concat(lista_datasets, join='outer', ignore_index=True)
        return dataset

    def retirar_acento(self, texto):
        """Retira o acento das palavras."""
        return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

    def ajustar_texto(self, dataset):
        """
        Retira espaços, textos que estejam
        todos maiúsculos e acentos.
        """
        dataset['bairro'] = dataset['bairro'].str.title().str.strip()
        for i in range(len(dataset['bairro'])):
            dataset.loc[i, 'bairro'] = self.retirar_acento(
                dataset['bairro'][i])
        return dataset

    def ajustar_nomes_bairros(self, dataset):
        """
        Ajusta os nomes dos bairros com relação 
        as listas de nomes corretos e errados.
        """
        nomes_errados = ['Canelas Ii', 'Panorama Ii', 'Todos Os Santos Ii',
                         'Vila Santa Maria', 'Vila Cidade Santa Maria',
                         'Jardim Sao Mateus', 'Jardim Niemeyer']
        nomes_certos = ['Canelas II', 'Panorama II', 'Todos Os Santos',
                        'Cidade Santa Maria', 'Cidade Santa Maria',
                        'Jardim Palmeiras', 'Jardim Sao Luiz']
        for i in range(len(nomes_errados)):
            mask = dataset['bairro'] == nomes_errados[i]
            dataset.loc[mask, 'bairro'] = nomes_certos[i]
        return dataset

    def inserir_coordenadas_geograficas(self, dataset, dataset_com_coordenadas):
        """
        Insere colunas de latitude e longitude, além de 
        populá-las com os valores correspondentes.
        """
        dataset.insert(1, 'latitude', 0)
        dataset.insert(2, 'longitude', 0)
        for i in range(len(dataset_com_coordenadas)):
            mask = dataset['bairro'] == dataset_com_coordenadas['BAIRROS'][i]
            dataset.loc[mask, ['latitude', 'longitude']] = \
                dataset_com_coordenadas[[
                    'LATITUDE', 'LONGITUDE']].iloc[i].values
        return dataset

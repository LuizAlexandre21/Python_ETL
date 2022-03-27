# Pacotes
import requests 
import tempfile
import zipfile
import os 

# Estrutura de requisição dos arquivos
link = 'http://web.antaq.gov.br/Sistemas/ArquivosAnuario/Arquivos/{}.zip'
    
# Definindo as classe de dados da antaq 
class antaq_data:
    
    # Definindo downloader dos dados 
    def downloader(self,year:list):

        # verificando a lista tem elementos 
        if len(year) >= 1:

            # Lista de requisições com sucesso 
            requestz = []

            # Requisições dos arquivos por anos 
            for ano in year:

                # Formatando os links 
                url =link.format(ano)

                # Fazendo downloads dos arquivos 
                try:
                   requestz.append(requests.get(url))                   
                except Exception as e:
                    print(e)
            
            # Retornando arquivos baixados
            return requestz

    # Definindo o extrator dos dados 
    def extrator(self,raw_data:True,contents):

        # Caso não queira salvar arquivos no computador 
        if raw_data is True:
            local = tempfile.NamedTemporaryFile().name +'.zip'

        # Caso queira salvar arquivos no computador 
        else:
            local = os.getcwd() + '/'+contents.url[-8:-4] + '.zip'

        # Salvando os arquivos nos locais temporarios 
        with open(local,'wb') as f:
            f.write(contents.content)

        # Criando pastas         
        dire = os.mkdir(contents.url[-8:-4])

        # Extraindo arquivos comprimidos
        ziper = zipfile.ZipFile(local,'r').extractall(path=contents.url[-8:-4])

        # Retornando as paginas 
        return local[:-4]


    # Definindo o main 
    def main(self):

        # Lista de arquivos 
        path = []

        # Download de arquivos para os anos de 2022
        down  = self.downloader(year=['2022'])

        # Extraindo arquivos baixados
        for files in down : 
            l = self.extrator(raw_data=False,contents=files) 

            # Salvando os arquivos de listas
            path.append(l)
        
        # Retornando a localização dos arquivos
        return path
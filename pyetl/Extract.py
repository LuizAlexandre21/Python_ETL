# Pacotes 
from pyspark.sql import SparkSession
from utils.scraping import antaq_data

# Criando ou Utilizando uma sessão spark 
spark = SparkSession.builder.getOrCreate()

def extract():
    # Solicitando os dados da antaq
    # Abrindo a classe para solicitar antaq
    antaq = antaq_data()

    # Download de dados 
    path = antaq.main()

    # Carregando arquivos baixados 
    # Criando dicionarios com os arquivos 
    files = {}

    # Criando os arquivos 
    for arq in path:
        arr = os.listdir(arq)
        files[str(arq[-4:])] = {}
        for txt in arr:
            files[str(arq[-4:])][str(txt[:-4])] = spark.read.options(header=True,delimiter=';').csv(arq+'/'+txt)

    return files 
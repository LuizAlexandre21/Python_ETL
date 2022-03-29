# Pacotes 
from Extract import * 
from Transform import *
from Load import * 

# Extraindo os arquivos 
database = extract()

# Carregando dados para um possivel datalake 



# Transformando os dados 
atracacao, carga = transformation(database)

# Verificando a existencia das tabelas 


# Carregando os dados de atracacao
export_atracacao(atracacao)

# Carregando os dados de carga 
export_carga(carga)


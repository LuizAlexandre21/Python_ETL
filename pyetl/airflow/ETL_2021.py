# Pacotes 
from Extract import * 
from Transform import *
from Load import * 

# Extraindo os arquivos por ano 
database_2021 = extract(2021)

# Transformando os dados 
atracacao_2021, carga_2021 = transformation(database_2021)

# Verificando a existencia das tabelas 
# Carregando os dados de atracacao
export_atracacao(atracacao_2021)

# Carregando os dados de carga 
export_carga(carga2021)


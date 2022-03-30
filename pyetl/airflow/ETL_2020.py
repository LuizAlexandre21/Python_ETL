# Pacotes 
from Extract import * 
from Transform import *
from Load import * 

# Extraindo os arquivos por ano 
database_2020 = extract(2020)

# Transformando os dados 
atracacao_2020, carga_2020 = transformation(database_2020)

# Verificando a existencia das tabelas 
# Carregando os dados de atracacao
export_atracacao(atracacao_2020)

# Carregando os dados de carga 
export_carga(carga2020)


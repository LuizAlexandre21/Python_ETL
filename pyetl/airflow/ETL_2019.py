# Pacotes 
from Extract import * 
from Transform import *
from Load import * 

# Extraindo os arquivos por ano 
database_2019 = extract(2019)

# Transformando os dados 
atracacao_2019, carga_2019 = transformation(database_2019)

# Verificando a existencia das tabelas 
# Carregando os dados de atracacao
export_atracacao(atracacao_2019)

# Carregando os dados de carga 
export_carga(carga2019)


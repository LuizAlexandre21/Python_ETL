# Pacotes 
from Extract import * 
from Transform import *
from Load import * 

# Extraindo os arquivos por ano 
database_2019 = extract(2019)
database_2020 = extract(2020)
database_2021 = extract(2021)



# Transformando os dados 
atracacao_2019, carga_2019 = transformation(database_2019)
atracacao_2020, carga_2020 = transformation(database_2020)
atracacao_2021, carga_2021 = transformation(database_2021)


# Verificando a existencia das tabelas 

db_1 = Atracacao_fato.select().exists()
if db_1 == False:
    database.create_tables([Atracacao_fato])

db_2 = Carga.Fato.select().exists()
if db_2 == False:
    database.create_tables([Carga_Fato])




# Carregando os dados de atracacao
export_atracacao(atracacao_2019)
export_atracacao(atracacao_2020)
export_atracacao(atracacao_2021)


# Carregando os dados de carga 
export_carga(carga2019)
export_carga(carga2020)
export_carga(carga2021)

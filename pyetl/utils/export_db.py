#Pacotes 
from peewee import *
from playhouse.db_url import connect 

# Estabelecendo conexão com o banco de dados 
try:
    database = connect("mysql://alexandre:34340012@localhost:3306/Antaq")
    print("Database successfully connected")
except:
    print("Database connection failed")

# Criando a classe de conexão com mysql 
class MySQLBitField(Field):
    field_type = "bit" 
    
    def __init__(self,*_,**__):
        pass

# Criando a classe do modelo basico 
class BaseModel(Model):
    class Meta:
        database = database 

# Criando os modelos relacionais 
# Atracacao fato 
class Atracacao_fato(BaseModel):
    id_atracacao = TextField(primary_key=True)
    CDTUP = TextField()
    Idberco = TextField()
    porto_atracacao = TextField()
    apelido_instalacao_portuaria = TextField()
    complexo_portuário = TextField()
    tipo_autoridade_portuaria = TextField()
    data_atracacao = TextField()
    data_chegada = TextField()
    data_desatracacao = TextField()
    inicio_operacao = TextField()
    termino_operacao = TextField()
    tipo_operacao = TextField()
    tipo_navegacao = TextField()
    nacionalidade_atracacao = TextField()]
    flag_mc_operacao_atracacao = TextField()
    terminal = TextField()
    municipio = TextField()
    UF = TextField()
    SGUF = TextField()
    regiao_geografica = TextField()
    num_capitania = TextField()
    IMO = TextField()
    espera_atracacao = TextField()
    espera_inicio_op = TextField()
    tipo_operacao = TextField()
    espera_desatracacao = TextField()
    tempo_atracado = TextField()
    tempo_estadia = TextField()
    ano = TextField()
    mes = TextField()

    class Meta:
        table_name = 'Atracacao_fato'


# Carga Fato 
class Carga_Fato(BaseModel):
    id_carga = TextField(primary_key = True)
    flag_transporte_via_interior = TextField()
    id_atracacao = TextField()
    percurso_vias_interior = TextField()
    origem = TextField()
    percurso_interior = TextField()
    destino = TextField()
    st_natureza_carga = TextField()
    cd_mercadoria = TextField()
    st_sh2 = TextField()
    tipo_operacao = TextField()
    st_sh4 = TextField()
    carga_geral_acondicionamento = TextField()
    natureza_carga = TextField()
    conteiner_estado = TextField()
    sentido = TextField()
    tipo_navegacao = TextField()
    TEU = TextField()
    flag_autorizacao = TextField()
    vl_peso_carga_bruta = TextField()
    qt_carga = TextField()
    flag_cabotagem = TextField()
    vl_peso_carga_bruta = TextField()
    flag_cabotagem_movimentacao = TextField()
    flag_container_tamanho = TextField()
    flag_mc_opercacao_carga = TextField()
    flag_off_shore = TextField()
    vl_peso_carga_bruta = TextField()
    ano = TextField()
    mes = TextField()
    SGUF = TextField()
    porto_atracacao = TextField()

    class Meta:
        table_name = 'Carga_fato'

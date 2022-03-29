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
    id_atracacao = CharField()
    CDTUP = CharField()
    Idberco = CharField()
    porto_atracacao = CharField()
    apelido_instalacao_portuaria = CharField()
    complexo_portuário = CharField()
    tipo_autoridade_portuaria = CharField()
    data_atracacao = CharField()
    data_chegada = CharField()
    data_desatracacao = CharField()
    inicio_operacao = CharField()
    termino_operacao = CharField()
    tipo_operacao = CharField()
    tipo_navegacao = CharField()
    nacionalidade_atracacao = CharField()
    flag_mc_operacao_atracacao = CharField()
    terminal = CharField()
    municipio = CharField()
    UF = CharField()
    SGUF = CharField()
    regiao_geografica = CharField()
    num_capitania = CharField()
    IMO = CharField()
    espera_atracacao = CharField()
    espera_inicio_op = CharField()
    tipo_operacao = CharField()
    espera_desatracacao = CharField()
    tempo_atracado = CharField()
    tempo_estadia = CharField()
    ano = CharField()
    mes = CharField()

    class Meta:
        primary_key=False
        table_name = 'Atracacao_fato'


# Carga Fato 
class Carga_Fato(BaseModel):
    id_carga = CharField()
    flag_transporte_via_interior = CharField()
    id_atracacao = CharField()
    percurso_vias_interior = CharField()
    origem = CharField()
    percurso_interior = CharField()
    destino = CharField()
    st_natureza_carga = CharField()
    cd_mercadoria = CharField()
    st_sh2 = CharField()
    tipo_operacao = CharField()
    st_sh4 = CharField()
    carga_geral_acondicionamento = CharField()
    natureza_carga = CharField()
    conteiner_estado = CharField()
    sentido = CharField()
    tipo_navegacao = CharField()
    TEU = CharField()
    flag_autorizacao = CharField()
    vl_peso_carga_bruta = CharField()
    qt_carga = CharField()
    flag_cabotagem = CharField()
    vl_peso_carga_bruta = CharField()
    flag_cabotagem_movimentacao = CharField()
    flag_container_tamanho = CharField()
    flag_mc_opercacao_carga = CharField()
    flag_off_shore = CharField()
    vl_peso_carga_bruta = CharField()
    ano = CharField()
    mes = CharField()
    SGUF = CharField()
    porto_atracacao = CharField()

    class Meta:
        primary_key=False
        table_name = 'Carga_fato'

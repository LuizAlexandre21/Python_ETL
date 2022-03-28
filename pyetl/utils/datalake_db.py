# Pacotes 
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
# Carga Conteinerizada
class Carga_Conteinerizada(BaseModel):
    id_carga = TextField(primary_key=True)
    cd_mercadoria_conteinerizada = TextField()
    vl_peso_carga_bruta_conteinerizada = TextField()

    class Meta:
        table_name = 'Carga_Conteinerizada'

# Tempo de Atracacao 
class Tempo_Atracacao(BaseModel):
    id_atracacao = TextField(primary_key = True)
    espera_atracacao = TextField()
    espera_inicio_op = TextField()
    tempo_operacao = TextField()
    espera_desatracacao = TextField()
    tempo_atracado = TextField()
    tempo_estadia =  TextField()

    class Meta:
        table_name = 'Tempo_Atracacao'


# Acordos Bilaterais
class Acordos_Bilaterais(BaseModel):
    nacionalidade_embarcacao = TextField()
    ano_acordo = TextField()
    total_acordo_bilateral = TextField()
    acordo_tipo_navegação = TextField()
    pais = TextField()
    flag_embarque_desembarque = TextField()

    class Meta: 
        table_name = 'Acordo_Bilateral'

# Atracacao 
class Atracacao(BaseModel):
    id_atracacao = TextField(primary_key = True)
    CDTUP = TextField()
    id_berco = TextField()
    berco = TextField()
    porto_atracacao = TextField()
    apelido_instalacao_portuario = TextField()
    complexo_portuário =TextField()
    tipo_autoridade_portuaria = TextField()
    data_atracacao = TextField() 
    data_chegada = TextField() 
    data_desatracacao = TextField()
    inicio_operacao = TextField()
    temino_operacao = TextField()
    ano = TextField() 
    mes = TextField()
    tipo_operacao =TextField()
    tipo_navegacao = TextField() 
    nacionalidade_armador = TextField() 
    flag_mc_operacao_atracacao = TextField()
    terminal = TextField()
    município = TextField() 
    UF = TextField()
    SGUF = TextField() 
    regiao_geografica = TextField()
    num_capitania = TextField() 
    IMO = TextField() 
    
    class Meta:
        table_name = 'Atracacao'

# Carga Região 
class Carga_Regiao(BaseModel):
    id_carga = TextField(primary_key=True)
    regiao_geografica = TextField()
    valor_movimentado = TextField()

    class Meta:
        table_name = 'Carga_Região'

# Carga 
class Carga(BaseModel):
    id_carga = TextField(primary_key=True)
    id_atracacao = TextField()
    origem = TextField()
    destino = TextField()
    cd_mercadoria = TextField()
    operacao_carga = TextField()
    carga_geral_acondicionamento = TextField()
    conteiner_estado = TextField()
    tipo_navegacao = TextField()
    flag_autorizacao = TextField()
    flag_cabotagem = TextField()
    flag_cabotagem_movimentacao = TextField()
    flag_container_tamanho = TextField() 
    flag_longo_curso = TextField()
    flag_mc_opercacao_carga = TextField()
    flag_off_shore = TextField()
    flag_transporte_via_interior = TextField()
    percurso_vias_interior = TextField()
    percurso_interior = TextField()
    st_natureza_carga = TextField()
    st_sh2 = TextField()
    st_sh4 = TextField()
    natureza_carga = TextField()
    sentido = TextField()
    TEU = TextField()
    qt_carga = TextField()
    vl_peso_carga_bruta = TextField()

        class Meta:
            table_name = 'Carga'
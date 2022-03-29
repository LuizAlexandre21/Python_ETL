# Pacotes
from utils.Load_datalake import *

# Exportando os dados para tabela de atracacao
def Tempo_Atracacao(tempo_atracacao):
    campo = list(tempo_atracacao.collect())
    for num in range(tempo_atracacao.count()):
        field = campo[num]
        tempo_atracacao.insert(
            id_atracacao = field[0],
            espera_atracacao = field[1],
            espera_inicio_op = field[2],
            tempo_operacao = field[3],
            espera_desatracacao = field[4],
            tempo_atracado = field[5],
            tempo_estadia = field[6],
        ).on_conflict_replace().execute()


# Acordos Bilaterais
def Acordos_Bilaterais(acordos_bilaterais):
    campo = list(acordos_bilaterais.collect())
    for num in range(acordos_bilaterais.count()):
        field = campo[num]
        acordos_bilaterais.insert(
            nacionalidade_embarcacao = field[0],
            ano_acordo = field[1],
            total_acordo_bilateral = field[2],
            acordo_tipo_navegação = field[3],
            pais = field[4],
            flag_embarque_desembarque = field[5],
        ).on_conflict_replace().execute()


# Atracacao 
def Atracacao(atracacao):
    campo = list(atracacao.collect())
    for num in range(atracacao.count()):
        field = campo[num]
        atracacao.insert(
            id_atracacao =  field[0],
            CDTUP = field[1],
            id_berco = field[2],
            berco = field[3],
            porto_atracacao = field[4],
            apelido_instalacao_portuario = field[5],
            complexo_portuário =field[6],
            tipo_autoridade_portuaria = field[7],
            data_atracacao = field[8],
            data_chegada = field[9], 
            data_desatracacao = field[10],
            inicio_operacao = field[11],
            temino_operacao = field[12],
            ano = field[13], 
            mes = field[14],
            tipo_operacao = field[15],
            tipo_navegacao = field[16], 
            nacionalidade_armador = field[17],
            flag_mc_operacao_atracacao = field[18],
            terminal = field[19],
            município = field[20], 
            UF = field[21],
            SGUF = field[22], 
            regiao_geografica = field[23],
            num_capitania = field[24], 
            IMO = field[25],
        ).on_conflict_replace().execute()


# Carga Região 
def Carga_Regiao(carga_regiao):
    campo = list(carga_regiao.collect())
    for num in range(carga_regiao.count()):
        field = campo[num]
        carga_regiao.insert(
            id_carga = field[0],
            regiao_geografica = field[1],
            valor_movimentado = field[2],
        ).on_conflict_replace().execute()


# Carga 
class Carga(carga):
    campo = list(carga.collect())  
    for num in range(carga_regiao.count()):
        field = campo[num]
        carga_regiao.insert(
            id_carga = field[0],
            id_atracacao = field[1],
            origem = field[2],
            destino = field[3],
            cd_mercadoria = field[4],
            operacao_carga = field[5],
            carga_geral_acondicionamento = field[6],
            conteiner_estado = field[7],
            tipo_navegacao = field[8],
            flag_autorizacao = field[9],
            flag_cabotagem = field[10],
            flag_cabotagem_movimentacao = field[11],
            flag_container_tamanho = field[12],
            flag_longo_curso = field[13],
            flag_mc_opercacao_carga = field[14],
            flag_off_shore = field[15],
            flag_transporte_via_interior = field[16],
            percurso_vias_interior = field[17],
            percurso_interior = field[18],
            st_natureza_carga = field[19],
            st_sh2 = field[20],
            st_sh4 = field[21],
            natureza_carga = field[22],
            sentido = field[23],
            TEU = field[24],
            qt_carga = field[25],
            vl_peso_carga_bruta = field[26],
        ).on_conflict_replace().execute()

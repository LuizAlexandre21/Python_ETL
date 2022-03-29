# Pacotes
from utils import export_db 

# Exportando os dados para dataframe 
def export_atracacao(atracacao):
    campo = list(atracacao.collect())
    for num in range(atracacao.count()):
        field = campo[num]
        Atracacao_fato.insert(
            id_atracacao = field[0],
            CDTUP = field[1],
            Idberco = field[2],
            porto_atracacao = field[3],
            apelido_instalacao_portuaria = field[4],
            complexo_portuário = field[5],
            tipo_autoridade_portuaria = field[6],
            data_atracacao = field[7],
            data_chegada = field[8],
            data_desatracacao = field[9],
            inicio_operacao = field[10],
            termino_operacao = field[11],
            tipo_operacao = field[12],
            tipo_navegacao = field[13],
            nacionalidade_atracacao = field[14],
            flag_mc_operacao_atracacao = field[15],
            terminal = field[16],
            municipio = field[17],
            UF = field[18],
            SGUF = field[19],
            regiao_geografica = field[20],
            num_capitania = field[21],
            IMO = field[22],
            espera_atracacao = field[23],
            espera_inicio_op = field[24],
            espera_desatracacao = field[25],
            tempo_atracado = field[26],
            tempo_estadia = field[27],
            mes = field[28],
            ano = field[29],
        ).on_conflict_replace().execute()
    return print("Sucess to export data")


# Exportando dados para cargo 
def export_carga(carga):
    campo = list(carga.collect())
    for num in range(carga.count()):
        field = campo[num]
        Carga_Fato.insert(
            id_carga = field[0],
            flag_transporte_via_interior =  field[1],
            id_atracacao =  field[2],
            percurso_vias_interior =  field[3],
            origem =  field[4],
            percurso_interior =  field[5],
            destino =  field[6],
            st_natureza_carga =  field[7],
            cd_mercadoria =  field[8],
            st_sh2 =  field[9],
            tipo_operacao =  field[10],
            st_sh4 =  field[11],
            carga_geral_acondicionamento =  field[12],
            natureza_carga =  field[12],
            conteiner_estado =  field[13],
            sentido =  field[14],
            tipo_navegacao =  field[15],
            TEU =  field[16],
            flag_autorizacao =  field[17],
            vl_peso_carga_bruta =  field[18],
            qt_carga =  field[19],
            flag_cabotagem =  field[20],
            vl_peso_carga_bruta =  field[21],
            flag_cabotagem_movimentacao =  field[22],
            flag_container_tamanho =  field[23],
            flag_mc_opercacao_carga =  field[24],
            flag_off_shore =  field[25],
            vl_peso_carga_bruta =  field[26],
            ano =  field[27],
            mes =  field[28],
            SGUF =  field[29],
            porto_atracacao =  field[30]
        ).on_conflict_replace().execute()

    return print("Sucess to export data")


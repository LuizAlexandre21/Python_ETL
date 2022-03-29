# Criando a função de transformação 
def transformation(dataframe):

    # Importando os dados 
    files = dataframe

    # Separando as tabelas por identificadores
    # Dicionario para as filtragem das tabelas
    sep = {
        'Atracacao':[], # Tabelas que contem identificadores de atracacao nos portos
        'Carga':[], # Tabelas que contem identificadores de cargas 
        }

    # Separando por tabelas por anos
    for ano in files.keys():

        # Filtrando por tabelas contidas 
        for tabelas in files[ano].keys():

            # Capturando as tabelas
            tabela = files[ano][tabelas]

            # Fitrando as colunas contidas nas tabelas 
            for col in tabela.columns:

                # Se a tabela contem atracacao irá salvará na chave Atracacao
                if 'IDAtracacao' in col:
                    sep['Atracacao'].append(tabela)

                # Se a tabela contem carga irá salvará na chave carga
                elif 'IDCarga' in col:
                    sep['Carga'].append(tabela)

    # Agregando as tabelas 
    # Tabelas de Atracacao
    for indx in range(len(sep['Atracacao'])):

        # Se a tabela é primeira salva na variavel atracacao 
        if indx == 0 :
            atracacao = sep['Atracacao'][indx]

        # Se a tabela não é primeira, será agregada a tabela inicial
        else:
            atracacao = atracacao.join(sep['Atracacao'][indx],['IDAtracacao'],'left')

    # Tabelas de Atracacao
    for indx in range(len(sep['Carga'])):
        
        # Se a tabela é primeira salva na variavel carga  
        if indx == 0:
            carga = sep['Carga'][indx]
        
        # Se a tabela não é primeira, será agregada a tabela inicial
        else:
            carga = carga.join(sep['Carga'][indx],['IDCarga'],'left')


    # Filtrando as colunas
    # Atracação 
    atracacao = atracacao.select(
        [
            'IDAtracacao',
            'CDTUP',
            'IDBerco',
            'Porto Atracação',
            'Apelido Instalação Portuária',
            'Complexo Portuário',
            'Tipo da Autoridade Portuária',
            'Data Atracação',
            'Data Chegada',
            'Data Desatracação',
            'Data Início Operação',
            'Data Término Operação',
            'Tipo de Operação',
            'Tipo de Navegação da Atracação',
            'Nacionalidade do Armador',
            'FlagMCOperacaoAtracacao',
            'Terminal',
            'Município',
            'UF',
            'SGUF',
            'Região Geográfica',
            'Nº da Capitania',
            'Nº do IMO',
            'TEsperaAtracacao',
            'TEsperaInicioOp',
            'TOperacao',
            'TEsperaDesatracacao',
            'TAtracado',
            'TEstadia',
            'Ano',
            'Mes'
            ]
        )

    # Carga 
    carga = carga.select(
        [
            'IDCarga',
            'FlagTransporteViaInterioir',
            'IDAtracacao',
            'Percurso Transporte em vias Interiores',
            'Origem',
            'Percurso Transporte Interiores',
            'Destino',
            'STNaturezaCarga',
            'CDMercadoria',
            'STSH2',
            'Tipo Operação da Carga',
            'STSH4',
            'Carga Geral Acondicionamento',
            'Natureza da Carga',
            'ConteinerEstado',
            'Sentido',
            'Tipo Navegação',
            'TEU',
            'FlagAutorizacao',
            'QTCarga',
            'FlagCabotagem',
            'VLPesoCargaBruta',
            'FlagCabotagemMovimentacao',
            #'Ano da data de início da operação da atracação', 
            'FlagConteinerTamanho',
            #'Mês da data de início da operação da atracação',
            'FlagLongoCurso' ,
            #'Porto Atracação',
            'FlagMCOperacaoCarga',
            #'SGUF',
            'FlagOffshore',
            'VLPesoCargaBruta',
        ]
    )

    # Ajustando as colunas faltantes na tabela carga carga 
    # Tabelas Faltantes
    Falta = atracacao.select('IDAtracacao','Ano','Mes','SGUF','Porto Atracação')
    carga = carga.join(Falta,['IDAtracacao'],'left')

    # substituindo valores nulos
    atracacao = atracacao.na.fill(value='Null')
    cargo = carga.na.fill(value='Null')
    return atracacao, carga

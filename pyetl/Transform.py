# Pacotes 
from Extract import * 

# Importando os dados 
files = extract()

# Separando as tabelas 
# Dicionario para as tabelas 
sep = {
    'Atracacao':[], 
    'Carga':[],
    }

for ano in files.keys():
    for tabelas in files[ano].keys():
        tabela = files[ano][tabelas]
        for col in tabela.columns:
            if 'IDAtracacao' in col:
                sep['Atracacao'].append(tabela)
            elif 'IDCarga' in col:
                sep['Carga'].append(tabela)

# Unindo as tabelas
# Atracação 
for indx in range(len(sep['Atracacao'])):
    if indx == 0 :
        atracacao = sep['Atracacao'][indx]
    else:
        atracacao = atracacao.join(sep['Atracacao'][indx],['IDAtracacao'],'inner')

# Carga 
for indx in range(len(sep['Carga'])):
    if indx == 0:
        carga = sep['Carga'][indx]
    else:
        carga = carga.join(sep['Carga'][indx],['IDCarga'],'inner')


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
        'Ano da data de início da operação',
        'Mês da data de início da operação'
        ]
    )

# Carga 
Carga = Carga.select(
    [

    ]
)
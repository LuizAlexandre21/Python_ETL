<h1 align=center> Python - ETL </h1>
<h2 align=center> Data Integration dos dados da Agência Nacional de Transportes Aquaviários </h2>

---

Agência Nacional de Transportes Aquaviários (ANTAQ) é uma autarquia especial brasileira, com autonomia administrativa e funcional, vinculada ao Ministério da Infraestrutura. Ela é responsável pela regulamentação, controle tarifário, estudo e desenvolvimento do transporte aquaviário no Brasil.

---

## Informações do projeto 
![GitHub repo size](https://img.shields.io/github/repo-size/LuizAlexandre21/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/LuizAlexandre21/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/LuizAlexandre21/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/LuizAlexandre21/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/LuizAlexandre21/README-template?style=for-the-badge)

### Ajustes e melhorias 

O projeto ainda se encontra em sua versão de desenvolvimento, e as próximas atualizações serão voltadas nas seguintes tarefas:

- [x] Containerização do projeto 
- [x] Otimização da performance das solicitações
- [x] Desenvolvimento da extração endogena de arquivos do Qlik 
- [x] Estruturação dos bancos de dados
- [ ] Otimização das DAGs 


## 💻 Pré-requisitos

Antes de começar, verifique a instalação dos seguintes requisitos 

- [Python 3.9+](https://www.python.org/downloads/)
- [MySQL 8+](https://www.mysql.com/) ou [Mariadb 10.6 +](https://mariadb.org/)
- [Spark](https://spark.apache.org/downloads.html)


### Configurando Pré-requisitos 
#### Poetry 
Poetry ajuda você a declarar, gerenciar e instalar dependências de projetos Python, garantindo que você tenha a pilha certa em todos os lugares. Poetry traz ao Python o tipo de ferramenta de gerenciamento de projetos “tudo em um” que Go e Rust apreciam há muito tempo. Permitir que os projetos tenham dependências determinísticas com versões específicas de pacotes para que sejam construídos consistentemente em diferentes locais. O Poetry também facilita a criação, empacotamento e publicação de projetos e bibliotecas no PyPI para que outros possam compartilhar os frutos de seus trabalhos em Python. O

##### Instalando o poetry
- Linux 
```sh 
curl -sSL \
https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
```
- Windows 
```sh 
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

#### Apache Spark 
O Spark é um mecanismo multilíngue para execu
dada a utilização do tutorial apresentado pelo Bruno Katekawa, disponibilizado no (Designed by Data)[https://medium.com/designed-by-data/instalando-apache-pyspark-para-funcionar-com-jupyter-notebook-no-macos-42f992c45842]


#### Apache Airflow 
O apache airflow é um código aberto plataforma de gerenciamento de fluxo de trabalho para pipelines de engenharia de dados. Tudo começou em Airbnb em outubro de 2014[2] como uma solução para os fluxos de trabalho de trabalho cada vez mais complexos da empresa. Fluxo de fluxo de permissão para o Airbnb autorizar e agendar programaticamente seus fluxos de trabalho e monitores de atravados do fluxo de ar incorporado interface do usuário.[3][4] Desde o início, o projeto foi tornado de código aberto, tornado-se um Incubadora Apache projeto em março de 2016 e um nível superior Apache Software Foundation projeto em janeiro de 2019.

- Para configuração do Apache Airflow é recomendada a utilização do tutorial apresentado no (dev.to)[https://dev.to/citizenkot/apache-airflow-installation-mysql-celery-4n76] e 


#### MySQL
O MySQL é um sistema de gerenciamento de banco de dados (SGBD), que utiliza a linguagem SQL (Linguagem de Consulta Estruturada, do inglês Structured Query Language) como interface. É atualmente um dos sistemas de gerenciamento de bancos de dados mais populares[da Oracle Corporation, com mais de 10 milhões de instalações pelo mundo

- Para configuração do Apache Airflow é recomendada a utilização do tutorial apresentado na Wiki do (Archlinux)[https://wiki.archlinux.org/title/MySQL]


## Arquivos do Repositórios 


- **/utils** : Pasta que contem arquivos e funções que auxiliam a construção do processo de ETL 
    - **scraping_Qlik.py** : Raspador de arquivos contidos na plataforma de análises de negócios Qlik. 
    - **scraping.py**: Raspador dos arquivos comprimidos disponibilizados pela a Antaq 
    - **datalake_db.py** : ORM destinado as tabelas para a exportação para as tabelas do datalake.
    - **export_db.py** : ORM destinado as tabelas para a exportação para as tabelas processados.
- **/airflow** :
    - **ETL_<year>** : Arquivo para extração, tratamento e carregamento para os dados da antaq utilizados no processamento do airflow, para um determinado ano

- **Extract.py** : Arquivo para a extração dos dados disponibilizados no anuario estatistico da Antaq 
- **Transform.py**  : Arquivo para o tratamento dos arquivos extraidos anteriormente pela função extract 
- **Load.py** : Arquivo para o carregamento dos arquivos extraidos e tratados para as tabelas finais
- **Load_datalake**: Arquivo para o carregamento das tabelas brutas extraidas 
- **ETL.py**: Arquivo para extração, tratamento e carregamento para os dados da antaq 

Para maiores detalhes dos arquivos, consultar o arquivo de documentação do projeto disponivel em 

## Execução do Projeto 
### Clonando o repositório

```sh
$ git clone https://github.com/LuizAlexandre21/Python_ETL.git
```

### Instalando as dependências do projeto 

```sh
$ sudo poetry install 
```

### Executando o processo 

```sh
$ sudo poetry run python ETL.py
```

### Executando o Airflow 
```
$ sudo airflow webserver 
$ sudo airflow scheduler
$ sudo airflow worker 
```


## 📫 Contribuindo para Python - ETL
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->
Para contribuir com Python - ETL, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).


## Algumas perguntas e respostas sobre o projeto 

#### Porque a utilização do poetry ?


#### Qual a motivação da escolha de um banco de dados SQL ao invés de um banco de dados NoSQL? E porque a escolha do MySQL?


#### Porque a utilização de ORM para a manipulação do banco de dados 


#### Vantagens da utilização do PySpark no projeto 


#### Porque da utilização de um webscraping ao inves de uma solicitação junto ao Qlik? 


## Contato 

:bust_in_silhouette: Luiz Alexandre Moreira Barros 

:mailbox_with_mail:	 luizalexandremoreira21@outlook.com

:octocat: https://github.com/LuizAlexandre21

:notebook_with_decorative_cover: http://lattes.cnpq.br/9458204748985902

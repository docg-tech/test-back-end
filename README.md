# Test Backend

## Rodar a aplicação

### Container
Para rodar a aplicação em container, é utilizado o docker-compose. 
```bash
docker-compose up
```

### Localmente

#### Ambiente Virtual
É necessario utilizar um ambiente virtual para gerenciar as dependencias.
Recomenda-se o uso do [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

Criar ambiente virtual:
```bash
conda -n <nome_ambiente> python=3.10
```

Instalar dependencias:
```bash
conda activate <nome_ambiente>
pip install -r requirements.txt
```

### Rodando a aplicação
É necessario criar um arquivo para as variaveis de ambiente
```bash
touch .env.example > .env
```
***Após criar, setar as configurações***

#### Banco de Dados
Criar tabela para a API:
```SQL
CREATE DATABASE nome_tabela;
```

Sincronizar com o Flask-Migrate:
```bash
flask db upgrade
```

#### Rodando
```bash
flask run
```
---
## Estrutura do Projeto
Neste projeto é utilizado Flask com algumas extensões para suporte, tais como
Flask-RESTful para padronização da estrutura REST, Flask-SQLAlchemy para integração
do ORM ao Flask, e Flask-Migrate para versionamento de banco de dados.


### Instalando o hook para pre-commit
`pre-commit install --hook-type pre-commit --hook-type commit-msg`


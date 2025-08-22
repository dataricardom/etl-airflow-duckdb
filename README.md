# Orquestrando ETL com Airflow e DuckDb 🦆

## Ricardo Marques


Criando orquestrações de Dados com Airflow e banco de dados DuckDb.


Primeiros passos:

Usando Astro CLI para criar um conteiner Docker com Airflow.

- O comando **astro dev init** inicializa um novo projeto Astronomer, criando a estrutura mínima de um projeto Airflow local (dags/, Dockerfile, requirements.txt, etc.).

```bash

astro dev init

```

- O Comando **astro dev start** Sobe o ambiente Airflow completo em Docker Compose (com Scheduler, Webserver, Triggerer, Postgres e Flower).

```bash

astro dev start

```

Os dois comandos acima são um atalho para você rodar e gerenciar um Airflow local usando Docker. Te fazendo economizar tempo com configuração de airflow.





# Migração PostgreSQL → DuckDB com Airflow

Este projeto define uma **DAG no Airflow** que realiza a migração incremental de dados de uma tabela no PostgreSQL para o DuckDB, utilizando um operador customizado.

---

## Objetivo

O objetivo é automatizar a sincronização de dados entre PostgreSQL e DuckDB, garantindo que apenas **novos registros** sejam inseridos no DuckDB a cada execução.

---

## DAG: `pipeline_de_migracao_postgres_to_duckdb`

- **Schedule:** A cada 5 minutos (`*/5 * * * *`)  
- **Catchup:** Desativado (`catchup=False`)  
- **Task:** `postgres_to_duckdb` usando o operador customizado `PostgresToDuckDBOperator`

---

## Operador Customizado: `PostgresToDuckDBOperator`

### Parâmetros
- `postgres_schema`: Schema da tabela de origem no PostgreSQL  
- `postgres_table_name`: Nome da tabela de origem no PostgreSQL e destino no DuckDB  
- `duckdb_conn_id`: ID da conexão Airflow para DuckDB  
- `postgres_conn_id`: ID da conexão Airflow para PostgreSQL  

### Funcionalidade
1. Conecta ao **DuckDB** e ao **PostgreSQL** via conexões do Airflow  
2. Instala e carrega o módulo `postgres` no DuckDB  
3. Cria a tabela no DuckDB se não existir, copiando todos os dados do PostgreSQL  
4. Realiza **migração incremental** inserindo apenas os registros novos (com base em `created_at`)  
5. Loga a operação ao final

---

## Como usar
1. Configurar as conexões do Airflow:
   - `motherduck_conn` → DuckDB  
   - `postgres_conn` → PostgreSQL  

2. Colocar os arquivos:
   - `duckdb_operator.py` → DAG  
   - `postgres_to_duckdb_operator.py` → operador customizado  

3. Iniciar o Airflow e a DAG será executada automaticamente a cada 5 minutos.

---

## Observações
- Certifique-se de que o módulo `postgres` do DuckDB está disponível  
- A sincronização incremental depende da coluna `created_at` na tabela do PostgreSQL

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
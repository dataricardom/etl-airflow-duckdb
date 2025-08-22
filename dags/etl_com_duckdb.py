#%%
import duckdb
from airflow.decorators import dag, task 
from datetime import datetime 

path = "./data/clientes_exemplo.csv"

@dag(
    dag_id="etl_com_duckdb",
    description="Etl utilizando duckdb",
    schedule="@daily",
    start_date=datetime(2025,8,21),
    catchup=False

)
def etl_com_duckdb_ex():
    @task
    def extrair():
# Criar conexão em memória
        con = duckdb.connect(database=":memory:")
        df = con.execute(f"SELECT * FROM read_csv_auto('{path}')").fetchdf()
        print(" Dados extraídos:")
        print(df)
        return df.to_dict(orient="list")
    @task
    def transformar(dados: dict):
        import pandas as pd
        df = pd.DataFrame(dados)
        # Exemplo: filtrar apenas clientes com idade > 30
        df_filtrado = df[df["idade"] > 30]
        print(" Dados transformados (idade > 30):")
        print(df_filtrado)
        return df_filtrado.to_dict(orient="list")
    @task
    def load(dados: dict):
        import pandas as pd
        df = pd.DataFrame(dados)

        # Salvar resultado em um novo CSV
        output_path = "./data/clientes_transformados.csv"
        df.to_csv(output_path, index=False, encoding="utf-8")

        print(f" Dados carregados em: {output_path}")

    t1 = extrair()
    t2 = transformar(t1)
    t3 = load(t2)
    
    t1 >> t2 >> t3


etl_com_duckdb_ex()

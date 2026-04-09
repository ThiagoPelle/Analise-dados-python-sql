
import os
import pandas as pd
import sqlite3

base_path = os.path.dirname(__file__)

data_path = os.path.join(base_path, "..", "data", "vendas_dataset.csv")
db_path = os.path.join(base_path, "..", "data", "vendas", "banco.db")

df = pd.read_csv(data_path)

conn = sqlite3.connect(db_path)
import sqlite3

conn = sqlite3.connect('banco.db')

df.to_sql("vendas", conn, if_exists="replace", index=False)

query = """
SELECT categoria, SUM(preco * quantidade) AS total_vendas
FROM vendas
GROUP BY categoria
"""

resultado = pd.read_sql_query(query, conn)

print(resultado)



# limpeza de dados
df = df.dropna()

# criar coluna total
df["total"] = df["preco"] * df["quantidade"]

print("\nDados tratados:")
print(df)

# conectar banco sqlite
conn = sqlite3.connect("data/vendas.db")

# salvar no banco
df.to_sql("vendas", conn, if_exists="replace", index=False)

print("\nDados enviados para o banco SQL")



print("\nResumo de vendas:")
print(resultado)
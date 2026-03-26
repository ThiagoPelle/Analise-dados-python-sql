import pandas as pd
import sqlite3

# carregar dados
df = pd.read_csv("data/vendas.csv")

print("Dados carregados:")
print(df.head())

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

# consulta SQL
query = """
SELECT categoria, SUM(total) as total_vendas
FROM vendas
GROUP BY categoria
"""

resultado = pd.read_sql_query(query, conn)

print("\nResumo de vendas:")
print(resultado)
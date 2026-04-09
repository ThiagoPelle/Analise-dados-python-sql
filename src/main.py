import pandas as pd
import sqlite3
import os

# Caminho do CSV
caminho_csv = os.path.join('data', 'vendas', 'dataset.csv')

# Ler os dados (sep=';' porque o CSV usa ponto e vírgula)
df = pd.read_csv(caminho_csv, sep=';')

print("Dados carregados:")
print(df.head())

# Criar conexão com banco SQLite
conn = sqlite3.connect('database.db')

# Enviar dados para o banco
df.to_sql('vendas', conn, if_exists='replace', index=False)

print("Dados enviados para o banco com sucesso!")

# Consulta SQL
query = """
SELECT produto, SUM(quantidade) as total_vendido,
SUM(quantidade * preco) as faturamento
FROM vendas
GROUP BY produto
"""

resultado = pd.read_sql(query, conn)

print("\nResultado da análise:")
print(resultado)

# Fechar conexão
conn.close()
# 📊Análise de Dados com Python e SQL

Pipeline completo de análise de vendas: da coleta ao insight — usando Python, Pandas e SQLite.

## 🧠 Sobre o Projeto
Este projeto simula um fluxo real de análise de dados em uma empresa de varejo, cobrindo todas as etapas do processo analítico: ingestão de dados brutos em CSV, armazenamento em banco de dados relacional, consultas SQL para extração de métricas e geração de insights de negócio.
O objetivo é demonstrar na prática como transformar dados brutos de vendas em informações estratégicas que apoiam a tomada de decisão.
  
## 🗂️ Estrutura do Projeto
  Analise-dados-python-sql/
  

├── data/
│   └── vendas/
│       └── dataset.csv         # Base de dados com 750 registros de vendas




├── notebooks/
│   └── analise.ipynb           # Análise exploratória interativa



├── sql/
│   └── consultas.sql           # Consultas SQL reutilizáveis



├── src/
│   └── main.py                 # Script principal do pipeline


├── database.db                 # Banco de dados SQLite gerado
└── README.md

## ⚙️ Tecnologias Utilizadas
Tecnologia Finalidade

Python: 3.14 Linguagem principal 

Pandas: Leitura,limpeza e manipulação de dados

SQLite3: Banco de dados relacional local

Jupyter Notebook: Análise exploratória e visualização

VS Code: Ambiente de desenvolvimento

## 🔄 Pipeline de Dados

1. Coleta — Leitura do CSV com separador ; via Pandas
2. Limpeza — Tratamento de tipos, valores nulos e inconsistências
3. Armazenamento — Inserção no banco SQLite com controle de duplicatas
4. Análise — Consultas SQL para geração de métricas de negócio


## 📦 Dataset
O dataset contém 750 registros de vendas com as seguintes colunas:
ColunaTipoDescriçãoidintIdentificador único da vendaprodutostrNome do produto vendidocategoriastrCategoria do produto (Eletrônicos, Móveis, Acessórios)precointPreço unitário do produtoquantidadeintQuantidade vendidadatastrData da venda (dd/mm/yyyy)

## 📈 Principais Análises

Faturamento por produto — Identificação dos produtos mais rentáveis
Volume de vendas por categoria — Comparativo entre Eletrônicos, Móveis e Acessórios
Tendência temporal — Evolução das vendas ao longo dos meses
Ticket médio — Valor médio por transação

## 🚀 Como Executar

Pré-requisitos
pip install pandas


Rodando o pipeline
 Clone o repositório
git clone https://github.com/seu-usuario/Analise-dados-python-sql.git

 Entre na pasta do projeto
cd Analise-dados-python-sql

 Execute o script principal
python src/main.py 


### Explorando os dados
Abra o Jupyter Notebook para a análise exploratória:

jupyter notebook notebooks/analise.ipynb



### 👨‍💻 Autor
Thiago

Desenvolvido como projeto prático de análise de dados com Python e SQL.

### 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.








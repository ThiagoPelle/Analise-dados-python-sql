
SELECT produto, 
       SUM(quantidade) AS total_vendido,
       SUM(quantidade * preco) AS faturamento
FROM vendas
GROUP BY produto;
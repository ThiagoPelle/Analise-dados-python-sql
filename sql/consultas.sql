
SELECT categoria, SUM(preco * quantidade) AS total_vendas
FROM vendas
GROUP BY categoria;


SELECT produto, SUM(quantidade) AS total_vendido
FROM vendas
GROUP BY produto
ORDER BY total_vendido DESC;
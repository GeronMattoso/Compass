SELECT * FROM LIVRO;
SELECT * FROM EDITORA;
SELECT * FROM AUTOR;
/*Exercicio 3 a
Listar livros publicados após 2014
*/
SELECT Titulo, Publicacao FROM LIVRO WHERE YEAR(Publicacao)>2014;
/*Exercicio 3 b
Listar 10 livros mais caros
*/
SELECT Titulo, Valor FROM LIVRO ORDER BY(Valor) DESC LIMIT 10;
/*Exercicio 3 c
Listar as 5 editoras que mais tem livros na biblioteca
*/
SELECT Nome, COUNT(*) "Qtd Livros" FROM EDITORA
	JOIN LIVRO
		ON EDITORA.CodEditora=LIVRO.Editora
			WHERE LIVRO.Autor
			GROUP BY Editora ORDER BY COUNT(*) DESC LIMIT 5;
/*Exercicio 3 d
 Listar a quantidade de publicações de cada autor
*/
SELECT Nome, COUNT(Nome) AS Publicacoes FROM programa_bolsas.AUTOR
	INNER JOIN programa_bolsas.LIVRO
		ON AUTOR.CodAutor = LIVRO.AUTOR GROUP BY Nome ORDER BY COUNT(NOME) DESC;
/*Exercicio 3 e
 Listar a quantidade de publicações de cada editora
*/
SELECT Editora, COUNT(*) FROM LIVRO GROUP BY Editora ORDER BY COUNT(*) DESC;
/*Exercicio 3 f
 Listar qual é o autor com mais publicações
*/
SELECT Nome, COUNT(NOME) AS N_PUBLICACOES
	FROM programa_bolsas.AUTOR 
    INNER JOIN programa_bolsas.LIVRO
    ON AUTOR.CodAutor = LIVRO.Autor
        GROUP BY Nome ORDER BY N_PUBLICACOES DESC LIMIT 1;
/*Exercicio 3 g
Listar qual é o autor com menos ou nenhuma publicação
*/
SELECT Autor, COUNT(*) FROM LIVRO GROUP BY Autor ORDER BY COUNT(*) ASC LIMIT 1;

SELECT Nome, COUNT(*) FROM AUTOR RIGHT JOIN LIVRO on AUTOR.CodAutor=LIVRO.Autor 
WHERE LIVRO.Autor GROUP BY Autor ORDER BY COUNT(*) ASC LIMIT 1;

SELECT Nome, COUNT(Publicacao) FROM AUTOR RIGHT JOIN LIVRO
	ON AUTOR.CodAutor=LIVRO.Autor 
	WHERE Publicacao iS NULL;
    #WHERE LIVRO.Autor GROUP BY Autor ORDER BY COUNT(*) ASC LIMIT 1;

#------------------

SELECT * FROM TbDependente;
SELECT * FROM TbEstoqueProduto;
SELECT * FROM TbVendas;
SELECT * FROM TbVendedor;

#Selecione o nome e o código do vendedor com o maior número de vendas
SELECT TbVendedor.NmVdd, TbVendedor.CdVdd, COUNT(*) AS Qtd_Vendas 
	FROM TbVendas
    INNER JOIN TbVendedor ON TbVendas.CdVdd = TbVendedor.CdVdd
GROUP BY CdVdd ORDER BY Qtd_Vendas DESC LIMIT 1;





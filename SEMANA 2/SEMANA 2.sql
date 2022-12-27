#Listar 10 livros mais caros
SELECT LIVRO.Cod AS "Codigo do Livro", LIVRO.Titulo, LIVRO.Autor AS "Codigo do Autor", AUTOR.Nome AS "Nome do Autor", LIVRO.Valor, LIVRO.Editora AS "Codigo da Editora", EDITORA.Nome AS "Nome da Editora"
FROM EDITORA
	INNER JOIN LIVRO
		ON EDITORA.CodEditora=LIVRO.Editora
	INNER JOIN AUTOR
		ON AUTOR.CodAutor = LIVRO.Autor
	ORDER BY(Valor) DESC LIMIT 10;

#Listar as 5 editoras que mais tem livros na biblioteca
SELECT LIVRO.Cod AS "Codigo do Livro", LIVRO.Titulo, LIVRO.Autor AS "Codigo do Autor", AUTOR.Nome AS "Nome do Autor", LIVRO.Valor, LIVRO.Editora AS "Codigo da Editora", EDITORA.Nome AS "Nome da Editora", count(*) AS "Qtd_Livros"
FROM EDITORA
	INNER JOIN LIVRO
		ON EDITORA.CodEditora=LIVRO.Editora
	INNER JOIN AUTOR
		ON AUTOR.CodAutor = LIVRO.Autor
	WHERE LIVRO.Autor
	GROUP BY Editora ORDER BY COUNT(*) DESC LIMIT 5;
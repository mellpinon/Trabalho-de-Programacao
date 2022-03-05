from model.Livro import Livro


class LivroDao:
    def __init__(self, connection):
        self.connection = connection

    def selecionarLivros(self) -> list:
        c = self.connection.cursor()
        sql = 'SELECT * FROM livro ORDER BY id'
        c.execute(sql)
        recset = c.fetchall()
        c.close()

        lista = []
        for item in recset:
            livro = Livro()
            livro.id = item[0]
            livro.titulo = item[1]
            livro.genero = item[2]
            livro.autor = item[3]

            lista.append(livro)

        return lista

    def selecionarLivro(self, id) -> Livro:
        c = self.connection.cursor()
        c.execute(f"SELECT * FROM livro WHERE id = {id}")
        recset = c.fetchone()
        c.close()

        print(recset)

        livro = Livro()
        livro.id = recset[0]
        livro.titulo = recset[1]
        livro.genero = recset[2]
        livro.autor = recset[3]

        return livro

    def inserirLivro(self, livro: Livro) -> Livro:
        c = self.connection.cursor()
        c.execute("""
            insert into livro(id, titulo, genero, autor)
            values('{}', '{}', '{}', '{}') RETURNING id
        """.format(livro.id, livro.titulo, livro.genero, livro.autor))
        self.connection.commit()

    def excluirLivro(self, livro: Livro) -> Livro:
        c = self.connection.cursor()
        c.execute("""
            delete from livro
            where id = '{}'
        """.format(livro.id))
        self.connection.commit()

    def alterarLivro(self, livro: Livro) -> Livro:
        c = self.connection.cursor()
        c.execute("""
            update livro
            SET titulo = '{}', genero = '{}', autor = '{}'
            WHERE id = '{}';
        """.format(livro.titulo, livro.genero, livro.autor, livro.id))

        self.connection.commit()



from config.Config import Config
from config.Database import Database
from dao.LivroDao import LivroDao
from model.Livro import Livro
from flask import Flask, request, render_template

app = Flask(__name__)
dao = LivroDao(Database(Config().config).conn)


@app.route('/livro/novo', methods=["GET"])
def novo():
    return render_template("inserir.html")

@app.route('/livro/novo', methods=["POST"])
def inserir():
    
    livro = Livro()
    livro.id = request.form.get("id")
    livro.titulo = request.form.get("titulo")
    livro.genero = request.form.get("genero")
    livro.autor = request.form.get("autor")

    dao.inserirLivro(livro)

    lista = dao.selecionarLivros()
    
    return render_template(
        "Listagem.html",
        lista=lista
    
    )

@app.route('/', methods=["GET"])
def listar():
    lista = dao.selecionarLivros()
    return render_template(
        "Listagem.html",
        lista=lista
    )

@app.route('/livro/remover/<id>', methods=["GET"])
def remover(id):
    
    livro = Livro()
    livro.id = id
    dao.excluirLivro(livro)
    
    lista = dao.selecionarLivros()
    
    return render_template(
        "Listagem.html",
        lista=lista
    )

@app.route('/livro/<id>', methods=["GET"])
def editarPagina(id):
    livro = dao.selecionarLivro(id)
    return render_template("editar.html", livro=livro)

@app.route('/livro/editar', methods=["POST"])
def editar():
    livro = Livro()
    livro.id = request.form.get("id")
    livro.titulo = request.form.get("titulo")
    livro.genero = request.form.get("genero")
    livro.autor = request.form.get("autor")
    livro = dao.alterarLivro(livro)

    lista = dao.selecionarLivros()
    
    return render_template(
        "Listagem.html",
        lista=lista
    )

if __name__ == '__main__':
    app.run()

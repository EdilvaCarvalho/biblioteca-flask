from flask import Flask, render_template, request

class Livro:
    def __init__(self, nome, genero, autor):
        self.nome = nome
        self.genero = genero
        self.autor = autor

livro1 = Livro('A Moreninha', 'Romance', 'Joaquim Manuel de Macedo')
livro2 = Livro('As Crônicas de Nárnia', 'Fantasia', 'C. S. Lewis')
livro3 = Livro('Iracema', 'Romance', 'José de Alencar')
lista = [livro1, livro2, livro3]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo="Livros", livros=lista)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo='Novo Livro')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    genero = request.form['genero']
    autor = request.form['autor']
    livro = Livro(nome, genero, autor)
    lista.append(livro)
    return render_template('lista.html', titulo="Livros", livros=lista)

app.run(debug=True)
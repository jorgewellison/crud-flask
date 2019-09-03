from flask import Flask, render_template, request, redirect, session, flash  # importando do pacote flask a classe Flask

app = Flask(__name__) #app recebe o objeto instanciado, que executa o modulo __name__
app.secret_key = 'dsc'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon GO', 'RPG', 'Mobile')
jogo3 = Jogo('Clash Royale', 'Estratégia', 'Mobile')
lista = [jogo1, jogo2, jogo3]

@app.route('/') #diretiva mostrando o caminho da rota
def index():
    return render_template('lista.html', titulo='Jogos',
                           jogos = lista) #helper ajuda a renderizar o html

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
     nome = request.form['nome']
     categoria = request.form['categoria']
     console = request.form['console']
     jogo = Jogo(nome, categoria, console)
     lista.append(jogo)
     return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario'] #dicionario com valores, flask guarda através de cookie a informação do usuario
        flash(request.form['usuario'] + ' logou com sucesso!') #mensagem flash, mensagem rápida
        return redirect('/')
    else:
        flash('Não logado, tente novamente!')
        return redirect('/login')

app.run(debug=True) #rodando o app
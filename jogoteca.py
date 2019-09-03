from flask import Flask, render_template, request, redirect, session, flash, \
    url_for  # importando do pacote flask a classe Flask

app = Flask(__name__)  # app recebe o objeto instanciado, que executa o modulo __name__
app.secret_key = 'dsc'  # encriptando dados da sessão


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha


usuario1 = Usuario('Jorge', 'Jorge Wellison', '1234')
usuario2 = Usuario('Airton', 'Airton Felix', '4321')
usuario3 = Usuario('Leonardo', 'José Leonardo', 'LZNHACKER')

usuarios = {usuario1.id: usuario1, usuario2.id: usuario2,
            usuario3.id: usuario3}  # através do dicionário, será possível achar o usuario através de seu ID

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon GO', 'RPG', 'Mobile')
jogo3 = Jogo('Clash Royale', 'Estratégia', 'Mobile')
lista = [jogo1, jogo2, jogo3]


@app.route('/')  # diretiva mostrando o caminho da rota
def index():
    return render_template('lista.html', titulo='Jogos',
                           jogos=lista)  # helper ajuda a renderizar o html


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]  # retorna o usuario com o id especifico
        if usuario.senha == request.form['senha']:
            session[
                'usuario_logado'] = usuario.id  # dicionario com valores, flask guarda através de cookie a informação do usuario
        flash(usuario.nome + ' logou com sucesso!')  # mensagem flash, mensagem rápida
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado')
    return redirect(url_for('login'))


app.run(debug=True)  # rodando o app

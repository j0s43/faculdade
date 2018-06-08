# importando as bibliotecas
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from db import config, connect

# Instanciar a app e o bd
faculdade = Flask(__name__)
mysql = MySQL()
mysql.init_app(faculdade)


# criar uma rota para /
@faculdade.route('/')

# metodo que responde a rota /
def index():
    return render_template('login.html')

# criar uma rota para login
@faculdade.route('/login', methods=['POST'])

# metodo que responde a rota /login
def login():
    # recupera os parametro
    param_nome = request.form.get('nome')
    param_senha = request.form.get('senha')

    # configurar o db
    config(faculdade)

    # obtendo a conexao e o cursor
    conn, cursor = connect(mysql)

    # executando o sql
    cursor.execute(f'SELECT idusuario FROM usuario where nomeusuario = "{param_nome}" and senhausuario = "{param_senha}"')

    # obter o retorno
    idusuario = cursor.fetchone()

    #fechar o cursor
    cursor.close()

    if idusuario is None:
        return 'Usuario invalido'
    else:
        return render_template('principal.html', nome=param_nome, idusuario=idusuario[0])


# rata para /listarturma
@faculdade.route('/listarTurma')
# metodo para tratar requesicao /listar turma
def listar_turmas():
    # recuperar os parametros
    id = request.args.get('id')

    # configurar o db
    config(faculdade)

    # obtendo a conexao e o cursor
    conn, cursor = connect(mysql)

    # executar o sql
    cursor.execute(f'SELECT d.nomedisciplina, d.cursodisciplina, t.nometurma, t.diaturma from disciplina d, turma t, usuario u where u.idusuario = {id} and t.idusuario = u.idusuario and d.iddisciplina = t.iddisciplina')

    #retorno do select
    turmas = cursor.fetchall()

    #fechar o cursor
    cursor.close()

    return render_template('turmas.html', id=id, turmas=turmas)

# Iniciar a app
faculdade.run(debug=True)

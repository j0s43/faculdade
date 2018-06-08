
# funcao para configurar db
def config(app):
    # conectar no bd
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'faculdade'

# funcao que retorna uma conexao e um cursor
def connect(mysql):
    # obter a conexao
    conn = mysql.get_db()
    # obter o cursor
    c = conn.cursor()

    return conn, c



# funcao para validar usuario
def validar_usuario(cur, nome, senha):
    # executar o sql
    cur.execute(f'SELECT idusuario FROM usuario where nomeusuario = "{nome}" and senhausuario = "{senha}"')

    # obter o retorno
    idusuario = cur.fetchone()

    # fechar o cursor
    cur.close()

    # retorno da funcao
    if idusuario is None:
        return False, None
    else:
        return True, idusuario[0]




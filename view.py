import sqlite3 as lite


#criando conexao

con = lite.connect('dados.bd')

#lista = ['Maria Teresa','joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de uma consultar pessoalmente']

#inserir informacoes
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario2 (nome, email, telefone, Dia_em, estado, assunto) VALUES (?,?,?,?,?,?)"
        cur.execute(query, i)



# ler informacoes
def mostar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario2"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista



# Update Atualizar informacoes

def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario2 SET nome=?, email=?, telefone=?, Dia_em=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query, i)





#deletar informacoes

def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario2 WHERE id=?"
        cur.execute(query, i )


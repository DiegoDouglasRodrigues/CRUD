import sqlite3 as lite


#criando conexao

con = lite.connect('dados.bd')

cur = con.cursor()


#nome = str('diego')
#data_consulta = str('30/11/2022')

print('conexao bem sucedida')
Dia_em = str('03/11/2022')
nome = str('D')


with con:
    cur = con.cursor()
    consulta_banco = f"""SELECT * FROM formulario2 
    WHERE nome LIKE ('{nome}%') 
AND Dia_em LIKE ('{Dia_em}')"""

    cur.execute(consulta_banco)
    print(consulta_banco)

        #informacao = cur.fetchall()

#pesquisar_info()
#print(query)
def pesquisar():
    nome = e_nome.get()
    Dia_em = e_Dia_em.get()
    with con:
        cur = con.cursor()
        query = f"""SELECT * FROM formulario2 
        WHERE nome LIKE ('{nome}%') 
        AND Dia_em LIKE ('{Dia_em}')"""
        cur.execute(query)
        informacao = cur.fetchall()

        lista = [nome, Dia_em]

        for i in informacao:
            lista.append(i)

            print(informacao)

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()
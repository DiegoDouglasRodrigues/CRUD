#importando Tkinter
from cgitb import text
from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import font
from tkinter import ttk
import phonenumbers


#importando views
from view import *
from tkinter import messagebox


cor0 = "#000608"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#4fa882"  # verde
cor3 = "#38576b"  # valor
cor4 = "#403d3d"   # letra
cor5 = "#e06636"   # - profit
cor6 = "#c3e6fa"   # azul
cor7 = "#9e5757"   # vermelha BOTAO
cor8 = "#3a9e4b"   # + verde BOTAO
cor9 = "#e9edf5"   # sky blue
cor10= "#e3f4fc" #azul mais claro
cor11= "#c3e3eb" #azul mais ou menos
cor12 = "#1e7898"  #azul escuro botao

# criando a janela

janela = Tk()
janela.title('SUS')
janela.geometry('1300x600')
janela.configure(bg=cor6)
#janela.resizable (width=FALSE, height=FALSE)

#frame de cima
frame_cima = Frame(janela, width=400, height=60, bg=cor2, relief='flat')
frame_cima.grid(row=0, column=0)

#frame debaixo
frame_debaixo = Frame(janela, width=400, height=1550, bg=cor10, relief='flat')
frame_debaixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

#frame direita ( maior )
frame_direita = Frame(janela, width=950, height=1550, bg=cor11, relief='flat')
frame_direita.grid(row=0, column=1, padx=1, pady=0, rowspan=2, sticky=NSEW,)


# label cima
nomesistema = Label(frame_cima, text='Formulario de consultoria', font=('arial 15 bold'), anchor=NW, foreground=cor1, bg=cor2, relief='flat')
nomesistema.place(x=10, y=20)





def mostrar():
    global tree
    lista = mostar_info()

    #lista para cabecalho
    tabela_cabecalho = ['ID', 'Nome', 'Email', 'Telefone', 'Data', 'estado', 'Obervacao']

    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_cabecalho, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","center","center","center"]
    h=[40,180,180,100,120,80,180]
    n=0

    for col in tabela_cabecalho:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)

#chamando a funcao mostrar
mostrar()

#variaveis
global tree

#funcao inserir
def inserir():
    nome = e_nome.get()
    nome = nome.upper()

    email = e_email.get()

    telefone = e_telefone.get()


    Dia_em = e_Dia_em.get()


    estado = e_estadoconsulta.get()
    estado = estado.upper()

    assunto = e_assunto.get()
    assunto = assunto.upper()

    digitos_telefone = 11

    if  len(telefone) != digitos_telefone:
        messagebox.showerror('Erro', 'O numero de telefone deve contar {} digitos \n APENAS NUMEROS!'.format(digitos_telefone))

    elif not '@' in email:
        messagebox.showerror('Erro', 'E-mail incorreto')

    elif not telefone.isnumeric():
       messagebox.showerror('Erro', 'Numero de telefone deve ser numérico')

    else:
        lista = [nome, email, telefone, Dia_em, estado, assunto]


        if nome=='':
            messagebox.showerror('Erro', 'Preencher o nome')
        else:
            inserir_info(lista)
            messagebox.showinfo('Sucesso', 'dados inseridos com sucesso')

            e_nome.delete(0,'end')
            e_email.delete(0,'end')
            e_telefone.delete(0,'end')
            e_Dia_em.delete(0,'end')
            e_estadoconsulta.delete(0, 'end')
            e_assunto.delete(0,'end')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()


#funcao atualizar
def atualizar():
    try:
        tree_dados = tree.focus()
        treev_dicionario = tree.item(tree_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_Dia_em.delete(0, 'end')
        e_estadoconsulta.delete(0,'end')
        e_assunto.delete(0,'end')


        e_nome.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_telefone.insert(0, tree_lista[3])
        e_Dia_em.insert(0, tree_lista[4])
        e_estadoconsulta.insert(0,tree_lista[5])
        e_assunto.insert(0,tree_lista[6])

        def update():
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_telefone.get()
            Dia_em = e_Dia_em.get()
            estado = e_estadoconsulta.get()
            assunto = e_assunto.get()



            lista = [nome, email, telefone, Dia_em, estado, assunto, valor_id]

            if nome == '':
                messagebox.showerror('Erro', 'Preencher o nome')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'dados Atualizados com sucesso')

                e_nome.delete(0, 'end')
                e_email.delete(0, 'end')
                e_telefone.delete(0, 'end')
                e_Dia_em.delete(0, 'end')
                e_assunto.delete(0, 'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()


        b_confirmar = Button(frame_debaixo, text='OK', command=update, font=('arial 10 bold'), anchor=NW, foreground=cor0, bg=cor8,
                         fg=cor1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=132, y=380)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')






#funcao deletar
def deletar():
    try:
        tree_dados = tree.focus()
        treev_dicionario = tree.item(tree_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('info','Dados apagados com sucesso')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()


    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')








lista_entrada_paciente = ['Normal', 'Urgência', 'Emergência']

#Nome
l_nome = Label(frame_debaixo, text='Nome', font=('arial 12 bold'), anchor=NW, foreground=cor0, bg=cor10, relief='flat')
l_nome.place(x=10, y=20)
e_nome = Entry(frame_debaixo, width=50, justify='left', relief='solid')
e_nome.place(x=10, y=45)

#Email
l_email = Label(frame_debaixo, text='E-mail', font=('arial 12 bold'), anchor=NW, foreground=cor0, bg=cor10, relief='flat')
l_email.place(x=10, y=75)
e_email = Entry(frame_debaixo, width=50, justify='left', relief='solid')
e_email.place(x=10, y=100)

#telefone
l_telefone = Label(frame_debaixo, text='Telefone', font=('arial 12 bold'), anchor=NW, foreground=cor0, bg=cor10, relief='flat')
l_telefone.place(x=10, y=130)
e_telefone = Entry(frame_debaixo, width=50, justify='left', relief='solid')
e_telefone.place(x=10, y=155)

#data da consulta
l_dataconsulta = Label(frame_debaixo, text='Data da consulta', font=('arial 11 bold'), anchor=NW, foreground=cor0, bg=cor10, relief='flat')
l_dataconsulta.place(x=10, y=200)
e_Dia_em = DateEntry(frame_debaixo, width=22, justify='left', relief='solid', locale='pt_br')
e_Dia_em.place(x=10, y=225)


#estado da consulta
l_estadoconsulta = Label(frame_debaixo, text='Estado da consulta', font=('arial 11 bold'), anchor=NW, foreground=cor0, bg=cor10, relief='flat')
l_estadoconsulta.place(x=180, y=200)
#e_estadoconsulta = Entry(frame_debaixo, width=22, justify='left', relief='solid')
e_estadoconsulta=ttk.Combobox(frame_debaixo, values=lista_entrada_paciente)
e_estadoconsulta.place(x=180, y=225)



#Observacao
l_observacao = Label(frame_debaixo, text='Observaçoes', font=('arial 11 bold'), anchor=NW, foreground=cor0, bg=cor10, relief='flat')
l_observacao.place(x=10, y=280)
e_assunto = Entry(frame_debaixo, width=50, justify='left', relief='solid')
e_assunto.place(x=10, y=300)

photo_bt_inserir = PhotoImage(file=r"C:\Users\DIEGO\Downloads\inserir.png")
photo_bt_inserir = photo_bt_inserir.subsample(25, 25)

photo_bt_atualizar = PhotoImage(file=r"C:\Users\DIEGO\Downloads\atualizar.png")
photo_bt_atualizar = photo_bt_atualizar.subsample(25, 25)

photo_bt_deletar = PhotoImage(file=r"C:\Users\DIEGO\Downloads\deletar.png")
photo_bt_deletar = photo_bt_deletar.subsample(25, 25)

photo_bt_pesquisar = PhotoImage(file=r"C:\Users\DIEGO\Downloads\pesquisar.png")
photo_bt_pesquisar = photo_bt_pesquisar.subsample(25, 25)






#botao inserir
b_inserir = Button(frame_debaixo, command=inserir, image=photo_bt_inserir, compound=LEFT, text=' Inserir ', font=('arial 11 bold'), anchor=NW, width=85, foreground=cor0, bg=cor8, fg=cor1, relief='raised', overrelief='ridge')
b_inserir.place(x=10, y=350)

b_atualizar = Button(frame_debaixo, text='Atualizar', command=atualizar, image=photo_bt_atualizar, compound=LEFT, font=('arial 11 bold'), anchor=NW, width=85, foreground=cor0, bg=cor12, fg=cor1, relief='raised', overrelief='ridge')
b_atualizar.place(x=130, y=350)

b_deletar = Button(frame_debaixo, text='Deletar', command=deletar, image=photo_bt_deletar, compound=LEFT, font=('arial 11 bold'), anchor=NW, width=85, foreground=cor0, bg=cor7, fg=cor1, relief='raised', overrelief='ridge')
b_deletar.place(x=250, y=350)





#funcao pesquisar
def pesquisar_data():
    nome = e_nome.get()
    Dia_em = e_Dia_em.get()
    print(Dia_em)
    print(nome)
    with con:
        cur = con.cursor()
        query = f"""SELECT * FROM formulario2 
        WHERE nome LIKE ('{nome}%')
        AND Dia_em = ('{Dia_em}')"""

        cur.execute(query)
        informacao = cur.fetchall()

        lista = [nome, Dia_em]

        for i in informacao:
            lista.append(i)

        print(informacao)

        #pesquisar_info(lista)
        messagebox.showinfo('Sucesso', 'dados pesquisados com sucesso')

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_Dia_em.delete(0, 'end')
        e_estadoconsulta.delete(0, 'end')
        e_assunto.delete(0, 'end')

        tree.delete(*tree.get_children())

        for record in informacao:
            tree.insert(parent='', index='end', text='',
                            values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]))
            print(record)

mostrar()



def pesquisar_nome():
    nome = e_nome.get()
    print(nome)
    with con:
        cur = con.cursor()
        query = f"""SELECT * FROM formulario2 
        WHERE nome LIKE ('{nome}%')"""

        cur.execute(query)
        informacao2 = cur.fetchall()

        lista = [nome]

        for i in informacao2:
            lista.append(i)

        print(informacao2)

        #pesquisar_info(lista)
        messagebox.showinfo('Sucesso', 'dados pesquisados com sucesso')

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_Dia_em.delete(0, 'end')
        e_estadoconsulta.delete(0, 'end')
        e_assunto.delete(0, 'end')

        tree.delete(*tree.get_children())

        for record in informacao2:
            tree.insert(parent='', index='end', text='',
                            values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]))
            print(record)

mostrar()






b_pesquisar = Button(frame_debaixo, text='Pesquisar Data', command=pesquisar_data, image=photo_bt_pesquisar, compound=LEFT, font=('arial 11 bold'), anchor=NW, width=150, foreground=cor2, bg=cor8, fg=cor1, relief='raised', overrelief='ridge')
b_pesquisar.place(x=10, y=420)


b_pesquisar = Button(frame_debaixo, text='Pesquisar nome', command=pesquisar_nome, image=photo_bt_pesquisar, compound=LEFT, font=('arial 11 bold'), anchor=NW, width=150, foreground=cor2, bg=cor8, fg=cor1, relief='raised', overrelief='ridge')
b_pesquisar.place(x=185, y=420)





janela.mainloop()
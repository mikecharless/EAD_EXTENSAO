from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class main():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.componentes_frame1()
        self.componentes_frame2()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de alunos ACADEMIA THOR")
        self.root.geometry("700x500")
        self.root.config(background='#243634')
        self.root.minsize(500,400)
        self.root.resizable(True, True)
    def frames(self):
        self.frame1 = Frame(self.root, bg='#CBF2E8')
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bg='#CBF2E8')
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def componentes_frame1(self):
        #ADICIONANDO OS BOTÕES
        self.bt_adicionar = Button(self.frame1, text='ADICIONAR')
        self.bt_adicionar.place(relx=0.2, rely=0.1, relwidth=0.12, relheight=0.1)
        self.bt_limpar = Button(self.frame1, text='LIMPAR')
        self.bt_limpar.place(relx=0.33, rely=0.1, relwidth=0.12, relheight=0.1)
        self.bt_procurar = Button(self.frame1, text='PROCURAR')
        self.bt_procurar.place(relx=0.61, rely=0.1, relwidth=0.12, relheight=0.1)
        self.bt_atualizar = Button(self.frame1, text='ATUALIZAR')
        self.bt_atualizar.place(relx=0.74, rely=0.1, relwidth=0.12, relheight=0.1)
        self.bt_excluir = Button(self.frame1, text='EXCLUIR')
        self.bt_excluir.place(relx=0.87, rely=0.1, relwidth=0.12, relheight=0.1)
        #ADICIONANDO LABELS E ENTRY
        self.lb_matricula = Label(self.frame1, text='Matrícula', bg='#CBF2E8')
        self.lb_matricula.place(relx=0.02, rely=0.02)
        self.matricula_entry = Entry(self.frame1)
        self.matricula_entry.place(relx=0.02, rely=0.1, relwidth=0.15, relheight=0.1)

        self.lb_nome = Label(self.frame1, text='Nome', bg='#CBF2E8')
        self.lb_nome.place(relx=0.02, rely=0.3)
        self.nome_entry =  Entry(self.frame1)
        self.nome_entry.place(relx=0.02, rely=0.4, relwidth=0.8, relheight=0.1)

        self.lb_celular = Label(self.frame1, text='Celular', bg='#CBF2E8')
        self.lb_celular.place(relx=0.02, rely=0.7)
        self.celular_entry = Entry(self.frame1)
        self.celular_entry.place(relx=0.02, rely=0.8, relwidth=0.25, relheight=0.1)

        self.lb_data_pg = Label(self.frame1, text='Dia de pagamento', bg='#CBF2E8')
        self.lb_data_pg.place(relx=0.61, rely=0.7)
        self.data_pg_entry = Entry(self.frame1)
        self.data_pg_entry.place(relx=0.61, rely=0.8, relwidth=0.1, relheight=0.1)
    def componentes_frame2(self):
        self.lista_alunos = ttk.Treeview(self.frame2, height=3, columns=("col1", "col2", "col3", "col4"))
        self.lista_alunos.heading("#0", text="")
        self.lista_alunos.heading("#1", text="Matrícula")
        self.lista_alunos.heading("#2", text="Nome")
        self.lista_alunos.heading("#3", text="Telefone")
        self.lista_alunos.heading("#4", text="Dia de pagamento")

        self.lista_alunos.column("#0", width=1)
        self.lista_alunos.column("#1", width=50)
        self.lista_alunos.column("#2", width=235)
        self.lista_alunos.column("#3", width=130)
        self.lista_alunos.column("#4", width=85)

        self.lista_alunos.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.barra_rolagem = Scrollbar(self.frame2, orient='vertical')
        self.lista_alunos.configure(yscroll=self.barra_rolagem.set)
        self.barra_rolagem.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

if __name__ == "__main__":
    main()




from tkinter import *
from tkinter import ttk
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

root = Tk()

class relatorios():
    def print_aluno(self):
        webbrowser.open('aluno.pdf')
    def gerar_relatorio(self):
        self.pdf = canvas.Canvas('aluno.pdf')

        self.matricula_pdf = self.matricula_entry.get()
        self.nome_pdf = self.nome_entry.get()
        self.celular_pdf = self.celular_entry.get()
        self.data_pg_pdf = self.data_pg_entry.get()

        self.pdf.setFont("Helvetica-Bold", 24)
        self.pdf.drawString(200, 790, 'Ficha do aluno')

        self.pdf.setFont("Helvetica-Bold", 18)
        self.pdf.drawString(50, 700, 'Matrícula: ')
        self.pdf.drawString(50, 670, 'Nome: ')
        self.pdf.drawString(50, 640, 'Celular: ')
        self.pdf.drawString(50, 610, 'Dia de pagamento: ')

        self.pdf.setFont("Helvetica", 18)
        self.pdf.drawString(150, 700, self.matricula_pdf)
        self.pdf.drawString(150, 670, self.nome_pdf)
        self.pdf.drawString(150, 640, self.celular_pdf)
        self.pdf.drawString(150, 610, self.data_pg_pdf)

        self.pdf.setFont("Helvetica-Bold", 24)
        self.pdf.drawString(250, 550, 'Treino')
        self.pdf.setFont("Helvetica", 18)
        self.pdf.drawString(50, 510, 'Treino A:')
        self.pdf.drawString(50, 480, 'Treino B: ')
        self.pdf.drawString(50, 450, 'Treino C:')
        self.pdf.drawString(50, 420, 'Treino D:')
        self.pdf.drawString(50, 390, 'Treino E:')

        self.pdf.rect(20, 350, 550, 230, fill=False, stroke=True)

        self.pdf.showPage()
        self.pdf.save()
        self.print_aluno()

class funcs():
    def variaveis(self):
        self.matricula = self.matricula_entry.get()
        self.nome = self.nome_entry.get()
        self.celular = self.celular_entry.get()
        self.data_pg = self.data_pg_entry.get()
    def limpar_dados(self):
        self.matricula_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.celular_entry.delete(0, END)
        self.data_pg_entry.delete(0, END)
    def conecta_banco(self):
        try:
            self.conexao = sqlite3.connect("alunos.db")
            self.cursor = self.conexao.cursor()
            print("Banco de dados conectado")
        except sqlite3.Error as erro:
            print(f"Erro ao conectar o banco: {erro}")
    def desconecta_banco(self):
        self.cursor.close()
        self.conexao.close()
    def create_table(self):
        self.conecta_banco()
        comando = """CREATE TABLE IF NOT EXISTS Alunos(
                     matricula INTEGER,
                     nome TEXT NOT NULL,
                     celular INTEGER(11),
                     dia_pg INTEGER(2) NOT NULL,
                     PRIMARY KEY (matricula)
                    );"""
        self.cursor.execute(comando)
        self.desconecta_banco()
    def adiconar_aluno(self):
        self.variaveis()
        self.conecta_banco()
        comando = """INSERT INTO Alunos (nome, celular, dia_pg) VALUES (?, ? ,?); """
        self.cursor.execute(comando, (self.nome, self.celular, self.data_pg))
        self.conexao.commit()
        self.desconecta_banco()
        self.select_alunos()
        self.limpar_dados()
    def select_alunos(self):
        self.lista_alunos.delete(*self.lista_alunos.get_children())
        self.conecta_banco()
        registros = self.cursor.execute("""SELECT * FROM Alunos ORDER BY dia_pg ASC;""")
        for registro in registros:
            self.lista_alunos.insert("", END, values=registro)
        self.desconecta_banco()
    def duplo_click(self, event):
        self.limpar_dados()
        self.lista_alunos.selection()
        for i in self.lista_alunos.selection():
            col1, col2, col3, col4 = self.lista_alunos.item(i, 'values')
            self.matricula_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.celular_entry.insert(END, col3)
            self.data_pg_entry.insert(END, col4)
    def excluir_aluno(self):
        self.variaveis()
        self.conecta_banco()
        comando = """DELETE FROM Alunos WHERE matricula = ?;"""
        self.cursor.execute(comando, self.matricula)
        self.conexao.commit()
        self.desconecta_banco()
        self.limpar_dados()
        self.select_alunos()
    def atualizar_aluno(self):
        self.variaveis()
        self.conecta_banco()
        comando = """UPDATE Alunos SET nome = ?, celular = ?, dia_pg = ? WHERE
         matricula = ?;"""
        self.cursor.execute(comando, (self.nome, self.celular, self.data_pg, self.matricula))
        self.conexao.commit()
        self.desconecta_banco()
        self.limpar_dados()
        self.select_alunos()

class main(funcs, relatorios):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.componentes_frame1()
        self.componentes_frame2()
        self.select_alunos()
        self.menu()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de alunos ACADEMIA THOR")
        self.root.geometry("700x500")
        self.root.config(background='#243634')
        self.root.minsize(500, 400)
        self.root.resizable(True, True)
    def frames(self):
        self.frame1 = Frame(self.root, bg='#CBF2E8')
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bg='#CBF2E8')
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def componentes_frame1(self):
        # ADICIONANDO OS BOTÕES
        self.bt_adicionar = Button(self.frame1, text='ADICIONAR', command=self.adiconar_aluno)
        self.bt_adicionar.place(relx=0.2, rely=0.1, relwidth=0.12, relheight=0.1)
        self.bt_limpar = Button(self.frame1, text='LIMPAR', command=self.limpar_dados)
        self.bt_limpar.place(relx=0.33, rely=0.1, relwidth=0.12, relheight=0.1)
        self.bt_procurar = Button(self.frame1, text='PROCURAR')
        self.bt_procurar.place(relx=0.61, rely=0.1, relwidth=0.12, relheight=0.1)
        self.bt_atualizar = Button(self.frame1, text='ATUALIZAR')
        self.bt_atualizar.place(relx=0.74, rely=0.1, relwidth=0.12, relheight=0.1)
        self.bt_excluir = Button(self.frame1, text='EXCLUIR', command=self.excluir_aluno)
        self.bt_excluir.place(relx=0.87, rely=0.1, relwidth=0.12, relheight=0.1)
        # ADICIONANDO LABELS E ENTRY
        self.lb_matricula = Label(self.frame1, text='Matrícula', bg='#CBF2E8')
        self.lb_matricula.place(relx=0.02, rely=0.02)
        self.matricula_entry = Entry(self.frame1)
        self.matricula_entry.place(relx=0.02, rely=0.1, relwidth=0.15, relheight=0.1)

        self.lb_nome = Label(self.frame1, text='Nome', bg='#CBF2E8')
        self.lb_nome.place(relx=0.02, rely=0.3)
        self.nome_entry = Entry(self.frame1)
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

        self.lista_alunos.bind("<Double-1>", self.duplo_click)
    def menu(self):
        menu_app = Menu(self.root)
        self.root.config(menu=menu_app)
        menu_1 = Menu(menu_app)
        menu_2 = Menu(menu_app)
        def sair(): self.root.destroy()
        menu_app.add_cascade(label='Opções', menu=menu_1)
        menu_app.add_cascade(label='Relatórios', menu=menu_2)
        menu_1.add_command(label='Sair', command=sair)
        menu_2.add_command(label='Ficha do aluno', command=self.gerar_relatorio)

if __name__ == "__main__":
    main()
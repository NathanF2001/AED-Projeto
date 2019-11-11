from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from passwords.Passwords_data import *
from Main_GUI import *
from Banco_de_dados.Dados import *

class Interface(object):

    def __init__(self,root):
        'Método Construtor que cria a tela de login inicial'


        self.root = root
        self.Frame1 = Frame(self.root,bg = '#FFF8F0')
        self.Frame1.grid(row = 0,column = 0, columnspan = 12)

        style = ttk.Style()
        style.theme_create('style',parent='alt',
                        settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'black',
                                       'fieldbackground': '#FFF8F0',
                                       'background': '#FFF8F0',
                                       'color' : 'black'
                                       }}}
                         )
        style.theme_use('style')
        
        for a in range(12):
            Labelmain = Label(self.Frame1,width = 5,bg = '#FFF8F0',height = 4)
            Labelmain.grid(row=0,column = a)
        

        Label1 = Label(self.Frame1,fg = 'black', font = ('Times',50),text = 'Apollo',bg = '#FFF8F0')
        Label1.grid(row = 1,column = 2,columnspan = 8,sticky = 'WE')

        self.Frame2 = Frame(self.Frame1,bg = '#191716',bd = 3,relief='ridge')
        self.Frame2.grid(row = 2,column = 1,columnspan = 10,sticky ='NSWE',pady = (80,0),ipady = 10)

        for a in range(12):
            Labelmain = Label(self.Frame2,width = 3,bg ='#191716')
            Labelmain.grid(row=0,column = a)

        login = Label(self.Frame2,text = 'Login',fg = 'white',bg = '#191716',font = ('Times',15,'bold'))
        login.grid(row=1,column = 0,columnspan = 6)

        self.login_entry = Entry(self.Frame2,bg = '#FFF8F0',font = ('Times',12))
        self.login_entry.grid(row = 1,column = 6,columnspan = 6,sticky='WE')

        password = Label(self.Frame2,text = 'Senha',fg = 'white',bg = '#191716',font = ('Times',15,'bold'))
        password.grid(row=2,column = 0,columnspan =6)

        self.password_entry = Entry(self.Frame2,bg = '#FFF8F0',font = ('Times',12),show = '*')
        self.password_entry.grid(row = 2,column = 6,columnspan = 6,sticky = 'WE')

        Entrar = Button(self.Frame2, text = 'Entrar',bg = '#191716',font= ('Times',12,'bold'),
        relief = 'ridge',fg ='white',activebackground= 'white',activeforeground= 'black',command = self.Entrar_system)
        Entrar.grid(row = 3, column = 6,columnspan = 3,sticky = 'WE',pady = (25,0))

        self.Cadastrar = Button(self.Frame1, text = 'Cadastrar',bg = '#191716',font = ('Times',12,'bold'),
        relief = 'ridge',fg ='white',activebackground= 'white',activeforeground= 'black',command = self.button_cadastrar)
        self.Cadastrar.grid(row = 3,column = 5,columnspan = 2,pady = (50,0),sticky ='WE')

    def Entrar_system(self):
        'Método para entrar no sistema'

        login = self.login_entry.get()
        senha = self.password_entry.get()

        Tree = pickle.load(open('passwords/Users.txt','rb'))

        Existe = Tree.tree_search(login)
        if Existe:
            if senha == Existe.password:
                self.Frame1.destroy()
                x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 5
                y = (root.winfo_screenheight() - root.winfo_reqheight()) / 10
                self.root.geometry('1020x610+%d+%d'%(x,y))
                root['bg'] = '#FFF8F0'
                root['relief'] = 'ridge'
                root['highlightbackground'] = '#191716'
                root['highlightcolor'] = '#191716'
                root['bd'] = 3
                root['highlightthickness'] = 5
                Main_Window(self.root,Existe,Tree)
                

    def apagar_frame(self):
        self.Frame1.destroy()

    def button_cadastrar(self):
        'Método para pedi os dados dos usuario'


        self.Frame2.grid_forget()
        self.Cadastrar.grid_forget()
        
        self.Frame_cadastrar = Frame(self.Frame1,bg = '#191716',bd = 3,relief='ridge',height = 320)
        self.Frame_cadastrar.grid(row = 2,column = 1,columnspan = 10,sticky ='NSWE',pady = (30,0))

        for a in range(12):
            Labelmain = Label(self.Frame_cadastrar,width = 3,bg ='#191716')
            Labelmain.grid(row=0,column = a)


        Msg = Label(self.Frame_cadastrar,text = 'Insira seus dados',fg = 'white',bg = '#191716',font = ('Times',15,'bold'))
        Msg.grid(row=0,column = 0,columnspan = 12,padx=(0,10))

        self.Nome_entry = self.create_question(self.Frame_cadastrar,1,'Nome')

        anos = [1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
        dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        meses = ['01','02','03','04','05','06','07','08','09','10','11','12']

        Nascimento = Label(self.Frame_cadastrar,text = 'Dt. Nascimento',fg = 'white',bg = '#191716',font = ('Times',15,'bold'))
        Nascimento.grid(row=2,column = 0,columnspan = 3,pady = (10,0))

        self.dia = ttk.Combobox(self.Frame_cadastrar,value = dias,width = 5,state ='readonly')
        self.mes= ttk.Combobox(self.Frame_cadastrar,value = meses,width = 5,state ='readonly')
        self.ano = ttk.Combobox(self.Frame_cadastrar,value = anos,width = 5,state ='readonly')
        
        self.dia.grid(row = 2,column= 3,columnspan = 2,pady = (10,0))
        self.mes.grid(row = 2,column = 5,columnspan = 2,pady = (10,0))
        self.ano.grid(row = 2,column = 7,columnspan = 2,pady = (10,0))

        self.Email_entry  = self.create_question(self.Frame_cadastrar,3,'Email')
       
        self.Estado_entry = self.create_question(self.Frame_cadastrar,4,'Estado')
        
        self.Cidade_entry = self.create_question(self.Frame_cadastrar,5,'Cidade')
        
        self.Bairro_entry = self.create_question(self.Frame_cadastrar,6,'Bairro')


        Voltar  =Button(self.Frame_cadastrar, text = 'Voltar',bg = '#191716',font = ('Times',12,'bold'),
        relief = 'ridge',fg ='white',activebackground= 'white',activeforeground= 'black',command = self.Voltar_menu)
        Voltar.grid(row = 7,column = 1, columnspan = 3,sticky = 'W',pady = (20,10))

        Continuar = Button(self.Frame_cadastrar, text = 'Continuar >>',bg = '#191716',font = ('Times',12,'bold'),
        relief = 'ridge',fg ='white',activebackground= 'white',activeforeground= 'black',command = self.create_account)
        Continuar.grid(row = 7,column = 4,columnspan = 7,sticky = 'E',pady = (20,10))


    def Voltar_menu(self):
        self.Frame_cadastrar.destroy()
        self.Frame2.grid(row = 2,column = 1,columnspan = 10,sticky ='NSWE',pady = (80,0),ipady = 10)
        self.Cadastrar.grid(row = 3,column = 5,columnspan = 2,pady = (50,0),sticky ='WE')


    def create_question(self,frame,r,string):
        Label_entry = Label(frame,text = string,fg = 'white',bg = '#191716',font = ('Times',15,'bold'))
        Label_entry.grid(row= r,column = 0,columnspan = 3,sticky ='W',pady = (10,0))

        Entry_question = Entry(frame,bg = '#FFF8F0',font = ('Times',12))
        Entry_question.grid(row = r,column = 3,columnspan = 8,sticky='WE',pady = (10,0))

        return Entry_question
    
    
    def create_account(self):
        'Método que pergunta os novos dados'


        self.Frame_cadastrar.grid_forget()

        self.Frame_login = Frame(self.Frame1,bg = '#191716',bd = 3,relief='ridge',height = 320)
        self.Frame_login.grid(row = 2,column = 1,columnspan = 10,sticky ='NSWE',pady = (30,0)) 

        for a in range(12):
            Labelmain = Label(self.Frame_login,width = 3,bg ='#191716')
            Labelmain.grid(row=0,column = a)

        self.new_login_entry = self.create_question(self.Frame_login,1,'Login')

        self.new_senha_entry = self.create_question(self.Frame_login,2,'Senha')

        self.confirm_senha_entry = self.create_question(self.Frame_login,3,'Confirmar')

        self.new_senha_entry['show'] = self.confirm_senha_entry['show'] = '*'
        
        Voltar  =Button(self.Frame_login, text = 'Voltar',bg = '#191716',font = ('Times',12,'bold'),
        relief = 'ridge',fg ='white',activebackground= 'white',activeforeground= 'black',command = self.voltar_cadastro)
        Voltar.grid(row = 7,column = 1, columnspan = 3,sticky = 'W',pady = (20,10))

        Continuar = Button(self.Frame_login, text = 'Prosseguir',bg = '#191716',font = ('Times',12,'bold'),
        relief = 'ridge',fg ='white',activebackground= 'white',activeforeground= 'black',command = self.adicionar_banco)
        Continuar.grid(row = 7,column = 4,columnspan = 8,sticky = 'E',pady = (20,10))

    def voltar_cadastro(self):
        self.Frame_login.destroy()
        self.Frame_cadastrar.grid(row = 2,column = 1,columnspan = 10,sticky ='NSWE',pady = (30,0))

    def adicionar_banco(self):
        'Adicionar os dados a árvore vermelho e preto'


        login = str(self.new_login_entry.get())
        senha = str(self.new_senha_entry.get())
        nome = str(self.Nome_entry.get())
        idade = (str(self.dia.get()),str(self.mes.get()),str(self.ano.get()))
        email = str(self.Email_entry.get())
        localidade = (str(self.Estado_entry.get()),str(self.Cidade_entry.get()),str(self.Bairro_entry.get()))

        Users = pickle.load(open('passwords/Users.txt','rb'))
        bol = Users.tree_search(login)
        if not bol:
            Users.RB_insert(login,senha,nome,idade,email,localidade)
            pickle.dump(Users,open('passwords/Users.txt','wb'))
        self.voltar_cadastro()
        self.Voltar_menu()

root = Tk()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 10
root.geometry('510x600+%d+%d'%(x,y))
root.title('APOLLO')
root['bg'] = '#FFF8F0'
root['relief'] = 'ridge'
root['highlightbackground'] = '#191716'
root['highlightcolor'] = '#191716'
root['bd'] = 3
root['highlightthickness'] = 5
Interface(root)
root.mainloop()

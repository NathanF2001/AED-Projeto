from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from random import choice
import pickle


class Main_Window(object):

    def __init__(self,root,User,Tree):
        'Método construtor menu do programa'
        self.User = User    #Nodulo do usuário logado   
        self.Tree = Tree    #árvore vermelho e preto

        self.root = root   #Raiz do tkinter 

        'variaveis quando uma função é chamada'
        self.call_Tabela = False    
        self.call_Gasto = False
        self.call_subgasto = False
        self.call_administrador = False

        'variaveis quando a funçãp é chamada uma vez'
        self.sidebar = True
        self.Gasto = True
        self.Tabela_ = True
        self.adm = True

        #Media de todos os usuarios
        self.all_users = pickle.load(open('Banco_de_dados/DAU.txt','rb'))
        

        self.main_frame = self.Create_Frame(r = 0,c = 0,frame = self.root,color = '#FFF8F0')

        self.atributes = User.labels


        self.widgets = []
        if self.atributes != {}:
            for a in self.atributes:
                self.widgets.append(a)

        self.image = PhotoImage(file = 'model.png')

        
        for a in range(12):
            Labelmain = Label(self.main_frame,image = self.image,bg = '#FFF8F0')
            Labelmain.grid(row=0,column = a)
        
        Label1 = Label(self.main_frame,fg = 'black', font = ('Times',50),text = 'Apollo',bg = '#FFF8F0')
        Label1.grid(row = 1,column = 0,rowspan = 3,columnspan = 8,sticky = 'W')

        name = Label(self.main_frame, text ='Nome: %s'%self.User.atributes['nome'],font = ('Times',12,'bold'),fg = 'black',bg = '#FFF8F0')
        idade = Label(self.main_frame, text ='Idade: '+ str(self.User.atributes['idade']),font = ('Times',12,'bold'),fg = 'black',bg = '#FFF8F0')
        email = Label(self.main_frame, text ='Email: %s'%self.User.atributes['email'],font = ('Times',12,'bold'),fg = 'black',bg = '#FFF8F0')
        estado = Label(self.main_frame, text ='Estado: %s'%self.User.atributes['localidade'][0],font = ('Times',12,'bold'),fg = 'black',bg = '#FFF8F0')
        cidade = Label(self.main_frame, text ='Cidade: %s'%self.User.atributes['localidade'][1],font = ('Times',12,'bold'),fg = 'black',bg = '#FFF8F0')
        bairro = Label(self.main_frame, text ='Bairro: %s'%self.User.atributes['localidade'][2],font = ('Times',12,'bold'),fg = 'black',bg = '#FFF8F0')

        name.grid(row = 2,column = 3,columnspan = 2,sticky = 'W')
        idade.grid(row = 2,column = 5,columnspan = 2,sticky = 'W')
        email.grid(row = 2,column = 7,columnspan = 2,sticky = 'W')
        estado.grid(row = 1,column = 9,columnspan = 2,sticky = 'W')
        cidade.grid(row = 2,column = 9,columnspan = 2,sticky = 'W')
        bairro.grid(row = 3,column = 9,columnspan = 2,sticky = 'W')

        Label1 = Label(self.main_frame,fg = 'black',font = ('Times',1),bg = '#191716')
        Label1.grid(row = 4,column = 0,columnspan = 12,sticky = 'WE')

        self.first_frame = self.Create_Frame(r = 5,c = 0,frame = self.main_frame,color = '#615b55')
        

        for a in range(12):
            Labelmain = Label(self.first_frame,image = self.image,bg = '#615b55')
            Labelmain.grid(row=0,column = a)

        self.create_button(l = 1,r = 0,text = 'Gastos',function = self.Gastos,frame = self.first_frame,pad = 1)
        
        self.create_button(l = 1,r = 2,text = 'Tabelas',function = self.Tabela,frame = self.first_frame, pad = 1)
        
        self.create_button(l = 1,r = 4,text ='Gerenciar Custos',function = None,frame = self.first_frame,pad = 1)

        self.create_button(l= 1,r =6,text = 'Salvar processos',function = self.salvar,frame =self.first_frame,pad = 1)

        if self.User.administrator:

            self.create_button(l=1,r=8,text = 'Delete(Administrator)',function = self.adminstrator_screen,frame = self.first_frame,pad = 1)
    

    

    def create_button(self,**kwargs):
        frame = kwargs.get('frame')
        string = kwargs.get('text')
        function = kwargs.get('function')
        l = kwargs.get('l')
        r = kwargs.get('r')
        pad = kwargs.get('pad')

        Button1 = Button(frame,text = string,font = ('Times',12,'bold'),bg = '#191716',fg ='#FFF8F0',
        relief = 'ridge',command = function )
        Button1.grid(row= l,column = r,columnspan = 2,sticky = 'WE',pady = pad)

        return Button1

    def Gastos(self):
        'A opção Gastos do programa 1º botão'
        self.call_Gasto = True
        if self.call_Tabela:
            self.call_Tabela = False
            self.Frame_Canvas.grid_forget()
        if self.call_administrador:
            self.call_administrador =FALSE
            self.administrator_frame.grid_forget()

        if self.Gasto:

            self.second_frame = self.Create_Frame(r = 6,c = 0,frame = self.first_frame,color = 'white')
            

            for a in range(12):
                Labelmain = Label(self.second_frame,image = self.image,bg = 'white')
                Labelmain.grid(row=0,column = a)

            navbar = self.Create_Frame(r = 0,c = 0,frame = self.second_frame,color = '#FFF8F0')
            
            Plus = Button(navbar, text = '+',font = ('Times',15,'bold'),bg = '#191716',fg ='#FFF8F0',command = self.add_atribute)
            Plus.grid(row =0,column = 0,sticky = 'WE')

            gastos = ['agua','alimentação','cartão','cursos','educação','iptu','ipva','lazer','luz','moradia','saude','serviços online','transporte','tv e internet e telefone','viagem','outros']
            self.Entry_plus = ttk.Combobox(navbar,value = gastos,state ='readonly',font = ('Times',20,'bold'))
            self.Entry_plus.grid(row = 0,column = 1,columnspan = 3,padx = (20,0),sticky = 'WE')

            Remove = Button(navbar, text = 'Remove',font = ('Times',15,'bold'),bg = '#191716',fg ='#FFF8F0',command = self.remove_atribute)
            Remove.grid(row=0,column = 4,padx = (20,0))


            self.listbox = Listbox(self.second_frame,bg ='#615b55',font = ('Times',15,'bold'),fg = 'white',height =17)
            self.listbox.grid(row = 1,column = 0,columnspan = 12,sticky = 'WE')
            for a in self.widgets:
                self.listbox.insert(END,a)

            self.Button_acces = self.create_button(l=0,r= 10,text = 'Acess',function = self.create_gasto,frame = self.second_frame,pad = 1)
            
            self.Gasto = False
        else:
            if self.call_subgasto:
                self.listbox_sector.delete(0,END)
                self.third_frame.grid_forget()
                self.Button_acces['command'] = lambda: self.create_gasto(False)
                self.call_subgasto = False
            self.second_frame.grid(row = 6,column = 0,columnspan = 12,sticky = 'WE')

    def add_atribute(self):
        'Adicionar um tipo de despesa'
        atribute = str(self.Entry_plus.get())
        if atribute not in self.atributes and atribute != '':
            self.atributes[atribute] = {}
            for a in range(2010,2020):
                self.atributes[atribute][str(a)] = [0 for a in range(12)]
            self.widgets.append(atribute.upper())
            self.listbox.insert(END,atribute.upper())

    def remove_atribute(self):
        'Remover um tipo de despesa'
        atribute = self.listbox.curselection()[0]
  
        del self.atributes[self.widgets[atribute].lower()]
        self.widgets.pop(atribute)
        self.listbox.delete(0,END)
        for a in self.widgets:
            self.listbox.insert(END,a)

    
    def create_gasto(self, bol = True):
        'Método que entrar nas opções da despesa entrada: (aqui mostra os anos e meses)'
        self.call_subgasto = True
        self.tipo = self.widgets[self.listbox.curselection()[0]].lower()
        self.anos = [str(a) for a in range(2010,2020)]
        self.meses = {}
        

        if self.listbox.curselection() != () and bol:
        
            self.second_frame.grid_forget()

            self.third_frame = self.Create_Frame(r = 6,c = 0,frame = self.first_frame,color = '#FFF8F0')

            for a in range(12):
                Labelmain = Label(self.third_frame,image = self.image,bg = 'white')
                Labelmain.grid(row=0,column = a)

            Label_Adicionar = Label(self.third_frame,bg = '#FFF8F0',text ='Adicionar Mês',font = ('Times',25,'bold'))
            Label_Adicionar.grid(row = 1,column = 0 ,columnspan = 6,ipady = 5,sticky = 'NSWE')

            self.mes,self.ano = self.Combobox_Gasto()

            Label_entry = Label(self.third_frame,text = 'Valor',fg = 'black',bg = '#FFF8F0',font = ('Times',15,'bold'))
            Label_entry.grid(row= 3,column = 0,columnspan = 2,sticky ='WE',pady = (50,0))

            self.valor = Entry(self.third_frame,bg = '#FFF8F0',font = ('Times',12))
            self.valor.grid(row = 3,column = 2,columnspan = 3,sticky='WE',pady = (50,0))

            self.Button = self.create_button(l = 4,r = 2,text = 'Adicionar',function = self.add_subatribute,frame = self.third_frame,pad = (60,0))

            self.label_box = Label(self.third_frame,text = 'Ano',fg = 'black',bg = '#FFF8F0',font = ('Times',15,'bold'))
            self.label_box.grid(row = 1,column = 6,columnspan = 6)

            self.listbox_sector = Listbox(self.third_frame,bg ='#615b55',font = ('Times',15,'bold'),fg = 'white',height =15,relief = 'ridge',highlightbackground = '#191716',highlightcolor = '#191716')
            self.listbox_sector.grid(row = 2,column = 6,rowspan = 4,columnspan = 6,sticky = 'WE')
            
            self.nextbutton = self.create_button(l=6,r=10,text = 'Next',function = lambda: self.proximo_list(True),frame = self.third_frame,pad = 1)


            self.backbutton =  Button(self.third_frame,text = 'Back',font = ('Times',12,'bold'),bg = '#191716',fg ='#FFF8F0',
            relief = 'ridge', command = lambda: self.back_list(False) )
        else:
            self.second_frame.grid_forget()
            self.third_frame.grid(row = 6,column = 0,columnspan = 12,sticky = 'WE')
            self.sidebar = True
            self.nextbutton.grid(row=6,column = 10,columnspan = 2,sticky = 'WE')
            self.backbutton.grid_forget()
        self.show_()
        

    def Combobox_Gasto(self):
        anos = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
        meses = ['01','02','03','04','05','06','07','08','09','10','11','12']

        mes= ttk.Combobox(self.third_frame,value = meses,width = 5,state ='readonly',font = ('Times',25,'bold'))
        ano = ttk.Combobox(self.third_frame,value = anos,width = 5,state ='readonly',font = ('Times',25,'bold'))

        mes.grid(row = 2,column = 0,columnspan = 3,pady=(70,0))
        ano.grid(row = 2,column = 3,columnspan = 3,pady =(70,0))

        return mes,ano

    def proximo_list(self,bol):#Mostrar os meses do ano escolhido
          
        if bol:
            self.change_side()

            ano = self.anos[self.listbox_sector.curselection()[0]]

            self.listbox_sector.delete(0,END)

            names =text = '{0:}{1:}{2:}'.format('Mês',' '*20,'Valor')

            self.label_box['text'] = names

            self.label_box.grid(row = 1,column = 6,columnspan = 6,sticky = 'W')

            for p,a in enumerate(self.atributes[self.tipo][ano]):
                text = '{0:0>2}{1:}{2:}'.format(p+1,' '*20,a)
                self.listbox_sector.insert(END,text)

            self.backbutton.grid(row=6,column = 6,columnspan = 2,sticky = 'WE')
            self.nextbutton.grid_forget()
        


    def back_list(self,bol):
        if not bol: #Volta o listbox, equivalente a mostrar todos os anos
            self.change_side()
            self.show_()
            self.nextbutton.grid(row=6,column = 10,columnspan = 2,sticky = 'WE')
            self.backbutton.grid_forget()
            

    def show_(self,month = None):#Mostrar listbox atualizado do Gasto
        
        self.listbox_sector.delete(0,END)   #Apaga listbox

        self.label_box['text'] = '{0:}{1:}{2:}'.format('Ano',' '*21,'Média por mês')  #Nome para aparecer na label

        self.label_box.grid(row = 1,column = 6,columnspan = 6,sticky = 'W') #Coloca a label para aparecer

        for a in self.anos: #coloca na listbox os valores dos anos
            text = '{0:0>2}{1:}{2:.2f}'.format(a,' '*20,self.User.numero_por_ano[int(a)-2010])
            self.listbox_sector.insert(END,text)

    def add_subatribute(self):
        'Método para adicionar valor novo no respectivo ano/mes'
        year = str(self.ano.get())
        month = str(self.mes.get())
        value = str(self.valor.get())

        position = int(month)-1
        second_position = int(year)-2010

        type_data = self.all_users.tree_search(self.tipo.lower())


        'Parte do Usuário'

        Valor_total = self.User.numero_por_ano[second_position] *self.User.quantidade_meses[second_position]
        Quantidade_de_meses = self.User.quantidade_meses[second_position]

        'Parte de todos os Usuário'
        Quantidade_de_dados_no_ano = type_data.Users_year[second_position]
        Valor_total_do_ano = type_data.years[second_position] * Quantidade_de_dados_no_ano

        Quantidade_de_dados_no_mes = type_data.Users_months[second_position][position]
        Valor_total_do_mes = type_data.months[second_position][position] * Quantidade_de_dados_no_mes

        if self.atributes[self.tipo][year][position] != 0:
            Valor_anterior =  int(self.atributes[self.tipo][year][position])
            
            if value != '0':

                self.User.numero_por_ano[second_position] = (Valor_total + int(value)- Valor_anterior) / Quantidade_de_meses

                type_data.years[second_position] = (Valor_total_do_ano + int(value) - Valor_anterior)/ Quantidade_de_dados_no_ano

                type_data.months[second_position][position] = (Valor_total_do_mes + int(value) - Valor_anterior) / Quantidade_de_dados_no_mes

            else:
                if Quantidade_de_meses-1 != 0:
                    self.User.numero_por_ano[second_position] = (Valor_total - Valor_anterior) / (Quantidade_de_meses-1)
                    self.User.quantidade_meses[second_position]-=1

                else:
                    self.User.numero_por_ano[second_position] = 0
                    self.User.quantidade_meses[second_position] = 0
                if Quantidade_de_dados_no_ano-1 != 0:
                    type_data.years[second_position] = (Valor_total_do_ano  - Valor_anterior)/ (Quantidade_de_dados_no_ano-1)
                    type_data.Users_year[second_position]-=1
                else:
                    type_data.years[second_position] = 0
                    type_data.Users_year[second_position] = 0
                if Quantidade_de_dados_no_mes-1 !=0:
                    type_data.months[second_position][position] = (Valor_total_do_mes - Valor_anterior) / (Quantidade_de_dados_no_mes-1)
                    type_data.Users_months[second_position][position]-= 1
                else:
                    type_data.months[second_position][position] = 0
                    type_data.Users_months[second_position][position] = 0
                if self.atributes[self.tipo][year] == []:
                    del self.atributes[self.tipo][year]

        elif value != '0':
            
            self.User.numero_por_ano[second_position] = (Valor_total + int(value))/(Quantidade_de_meses+1)
            self.User.quantidade_meses[second_position] += 1

            Quantidade_de_dados_no_ano += 1
            type_data.years[second_position] = (Valor_total_do_ano + int(value))/ Quantidade_de_dados_no_ano
            type_data.Users_year[second_position] +=1

            Quantidade_de_dados_no_mes += 1
            type_data.months[second_position][position] = (Valor_total_do_mes + int(value)) / Quantidade_de_dados_no_mes
            type_data.Users_months[second_position][position] +=1


        if value != '0':
            self.atributes[self.tipo][year][int(month)-1] = int(value)  #Adiciona o valor do dicionário da árvore.
        else:
            self.atributes[self.tipo][year][int(month)-1] = 0

        if not self.sidebar:    #Se for para mostrar os meses de certo ano
            text = '{0:0>2}{1:}{2:}'.format(int(month),' '*20,self.atributes[self.tipo][year][int(month)-1])
            self.listbox_sector.delete(position)
            self.listbox_sector.insert(position,text)
        else:   #Mostrar todos os anos
            self.show_()

    def voltar_gastos(self):
        self.second_frame.grid_forget()
        self.third_frame.grid(row = 6,column = 0,columnspan = 12,sticky = 'WE')

    def change_side(self):
        self.sidebar = not self.sidebar

    def salvar(self):#Salvar em um txt
        pickle.dump(self.Tree,open('passwords/Users.txt','wb'))
        pickle.dump(self.all_users,open('Banco_de_dados/DAU.txt','wb'))
        
    def Create_Frame(self, **kwargs):
        row = kwargs.get('r')
        column = kwargs.get('c')
        frame = kwargs.get('frame')
        color = kwargs.get('color')

        frame_model = Frame(frame,bg = color)
        frame_model.grid(row = row,column = column,columnspan= 12,sticky = 'WE')

        return frame_model

    def Tabela(self):  
        'Método para botão de gerar tabela'
        self.call_Tabela = True
        if self.call_Gasto:
            self.call_Gasto = False
            self.second_frame.grid_forget()
        if self.call_administrador:
            self.call_administrador = False
            self.administrator_frame.grid_forget()

        if self.Tabela_:
            self.Frame_Canvas = self.Create_Frame(r = 6,c = 0,frame = self.first_frame,color = '#615b55')
            
            self.check = IntVar()
            for a in range(12):
                Labelmain = Label(self.Frame_Canvas,image = self.image,bg = 'white')
                Labelmain.grid(row=0,column = a)
            
            self.Canvas = Canvas(self.Frame_Canvas,width = 1000,height = 410,bg = 'white')
            self.Canvas.grid(row = 2,column =0,columnspan = 12)

            self.Label_tipo = Label(self.Frame_Canvas,text = 'Tipo',bg = 'black',font = ('Times',15,'bold'),fg = 'white')
            self.Label_tipo.grid(row= 3,column = 0,sticky ='WE')

            self.Combo_tipo = ttk.Combobox(self.Frame_Canvas,value = self.widgets,state ='readonly',width = 15,font = ('Times',15,'bold'))
            self.Combo_tipo.grid(row = 3,column = 1,columnspan = 3,sticky = 'W')

            self.Label_ano = Label(self.Frame_Canvas,text = 'Ano',bg = 'black',font = ('Times',15,'bold'),fg = 'white')
            self.Label_ano.grid(row= 3,column = 4,sticky = 'WE')

            anos = [2010+a for a in range(10)] + ['']

            self.Combo_ano = ttk.Combobox(self.Frame_Canvas,value = anos,state ='readonly',width = 15,font = ('Times',15,'bold'))
            self.Combo_ano.grid(row = 3,column = 5,columnspan = 3,sticky = 'W')

            self.check_total = Checkbutton(self.Frame_Canvas,text = 'Mostrar todos',variable = self.check,onvalue = 1, offvalue = 0,font = ('Times',15,'bold'),bg = '#615b55',fg='white',selectcolor ='black')
            self.check_total.grid(row = 3,column = 8,columnspan = 2)

            self.create_button(l=3,r=10,columnspan = 2,text = 'Search',function = self.Search_Graph,frame = self.Frame_Canvas,pad = 1)
            self.Tabela_ = False
        else:
            self.Frame_Canvas.grid(row = 6,column = 0,columnspan= 12,sticky = 'WE')

    def Search_Graph(self, **kwargs):
        'Método para fazer o filtro de qual ano/mes vai gerar grafico'
        tipo = self.Combo_tipo.get().upper()
        ano = self.Combo_ano.get()
        self.Canvas.delete('all')
        if ano != '':
            vetor = self.atributes[tipo.lower()][ano]
            maior = 0
            for a in vetor:
                if a > maior:
                    maior = a
            mes = ['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEC']
            if self.check.get():
                node = self.all_users.tree_search(tipo.lower())
                vetor_todos_usuarios = node.months[int(ano)-2010]   
                for a in vetor_todos_usuarios:
                    if a > maior:
                        maior = a

            for p,a in enumerate(vetor):
                valor = 360*a//maior
                self.Canvas.create_text(100+(75*p),20,fill = 'black',font = ('Times',15,'bold'),text = '%s'%(mes[p]))
                self.Canvas.create_rectangle(75+(75*p),410-valor,100+(75*p),410,fill= 'red')
                self.Canvas.create_text(100+(75*p),390,fill = 'black',font = ('Times',15,'bold'),angle = 90,text = '%d'%int(a),anchor = 's')
                if self.check.get():
                    valor_total = 360*vetor_todos_usuarios[p]//maior
                    self.Canvas.create_rectangle(100+(75*p),410-valor_total,125+(75*p),410,fill= 'green')
                    self.Canvas.create_text(125+(75*p),390,fill = 'black',font = ('Times',15,'bold'),angle = 90,text = '%d'%int(vetor_todos_usuarios[p]),anchor = 's')
        else:
            if tipo != '':
                maior = 0
                for a in self.User.numero_por_ano:
                    if a > maior:
                        maior = a
                if self.check.get():
                    node = self.all_users.tree_search(tipo.lower())
                    vetor_todos_usuarios = node.years
                    for a in vetor_todos_usuarios:
                        if a > maior:
                            maior = a
                for p,a in enumerate(self.User.numero_por_ano):
                    valor = 360*a//maior
                    self.Canvas.create_text(110+(90*p),20,fill = 'black',font = ('Times',15,'bold'),text = '%d'%(2010+p))
                    self.Canvas.create_rectangle(80+(90*p),410-valor,110+(90*p),410,fill= 'red')
                    self.Canvas.create_text(110+(90*p),390,fill = 'black',font = ('Times',15,'bold'),angle = 90,text = '%d'%int(a),anchor = 's')
                    if self.check.get():
                        valor_total = 360*vetor_todos_usuarios[p]//maior
                        self.Canvas.create_rectangle(110+(90*p),410-valor_total,140+(90*p),410,fill= 'green')
                        self.Canvas.create_text(140+(90*p),390,fill = 'black',font = ('Times',15,'bold'),angle = 90,text = '%d'%int(vetor_todos_usuarios[p]),anchor = 's')

    def adminstrator_screen(self):
        'Método do botão de administrador'
        if self.call_Gasto:
            self.call_Gasto = False
            self.second_frame.grid_forget()
        if self.call_Tabela:
            self.call_Tabela = False
            self.Frame_Canvas.grid_forget()
        self.call_administrador = True
        if self.adm:
            self.administrator_frame = self.Create_Frame(r = 6,c = 0,frame = self.first_frame,color = 'white')  

            self.listbox_administrator = Listbox(self.administrator_frame,bg ='#615b55',font = ('Times',15,'bold'),fg = 'white',width=100,height =15,relief = 'ridge',highlightbackground = '#191716',highlightcolor = '#191716')
            self.listbox_administrator.grid(row = 1,column = 0,rowspan = 4,columnspan = 12,sticky = 'WE')

            Label(self.administrator_frame,bg = '#FFF8F0',fg = 'black',font = ('Times',15,'bold'), text = '{0:}{4:}{1:}{4:}{2:}{4:}{3:}'.format('LOGIN','SENHA','EMAIL','NAME','|')).grid(row = 0,column = 0,columnspan = 12,sticky = 'W')
            node = self.Tree.root
            self.insertlistbox(node)
            self.adm = False
        else:
            self.administrator_frame.grid(row = 6,column = 0,columnspan= 12,sticky = 'WE')


        self.create_button(l= 5,r =0,text = 'Deletar usuário',function = self.Toplevel,frame =self.administrator_frame,pad = 1)

    def insertlistbox(self,node):
        if not node.administrator:
            text = '{0:}{4:}{1:}{4:}{2:}{4:}{3:}'.format(node.getinfo(),node.password,node.atributes['email'],node.atributes['nome'],'|')
            self.listbox_administrator.insert(END,text)
        if node.getleft() != self.Tree.vazio:
            self.insertlistbox(node.getleft())
        if node.getright() != self.Tree.vazio:
            self.insertlistbox(node.getright())
        return

    def Toplevel(self):
        level = Toplevel(self.root,bg ='#FFF8F0')
        k = self.listbox_administrator.get(self.listbox_administrator.curselection()[0])
        dados = k.split('|')
        text = Label(level,bg = '#FFF8F0',fg = 'black',text = 'Tem certeza de retirar o usuário:\n%s'%dados[3],font = ('Times',12,'bold'))
        text.grid(row = 0,column = 0,columnspan = 2)
        yes = Button(level,font = ('Times',12,'bold'),bg = '#191716',fg ='#FFF8F0',relief = 'ridge',text = 'Sim',command = lambda: self.delete(level,dados[0]))
        yes.grid(row= 1, column = 0)

        no = Button(level,font = ('Times',12,'bold'),bg = '#191716',fg ='#FFF8F0',relief = 'ridge',text = 'Não',command = lambda: self.quit(level))
        no.grid(row= 1, column = 1)

    def quit(self,level):
        level.destroy()

    def delete(self,level,k):
        'Método para retirar o usuario da arvore vermelho e preto'
        g = self.Tree.tree_search(k)
        self.Tree.RB_delete(g)
        self.salvar()
        self.listbox_administrator.delete(self.listbox_administrator.curselection()[0])
        self.quit(level)




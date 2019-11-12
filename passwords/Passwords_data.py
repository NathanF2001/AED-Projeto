import pickle
class Login:

    def __init__(self,login,password,nome,idade,email,localidade,bol = True,right = None,left = None,daddy = None,color = 'RED',administrator = False):
        if bol:
            self.password = password
            self.atributes = {'nome': nome,'idade': idade,'email': email, 'localidade': localidade}
            self.labels = {}
           
        self.administrator = administrator
        self.quantidade_meses = [0 for a in range(10)]
        self.numero_por_ano = [0 for a in range(10)]
        self.login = login
        self.left = left
        self.right = right
        self.daddy = daddy
        self.color = color


    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getinfo(self):
        return self.login

    def getfather(self):
        return self.daddy

    def getpassword(self):
        return self.password

    def setpassword(self,i):
        self.password = i

    def setleft(self,i):
        self.left = i

    def setright(self,i):
        self.right = i

    def setinfo(self,i):
        self.login = i

    def setfather(self,i):
        self.daddy = i


class Binary_tree_Login:

    def __init__(self):
        self.vazio = Login(None,None,None,None,None,None,False,color = 'BLACK')
        self.vazio.setfather(self.vazio)
        self.vazio.setright(self.vazio)
        self.vazio.setleft(self.vazio)
        self.root = self.vazio

                           
    def RB_insert(self,login,senha,nome,idade,email,localidade):
        'Método de inserir'
        nodulo = Login(login,senha,nome,idade,email,localidade,True,self.vazio,self.vazio,self.vazio)
        x = self.root
        y = self.vazio
        while x != self.vazio:
            y = x
            if login < x.getinfo():
                x = x.getleft()
            else:
                x = x.getright()
        nodulo.setfather(y)
        if y == self.vazio:
            self.root = nodulo
        else:
            if login < y.getinfo():
                y.setleft(nodulo)
            else:
                y.setright(nodulo)
        self.RB_insert_fixup(nodulo)


    def RB_insert_fixup(self,z):
        'Método de fixup de inserir'
        while z.getfather().color == 'RED':
            print(z.getinfo())
            if self.isleft(z.getfather()):
                y = z.getfather().getfather().getright()
                if y.color == 'RED':
                    z.getfather().color = 'BLACK'
                    y.color = 'BLACK'
                    z.getfather().getfather().color = 'RED'
                    z = z.getfather().getfather()
                else:
                    if self.isright(z):
                        z = z.getfather()
                        self.left_rotate(z)
                    z.getfather().color = 'BLACK'
                    z.getfather().getfather().color = 'RED'
                    self.right_rotate(z.getfather().getfather())
            else:
                y = z.getfather().getfather().getleft()
                if y.color == 'RED':
                    z.getfather().color = 'BLACK'
                    y.color = 'BLACK'
                    z.getfather().getfather().color = 'RED'
                    z = z.getfather().getfather()
                else:
                    if self.isleft(z):
                        z = z.getfather()
                        self.right_rotate(z)
                    z.getfather().color = 'BLACK'
                    z.getfather().getfather().color = 'RED'
                    self.left_rotate(z.getfather().getfather())
        self.root.color = 'BLACK'
        
    def RB_delete(self,nodule): 
        'Método de deletar'
        if nodule.getleft() is self.vazio or nodule.getright() is self.vazio:
            y = nodule
        else:
            y = self.tree_successor(nodule)
        if y.getleft() is not self.vazio:
            x = y.getleft()
        else:
            x = y.getright()
        if x is not self.vazio:
            x.setfather(y.getfather())
        if y.getfather() is self.vazio:
            self.root = x
        else:
            if y == y.getfather().getleft():
                y.getfather().setleft(x)
            else:
                y.getfather().setright(x)

        if y != nodule:
            nodule.setinfo(y.getinfo())
        if y.color == 'BLACK':
            self.RB_DELETE_FIXUP(x)
    
        return y

    def RB_DELETE_FIXUP(self,x):
        'Fixup do deletar arvore vermelho e preto'
        while x != self.root and x.color == 'BLACK':
            if self.isleft(x):
                w = x.getfather().getright()
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.getfather().color = 'RED'
                    self.left_rotate(x.getfather())
                    w = x.getfather().getright()
                if w.getleft().color =='BLACK' and w.getright().color == 'BLACK':
                    w.color = 'RED'
                    x = x.getfather()
                else:
                    if w.getright().color == 'BLACK':
                        w.getleft().color = 'BLACK'
                        w.color = 'RED'
                        self.right_rotate(w)
                        w = x.getfather().getright()
                        w.color = x.getfather().color
                        x.getfather().color = 'BLACK'
                        w.getright().color = 'BLACK'
                        self.left_rotate(x.getfather())
                        x = self.root
            else:
                w = x.getfather().getleft()
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.getfather().color = 'RED'
                    self.right_rotate(x.getfather())
                    w = x.getfather().getleft()
                if w.getright().color =='BLACK' and w.getleft().color == 'BLACK':
                    w.color = 'RED'
                    x = x.getfather()
                else:
                    if w.getleft().color == 'BLACK':
                        w.getright().color = 'BLACK'
                        w.color = 'RED'
                        self.left_rotate(w)
                        w = x.getfather().getleft()
                        w.color = x.getfather().color
                        x.getfather().color = 'BLACK'
                        w.getleft().color = 'BLACK'
                        self.right_rotate(x.getfather())
                        x = self.root
        x.color = 'BLACK'

    def isleft(self,nodule):
        q = nodule.getfather()
        if q == self.vazio:
            return False
        if q.getleft() is nodule:
            return True
        return False

    def isright(self,nodule):
        q = nodule.getfather()
        if q == None:
            return False
        if q.getright() is nodule:
            return True
        return False

    def tree_search(self,i):
        nodule = self.root
        while nodule.getinfo() is not None and i != nodule.getinfo(): 
            if i < nodule.getinfo():
                nodule = nodule.getleft()
            else:
                nodule = nodule.getright()
        if nodule is self.vazio:
            return False
        else:
            return nodule
            
    def tree_minimum(self,nodule):
        while nodule.getleft() is not self.vazio:
            nodule = nodule.getleft()
        return nodule

    def tree_maximum(self,nodule):
        while nodule.getright() is not self.vazio:
            nodule = nodule.getright()
        return nodule

    def tree_successor(self,nodule):
        if nodule.getright() is not None:
            return self.tree_minimum(nodule.getright())
        y = nodule.getfather()
        while y != None and nodule == y.getright():
            nodule = y
            y = y.getfather()
        return y

    def tree_predecessor(self,nodule):
        if nodule.getleft() is not None:
            return self.tree_maximum(nodule.getleft())
        y = nodule.getfather()
        while y != None and self == y.getleft():
            x = y
            y = y.getfather()
        return y


    def left_rotate(self,x):
        y = x.getright()
        x.setright(y.left)
        if y.getleft() != self.vazio:
            y.getleft().setfather(x)
        y.setfather(x.getfather())
        if x.getfather() == self.vazio:
            self.root = y
        else:
            if self.isleft(x):
                x.getfather().setleft(y)
            else:   
                x.getfather().setright(y)
        y.setleft(x)
        x.setfather(y)

    def right_rotate(self,x):
        y = x.getleft()
        x.setleft(y.right)
        if y.getright() != self.vazio:
            y.right.setfather(x)
        y.setfather(x.getfather())
        if x.getfather() == self.vazio:
            self.root = y
        else:
            if self.isright(x):
                x.getfather().setright(y)
            else:   
                x.getfather().setleft(y)
        y.setright(x)
        x.setfather(y)




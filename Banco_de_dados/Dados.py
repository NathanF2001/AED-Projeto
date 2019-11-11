import pickle
class Data_all_users:

    def __init__(self,tipo,bol = True,right = None,left = None,daddy = None,color = 'RED'):
        
            
        self.years = [0 for a in range(10)]
        self.months = [[0 for a in range(12)]for b in range(10)]
        self.Users_year = [0 for a in range(10)]
        self.Users_months = [[0 for a in range(12)]for b in range(10)]
        self.tipo = tipo
        self.left = left
        self.right = right
        self.daddy = daddy
        self.color = color


    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getinfo(self):
        return self.tipo

    def getfather(self):
        return self.daddy

    def getmonth(self):
        return self.month

    def setmonth(self,i):
        self.month = i

    def setleft(self,i):
        self.left = i

    def setright(self,i):
        self.right = i

    def setinfo(self,i):
        self.tipo = i

    def setfather(self,i):
        self.daddy = i


class Binary_tree_Data:

    def __init__(self):
        self.vazio = Data_all_users(None,False,color = 'BLACK')
        self.vazio.setfather(self.vazio)
        self.vazio.setright(self.vazio)
        self.vazio.setleft(self.vazio)
        self.root = self.vazio

                        
    def add(self,tipo):
        nodulo = Data_all_users(tipo,True,self.vazio,self.vazio,self.vazio)
        x = self.root
        y = self.vazio
        while x != self.vazio:
            y = x
            if tipo < x.getinfo():
                x = x.getleft()
            else:
                x = x.getright()
        nodulo.setfather(y)
        if y == self.vazio:
            self.root = nodulo
        else:
            if tipo < y.getinfo():
                y.setleft(nodulo)
            else:
                y.setright(nodulo)



        
    def delete(self,nodule): 
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
    
        return y


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
        while y != None and self == y.getright():
            x = y
            y = y.getfather()
        return y





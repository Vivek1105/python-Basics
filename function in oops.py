class Empoly:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def displayEmpoly(self):
        return(self.name,str(self.age))


e1 = Empoly("viv",19)
e2 = Empoly("vishu",18)
e3 = Empoly("vivek",20)
print(e3.displayEmpoly())
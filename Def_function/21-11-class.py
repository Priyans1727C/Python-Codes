'''class a:
    def __init__(smd,era):
        smd.era=era
    def display(smd):
        print("ERA: ",smd.era)
class b:
    pass
class c:
    def __init__(self,naam,pata):
        self.naam=naam                       #str(input("Name: "))
        self.pata=pata                       #str(input("Address: "))
    def display(self):
        print("Name: ",self.naam)
        print("Adress: ",self.pata)
    
gp=a("ram")
z=c("Priyanshu","Varanasi")           
print(isinstance(gp,a))                        # working number of object in your class
print(isinstance(z,a))
print(isinstance(z,b))
print(isinstance(z,c))
#p=a()
#q=b()
#r=c()
#r.display()
#print(isinstance(p,a))'''


class sub:
    def visheay(self):
        print("This is class of subject ")
class math:
    def garhit(self):
        print("This is class of math")

class math(sub):
    



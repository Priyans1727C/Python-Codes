'''class student:
    def __init__(self,f1,f2):
        self.f1=f1
        self.f2=f2
    def __str__(self):
        return f"{self.f1}{self.f2}"

p=student("priyanshu","18")
print(p)'''

class student:
  def __init__(self, name, age,no):
    self.name = name
    self.age = age
    self.no = no
  def add(self):
    print("My name is ",self.name)
#    print("My age is ",self.age)          >>>> it will deleted
    print("My roll no is",self.no)


p=student("priyanshu",18,12206141)
del p.age
p.add()
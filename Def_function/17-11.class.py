class info:
    def __init__ (information,place,phone_no,gender):
        pass

class lpu():
    def __init__ (self,naam,pata):
        self.__init__ (self,naam,pata)
        pass


class student:
  def __init__(self, name, age,no):
    self.name = name
    self.age = age
    self.no = no
  def display(self):
    print("Name: ",self.name)
    print("Age: ",self.age)
    print("Rollno: ",self.no)

a=student("Priyanshu",18,12206142)
a.display()


print()
print()

l=[]
while 1:
    a=map(input("Name: ").split(","))
    if a=="end":
        break
#    b=input("Age: ")
#    c=input("Rollno: ")
    l.append(a)

print()
print("mylis: ",l)
for i in l:
    st=student(i)
    st.display()
class student:
    def __init__ (self,name,rollno,age):
        self.name = name
        self.rollno = rollno
        self.age = age
    
    def display(self):
        print("Name: ",self.name)
        print("Rollno: ",self.rollno)
        print("Age: ",self.age)

print()


print('''
                                                                                                
88888888ba,                                     88                                              
88      `"8b                 ,d                 88                                              
88        `8b                88                 88                                              
88         88  ,adPPYYba,  MM88MMM  ,adPPYYba,  88,dPPYba,   ,adPPYYba,  ,adPPYba,   ,adPPYba,  
88         88  ""     `Y8    88     ""     `Y8  88P'    "8a  ""     `Y8  I8[    ""  a8P_____88  
88         8P  ,adPPPPP88    88     ,adPPPPP88  88       d8  ,adPPPPP88   `"Y8ba,   8PP"""""""  
88      .a8P   88,    ,88    88,    88,    ,88  88b,   ,a8"  88,    ,88  aa    ]8I  "8b,   ,aa  
88888888Y"'    `"8bbdP"Y8    "Y888  `"8bbdP"Y8  8Y"Ybbd8"'   `"8bbdP"Y8  `"YbbdP"'   `"Ybbd8"'  
''')

l=[]
while True:
    print()
    print()
    a=input("Name: ")
    if a=="end":
        print()
        print()
        break
    b=input("Rollno: ")
    c=input("Age: ")
    print()
    print()
    z=student(a,b,c)
    l.append(z)
    print('''Enter Name -- "end" -- to exit loop''')

##########       RESULT         ###########################

print("THE LIST OF TOTAL STUDENT ARE:",len(l))
print()
for i in l:
    i.display()
    print()

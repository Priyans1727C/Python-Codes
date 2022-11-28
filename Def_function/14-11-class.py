class student:
  def __init__(self, name, age,no):
    self.name = name
    self.age = age
    self.no = no
'''
p1 = student("John", 36,123456677)

print(p1.name)
print(p1.age)
print(p1.no)


print()
print()
print()

data = student("Priyanshu",18,12206141)
print("name:", data.name)
print("age:",data.age)
print("rollno:",data.no)

print()
print()'''

l=[]
while 4:
  a=input("name: ")
  if a=="break":
    break
  b=input("age: ")
  c=input("rollno: ")
  data = (a,b,c)
  l.append(data)
for i in l:
  c=student
  print("name:", data.name)
  print("age:",data.age)
  print("rollno:",data.no)
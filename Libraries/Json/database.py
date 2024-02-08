import json
import pyfiglet

def inputs():
    print()
    data={}
    student_size=int(input('No_Of_Stdents: '))
    print()
    for i in range(0,student_size):
        print(f"Student Details {i+1}:") 
        reg_no=int(input('    Reg_no     : '))
        name=input('    Name       : ')
        occupation=input('    Occupation : ')
        dob=input('    DOB        : ')
        value={'Name':name,'Occupation':occupation,'DOB':dob}
        data[reg_no]=value
    return data
    

def insertion(temp_data):
    data={}
    try:    
        with open("database.json",'r') as f:
            temp=f.read()
            data=json.loads(temp)
            # print(data) 

        with open("database.json",'w') as f:
            for key, value in temp_data.items():
                data[key]=value
            f.write(json.dumps(data,indent=4))
   
    except:
        with open("database.json",'w') as f:
            for key, value in temp_data.items():
                data[key]=value
            f.write(json.dumps(data,indent=4))

def update():
    print()
    reg_no=input('    Reg_no     : ')
    name=input('    Name       : ')
    occupation=input('    Occupation : ')
    dob=input('    DOB        : ')
    value={'Name':name,'Occupation':occupation,'DOB':dob}
    try:
        with open("database.json",'r') as f:
            temp=f.read()
            data=json.loads(temp)
        if(reg_no in data):
            with open("database.json",'w') as f:
                data[reg_no]=value
                f.write(json.dumps(data,indent=4))
        else:
            print("NO such reg.no exist")
    except Exception as f:
        print('NO data found!')
        print(f)
      
def searching():
    reg_no=input()
    with open('database.json','r') as f:
        data=json.loads(f.read())
        try:
            print(data[reg_no])   
        except:
            print('No data found!')

def display():
    with open('database.json','r')as f:
        print(f.read())

                
print('''\033[36m 
      
    ________            __          __________                          
    \______ \  _____  _/  |_ _____  \______   \_____     ______  ____   
     |    |  \ \__  \ \   __\\\__  \  |    |  _/\__  \   /  ___/_/ __ \  
     |    `   \ / __ \_|  |   / __ \_|    |   \ / __ \_ \___ \ \  ___/  
    /_______  /(____  /|__|  (____  /|______  /(____  //____  > \___  > 
            \/      \/            \/        \/      \/      \/      \/  
                                                                    
      
                                            \033[32m   ~by Priyanshu Singh  \033[39m
      ''')
print()
print("Choices are: \n\n    1)Creation\n    2)Updation\n    3)Display\n    4)Searching")
print()

while(True):
    try:
        choice=int(input('Enter choice: '))
        if(choice==1):
            temp_data=inputs()
            insertion(temp_data)
        elif(choice==2):
            update()
        elif(choice==3):
            display()
        elif(choice==4):
            searching()
        elif(choice==0):
            break
        else:
            print("Enter valid choice")
    except Exception as s:
            print("Enter valid choice\nProblem: ",s)
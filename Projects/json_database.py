import json

def inputs():
    print()
    data={}
    student_size=int(input('no_of_stdents: '))
    print()
    for i in range(0,student_size):
        print(f"Student Details {i+1}:")
        print() 
        reg_no=input('    reg_no     : ')
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
 

choice=int(input('choice: '))
if(choice==1):
    temp_data=inputs()
    insertion(temp_data)
elif(choice==2):
    update()
else:
    print("Enter valid choice")

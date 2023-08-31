import json

table={
    'data1':{
              'id':1,
              'name':'priyanshu',
              'class':9        
    },
    
    'data2':{
              'id':2,
              'name':'harsh',
              'class':10        
    }   
    
}

data=json.dumps(table,indent=5)

with open("file.json","w") as f:
    f.write(data)
# print(json.dumps(table,indent=7))
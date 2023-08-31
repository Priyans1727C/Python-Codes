import json

print("list conversion to Array")
print(json.dumps(["hii",2,"priyanshu"]))


print("\nstring conversion to String")
print(json.dumps("hello priyanshu"))

print("\nint conversion to Number")
print(json.dumps(34))

print("\ntuple conversion to Array")
print(json.dumps((2,3,4,"hii")))


print("\nNone value to null")
print(json.dumps(None))

print("\nfloat conversion to Number")
print(json.dumps(44.33))

print("\nBoolean conversion to their respective values")
print(json.dumps(True))
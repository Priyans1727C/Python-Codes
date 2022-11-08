a=input("Type your string: ")
x,y=map(str,input("old-word new-word: ").split())

# using upper case
print("In upper case: ",a.upper())

#using lower case
print("In lower case: ",a.lower())

#using title
print("In title format: ",a.title())

#using capitalize
print("In capitalize format: ",a.capitalize())

#using swapcase
print("In swapcase: ",a.swapcase())

#using replace
print("After replacing: ",a.replace(x,y))

#sprit use to remove space in string 
print("Using left-strip:",a.lstrip())

#using right strip
print("Using right-strip:",a.rstrip())

#using  strip
print("Using strip:",a.strip())



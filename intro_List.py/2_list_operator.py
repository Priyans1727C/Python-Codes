#operator use in list are following

list1=["ram", "Harsh","subham"]
list2=["priyanshu","Harry","Ayush"]
list3=[1,2,3,4,4,5]
list4=[5,4,3,3,1,2]


# Multipllication and subtraction not be use betwwen two list

#Addition
new_list =list1+list2
print("addition:",new_list)

new_list =list1+list3
print("addition:",new_list)


new_list =list3+list2+list1+list4
print("addition:",new_list)


##########         Attributs             ###############
lst = ["Raju","ram",1,"Harsh",4.5443,5,45]
lst2 = [3 , 3 ,2,8,333,56,8,96,6]

#append ---- Used to add element in list
lst.append("WORDS")
print("append:",lst)

#len ----- Used to know number of elements present in list

print("len:",len(lst))

#sort ---- Used to arrange in accending order
lst2.sort()
print("sort :",lst2)

#insert ---Used to add element at specific position
lst2.insert(4,"word")
print("insert at [4]:", lst2)

#del ---Used to delet delete element of any position  
del lst[3]
print("del at [3]:",lst)
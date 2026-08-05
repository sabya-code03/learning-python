student = {'name' : 'John' , 'age' : 25 , 'courses' : ['math','bio','phys','chem'] ,'phone' :'98745-61230'}

#print without using loop
print(len(student)) #print length of the directory
print(student.keys()) #print directory keys()
print(student.items()) #print all the items
print(' ')
#print Using lopp
for key in student :
    print(key) #print directory keys
print(' ')
for Value in student.items():
    print(Value)
print(' ')
for key,Value in student.items():
    print(key,Value)
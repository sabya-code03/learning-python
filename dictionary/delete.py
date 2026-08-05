student = {'name' : 'John' , 'age' : 25 , 'courses' : ['math','bio','phys','chem'] ,'phone' :'98745-61230'}
print(student)

#delete function
del student['age']
print(student)

#in delete function we lost the dat
# spo we use pop
pop1 = student.pop('courses')
print(student) # dictionary after popping
print(pop1) #value of popped key
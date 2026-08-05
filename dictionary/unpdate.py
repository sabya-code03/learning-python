
student = {'name' : 'John' , 'age' : 25 , 'courses' : ['math','bio','phys','chem']}
student['phone'] = '98745-61230'


#update key-value
#in this method we can update multiple key
student.update({'name' : 'Rohan' , 'age' : 19 , 'phone' : '96547-81230'})
print(student)
 #we can also add new key-value through update method
student.update({'grade' : 'A'})
print(student)

#delete key value
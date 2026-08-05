
student = {'name' : 'John' , 'age' : 25 , 'courses' : ['math','bio','phys','chem']}
print(student.get('grade')) #give 'none' instead of error
#we can use custon msg if not found
print(student.get('age' , 'not found'))
print(student.get('grade' , 'not found'))

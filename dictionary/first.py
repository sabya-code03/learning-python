#dictionary = {'key' : 'value', ......}
# key and value may be any data type 
student = {'name' : 'John' , 'age' : 25 , 'courses' : ['math','bio','phys','chem']}
print(student) #print the whole dictionary
#if i want to print a specific value we can recall it by their key 
print(student['name'])
print(student['courses'])
# if we acces a key that doesnt exist it will give error
#there is a solution to get ridoff from the errror
print(student.get('age'))
print(student.get('grade')) #give 'none' instead of error

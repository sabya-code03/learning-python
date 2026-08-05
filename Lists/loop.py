courses = ['hist','math','bio','phys','geo','chem']

for i in courses :
     print(i)
#we can take any variable instead of i 
for course in courses: 
    print(course)
    
#we can  also access item as well as index    
for index , course in enumerate(courses):  #this  index will start from 0 as default
    print(index , course)
for index , course in enumerate(courses, start=2):  #this is how we can start from where we want  
    print(index , course)

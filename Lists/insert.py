#in insert we can add an element at any position
courses = ['hist','math','bio','phys','geo','chem']
print(courses)
courses.insert(0,'lang')
print(courses)

#we can insert a entire list to a list
course_1 = ['math','bio','phys','chem']
course_2 = ['lang','hist','geo']
course_1.insert(2,course_2) # no. 2 will work as a list instead of an element
print(course_1)
print(course_1[3]) #return an element
print(course_1[2]) #return a list


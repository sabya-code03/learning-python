#various method to delete item from list
courses = ['hist','math','bio','phys','geo','chem']
#remove
courses.remove('math') 
print(courses)

#pop method
popped = courses.pop() #work as a stack and remove last element
print(courses)
print(popped) #it will return the item which is popped

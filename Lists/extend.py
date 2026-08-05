#in insert we can insert a new list as a whole list but it will not work as intigrated part of the list
#for this we use extend
#extend add the new elemets from list2 into list1 at the exnd of the list
course_1 = ['math','bio','phys','chem']
course_2 = ['lang','hist','geo']
course_1.extend(course_2)
print(course_1)

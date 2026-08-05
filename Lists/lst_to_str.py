# in this method we will convert list to string
courses = ['hist','math','bio','phys','geo','chem']
course_str1 = ' , '.join(courses) 
print(course_str1) # the whole list will work as string
# joining symbol can be changed as i want 
course_str = '-'.join(courses)
print(course_str)

# we can also convert the string into a list by the following method
new_list = course_str.split('-')
print(new_list)
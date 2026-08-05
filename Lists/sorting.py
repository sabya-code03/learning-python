#various method to the sorting a list
courses = ['hist','math','bio','phys','geo','chem']
 # courses.reverse() #reverse the whole list
print(courses)


courses.sort()
print(courses)#sorting according to ascending order
courses.sort(reverse=True) #sorting according to descending order
print(courses)

nums = [1,5,3,2,9]
nums.sort()
print(nums)
nums.sort(reverse=True) # true for reverse / descending , false to stick in ascending
print(nums)

# in  previous methods sorting changes the oringinal file and changing the original list
#but if we dont want to original data we can use sorted()
# for this we have to take a new variable
Sorted_courses = sorted(courses)
print(courses) #original list
print(Sorted_courses) #sorted list
# difference is the function which not included in list or tuple
course_1 = {'hist','math','bio','phys','chem'}
course_2 = {'lang','hist','geo', 'math'}
print(course_1.difference(course_2))
print(course_2.difference(course_1))
print(course_1.difference(course_1))
import my_modulo as mm # will import data from file name "my_modulo.py"
# we can make a shrot form for better use
course = [ 'math' , 'sci' , 'hist' , 'geo']
index = mm.find_index(course , 'math')
print(index)


#another form of import
from my_modulo import find_index ,test
course = [ 'math' , 'sci' , 'hist' , 'geo']
index = find_index(course , 'math')
print(index)
print(test)

from my_modulo import *
course = [ 'math' , 'sci' , 'hist' , 'geo']
index = find_index(course , 'math')
print(index)
print(test)

from my_modulo import find_index ,test
import sys
course = [ 'math' , 'sci' , 'hist' , 'geo']
index = find_index(course , 'math')
print(sys.path)

import random
course = [ 'math' , 'sci' , 'hist' , 'geo']
random_course = random.choice(course)
print(random_course)
# difff btween 'is' and '=='
a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b)
# a and b  are equal in value but their identities are different
#proof
print(id(a))
print(id(b))
print(' ')

c =[1,2,3]
d = c
#here we have assigned the whole vaible so  id is same and "is" also works
print(id(a))
print(id(b))
print(a is b)
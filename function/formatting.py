# {} indicates the greeting 
#format should be used outside '' 
#greeting doesnt effect anything outside the funtion, it loccally 
#1
def nor_func(greeting):
    return '{} Function'.format(greeting)
# print(nor_func()) give error because greeting is missing
print(nor_func('Hello'))
#2
#using of default valuue  and multipld
def nor_func(greeting , name = 'you'):
    return '{}, {}'.format(greeting , name )
print(nor_func('Hello'))
#3
#When both are default
def nor_func(greeting = 'hi' , name  = 'you' ):
    return '{}, {}'.format(greeting , name )
print(nor_func())
#4
#using both variable
def nor_func(greeting , name  = 'you' ):
    return '{}, {}'.format(greeting , name )
print(nor_func('Hello' , 'Sabyasachi'))


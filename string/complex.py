greeting = 'Hello'
name = 'Johny'

#addition of two different string 
msg = greeting + ', ' + name 
print(msg)

#these are the examples of unformatted strings
msg_1 = greeting + ', ' + name + '. Welcome to my home.'
print(msg_1)

#now we will learn formatted strings
new_msg ='{}, {}. Welcome to my home.'.format(greeting,name) 
#we use the curly bracets to use predefined strings. in this way we can differ predifined and newly generated string components.
print(new_msg)



#concept of F-string
f_msg = f'{greeting.lower()}, {name.upper()}. Welcome to my home.' 
#dd "f" before starting will format the whole string . thats the concept of f string
#also can change font due to having formating .
print(f_msg)

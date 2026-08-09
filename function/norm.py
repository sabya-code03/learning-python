def nor_func():
    pass
print(nor_func) #function call
#as i have instructed anything in this function it will just print random thing in terminal

#now let the function do some work
def fr_function():
    print("first function")
print(fr_function) #will print the random thing as previous
fr_function()  # function call

#another form
def f1r_function():
    return 'first function' 
     #we can also use return instead of print
f1r_function() #normal function call will not print anything
print(f1r_function()) # but when print is added it will give output

#innn func2 we use print -> so it will print the value whenever we call the function
#but in func3 we used return -> it will print value whenever it is asked to print 
#print is like loudspeaker
#return is like quietly building

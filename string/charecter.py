#finding the charecter in string
message = 'Hello World'
print(message[2]) # finding single charecter
print(message[10])
#finding a range 0f charecter
print(message[0:4]) #its inlclude the first letter(0) but end before the last letter(4)
print(message[:4]) #if we not include any number in first then it will default 0
print(message[5:]) #if we not include any number in last then it will default last digint(here 10)
print(message[5:4]) # no output
print(message[:]) #default
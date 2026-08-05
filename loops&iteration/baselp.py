#differences between continue and break.....
nums = [1,2,3,4,5]
for i in nums:
    if i == 3 :
        print('found!!')
        continue; #skip this iteration and continue the loop
    print(i)
    
print(' ')


for i in nums:
    if i == 3 :
        print('found!!')
        break; #end the loop right here
    print(i)
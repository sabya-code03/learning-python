#in this formatitng * denotes -> arguments in tuple/list aand ** deniotes -> key words argument s in dcitionnary

def stu_info(*args, **kwargs):
    print(args) #retunr tuple here
    print(kwargs) #return dict here
stu_info('math' , 'science' , name = 'John' , age = 23)


def stu_info1(*args1, **args2):
    print(args1)
    print(args2)
games = ['cric' , 'football' ,  'volleyball' 'badminton' , 'hockey']
info = {'name' : 'peter' , 'age' :22 , 'height': '5f6i'} #here we have to format proper like a dictionary
# stu_info1( **info, *games ) will be wrong formATIING
stu_info1(  *games , **info)
#function with no argument no retrun value
def add():
 pass
add()

def add():
    a=10
    b=20
    print('addition of (a) and (b) is:',a+b)
add()

#function with argument but no return value
def add(a,b):
    print('addition of (a) and (b) is:',a+b)
a=10
b=20
add(a,b)

# function with no argument but return value
def add():
    a=10
    b=20
    return a + b
sum=add()
print(sum)

# fucntion with argument and return value
def add(a,b):
    return a+b
    print('hii') # after return no executable
a=8
b=9
sum=add(a,b)
print(sum)

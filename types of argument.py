# types of argument
#1)Positional Argument
#2)Default argument
#3)keyword argument
#4)variable length argument

#1) define: dusring a function call,values passed through arguments should be in the order of parameters in the function defintion.

##def simple_int (p,r,t):
##    print('principle is:',p)
##    print('rate is:',r)
##    print('time is:',t)
##
##    si=p*r*t/100
##    print('simple intrest is:',si)
##
##p=5000
##r=10
##t=5
##simple_int(p,r,t)


#2) default argument

#define:

##def simple_int (p,r,t=10):
##    print('principle is:',p)
##    print('rate is:',r)
##    print('time is:',t)
##
##    si=p*r*t/100
##    print('simple intrest is:',si)
##
##p=5000
##r=10
##t=5
##simple_int(p,r)

##def simple_int (p=1000,r=5,t=10):
##    print('principle is:',p)
##    print('rate is:',r)
##    print('time is:',t)
##
##    si=p*r*t/100
##    print('simple intrest is:',si)
##
##p=5000
##r=10
##t=5
##simple_int(p,r,t)

#3)keyword argument:
# only arguments mean whenever we pass the argument(or value)by their parameter names at the time of calling the function in python in

##def simple_int (r,p,t):
##    print('principle is:',p)
##    print('rate is:',r)
##    print('time is:',t)
##
##    si=p*r*t/100
##    print('simple intrest is:',si)
##
##
##simple_int(p=5000,r=10,t=5)


# scope
#1)Local scope
#2)Global scope

#1) Local scope: a variable can be declared inside the function is called as local variable
#scope of local variable is inside the function only

##def display():
##    a=10
##    print(a)
##print(a)
##display()


#2) Global Scope: a variable can be declared outside the function is called as global variable
#scope of global variable is inside as well as outside the function

##A=15
##def display():
##    a=10
##    b=20
##    print(a)
##    print(A)
##
##print(A)
##display()
##print(A)

# what if? A variable is declared inside as well as outside

##A=30
##def display():
##    A=30
##    print(A)
##print(A)
##display()
##print(A)

##A=30
##def display():
##    global A
##    A=20
##    print(A)
##print(A)
##display()
##print(A)

###################
##B=30
##def display(x):
##    global a
##    a=a+x
##    return a
##
##a=20
##b=5
##display(b)
##print(a)
##
##################
##a=10
##y=5
##def myfun():
##    a=2
##    y=a
##    print(y,a)
##myfun()
##print(y,a)
#################
##
##a=10
##y=5
##def myfun():
##    global a
##    y=a
##    a=2
##    print(y,a)
##myfun()
##print(y,a)
##
#################
##
##a=10
##y=5
##def myfun():
##    global a
##    a=2
##    y=a
##    print(y,a)
##myfun()
##print(y,a)

#################

a=1
def display():
    return a
print(a)
print(display())
print(a)



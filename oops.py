#class is a blueprint that defines some properties and behaviors, an object is an instance
#of a class that has those properties and behaviour attached. a class is not allocated memory
# when it is defined. an object is allocated memory when it is created. class is a logical
# entity whereas objects are physical entites.


##a=10
##
##print roll_nt(type(a))
##

##b=20
##
##print(type(a))


##b='rajesh'
##print(type(c))

##class str
##
##class student

##class student:
##    name='sanket'
##    email='r@gmail.com'
##    roll_no=121
##
##s=student()
##print(s.name)
##print(s.email)
##print(s.roll_no)

##class student:
##    name='sanket'
##    email='r@gmail.com'
##    roll_no=121
##
##    def demo(s):
##        name='rajesh'
##        print(name)
##
##s=student()
##s.demo()

##class student:
##    name='sanket'
##    email='r@gmail.com'
##    roll_no=121
##
##    def demo(self):  #self is default parameter that represent instance of class
##        name='rajesh'
##        print(name)

##s=student()
####s.demo()
##k=student()
##k.demo()
##
##m=student
##m.demo()

##class A:
##    def demo(self,department):
##        print(department)
##        print(self)
##        name='sanket'
##        age=26
##        roll_no=123
##        print(name,age,roll_no)
##
##    def display(self):
##        email='s@gmail.com'
##        address='thane'
##        print(email,address)
##
##a=A()
####a.demo()
####print(a)
##
####a.display()
####a.demo('k')
####a.demo('mech')

##class student:
##    def show(self,name,roll_no):
##        print('my name is',name)
##        print('roll no',roll_no)
##        print('i am a python developer')
##
##    def display(self):
##        print('java developer')
##
##s=student()
##s.show('sanket',123)
##s.display()


#static variable scope


##class student:
##    name='sanket'
##    email='s@email'
##    def show(self):
##        print(self.name,self.email)
##        print('python developer')
##    def display(self):
##        print(self.name)
##        print('java developer')
##
##a=student()
####print(a.name)
##a.show()
##
##a.display()




#local variable
##class A:
##    def show(self,roll_no,dep_name):
##        print(roll_no,dep_name)
##        name='rajesh'
##        age=31
##        print(name,age)
##
##    def display(self):
##        print(dep_name)
##        email='s@gmail.com'
##        branch='extc'
##        print(name)
##        print(email,branch)
##
##a=A()
##a.show(123,'mech')
###print(a.name)
##a.display()

#instance variable

##class A:
##    def show(self,name,age,salary):
##        a.name1=name
##        self.age1=age
##        self.salary1=salary
##        print(a.name1,self.age1,self.salary1)
##
##    def display(self):
##        print(a.name1,self.age1,self.salary1)
##
##a=A()
##a.show('sanket',31,70000)
##a.display()

# static 
##class student:
##    name='sanket'
##    email='s@email'
##    roll_no=12
##    def show(self):
##        print(self.name,self.email,self.roll_no)
##        print('python developer')
##    def display(self):
##        print(self.name)
##        print('java developer')
##
##s=student()
##s.show()
##s.display()

########################################################

##class A:
##    def show(self):
##        self.name=input('enter your name:')
##        self.age=int(input('enter your age:'))
##        self.salary=int(input('enter salary:'))
##
##    def display(self):
##        print('my name is',self.name)
##        print('my age is',self.age)
##        print('salary is',self.salary)
##
##a=A()
##a.show()
##a.display()
##
##b=A()
##b.show()
##b.display()

###############################################################

##class A:
##    def show(self,name,address):
##        print('python developer')
##
##    def display(self):
##        self.show('pratham','mumbai')
##        a.show('kedar','itvedant')
##
##        print('java developer')
##
##a=A()
##a.show('sanket','thane')
##a.display()


################################################################

##class A:
##    a=10
##    b=20
##
##    def demo(s):
##        s.a=s.a+1
##        A.b=A.b+1
##        print(s.a,A.b)
##
##x=A()
##x.demo()
##
##y=A()
##y.demo()
##
##z=A()
##z.demo()

# constructor: __init__ method runs autmotically when object is created which is
# used to initialize the instance obejct

##class A:
##
##    def __init__(s):
##        print('sanket')
##        s.id=10
##        s.name='sanket'
##        s.salary=70000
##
##    def display(s):
##        print('id is',s.id)
##        print('name is',s.name)
##        print('salary is',s.salary)
##
##a=A()
##a.display()


##class A:
##
##    def __init__(s):
##        s.name=input('enter your name:')
##        s.pincode=int(input('enter your pincode:'))
##
##    def display(s):
##        print('name is',s.name)
##        print('pincode is',s.pincode)
##
##a=A()
##a.display()


##class A:
##    def __init__(s,name,age,salary):
##        s.name=name
##        s.age=age
##        s.salary=salary
##
##    def display(s):
##        print(s.name,s.age,s.salary)
##    
##a=A('sanket',31,70000)
##a.display()



# string str method

##class A:
##    def __init__(s,name,age,salary):
##        s.name=name
##        s.age=age
##        s.salary=salary
##
##    def display(s):
##        print(s.name,s.age,s.salary)
##
##    def __str__(s):
##        return s.name+' '+str(s.age)+' '+str(s.salary)
##
##a=A('sanket',31,70000)
##a.display()
##
##print(a)


##class A:
##    def display(s,name,age):
##        s.email='s@gmail.com'
##        print(name,age,s.email)
##        print('python developer')
##
##    def show(s):
##        print(s.email)
##        s.display('raj',31)
##        print('java developer')
##
##    def demo(k):
##        print(k.email)
##        print(a.email)
##
##a=A()
##a.display('janvi',21)
##a.show()
##a.demo()
        

#destructor

#destructor is a member method of a class it delete the memory
# of object it can be call with object
# name is __del__

# garbage collector:
# a program to delete reference
# it runs automatically
# it does memory management

##class A:
##    def __init__(self):
##        self.name='rajesh'
##        print('python developer')
##
##    def show(self):
##        print('java developer')
##
##    def __del__(self):
##        print('object deleted')
##
##a=A()
##a.show()
##
##del a
##
##c=A()
##c.show()


#Inheritance or single level inheritance

#one class can inherit the properties and method of another class this process is known as inheritence

##class A:
##    a=10
##
##    def show(s):
##        print('python developer')
##
##class B(A):
##
##    b=20
##
##    def display(s):
##        print(s.b,c.b,c.a,B.a,B.b)
##
##        print('java developer')
##
##a=A()
##a.show()
##
##c=B()
##c.display()
##b.show()


# multi level inheritance:
# the inheritance in which a class can be derived from another derived class is known as multilevel

##class A:
##    a=10
##    def show(s):
##        print('grant parent method is called')
##
##class B(A):
##    b=20
##    def display(s):
##        print('parent method called')
##
##class C(B):
##    c=30
##    def data(s):
##        print(s.a+s.b+s.c)
##        print('child method called')
##
##x=C()
##print(x.c)
##x.data()
##x.display()
##x.show()

# hirarchical inheritance ==(one parent have multiple child)
# if multiple derived classes are created from same base ,this kind of inheritance is know as

##class A:
##    a=10
##    def show(s):
##        print('python developer')
##
##class B(A)
##
##
##
##


# muliple inheritance
# if a child class inherita from than one class, i.e this child
# class is derived from multiple classes, we call it multiple
# inhertiance in python

##class A:
##    a=10
##    def show(s):
##        print('python developer')
##
##class B:
##    b=20
##    def display(s):
##        print('java developer')




#################################################

##class Engineer:
##    def study(s):
##        print('Engineer study method called')
##
##    def show(s):
##        print('Engineer show method called')
##
##class Doctor:
##    def study(s):
##        print('doctor study method called')
##
##    def display(s):
##        print('doctor display method called')
##
##class student(Engineer,Doctor):
##    def demo(s):
##        print('Pharmacist')
##
##s=student()
##s.display()
##s.show()
##
##s.study()


########################################################

#Polymorphism

#Polymorphism means many form
# an entity can work in muliple role this capability is called as polymorphism
# 1) function overriding @) function overloading

#1)
#function overriding
#in function overriding we can  declare a function in base class and derived class with same name and same parameters
# it occurs when one class is inherit from another class

##class A:
##    def display(self):
##        print('python developer')
##
##class B(A):
##    def display(self):
##        print('java developer')
##
##ob=B()
##ob.display()
##
##a=A()
##a.display()

#2)
# function overloading
# more than one function with same name defined in same class and call with different parameter
# this process is know as method overloading
# but python does not support method overloading

##class A:
##    def show(self,x):
##        print('hii')
##    def show(self,x,y):
##        print('bye')
##    def show(self):
##        print('hello')
##
##a=A()
##a.show()
##a.show(10)
##a.show(10,30)

##

##class A:
##    def show(self,x,y):
##        print(x+y)
##a=A()
##a.show(10,30)
##
####
####
##
##class A:
##    def show(self,x=90,y=100):
##        print(x+y)
##
##a=A()
##a.show(10,30)

#another way to solve this problem

##class A:
##    def show(self,a=None,b=None,c=None):
##        if(a!=None,b!=None,c!=None):
##            print(a+b+c)
##        elif(a!=None,b!=None):
##            print(a+b)
##        else:
##            print(a)
##
##a=A()
##x.show(10)
##x.show(2,3)
##x.show(10,20,30)


###########################################################

#Exceptional Handling
#
#Exceptional handeling an exception is an event , which occurs during the execution of a program, that
# interrupt the normal flow of the program's instruction.

#the try block which is used to test a block of code for errors

#the except block used to handle the errors.

##print('python developer')
##a=int(input('enter the first number:'))
##b=int(input('enter the second number:'))
##try:
##    print(a/b)
##except:
##    print('exception handled')
##print('java developer')

##

##print('Hiiii')
##a=[11,22,33,44,55]
##try:
##    print(a[len(a)])
##except:
##    print('list index out of range')
##
##print('hello')
##
####
##
##print('Hiiii')
##a=[11,22,33,44,55]
##try:
##    print(a[len(a)])
##except Exception as e:
##    print(e)
##print('hello')


##

##print('python developer')
##try:
##    a=int(input('enter the first number')
##    b=int(input('enter the second number')
##    print(a/b)
##except Exception as e:
##    print('value error:',e)
##print('java developer')

##

##try:
##    print (' Thane')
##    print (2/0)
##    print (int (' demo' ) )
##    print (' Dadar')
##
##except ZeroDivisionError as e:
##    print (e)
##except ValueError as v:
##    print (' value error', v)
##except Exception as e:
##    print ('exception handeled', e)
##except:
##    print ('exception handeled' )

##

##k=[11,22,33]
##try:
##    print(k[1])
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(int('rajesh'))
##    except:
##        print('value Error')
##except:
##    print('Exception handeled outer try')
##    
##else:
##    print('when exception is not occured')
##

##

##k=[]
##try:
##    print(k[2])
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(int('rajesh'))
##    except:
##        print('value Error')
##except:
##    print('Exception handeled outer try')


##

##try:
##    print('thane')
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(int('rajesh'))
##    except:
##        print('value Error')
##except:
##    print('Exception handeled outer try')
##    


##


##k=[]
##try:
##    print('thane')
##    #print(9/0)
##    #print(abc)
##    #print(k[2])
##    print(int('rajesh'))
##
##
##except ZeroDivisionError as e:
##    print('zero division',e)
##
##except NameError as e:
##    print(e)
##except IndexError as e:
##    print(e)
##except ValueError as e:
##    print(e)
##
##except Exception as e:
##    print(e)
##
##except:
##    print('Exception handeled')   # default except block must be last


##
##k[]
##try:
##    print(k[2])
##    print('thane')
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(abc)
##    except Exception as e:
##        print(e)
##
##except:
##    print('outer exception handeled')
##
##else:
##    print('it will execute only when exception is not occured')
##
##finally:
##    print('it always be executed')






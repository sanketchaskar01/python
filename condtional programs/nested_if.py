# find the largest number of out of three
n1=int(input('enter the number'))
n2=int(input('enter the number'))
n3=int(input('enter the number'))

if n1>n2:
    if n1>n3:
        print(n1,'is the largest')
    else:
        print(n3,'is largest')
else:
    if n2>n3:
        print(n2,'is largest')
    else:
        print(n3,'is largest')
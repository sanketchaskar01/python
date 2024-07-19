#recursion: when a function call itself , then that function is called as
# recursive function and the process is called as recursion

##def demo():
##    print('sanket')
##    demo()
##
##demo()

#############################################

##i=0
##def demo():
##    global i
##    i=i+1
##    print('rajesh',i)
##    demo()
##
##demo()

#############################################

##import sys
##
##print(sys.getrecursionlimit())
##
##sys.setrecursionlimit(200)
##
##print(sys.getrecursionlimit())
##
##i=0
##def demo():
##    global i
##    i=i+1
##    print('sanket',i)
##    demo()
##
##demo()

##################################################

#advantage:
#1) clean code/less number of code
#2) complex problem can be sollved

#disadvantage:
#1)hard ro debug
#2) not memory efficient

##################################################

#WAP for fibbonacci series using recursion

#0,1,1,2,3,5,8,13,21,34,..........

##formula
#fibbo(1)=0
#fibbo(2)=1
#fibbo(3)=fibbo(1)+fibo(2)
#fibbo(3)=fibbo(3-2)+fibbo(3-1)
#fibbo(n)=fibbo(n-2)+fibbo(n-1)

##def fibbo(n):
##    if n==1:
##        return 0
##    if n==2:
##        return 1
##    return fibbo(n-2)+fibbo(n-1)
##n=int(input('enter the number of terms: '))
##print(fibbo(n))

########################################################

##find recursion base point to stop
##print your name 10 time without using loops and manually
##factorial programm without recrusion
##find power of number using recrusion
##find the prime number using recrusion
##wap a counting number of digit in given number with using recrusion
##sum of 1st and number using recrusion
## wap for printing n to 1 seq.




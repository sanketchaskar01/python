Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# int to int
>>> 10+5
15
>>> 10-5
5
>>> 10*5
50
>>> 10/5
2.0
>>> 10**5
100000
>>> 10//5
2
>>> 10%5
0
>>> 
>>> # int to float
>>> 10+5.5
15.5
>>> 
>>> 10-5.5
4.5
>>> 
>>> 10*5.5
55.0
>>> 
>>> 10**5.5
316227.7660168379
>>> 
>>> 10/5.5
1.8181818181818181
>>> 
>>> 10//5.5
1.0
>>> 
>>> 10%5.5
4.5
>>> 
>>> #int to bool
>>> 
>>> 10+True
11
>>> 
>>> 10+False
10
>>> 
>>> True+10
11

False+10
10

10-True
9

10-False
10

10*True
10

10*False
0

10**True
10

10**False
1

10/True
10.0

10/False
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    10/False
ZeroDivisionError: division by zero
10%True
0

10%False
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    10%False
ZeroDivisionError: integer modulo by zero

#int to str

10+"hi"
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    10+"hi"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"hi"+10
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    "hi"+10
TypeError: can only concatenate str (not "int") to str
"hi"*2
'hihi'

True+True
2
True+False
1
False+False
0

#float with bool

10.5+True
11.5

10.5-False
10.5

10.5%False
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    10.5%False
ZeroDivisionError: float modulo

#float and str

10.5+"hi"
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    10.5+"hi"
TypeError: unsupported operand type(s) for +: 'float' and 'str'
"hi","hi"-1
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    "hi","hi"-1
TypeError: unsupported operand type(s) for -: 'str' and 'int'
"hihi"-1
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    "hihi"-1
TypeError: unsupported operand type(s) for -: 'str' and 'int'
"hihi"*2
'hihihihi'

# bool and str
"hi"+True
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    "hi"+True
TypeError: can only concatenate str (not "bool") to str
"hi"+False
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    "hi"+False
TypeError: can only concatenate str (not "bool") to str
"hi"*True
'hi'
"hi"*False
''

"hihi"/True
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    "hihi"/True
TypeError: unsupported operand type(s) for /: 'str' and 'bool'


#hw2

int(10.5)
10
int(True)
1
int(False)
0
int("hi")
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'

int(10)
10

float(10)
10.0
float(True)
1.0
float(False)
0.0
float("hi")
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'

bool(True)
True
bool(False)
False
bool(10)
True
bool(1.0)
True
bool(-5.5)
True
bool(0)
False
bool(-5)
True
bool('hi')
True

str(True)
'True'
str(False)
'False'
str(10)
'10'
str(10.5)
'10.5'
str("hi")
'hi'


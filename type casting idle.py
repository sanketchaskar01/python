Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> int(45.5)
45
>>> int("hello")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
>>> int(True)
1
>>> 
>>> str(40)
'40'
>>> str(40.5)
'40.5'
>>> str(True)
'True'
>>> 
>>> bool(40)
True
>>> bool(40.5)
True
>>> bool("hello")
True
>>> 
>>> float(40)
40.0
>>> float(True)
1.0
>>> float("hello")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float("hello")
ValueError: could not convert string to float: 'hello'
>>> float(false)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    float(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> float(False)
0.0
>>> bool(" ")
True
>>> bool("")
False

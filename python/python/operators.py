Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5>6
False
5<6 & 9>2
False
0101<<2 010101
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
5<<3
40
7^9
14
7&9
1
num1 is int
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    num1 is int
NameError: name 'num1' is not defined
num1=10
num1 is int
False
type(num1) is int
True
type(num1) is not str
True
print(num1)
10
hi
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    hi
NameError: name 'hi' is not defined
'hi'
'hi'
"hi"
'hi'
print(hi)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(hi)
NameError: name 'hi' is not defined
print("hi"+"hello")
hihello
print("hi"+10)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print("hi"+10)
TypeError: can only concatenate str (not "int") to str
print("sum': '+'\n', num1+10)
      
SyntaxError: incomplete input
print('sum': '+'\n', num1+10)
      
SyntaxError: invalid syntax
print("sum: '+'\n', num1+10)
      
SyntaxError: incomplete input
print('sum: '+'\n', num1+10)
      
sum: 
 20
input()
      
5
'5'
input()
      
"hello"
'"hello"'
input()
      
hello
'hello'
bool(input('enter a number:'))
      
enter a number:0
True
bool(input('enter a number:'))
      
enter a number:
False
"Ram's House"
      
"Ram's House"
Str1="hello"
      
str1
      
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    str1
NameError: name 'str1' is not defined. Did you mean: 'Str1'?
Str1
      
'hello'
Str1(0)
      
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    Str1(0)
TypeError: 'str' object is not callable
Str1{[0]
     
SyntaxError: '{' was never closed
Str[0]
     
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    Str[0]
NameError: name 'Str' is not defined. Did you mean: 'Str1'?
Str1[1]
     
'e'
Str1[o:3]
     
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    Str1[o:3]
NameError: name 'o' is not defined
Str1[0:3]
     
'hel'
Str1{[-2]
     
SyntaxError: '{' was never closed
Str1[-2]
     
'l'
Str1[-5]
     
'h'
Str1[0]
     
'h'
Str1[0,4]
     
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    Str1[0,4]
TypeError: string indices must be integers
Str1[0:5]
     
'hello'
Str1[0:7]
     
'hello'
Str1[-10:-1:-2]
     
''
Str2="hello dear"
     
Str2.Capitalize()
     
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    Str2.Capitalize()
AttributeError: 'str' object has no attribute 'Capitalize'. Did you mean: 'capitalize'?
Str2.capitalize()
     
'Hello dear'
Str2.uppercase();
     
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    Str2.uppercase();
AttributeError: 'str' object has no attribute 'uppercase'
Str2.uppercase()
     
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    Str2.uppercase()
AttributeError: 'str' object has no attribute 'uppercase'
KeyboardInterrupt
Str2.upper()
     
'HELLO DEAR'
Str2.lower()
     
'hello dear'
Str2.endswith("o")
     
False
Str2.endswith("r")
     
True
Str2.find("d")
     
6
Str2.endswith("a")
     
False
KeyboardInterrupt
Str2.find("a")
     
8
Str2.find("b")
     
-1
Str2.index("d")
     
6
Str2.index("b")
     
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    Str2.index("b")
ValueError: substring not found
Str2.replace[“h”,”k”]
     
SyntaxError: invalid character '“' (U+201C)
Str2.replace['h','k']
     
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    Str2.replace['h','k']
TypeError: 'builtin_function_or_method' object is not subscriptable
Str2.replace(“h”,”k”)
     
SyntaxError: invalid character '“' (U+201C)
Str2.replace('h', 'k')
     
'kello dear'
Str2.replace('h', 'k')
Str2.split(' ')
     
SyntaxError: multiple statements found while compiling a single statement
Str2.split('_')
     
['hello dear']
Str2.strip()
     
'hello dear'
str3='   j   '
     
str3.split()
     
['j']
str3.strip()
     
'j'
Str2='hi'
     
Str2
     
'hi'
numbers=[10,20,30]
     
id(numbers)
     
2238150454336
numers.append(40)
     
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    numers.append(40)
NameError: name 'numers' is not defined. Did you mean: 'numbers'?
numbers.append(40)
     
numbers
     
[10, 20, 30, 40]
numbers[2]
     
30
numbers.count(40)
     
1
numbers.index(40)
     
3
numbers.remove(30)
     
numbers
     
[10, 20, 40]
numbers.pop()
     
40
numbers
     
[10, 20]
numbers.pop(-2)
     
10
numbers
     
[20]
numbers.insert(50)
     
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    numbers.insert(50)
TypeError: insert expected 2 arguments, got 1
numbers.append(50,60)
     
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    numbers.append(50,60)
TypeError: list.append() takes exactly one argument (2 given)
numbers.append(50)
     
numbers.append(60)
     
numbers
     
[20, 50, 60]
numbers.reverse()
     
numbers
     
[60, 50, 20]
numbers.extend(12,33,44,55)
     
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    numbers.extend(12,33,44,55)
TypeError: list.extend() takes exactly one argument (4 given)
numbers.extend[([12,33,44,55])
               numbers
               
SyntaxError: incomplete input
numbers.extend([12,33,44,55])
               
numbers
               
[60, 50, 20, 12, 33, 44, 55]
numbers.sort()
               
numbers
               
[12, 20, 33, 44, 50, 55, 60]
numbers.clear()
               
numbers
               
[]
numbers.delete()
               
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    numbers.delete()
AttributeError: 'list' object has no attribute 'delete'
KeyboardInterrupt
tup1=(10,22,3,44,55)
               
tup1.count()
               
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    tup1.count()
TypeError: tuple.count() takes exactly one argument (0 given)
tup1.count(10)
               
1
set=+{10,22,33,44,55}
               
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    set=+{10,22,33,44,55}
TypeError: bad operand type for unary +: 'set'
>>> set={10,22,33,44,55}
...                
>>> set2={12,24,35,44,55}
...                
>>> set.union(set2)
...                
{33, 35, 10, 44, 12, 22, 55, 24}
>>> set.sort()
...                
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    set.sort()
AttributeError: 'set' object has no attribute 'sort'
>>> set3=set.union(set2)
...                
>>> set3
...                
{33, 35, 10, 44, 12, 22, 55, 24}
>>> set3.sort( )
...                
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    set3.sort( )
AttributeError: 'set' object has no attribute 'sort'
>>> set.intersection(set2)
...                
{44, 55}
>>> sort(set3)
...                
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    sort(set3)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
>>> sorted(set3)
...                
[10, 12, 22, 24, 33, 35, 44, 55]

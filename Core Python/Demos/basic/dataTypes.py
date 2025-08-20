#python has only single line comment

###### data types in python

#1.int
x=10
print(type(x))

#2.float
x=3.14
print(type(x))

#3. complex
x= 10 +4j
print(type(x))

#4. string
s='single inverted quote'
print(type(s))

s="double inverted quote"
print(type(s))

s=''' multiline string
 using three single inverted quote'''
print(type(s))

s=""" multiline string
 using three single inverted quote"""
print(type(s))


####### sequnatials 
#1. List
x= [1,2,'stringType',3.14]
print(type(x))

#2. Tuple
x=(1,2, 'string', 9.87)
print(type(x))

#3.Range
x= range(1,17)
print(type(x))

####### set Types
#1. set
x={1,5,45, 'abs', "str"}
print(x)
print(type(x))

#2. FrozenSet
x=frozenset({1,45,65,'str', "abs"})
print(x)
print(type(x))

#### Mapping
#1. dict
x={'name':'Yuvraj', 'department':'Mechanical' }
print(x)
print(type(x))

####Boolean type
# 1.True
x=True
print(x)
print(type(x))

#2. False
x=False
print(x)
print(type(x))

#### None
x=None
print(x)
print(type(x))
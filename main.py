print('hello world!, ilker')

#print (input('What is your name?'))

## name = input('What is your name?\n>>> ')
## print ('Hello, ' + name)

###  Fundamental Data Types ###

int
##--------------------------------------------------------------------
# int(x: Union[Text, bytes, SupportsInt, _SupportsIndex]=...)
# int([x]) -> integer int(x, base=10) -> integer
# 
# Convert a number or string to an integer, or return 0 if no arguments are given. If x is a number, return x.int(). For floating point numbers, this truncates towards zero.
# 
# If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance representing an integer literal in the given base. The literal can be preceded by '+' or '-' and be surrounded by whitespace. The base defaults to 10. Valid bases are 0 and 2-36. Base 0 means to interpret the base from the string as an integer literal.
# 
# int('0b100', base=0) 4
##--------------------------------------------------------------------

float
##--------------------------------------------------------------------
# float(x: Union[SupportsFloat, _SupportsIndex, Text, bytes, bytearray]=...)
# Convert a string or number to a floating point number, if possible.
##--------------------------------------------------------------------

print (2 + 4)
print (type (2+4)) # tells the class type
print (type (2 / 4)) #-> 0.5 --> float
print (2 ** 2) # 2 to the power of 2
print (2 ** 3) # 2 to the power of 3
print (5 ** 3) # 5 to the power of 3
print (type(5 ** 3)) # 5 to the power of 3

print (5.0 / 4.0) 
print (5 // 4) #round it down to integer 1.25 to 1

print (9.0 / 5.0) 
print (9 // 5) #round it down to integer 1.80 to 1


print (9 % 5) # moduler




bool
##--------------------------------------------------------------------
# bool(o: object=...)
# bool(x) -> bool
# 
# Returns True when the argument x is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.
##--------------------------------------------------------------------

str
##--------------------------------------------------------------------
# str(o: object=...)
# str(object='') -> str str(bytes_or_buffer[, encoding[, errors]]) -> str
# 
# Create a new string object from the given object. If encoding or errors is specified, then the object must expose a data buffer that will be decoded using the given encoding and error handler. Otherwise, returns the result of object.str() (if defined) or repr(object). encoding defaults to sys.getdefaultencoding(). errors defaults to 'strict'.
##--------------------------------------------------------------------

list
##--------------------------------------------------------------------
# list()
# Built-in mutable sequence.
# 
# If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified.
##--------------------------------------------------------------------

tuple
##--------------------------------------------------------------------
# tuple(iterable: Iterable[_T_co]=...)
# Built-in immutable sequence.
# 
# If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.
# 
# If the argument is a tuple, the return value is the same object.
##--------------------------------------------------------------------

set
##--------------------------------------------------------------------
# set(iterable: Iterable[_T]=...)
# set() -> new empty set object set(iterable) -> new set object
# 
# Build an unordered collection of unique elements.
##--------------------------------------------------------------------

dict
##--------------------------------------------------------------------
# dict(**kwargs: _VT)
# dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2)
##--------------------------------------------------------------------

#Classes --> Custom Data Types


#Specilized Data Types -> Not build in python --> Modules

None #means nothing 































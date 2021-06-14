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


#The math module is a standard module in Python and is always available.
# Square root calculation

import math
print (math.sqrt(4))

print('---------------------------')

print (round(3.1))

#Operator presedence
print(20+4*3/12-1)

#Order
# ()
# ** --> Power of
# * /
# + -


##--------------------------------------------------------------------
# List of Functions in Python Math Module
# Function	Description
# ceil(x)	Returns the smallest integer greater than or equal to x.
# copysign(x, y)	Returns x with the sign of y
# fabs(x)	Returns the absolute value of x
# factorial(x)	Returns the factorial of x
# floor(x)	Returns the largest integer less than or equal to x
# fmod(x, y)	Returns the remainder when x is divided by y
# frexp(x)	Returns the mantissa and exponent of x as the pair (m, e)
# fsum(iterable)	Returns an accurate floating point sum of values in the iterable
# isfinite(x)	Returns True if x is neither an infinity nor a NaN (Not a Number)
# isinf(x)	Returns True if x is a positive or negative infinity
# isnan(x)	Returns True if x is a NaN
# ldexp(x, i)	Returns x * (2**i)
# modf(x)	Returns the fractional and integer parts of x
# trunc(x)	Returns the truncated integer value of x
# exp(x)	Returns e**x
# expm1(x)	Returns e**x - 1
# log(x[, b])	Returns the logarithm of x to the base b (defaults to e)
# log1p(x)	Returns the natural logarithm of 1+x
# log2(x)	Returns the base-2 logarithm of x
# log10(x)	Returns the base-10 logarithm of x
# pow(x, y)	Returns x raised to the power y
# sqrt(x)	Returns the square root of x
# acos(x)	Returns the arc cosine of x
# asin(x)	Returns the arc sine of x
# atan(x)	Returns the arc tangent of x
# atan2(y, x)	Returns atan(y / x)
# cos(x)	Returns the cosine of x
# hypot(x, y)	Returns the Euclidean norm, sqrt(x*x + y*y)
# sin(x)	Returns the sine of x
# tan(x)	Returns the tangent of x
# degrees(x)	Converts angle x from radians to degrees
# radians(x)	Converts angle x from degrees to radians
# acosh(x)	Returns the inverse hyperbolic cosine of x
# asinh(x)	Returns the inverse hyperbolic sine of x
# atanh(x)	Returns the inverse hyperbolic tangent of x
# cosh(x)	Returns the hyperbolic cosine of x
# sinh(x)	Returns the hyperbolic cosine of x
# tanh(x)	Returns the hyperbolic tangent of x
# erf(x)	Returns the error function at x
# erfc(x)	Returns the complementary error function at x
# gamma(x)	Returns the Gamma function at x
# lgamma(x)	Returns the natural logarithm of the absolute value of the Gamma function at x
# pi	Mathematical constant, the ratio of circumference of a circle to it's diameter (3.14159...)
# e	mathematical constant e (2.71828...)
##--------------------------------------------------------------------


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































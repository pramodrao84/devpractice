from decimal import *
a = Decimal ('0.10')
b = Decimal ('0.30')
x = a + a + a - b
print('x is{}'.format(x))
print (type(x))
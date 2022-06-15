
# *Numeric abstract base classes....
from numbers import Number, Complex
import numbers


# x = 77
# y = "yyyyy"
# print(isinstance(x, Number))
# print(isinstance(y, Number))

# *******************************************************************************************************
#   complex()
r = 5
s = (4 + 3j == 4 +8j)
print(s)
print(type(s))
print(s.conjugate())
print()

print(s.real)
print(s.imag)

a = complex(4, 3)
print(type(a))
print(a)

print(a.real)
print(a.imag)

# Abstract. Returns the complex conjugate. For example, (1+3j).conjugate() == (1-3j).
print(a.conjugate()) # It returns the +/- if +ive then retun the -ive value like that...

print(isinstance(r, numbers.Real))
print(isinstance(s, numbers.Rational))





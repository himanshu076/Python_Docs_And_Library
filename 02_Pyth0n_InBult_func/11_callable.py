
# *Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed.

# Python program to illustrate
# callable()
# a test function
def Geek():
	return 5

# an object is created of Geek()
let = Geek
# print(callable(let))

# a test variable
num = 5 * 5
# print(callable(num))



# *Ex_01 -
# Python program to illustrate
# callable()
class Geek:
	def __call__(self):
		print('Hello GeeksforGeeks')

# Suggests that the Geek class is callable
# print(callable(Geek))

# This proves that class is callable
GeekObject = Geek()
# GeekObject()

# Geek().__call__()

# *Ex_02 -
# Python program to illustrate
# callable()
class Geek:
    def testFunc(self):
        print('Hello GeeksforGeeks')

# Suggests that the Geek class is callable
print(callable(Geek))

GeekObject = Geek()
# The object will be created but
# returns an error on calling
GeekObject()


# *Example 1: Convert string to bytes

# python code demonstrating
# int to bytes
str = "Welcome to Geeksforgeeks"
arr = bytes(str, 'utf-8')
arr1 = bytes(str, 'utf-16')
arr2 = bytes(str, 'utf-32')
# print(arr)
# print(arr1)
# print(arr2)


# *Example 2: Array of bytes from an integer

# python code to demonstrate
# int to bytes
number = 12
result = bytes(number)
# print(result)

# *Example 3: Null parameters with bytes()
# print(bytes())

# *Example 4: Demonstrating byte() on integers, none and iterables
# Python 3 code to demonstrate the
# working of bytes() on int, iterables, none

# initializing integer and iterables
a = 4
lis1 = [1, 2, 3, 4, 5]
# No argument case
# print (f"Byte conversion with no arguments : {str(bytes())}")
# # conversion to bytes
# print (f"The integer conversion results in : {str(bytes(a))}")
# print (f"The iterable conversion results in : {str(bytes(lis1))}")


# print(bytes())
# print(bytes(a))
# print(bytes(lis1))


# *Example 5: Demonstration of bytes() using string.
# Python 3 code to demonstrate the
# working of bytes() on string

# initializing string
str1 = 'GeeksfÖrGeeks'

# Giving ascii encoding and ignore error
print("Byte conversion with ignore error : " +
	str(bytes(str1, 'ascii', errors='ignore')))

# Giving ascii encoding and replace error
print("Byte conversion with replace error : " +
	str(bytes(str1, 'ascii', errors='replace')))

# Giving ascii encoding and strict error
# throws exception
print("Byte conversion with strict error : " +
	str(bytes(str1, 'ascii', errors='strict')))




# * EX_01 - IF an string

str = "Geeksforgeeks"

# encoding the string with unicode 8 and 16
array1 = bytearray(str, 'utf-8')
array2 = bytearray(str, 'utf-16')
array3 = bytearray(str, 'utf-32')

# print(array1)
# print(array2)
# print(array3)


# * EX_02 - if an integer

# size of array
size = 3

# will create an array of given size
# and initialize with null bytes
array1 = bytearray(size)

print(array1)


# * EX_03 - If an object

# Creates bytearray from byte literal
arr1 = bytearray(b"abcd")

# iterating the value
for value in arr1:
	print(value)

# Create a bytearray object
arr2 = bytearray(b"aaaacccc")

# count bytes from the buffer
print("Count of c is:", arr2.count(b"c"))


# * EX_04 - If an Iterable

# simple list of integers
list = [1, 2, 3, 4, 257]

# iterable as source
array = bytearray(list)

print(array)
print("Count of bytes:", len(array))

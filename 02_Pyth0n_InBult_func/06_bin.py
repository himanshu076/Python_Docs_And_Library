
# *Convert an integer number to a binary string prefixed with “0b”.

# declare variable
num = 100

# print binary number
print(bin(num))
print("Without '0b-binary-object' or with --", format(num, 'b'), format(num, '#b'))
print("Without '0b-binary-object' or with --", f"{num:b}", f"{num:#b}")

# *Second Example -


# Python code to demonstrate working of
# bin()

# function returning binary string
def Binary(n):
    s = bin(n)

    # removing "0b" prefix
    s1 = s[2:]
    return s1

print("The binary representation of 100 (using bin()) is : ", end="")
print(Binary(100))


# *Third Example -
# Python code to demonstrate working of
# bin()
class number:
    num = 100

    def __index__(self):
        return(self.num)

print(bin(number()))
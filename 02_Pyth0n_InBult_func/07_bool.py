
# *Return a Boolean value, i.e. one of True or False.

# Returns False as x is False
x = False
print(bool(x))

# Returns True as x is True
x = True
print(bool(x))

# Returns False as x is not equal to y
x = 5
y = 10
print(bool(x == y))

# Returns False as x is None
x = None
print(bool(x))

# Returns False as x is an empty sequence
x = ()
print(bool(x))

# Returns False as x is an empty mapping
x = {}
print(bool(x))

# Returns False as x is 0
x = 0.0
print(bool(x))

# Returns True as x is a non empty string
x = 'GeeksforGeeks'
print(bool(x))

# ----------------------------------------------------------------------------------------

def check(num):
    return(bool(num % 2 == 0))
 
# Driver Code
num = 8
if(check(num)):
    print("Even")
else:
    print("Odd")


# ------------------------------------------------------------------------------------------

user_input = bool(input("Are you hungry? True or false: "))
if user_input == "True":
    print(" You need to eat some foods ")
else:
    print("Let's go for walk")
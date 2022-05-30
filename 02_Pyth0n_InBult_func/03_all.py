
# *all in-built function


# *Examole_01
# All elements of list are true
l = [5, 6, 3 ,6]
print(all(l))

# All elements of list are false
l = [0, 0, False]
print(all(l))

# Some elements of list are
# true while others are false
l = [1, 0, 6, 7, False]
print(all(l))

# Empty List
l = []
print(all(l))
print("")


# *Example_02

# All elements of tuple are true
t = (2, 4, 6)
print(all(t))
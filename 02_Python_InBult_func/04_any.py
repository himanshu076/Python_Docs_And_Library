
# All elements of list are true
l = [ 4, 5, 1]
print(any( l ))
 
# All elements of list are false
l = [ 0, 0, False]
print(any( l ))
 
# Some elements of list are
# true while others are false
l = [ 1, 0, 6, 7, False]
print(any( l ))
 
# Empty List
l = []
print(any( l ))


# initializing list
test_list = [4, 5, 8, 9, 10, 17]
 
# printing list
print("The original list : " + str(test_list))
 
# Check if any element in list satisfies a condition
# Using any()
res = any(ele > 10 for ele in test_list)
 
# Printing result
print("Does any element satisfy specified condition ? : " + str(res))
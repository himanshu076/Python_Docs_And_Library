
# Exercise 1: Calculate the multiplication and sum of two numbers -
# *Q1. Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
# *solutions :
# class MultiplicationOrSum:
#     def multi_sum(num1, num2):
#         if num1 * num2 <= 1000:
#             print(num1 * num2)
#         else:
#             print(num1 + num2)

# MultiplicationOrSum.multi_sum(20, 30)
# MultiplicationOrSum.multi_sum(40, 30)


# ************************************************************************************
# Exercise 2: Print the sum of the current number and the previous number
# *Q2. Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
# *Solutions :
# class AddCurrentAndPrevious:
#     def add_num(self, num1, num2):
#         return num1 + num2

#     def iterate_in_range(self, n):
#         c = 0
#         for i in range(0, n):
#             sum = self.add_num(c, i)
#             print(f"Current Number {i} Previous Number  {c}  Sum: {sum}")
#             c = i


# AddCurrentAndPrevious().iterate_in_range(10)


# ************************************************************************************
# Exercise 3: Print characters from a string that are present at an even index number
# *@3. Write a program to accept a string from the user and display characters that are present at an even index number.
# *Solutions :
# *Method : 1
# class EvenString:
#     def strin(char="kishorpal"):
#         for i in range(0, len(char), 2):
#             print(char[i])

# str1 = input()
# EvenString.strin(str1)

# class EvenString:
#     def word(char):
#         l = char[0::2]
#         for i in l:
#             print(i)

# str1 = input()
# EvenString.word(str1)


# ************************************************************************************

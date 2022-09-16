
# * Class Methos -

class geeks:
	course = 'DSA'

	def purchase(self):
		print("Puchase course : ", self.course)


# geeks.purchase = classmethod(geeks.purchase)
# geeks.purchase()

# Python program to understand the classmethod

class Student:

	# create a variable
	name = "Geeksforgeeks"

	# create a function
	def print_name(obj):
		print("The name is : ", obj.name)


# create print_name classmethod
# before creating this line print_name()
# It can be called only with object not with class
Student.print_name = classmethod(Student.print_name)

# now this method can be called as classmethod
# print_name() method is called a class method
# Student.print_name()



# Python program to demonstrate
# use of a class method and static method.
from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a
	# Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a
	# Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))


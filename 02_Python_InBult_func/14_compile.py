
# *Python compile() function example

# *Example 1: Simple compile() example in Python.


# Python code to demonstrate working of compile().

# Creating sample sourcecode to multiply two variables
# x and y.
srcCode = 'x = 10\ny = 20\nmul = x * y\nprint("mul =", mul)'

# Converting above source code to an executable
execCode = compile(srcCode, 'mulstring', 'exec')

# Running the executable code.
# print(type(execCode))
# exec(execCode)


# *Example 2:  Another demonstration working of compile

# Another Python code to demonstrate working of compile().
x = 50

# Note eval is used for single statement
a = compile('x', 'test', 'single')
# print(type(a))
# exec(a)

# *Example 3: Python compile function from file
# reading code from a file
f = open('main.py', 'r')
temp = f.read()
f.close()

code = compile(temp, 'main.py', 'exec')
# exec(code)






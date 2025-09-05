# Python Variables

'''
On this third day of my 100 days of code, I will be looking at variables in python.
By the end, we should know what variables are and some rules regarding choice of variable names and
see some variables in action.
'''

# What is a Variable in Python?
'''
A variable can only be describled for best understanding. Here's how I understand it, imaging you want
to drink water and you are at the tap to get water. What do you look for next? You guessed it right.
Something with which to fetch the water from the tap. Let's call it a CONTAINER and the water here
represents DATA (DATA TYPES). 

So, a variable is where we put(store) the data we are using in a python program for ease of access and operation.

When a value or data is not in a variable it is said to be explicitly defined. Example, print(4).
'''

# Naming varables
'''
Just like we have names for different containers we use in fetching water like cup, gallon etc.In python, 
variables are also named and there are some rules to observe when chosing variable names. It is important
to note that python is dynamically typed i.e. at every operation the latest version of a variable is used.
'''

# Rule 1: A variable cannot be named using a python keyword (these are words that python is using at its core)
# example, words like class, pass etc cannot be used alone as a variable name in python.

# Rule 2: A variable name cannot start with a number or symbols except the underscore symbol. 
# Rule 3: A variable name can contain alphabets and numbers and the underscore symbol.
# Rule 4: Variable names are case sensitive. So, "name" is not the same as "Name" in python.
# Rule 5: Values are assigned to variables usin the assignment operator =

# Using variables
'''
At this point let us see how variables are used to make our coding experience more pleasant.
'''

print(4) # This is explicit definition of a value or data.

print('==============\n') # Note that I am using the print and that is not a variable but 
# an inbuilt function of python used to display results of our code.
x = 3
print(x)

print ('================\n')

name = 'Uchechukwu Bright Ohajuru'
print(name)

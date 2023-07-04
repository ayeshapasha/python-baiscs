#!/usr/bin/env python
# coding: utf-8

# In[1]:


# integer
a=5
print(type(a))


# ### Floats
# 
# Float literals can be created by adding a decimal component to a number.

# In[2]:


# Float
b=5.5
print(type(b))


# ### Complex
# 
# Complex literals can be created by using the notation x + yj where x is the real component and y is the imaginary component.

# In[3]:


# Complex
c= 2+1j
print(type(c))


# In[4]:


print(c.real, c.imag)


# In[5]:


print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a//2)  # Floor division #  it will find out the integer value smaller than the quotient

print(a**3) # exponent


# ### Variable assignment
# 
# 
# 
# A variable in Python is defined through assignment. There is no concept of declaring a variable outside of that assignment.

# In[1]:


numbers = 2

A = 5

B = 6

C = print(A/B)


# In[7]:


x = 2
y = 5


# In[8]:


x+y


# # String

# 
# String literals can be defined with any of single quotes ('), double quotes ("). All give the same result with two important differences.
# 
# - If you quote with single quotes, you do not have to escape double quotes and vice-versa.
# - If you quote with triple quotes, your string can span multiple lines.

# In[9]:


# string
name = 'my name is animesh'
type(name)
name


# In[10]:


"double quotes"


# In[11]:


# If you want to wrap a lot of other qouotes

" wrap lot's of other quotes too"


# ## Operations on string 

# In[12]:


s = 'I am your instructor'


# In[13]:


# reversing the string 
s[::-1]


# In[14]:


# Indexing in string

s[0]


# In[ ]:


# Grab everything UP TO the 3rd index
s[:3]


# In[ ]:


#Everything
s[:]


# In[ ]:


# Upper Case a string
s.upper()


# In[ ]:


# Lower case
s.lower()


# In[ ]:


# Split a string by blank space (this is the default)
s.split()


# In[ ]:


# Join operation
b = s.split()
' '.join(b)


# In[ ]:


# Concatenate strings!
s + ' in this research project'


# In[ ]:


s.count('o')


# In[ ]:


# .islower() will return True is it's lowercase similarly for upper case

s.islower()


# In[ ]:


# to find if there are digits in the string

s.isdigit()


# In[ ]:


a = '2353'
a.isdigit()


# In[ ]:


#### Summary 


# In[ ]:


string="welcome to spartificial"
print(len(string))
print(string.capitalize())
print(string.upper())
print(string.lower())
print(string.replace('e','2'))


# # Printing

# In[ ]:


x = 'hello'


# In[ ]:


x


# In[ ]:


print(x)


# In[ ]:


num = 12
name = 'animesh'


# In[ ]:


# using .format()
print('My number is: {one}, and my name is: {two}'.format(one=num,two=name))


# In[ ]:


print('My number is: {}, and my name is: {}'.format(num,name))


# In[ ]:


# Printing using f string method

name = 'Animesh'
age = 25
print(f"Hello, My name is {name} and I'm {age} years old.")


# # List

# Earlier, while discussing introduction to strings we have introduced the concept of a *sequence* in Python. 
# 
# In Python, Lists can be considered as the most general version of a "sequence". Unlike strings, they are mutable which means the elements inside a list can be changed!
# 
# Lists are constructed with brackets [] and commas separating every element in the list.
# 
# Let's go ahead and see how we can construct lists!

# 1 - Dimensional data structure / container
# 
# There is no limitation on data type - a list can store integer, string, boolean and so on
# 
# Every data type is preserved - there is no forced type casting that happens

# In[ ]:


# Assign a list to an variable named my_list
my_list = [1,2,3]


# We just created a list of integers, but lists can actually hold different object types. For example:

# In[ ]:


my_list2 = ['A string',23,100.232,'o']


# In[ ]:


# Length of string

len(my_list2)


# ### Indexing and Slicing
# 
# Indexing and slicing of lists works just like in Strings. Let's make a new list to remind ourselves of how this works:

# In[ ]:


mylist = [10,10.3,"Abc", "Spartificial",True]


# In[ ]:


# Grab element at index 0
mylist[0]


# In[ ]:


# Grab index 1 and everything past it
mylist[1:]


# In[ ]:


# Grab everything UP TO index 3
mylist[:3]


# In[ ]:


# Concatination in list 

# We can also use "+" to concatenate lists, just like we did for Strings.

mylist + ['new item',5]


# But this actually does not change the original list:
# 
# To make the changes in the original list we have to reassign the list
# 

# In[ ]:


mylist


# In[ ]:


mylist = mylist + ['new item',5]


# In[ ]:


mylist


# In[ ]:


# Make the list double
mylist * 2


# In[ ]:


# Doubling is also not parmanent 
mylist


# In[ ]:


# List can have list inside of a list also 
l = ['hi',1,[1,2]]
l


# ## Basic List Methods
# 
# If you are familiar with another programming language, start to draw parallels between lists in Python and arrays in other language. There are two reasons which tells why the lists in Python are more flexible than arrays in other programming language:
# 
# a. They have no fixed size (which means we need not to specify how big the list will be)
# b. They have no fixed type constraint 
# 
# Let's go ahead and explore some more special methods for lists:

# In[ ]:


# defining a emplty list

#method 1

l = []

#method 2

l = list()

l


# In[ ]:


# defining a list

l = [1,2,3,4,5]


# In[ ]:


# Use the .append() method to permanently add an item to the end of a list:

l.append(10)


# In[ ]:


l


# In[ ]:


# use .pop() method to remove last element from the list

l.pop()


# In[ ]:


l


# In[ ]:


# Pop off the 0 indexed item
l.pop(0)


# In[ ]:


l


# In[ ]:


help(l)


# In[ ]:


dir(l)


# In[ ]:


l


# In[ ]:


# to remove an element
l.remove(2)


# In[ ]:


l


# In[ ]:


l = [2,5,4,3,6,9,7]

# sort the list 
l.sort()
l


# In[ ]:


# to reverse the list
l.reverse()


# In[ ]:


l


# ### Nesting Lists
# 
# Nesting Lists is one of the great features in Python data structures. Nesting Lists means we can have data structures within data structures.
# 
# For example: A list inside a list.
# 
# Let's see how Nesting lists works!

# In[1]:


# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]


# In[2]:


matrix


# In[3]:


nest = [1,2,3,[4,5,['target']]]


# In[4]:


nest[3]


# In[5]:


nest[3][2][0]


# extend: extends list by appending elements from the iterable

# In[6]:


x = [1, 2, 3]
x.extend('ty')
print(x)


# In[ ]:


mylist


# In[ ]:


# Performing mutation operation on list

# When the values can change [MUtable data type] - Add, Remove, Reassign element

mylist[0] = 1000
mylist


# In[ ]:


### Summary


# In[7]:


lst=["Research","Machine Learning", "Python"]
print("List :", lst)
print("Concatenated list", lst+["Julia", "Hadoop", "R"])
print("Repeated List : ", lst * 2)
print("Is Sales a memeber of the list", 'Sales' in lst)
print("The zeroth element of the list is ", lst[0])
print("Slice", lst[0:2])


# In[8]:


lst=["Fruits","Juice","Draw cash","Fruits","Juice", "Clothes", "utensils","Draw cash", "Clothes", "utensils","Draw cash"]
lst.append("Call sister")
del(lst[0])
del(lst[2])
lst[0]="Water Melon"
print(lst)
del(lst[2:5])

print(lst)


# In[ ]:


lst=[0,1,2,3,4,5]
print(lst)
lst.append(6)
print(lst)
lst2=[7,8]
lst.append(lst2)
print(lst)
lst3=[9,10]
lst.extend(lst3)
print(lst)
lst.insert(1,0.5)
print(lst)
del(lst[1])
print(lst)
print(lst[::-1])
print(lst[::-2])
print(lst[::-3])


# # Dictionaries
# 
# We have learned about "Sequences" in the previous session. Now, let's switch the gears and learn about "mappings" in Python. These dictionaries are nothing but hash tables in other programming languages.
# 
# In this section, we will learn briefly about an introduction to dictionaries and what it consists of:
# 
#     1.) Constructing a Dictionary
#     2.) Accessing objects from a Dictionary
#     3.) Nesting Dictionaries
#     4.) Basic Dictionary Methods
# 
# Before we dive deep into this concept, let's understand what are Mappings? 
# 
# Mappings are a collection of objects that are stored by a "key". Unlike a sequence, mapping store objects by their relative position. This is an important distinction since mappings won't retain the order since they have objects defined by a key.
# 
# A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.
# 
# 
# ## Constructing a Dictionary
# Let's see how we can construct dictionaries to get a better understanding of how they work!

# In[ ]:


# Can we convert 2 lists into dictionary
# When ? 
# can we do it? 
# One of the list should have unique values so that I can make that Key
# two lists should be of equal length
mylist1 = [10,15,20,30] # Key
mylist2 = ['a','b','c','d'] # value

mydict = dict(zip(mylist2,mylist1))


# In[ ]:


mydict


# In[ ]:


# Call values by their key
mydict['b']


# In[ ]:


# Dictionaries are very flexible in the data types they can hold. For example

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}


# In[ ]:


#Let's call items from the dictionary
my_dict['key2'][2]


# In[ ]:


# Can call an index on that value
my_dict['key3'][0]


# In[ ]:


#Can then even call methods on that value
my_dict['key3'][0].upper()


# In[ ]:


# We can effect the values of a key as well. For instance:

my_dict['key1']


# In[ ]:


# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123

#Check
my_dict['key1']


# We can also create keys by assignment. For instance if we started off with an empty dictionary, we could continually add to it:

# In[ ]:


# Create a new dictionary
d = {}
type(d)


# In[ ]:


# Create a new key through assignment
d['animal'] = 'xyz'
d


# In[ ]:


# Can do this with any object
d['answer'] = 42


# In[ ]:


d


# In[ ]:


# access values
d.values()


# In[ ]:


# accessing keys

d.keys()


# In[ ]:


mydict


# In[ ]:


# returning all the values key values as list
# Method to return a list of all keys 
f= mydict.keys()
list(f)


# In[ ]:


# Method to return tuples of all items  (we'll learn about tuples soon)
mydict.items()


# In[ ]:


# Performing operations on dictonaries
# pop

mydict.pop('a')


# In[ ]:


mydict


# In[ ]:


# update value

mydict.update({'b':50})


# In[ ]:


mydict


# In[ ]:


help(mydict)


# In[ ]:


### Summary


# In[ ]:


Scores={"Sachin":100, "Dhoni":52}
print(Scores)
Scores["Sachin"]+=6
print(Scores["Sachin"])
Scores["Kapil"]=80
print(Scores)
print(Scores.keys())
print(Scores.values())
print(Scores.items())
s=str(Scores)
print(type(s))
for player in Scores.keys():
    print (player,Scores[player])
Scores.get("Sachin")
newscores=Scores.copy()
newscores["Sehwag"]=40
Scores.clear()
print(Scores)


# # Booleans

# Boolean expressions are created with the keywords and, or, not and is. For example:

# In[ ]:


a=True
b=False
print(a,b)


# # Tuples

# # Tuples
# 
# In Python, tuples are similar to lists but they are immutable i.e. they cannot be changed. You would use the tuples to present data that shouldn't be changed, such as days of week or dates on  a calendar.
# 
# In this section, we will get a brief overview of the following key topics:
# 
#     1.) Constructing Tuples
#     2.) Basic Tuple Methods
#     3.) Immutability
#     4.) When to Use Tuples
# 
# You'll have an intuition of how to use tuples based on what you've learned about lists. But, Tuples work very similar to lists but the  major difference is tuples are immutable.
# 
# ## Constructing Tuples
# 
# The construction of tuples use () with elements separated by commas where in the arguments will be passed within brackets. For example:

# In[ ]:


# Can create a tuple with mixed types
t = (1,2,3)


# In[ ]:


# Slicing just like a list
t[-1]


# In[ ]:


# Use .count to count the number of times a value appears
t.count('one')


# ### Immutability
# 
# As tuples are immutable, it can't be stressed enough and add more into it. To drive that point home:

# In[ ]:


t[0]= 'change'


# In[ ]:


t.append('nope')


# ## When to use Tuples
# 
# You may be wondering, "Why to bother using tuples when they have a few available methods?" 
# 
# Tuples are not used often as lists in programming but are used when immutability is necessary. While you are passing around an object and if you need to make sure that it does not get changed then tuple become your solution. It provides a convenient source of data integrity.
# 
# You should now be able to create and use tuples in your programming as well as have a complete understanding of their immutability.

# In[ ]:


### Summary


# In[ ]:


t=("c","c++","c#","java", "python")
print(len(t))
print(max(t))
print(min(t))
print(t*3)
print("python" in t)
print(sorted(t))
print(t[::-1])


# In[ ]:


t=(0,1,3,4,5)
print(t)
t=t[:2]+(2,)+t[2:]
print(t)
t=t[:len(t)]+(6,)
print(t)
t=t[:2]+("two",)+t[2:]
print(t)
t=t[:2]+t[3:]
print(t)


# In[ ]:


matrix=(['00','01','02'],[10,11,12],[20,21,22])
matrix[0][0]=100
print(matrix)
matrix[0][1]=[100,111,222]
print(matrix)


# # Sets

# Sets are an unordered collection of unique elements which can be constructed using the set() function.
# 
# Let's go ahead and create a set to see how it works.

# In[ ]:


x = set()


# In[ ]:


# We add to sets with the add() method
x.add(3)


# In[ ]:


x


# Note that the curly brackets do not indicate a dictionary! Using only keys, you can draw analogies as a set being a dictionary.
# 
# We know that a set has an only unique entry. Now, let us see what happens when we try to add something more that is already present in a set?

# In[ ]:


# Add a different element
x.add(2)


# In[ ]:


x


# In[ ]:


# Create a list with repeats
l = [1,1,2,2,3,4,5,6,1,1]


# In[ ]:


# Cast as set to get unique values
set(l)


# In[ ]:


a={1,2,3,4,5,6,6,7}


# In[ ]:


a.remove(7)
a


# In[ ]:


b={1,2,3}
b.issubset(a)


# In[ ]:


a.union(b)


# # Comparison Operators

# In[ ]:


a = 2
b = 10


# In[ ]:


a  > b


# In[ ]:


a < b


# In[ ]:


a == b


# In[ ]:


a != b


# In[ ]:


a >= b


# In[ ]:


a <= b


# In[ ]:


'hi' == 'bye'


# ### Logic Operators

# In[ ]:


(1 > 2) and (2 < 3)


# In[ ]:


(1 == 2) or (2 == 3) or (4 == 4)


# In[ ]:


(1 > 2) or (2 < 3)


# In[ ]:


# Membership operators -- in / not in
"Animesh" in [10,20,30,40,50,"Animesh"]


# In[ ]:


## Summary 


# In[ ]:


# Conditional Statements using Comparison and Logical Operator
a = 5
b = 10
c =5

if (a > 5):
    print("a > 5")
    if(a == c):
        print("a=c")
elif (a < 5):
    print("a <5")
    if(a == c):
        print("a=c")
else:
    print("a = 5")
    if(a == c):
        print("a=c")


# # Input

# This is how we take any input 

# In[ ]:


a = input('Enter a number') # It alwasy gives output as string


# In[ ]:


a


# In[ ]:


# How do I take multiple inputs

key_input = input("Enter the values separated by ,")


# In[ ]:


key_input


# In[ ]:


input_numbers = key_input.split(',')
input_numbers


# In[ ]:


nums = [int(num) for num in input_numbers]


# In[ ]:


nums


# # if,elif, else Statements

# In[ ]:


if 1 < 2:
    print('Yep!')


# In[ ]:


if 1 < 2:
    print('yep!')


# In[ ]:


if 1 < 2:
    print('first')
else:
    print('last')


# In[ ]:


if 1 > 2:
    print('first')
else:
    print('last')


# In[ ]:


if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')


# In[ ]:


a=int(input('Enter a number '))
b=int(input('Enter a number '))
if a>b:
    print(a)
elif b>a:
    print(b)


# In[ ]:


for i in range(int(input("Enter a number"))):
    print(i,end=' ')
    


# In[ ]:


for i in range(int(input("Enter a number"))):
    print(i)
else:
    print('Loop executed without any breaks')


# In[ ]:


# Let's take an assignment
mylist1 = [8,9,10,11,14,"animesh",20,21,22,23,27]

# I want you to print only even elements :

# I want you to create another list with the even numbers

mylist2 = []
for elem in mylist1:
    if(type(elem) == int):
    
        if(elem%2 == 0):
            print(elem)
            mylist2.append(elem)


# In[ ]:


mylist2


# # LOOPS
# 
# 
# In general, statements are executed sequentially: The first statement in a function is executed first, followed by the second, and so on. There may be a situation when you need to execute a block of code several number of times.
# 
# Programming languages provide various control structures that allow for more complicated execution paths.

# ## FOR Loop

# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.
# 
# Loop continues until we reach the last item in the sequence. The body of for loop is separated from the rest of the code using indentation.
# 

# In[ ]:


seq = [1,2,3,4,5]

for item in seq:
    print(item)


# In[ ]:


# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = ["Fsdfsf","fsdfs","sdffsfs"]

# variable to store the sum
summ=''

# iterate over the list
for x in numbers:
    summ = summ+x

# Output: The sum is
print(summ)


# ### for loop with else
# A for loop can have an optional else block as well. The else part is executed if the items in the sequence used in for loop exhausts.
# 
# break statement can be used to stop a for loop. In such case, the else part is ignored.
# 
# Hence, a for loop's else part runs if no break occurs.
# 
# Here is an example to illustrate this.

# In[ ]:


digits = [0, 1, 5]

for sfdsf in [0,1,2,3]:
    if sfdsf == 3:
        break
else:
    print("No items left.")
print("Fsdfsfsf")


# ## While loop
# 
# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
# 
# We generally use this loop when we don't know beforehand, the number of times to iterate.
# 
# In while loop, test expression is checked first. The body of the loop is entered only if the test_expression evaluates to True. After one iteration, the test expression is checked again. This process continues until the test_expression evaluates to False.
# 
# In Python, the body of the while loop is determined through indentation.
# 
# Body starts with indentation and the first unindented line marks the end.
# 
# Python interprets any non-zero value as True. None and 0 are interpreted as False.

# In[ ]:


i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1


# In[ ]:


# Program to add natural
# numbers upto 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)


# # The range() function
# 
# 
# We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).
# 
# We can also define the start, stop and step size as range(start,stop,step size). step size defaults to 1 if not provided.
# 
# This function does not store all the values in memory, it would be inefficient. So it remembers the start, stop, step size and generates the next number on the go.
# 
# To force this function to output all the items, we can use the function list().
# 
# The following example will clarify this.

# In[ ]:


range(6)


# In[ ]:


list(range(10))


# In[ ]:


print(list(range(8, 2,-2)))


# In[ ]:


print(list(range(2, 20, 5)))


# We can use the range() function in for loops to iterate through a sequence of numbers. It can be combined with the len() function to iterate though a sequence using indexing. Here is an example.

# In[ ]:


# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz','sapna']

# iterate over the list using index
for i in range(len(genre)-1,0,-2):
    print("I like", genre[i])


# # list comprehension

# In[ ]:


x = [1,2,3,4]

out = []
for item in x:
    out.append(item**2)
print(out)


# In[ ]:


[item**2 for item in x]


# # Functions

# #### Functions --- PYTHON built-in functions
# #### User defined function

# **So what is a function?**
# 
# A function groups a set of statements together to run the statements more than once. It allows us to specify parameters that can serve as inputs to the functions.
# 
# Functions allow us to reuse the code instead of writing the code again and again. If you recall strings and lists, remember that len() function is used to find the length of a string. Since checking the length of a sequence is a common task, you would want to write a function that can do this repeatedly at command.
# 
# Function is one of the most basic levels of reusing code in Python, and it will also allow us to start thinking of program design.

# ## def Statements
# 
# Now, let us learn how to build a function and what is the syntax in Python.
# 
# The syntax for def statements will be in the following form:

# In[ ]:


def name_of_function(arg1,arg2):
    '''
    This is where the function's Document String (doc-string) goes
    '''
    # Do stuff here
    #return desired result


# We begin with def then a space followed by the name of the function. Try to keep names relevant and simple as possible, for example, len() is a good name for a length() function. Also be careful with names, you wouldn't want to call a function the same name as a [built-in function in Python](https://docs.python.org/2/library/functions.html) (such as len).
# 
# Next, comes the number of arguments separated by a comma within a pair of parenthesis which acts as input to the defined function,  reference them and the function definition with a colon.  
# 
# Here comes the important step to indent to begin the code inside the defined functions properly. Also remember, Python makes use of *whitespace* to organize code and lot of other programming languages do not do this.
# 
# Next, you'll see the doc-string where you write the basic description of the function. Using iPython and iPython Notebooks, you'll be able to read these doc-strings by pressing Shift+Tab after a function name. It is not mandatory to include docstrings with simple functions, but it is a good practice to put them as this will help the programmers to easily understand the code you write.
# 
# After all this, you can begin writing the code you wish to execute.
# 
# The best way to learn functions is by going through examples. So let's try to analyze and understand examples that relate back to the various objects and data structures we learned.

# ## Example 1: Simple print hello function

# In[ ]:


def say_hello():
    print('hello')


# In[ ]:


# call the function

say_hello()


# ### Example 2: A simple greeting function
# Let's write a function that greets people with their name.

# In[ ]:


def greeting(name):
    print('Hello %d' %name)


# In[ ]:


x = greeting(90)


# ## Using return
# Let's see some examples that use a return statement. Return allows a function to "return" a result that can then be stored as a variable, or used in whatever manner a user wants.
# 
# ### Example 3: Addition function

# In[ ]:


def add_num(num1,num2):
    return num1+num2


# In[ ]:


add_num(4,5)


# In[ ]:


# Can also save as variable due to return
result = add_num(4,5)
result


# In[ ]:


print(result)


# In[ ]:


# What if we inter two different things

print(add_num('one',1))


# In Python we don't declare variable types, this function could be used to add numbers or sequences together! Going forward, We'll learn about adding in checks to make sure a user puts in the correct arguments into a function.
# 
# Let's also start using *break*,*continue*, and *pass* statements in our code. We introduced these during the while lecture.

# ### Break
# 
# The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.
# 
# If break statement is inside a nested loop (loop inside another loop), break will terminate the innermost loop.

# In[ ]:


def is_prime(num):
    '''
    Naive method of checking for primes. 
    '''
    for n in range(2,num):
        if num % n == 0:
            print('not prime')
            break
    else: # If never mod zero, then prime
        print('prime')


# In[ ]:


is_prime(17)


# ### continue
# The continue statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.

# In[ ]:


# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")


# # Map Function

# The **map** function allows you to "map" a function to an iterable object. That is to say you can quickly call the same function to every item in an iterable, such as a list. For example:

# In[ ]:


def square(num):
    return num**2


# In[ ]:


my_nums = [1,2,3,4,5]


# In[ ]:


map(square,my_nums)


# In[ ]:


# To get the results, either iterate through map() 
# or just cast to a list

list(map(square,my_nums))


# In[ ]:


# Example 2: More complex

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]


# In[ ]:


mynames = ['John','Cindy','Sarah','Kelly','Mike']


# In[ ]:


list(map(splicer,mynames))


# ## filter function
# 
# The filter function returns an iterator yielding those items of iterable for which function(item)
# is true. Meaning you need to filter by a function that returns either True or False. Then passing that into filter (along with your iterable) and you will get back only the results that would return True when passed to the function.

# In[ ]:


def check_even(num):
    return num % 2 == 0 


# In[ ]:


nums = [0,1,2,3,4,5,6,7,8,9,10]


# In[ ]:


filter(check_even,nums)


# In[ ]:


list(filter(check_even,nums))


# ## lambda expression
# 
# One of Pythons most useful (and for beginners, confusing) tools is the lambda expression. lambda expressions allow us to create "anonymous" functions. This basically means we can quickly make ad-hoc functions without needing to properly define a function using def.
# 
# Function objects returned by running lambda expressions work exactly the same as those created and assigned by defs. There is key difference that makes lambda useful in specialized roles:
# 
# **lambda's body is a single expression, not a block of statements.**
# 
# * The lambda's body is similar to what we would put in a def body's return statement. We simply type the result as an expression instead of explicitly returning it. Because it is limited to an expression, a lambda is less general that a def. We can only squeeze design, to limit program nesting. lambda is designed for coding simple functions, and def handles the larger tasks.

# Lets slowly break down a lambda expression by deconstructing a function:

# In[ ]:


def square(num):
    result = num**2
    return result


# In[ ]:


square(6)


# We could simplify it:

# In[ ]:


def square(num):
    return num**2


# In[ ]:


square(5)


# We could actually even write this all on one line.

# In[ ]:


def square(num): return num**2


# In[ ]:


square(6)


# This is the form a function that a lambda expression intends to replicate. A lambda expression can then be written as:

# In[ ]:


lambda num: num ** 2


# In[ ]:


# You wouldn't usually assign a name to a lambda expression, this is just for demonstration!
square = lambda num: num **2


# In[ ]:


square(2)


# **So why would use this?**
# 
# Many function calls need a function passed in, such as map and filter. Often you only need to use the function you are passing in once, so instead of formally defining it, you just use the lambda expression. Let's repeat some of the examples from above with a lambda expression

# In[ ]:


list(map(lambda num: num ** 2, my_nums))


# In[ ]:


list(filter(lambda n: n % 2 == 0,nums))


# In[ ]:


# Example summary
ssum = lambda x,y : x + y
ssum(3,4)


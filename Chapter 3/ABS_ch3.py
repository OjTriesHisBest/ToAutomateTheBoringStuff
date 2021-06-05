# Automate the boring stuff Chapter 3

def answer_1():
    print("Functions allow your code to be reuseable (meaning you don't need to duplicate it). As a result, it means your code is shorter, and easier to maintain.")

def answer_2():
    print("It executes when it is called. Defining says what it's going to do. Calling it runs the fuction.")

def answer_3():
    print("You start the fuction creation with 'def'. This can be viewed as short for define. In fact, if you look at the answer file for this workbook, you'll see a list of functons that start with 'def'. " )

def answer_4():
    print('''A function by itself contains the following: 
"def function():  <- def statement
        print("hello world")    <- The code to be executed"

The function call tells the program to execute the the code within the defined function. You need to include the brackets at the end otherwise you'll just be given a memory location.

Try running 'answer_4', then 'answer_4()' and see what the difference is.''')

def answer_5():
    print("There is one global scope and a local scope whenever a function is called. Can you explain what the difference is between global and local variables?")

def answer_6():
    print('''When a function is called, all of the local variables within the function are forgotten (or 'destroyed'). 
    
This means when you try to call them outside of this function, you'll encounter an error. What error is mentioned when you do this?''')

def answer_7():
    print('''A return value is whatever the fuction evaluates the code to. Yes a return value can be part of an expression.''')

def answer_8():
    print("The return value is 'None'.")

def answer_9():
    print('''A global statement will make a variable in the function refer to (or create) the global variable.
    
If this is still a little confusing, here's an alternative explanation:

Python global keyword: https://www.programiz.com/python-programming/global-keyword''')

def answer_10():
    print('''"None" has the type of "NoneType". This points to a null value. In Python, this is different from '0'. 

Interestingly, 'print()' has no return value by itself and won't actually print 'None' explicitly. Try the following two commands: 

print()
print(print())

The second will show that print() returns None. You don't need to remember this, it's just interesting. To me, at least.''')

def answer_11():
    print("It imports a modue named areallyourpetsnamederic. This isn't a real module. It gives you access to all of the functions, and other code within a document. As your code becomes more complex, you'll be importing modules frequently.")

def answer_12():
    print('''You would do this by typing spam.bacon(). 

You can also rename modules by saying import spam as sp. Then you'll be able to write sp.bacon() instead. This can be helpful when module names are long. 

You can also just import particular functions so you don't need to refer to the module. How might you do that?''')

def answer_13():
    print('''You can place the expected code into a 'try' block so that if an error occurs, it skips over to the 'except' block.
    
Error handling here is often viewed as try/expect/finally blocks. What does a finally block do?''')

def answer_14():
    print('''The code that might cause an error goes into the try block. If you have code that executes when the error occurs, that would go into the except block.''')

def project_ch3():
    print('''Don't worry if this might have been confusing. Practice makes... better. 
    
This is the first part: 

number = int(input("Please enter a number:"))

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2 
    else:
        print(3*number+1)
        return 3*number+1

This function takes an argument and then asks of that argument, if it is even, print the result and return it (which means that you can access the result in a variable).

From the last chapter, you'll remember that int() changes the value to an integer where possible. Without it, the input will default to a string and from the *first* chapter - we can't do maths with a string! 

This is the second part: 
        
number = int(input("Please enter a number:"))
while number != 1:
    number = collatz(number)

This part put the function into a while loop. 
    
This is the third part: 

try: 
    number = int(input("Please enter a number:"))
except ValueError:
    print("Please input a valid integer")

while number != 1:
    number = collatz(number)
    
Now this just adds an error handler. For example, if you had written "puppy", you'll get a value error because it can't be changed into an integer. 

THE FINAL PROGRAM: 

# The function
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2 
    else:
        print(3*number+1)
        return 3*number+1

# The logic

try: 
    number = int(input("Please enter a number:"))
except ValueError:
    print("Please input a valid integer")

while number != 1:
    number = collatz(number)

There are other ways to write this though! That is the wonder of coding.''')

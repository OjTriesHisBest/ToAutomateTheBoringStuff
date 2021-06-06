#ABS_c2

import pandas as pd

def answer_1(): 
    print("'True' and 'False' are Boolean values. Be sure to write them with a capital letter.")

def answer_2(): 
    print("'AND', 'OR', 'NOT'")

def answer_3(): 
    combinations = ["T and T", "T and F", "F and T", "F and F"]

    and_dict = {"Combinations": combinations, "Final evaluation": ["T", "F", "F", "T"]}
    and_df = pd.DataFrame(and_dict)
    and_df = and_df.style.set_table_attributes("style='display:inline'").set_caption('AND boolean truth values')

    or_dict = {"Combinations": combinations, "Final evaluation": ["T", "T", "T", "F"]}
    or_df = pd.DataFrame(or_dict)
    or_df = or_df.style.set_table_attributes("style='display:inline'").set_caption('OR boolean truth values')

    not_dict = {"Combinations": ["Not True", "Not False"], "Final evaluation": ["F", "T"]}
    not_df = pd.DataFrame(not_dict)
    not_df = not_df.style.set_table_attributes("style='display:inline'").set_caption('NOT boolean truth values')

    return and_df, or_df, not_df

def answer_4(): 

    questions = ["(5 > 4) and (3 == 5)", "not (5 > 4)","(5 > 4) or (3 == 5)","not ((5 > 4) or (3 == 5))","(True and True) and (True == False)","(not False) or (not True)"]
    answers = ["F", "F", "T", "F", "F","T"]

    ans_4_df = pd.DataFrame({"Questions": questions, "Answers": answers})
    return ans_4_df

def answer_5(): 
    operators = ["==", "!=", "<", ">", "<=", ">="]
    meaning = ["Equal to", "Not equal to", "less than", "greater than", "less than or equal to", "greater than or equal to"]
    ans_5_df = pd.DataFrame({"Operators":operators, "Meaning":meaning})
    return ans_5_df

def answer_6():
    print('''The assignment operator (=) puts a value into a variable. The equal to operator (==) checks if the values on either side are the same. 
    
Try running 'six = 5' and 'six == 6' and see what the difference in the output is. Why are is six == 6 False?''')

def answer_7():
    print("Conditions are another name for expressions in the context of a flow statement. They evaluate down to a True or False value. Within a flow statement, you can make a decision based on the value of a condition (if x is True, do this. If x is False, do that instead.)")

def answer_8(): 
    print('''
    spam = 0
    if spam == 10:
        print('eggs')       <- Block 1 
        if spam > 5:
            print('bacon')  <- Block 2
        else:
            print('ham')    <- Block 3
        print('spam')
    print('spam')

Blocks begin when indentation increases and can contain other blocks.
    ''')

def answer_9():
    print('''
    if spam == 1: 
        print("Hello")
    elif spam == 2:
        print("Howdy")
    else:
        print("Greetings!")
        
You'll see that there are three blocks in this program and you have used if/elif/else to control what happens when you run the program and the equal to operator! This sort of control flow is fundamental to the running of many programs and can be made much more complex (which you will come to find out.)''')

def answer_10():
    print("Ctrl + C")
    print("This is known as a keyboard interrupt (which is what you'll see on the error message). There is a way to suppress these errors so they don't influence your code but you'll have to Google that. I fear you'll create a virus if I tell you. Though, now that I say this, you can very easily check yourself... well I've written it now and my backspace is conveniently broken.")

def answer_11():
    print('''The difference between break and continue: 
    
    Break exits the current loop. 
    Continue stops the current iteration of the loop and goes back to the start of the loop. 
    
    To visualise the difference, copy and run the code below:
    
    for i in range(10):    
        if i == 7:
            continue  
        print("The Number is :" , i)
    
Now replace continue with break - what is the difference?''')

def answer_12():
    print('''They all do exactly the same thing but utilise the arguments within the brackets differently. They all count from 0 up to 9.
    
    range(10) counts from 0 up to, but not including, 10.
    range(0, 10) starts explicitly at 0 and counts up to, but not including, 10.
    range(0, 10, 1) starts explicitly at 0, counts up to, but not including, 10 and does it in increments of 1. 
    
The reasons why they technically all do the same thing is because of default arguments. The default for the range function is to start at 0 and count in increments of 1.''')

def answer_13(): 
    print('''For-loop version: 
    
    for number in range(1,11):
        print(number)
        
While-loop version:
    
    number = 1
    while number <= 1:
        print(number)
        number = number + 1
        
Which version is easier for you to understand?''')

def answer_14():
    print("spam.bacon()")
    print("You can also rename modules when you import them or import the function directly. How would you do that?")

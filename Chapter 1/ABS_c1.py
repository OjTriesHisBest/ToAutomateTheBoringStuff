# Automate the boring stuff week 1

def answer_1():
    print(""" * , - , / , + are operators.\n\n "hello", -88.8, 5 are values (text, float, integer respectively).""")

def answer_2(): 
    print("spam without quotation marks is a variable. Though it isn't defined. In order for this to run, I had to assign it to 'None' - don't do this though.\n\n'spam' with single quotes is a string.")
spam = None

def answer_3():
    print("The correct answer is:\nFloating-point numbers (or floats)\nIntegers\nStrings")

def answer_4():
    print('''Expressions contain values (e.g. "2", "two") and operators(e.g. "*")
            
When put in the correct order, it evaluates the down to a single value. Similar to a normal sentence, you can have nouns and conjunctions to make a readable sentence. If you put them in the wrong order, you won't make sense!''')

def answer_5():
    print('''A statement contains three things: 1) a variable name, 2) an assingment operator (=), 3) a value to be stored.

An expression contains values and operators - it doesn't assign anything to anything else. you can assign an expression to a variable!''')

def answer_6(): 
    print('''The answer is 21!
    The argument essentially does this: 
    
    bacon = 20
    20 + 1
    21''')

def answer_7():
    print('''"spamspamspam" for both lines. 

You can apply operators to values of the same kind (strings and numbers). For strings, only * and + will work. Try spam**4, do you get an error?''')

def answer_8(): 
    print('''You can't make a variable a number. If this was possible, you'd never be able to use it anywhere else within your program. Which is  dangerous practice. 
    
You can however, use words or letters because you can differentiate between variable names and strings easily. There are some words you cannot assign values to (like "True = False" - though you used to be able to in previous versions of Python!)''')

def answer_9(): 
    print('''int()\nstr()\nfloat()''')

def answer_10():
    print('''The string and number are different data types. You cannot concatenate these.

You can try a few different ways to fix this: 

'I have eaten ' + '99' + ' burritos'

Google "f-strings": 

Num_burritos = 99
f'I have eaten {Num_burritos}' + ' burritos' ''')

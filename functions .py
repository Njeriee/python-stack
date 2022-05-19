# funtions in python can be empty or take in parameters as arguments.
# when we are unsure of the number of parameters to be passed to a function we use *args
# and **kwargs as the parameters when defining a function

# normal function that takes in one argument
def greet(name):
    print('Hello',name)

greet('Mary')

def addtwo(a,b):
    result = a+b
    print(result) 

addtwo(8,5)

# funtion with *args
def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)

# function with kwargs
def user(**data):
    for k, v in data.items():
        print(k,v)


user(fname = 'John', lname = 'doe',adress = '106 and park')
# lambda funtion
sqr = lambda x:x*x
print(sqr(2))

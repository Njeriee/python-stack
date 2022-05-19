# here is another function
def deco(func):
    def inner():
        print('Hi I am an inner function')
        func()
    return inner
@deco
def f2():
    print('I am another function and I can be accessed inside another function by passing me as a parameter')

f2()

# decorators with functions with parameters
# here we use *args and **kwargs to define parameters to be passed inside the functions for both the decorator function and the decorated function

def f3(func):
    def inner(*args, **kwargs):
        print('It all starts here')
        func(*args, **kwargs)
        print('It all ends here')
    return inner
@f3
def f4(a,b):
    sum = a + b
    print(sum)

f4(4,8)

# return value i.e the above decorated function instead of printing a value is returned
def f3(func):
    def inner(*args, **kwargs):
        print('It all starts here')
        val = func(*args, **kwargs)
        print('It all ends here')
        return val
    return inner
@f3
def f4(a,b):
    return a + b
    

f4(4,8)

# generators
# simple generator
def sqr_root(*nums):
    for i in nums:
        yield(i*i)

my_num = sqr_root(1,2,3,4,5,6,7,9)

for num in my_num:
    print (num)

my_num_list = [1,2,3,4,5,6,7,8,9,10]
# generetor expression
my_num2 = (i*i for i in my_num_list)
# this will return the generator object created
print(my_num2)

# to access the result
# this will return the first item in the list
print(next(my_num2))
# second item in the list
print(next(my_num2))
# third item in the list
print(next(my_num2))
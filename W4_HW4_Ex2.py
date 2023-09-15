
#Count Function Calls

from Ex1 import memoize


def count_calls(func):
    count = 0
    def inner(*args):
        nonlocal count #The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function. Use the keyword nonlocal to declare that the variable is not local.
        count += 1
        return func(*args)
    return inner


@count_calls
@memoize
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
       
    
print(fib(10))
print(fib(20))
print(fib(100))




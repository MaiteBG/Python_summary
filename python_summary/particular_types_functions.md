
#### [Return to README.md](../README.md)
# Particular types of functions

<!-- TOC -->
  * [1. Recursive functions](#1-recursive-functions)
  * [2. Nested functions](#2-nested-functions)
    * [2.1. Closure](#21-closure)
  * [3. Lambda Functions](#3-lambda-functions)
  * [4. Decorators (@func)](#4-decorators-func)
    * [4.1. Decorating with arguments](#41-decorating-with-arguments)
    * [4.2. Decorating a lambda function (indirectly)](#42-decorating-a-lambda-function-indirectly)
  * [5. Generator Function (`yield`)](#5-generator-function-yield)
    * [5.1. Generator expression (anonymous generator)](#51-generator-expression-anonymous-generator)
      * [5.1.1. Passing a Generator Expression to a Function](#511-passing-a-generator-expression-to-a-function)
<!-- TOC -->



## 1. Recursive functions
* Functions that call themselves.
* Must reach a base case to avoid infinite loops.

``` python
def function_recursiva(...):
    # Base case
    if condition:
        ...
    else:  # Recursive case
        ...
        function_recursiva(...)
```


## 2. Nested functions
* Functions defined inside other functions.
* Inner functions can access variables from the outer function (closure).
* If a helper function is only needed inside another function, nesting keeps it private and organized.
* Decorators often use nested functions to modify the behavior of other functions.
```python
def outer_function(...):
    # Outer function logic
    ...

    def inner_function(...):
        # Inner function logic
        ...

    # Call to inner function
    inner_function(...)
    ...
```

### 2.1. Closure
A **closure** is an inner function (can be a lambda function) that:
- Is defined inside another function (the enclosing function).
- **Refers to non-local variables from the environment** where it was created.
- Is returned or used outside its original scope, while still retaining access to those variables even after the outer function has finished executing.

``` python
def outer():
    x = 10
    def inner():
        return x  # x no es un parámetro ni está en inner
    return inner

f = outer()
print(f())  # Output: 10
```


## 3. Lambda Functions

Anonymous and small functions (one line of code). They can be directly assigned to a variable and called like a regular function with parameters in parentheses.
* Can be without arguments or with default arguments, variable-length parameters, etc.

`my_lambda_function = lambda arg1, arg2=1: arg1 + arg2`

**Nested Lambda Functions**

You can nest lambda functions inside other lambdas. This allows you to return a lambda from another lambda, or define compact logic in multiple layers.

```python
multiply = lambda x: (lambda y: x * y)
double = multiply(2)
print(double(5))  # Output: 10
```



## 4. Decorators (@func)
Decorators are special functions that modify or enhance the behavior of other functions or methods without changing their code. 
They take a function as input and return another function—usually a new one that adds extra behavior.
* Alwaysa a nested function.

 This is very useful for tasks like:
- Logging
- Measuring execution time
- Checking permissions
- Repeating or caching results


In this example, when we call say_name, we are calling greet_decorator with the say_name function as a parameter. This returns the wrapper function, which is the function that gets executed.
```python
def greet_decorator(func):
    def wrapper():
        print("Hello!") # Before function
        func()
        print("Goodbye!") # After function
    return wrapper  # Devuleve funcion decoradora

@greet_decorator
def say_name():
    print("My name is Alice")

say_name()
```

### 4.1. Decorating with arguments
```python
def decorador(func):
    def envoltura(*args, **kwargs):
        print("Before func call")
        resultado = func(*args, **kwargs)
        print("After func call")
        return resultado 
    return envoltura # decorador devuleve funcion decoradora
```

### 4.2. Decorating a lambda function (indirectly)
Decorating a lambda manually (not with @ syntax)

``` python
my_lambda = decorator_fun(lambda x: x + 3)
```


## 5. Generator Function (`yield`)

A generator function is any function that contains the `yield` keyword. Instead of returning a single value using `return`, it yields multiple values one at a time, pausing between each one.

The use of generators is more efficient in terms of memory and performance compared to other structures that return a complete list or set of results (such as list comprehensions), primarily due to their lazy evaluation.

```python
# Create a list of 1 million numbers (uses a lot of memory)
numbers_list = [i for i in range(10**6)]  # Using list comprehension
# Crear un generador que produce los mismos números (mucho menos uso de memoria)
generador = (i for i in range(10**6))
``` 

Basic Generator Example: 
```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```
* After the last value, it raises `StopIteration`.


### 5.1. Generator expression (anonymous generator)

When assigning a generator expression to a variable, you should enclose it in parentheses.


```python
squares = (value * value for value in range(4) )
print(squares)       # <generator object <genexpr> at 0x...>
print(next(squares)) #0
print(next(squares)) #1
print(next(squares)) #4
print(next(squares)) #9
```


#### 5.1.1. Passing a Generator Expression to a Function

You can also pass a generator expression directly to a function, without the need for parentheses.
```python
import math
sum_result = sum(value * value for value in range(4))
print(f'Result of sum: {sum_result}')  # 0 + 1 + 4 + 9 = 14
```
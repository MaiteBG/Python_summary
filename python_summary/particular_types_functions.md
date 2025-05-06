#### [Return to README.md](../README.md)

# Particular types of functions and Decorators

<!-- TOC -->
  * [1. Recursive functions](#1-recursive-functions)
  * [2. Nested functions](#2-nested-functions)
    * [2.1. Closure](#21-closure)
  * [3. Lambda Functions](#3-lambda-functions)
  * [4. Generator Function (`yield`)](#4-generator-function-yield)
    * [4.1. Generator expression (anonymous generator)](#41-generator-expression-anonymous-generator)
      * [4.1.1. Passing a Generator Expression to a Function](#411-passing-a-generator-expression-to-a-function)
  * [5. Decorators (@func)](#5-decorators-func)
    * [5.1. Decorating with arguments](#51-decorating-with-arguments)
    * [5.2. Decorating a lambda function (indirectly)](#52-decorating-a-lambda-function-indirectly)
    * [5.3. Class decorators](#53-class-decorators)
      * [5.3.1. Inspecting a Class and metaprogramacion - Especially for Decorators](#531-inspecting-a-class-and-metaprogramacion---especially-for-decorators)
    * [5.4. Multiple decorators](#54-multiple-decorators)
<!-- TOC -->

## 1. Recursive functions

* Functions that call themselves.
* Must reach a base case to avoid infinite loops.

```python
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

```python
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



## 4. Generator Function (`yield`)

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

### 4.1. Generator expression (anonymous generator)

When assigning a generator expression to a variable, you should enclose it in parentheses.

```python
squares = (value * value for value in range(4) )
print(squares)       # <generator object <genexpr> at 0x...>
print(next(squares)) #0
print(next(squares)) #1
print(next(squares)) #4
print(next(squares)) #9
```

#### 4.1.1. Passing a Generator Expression to a Function

You can also pass a generator expression directly to a function, without the need for parentheses.

```python
import math
sum_result = sum(value * value for value in range(4))
print(f'Result of sum: {sum_result}')  # 0 + 1 + 4 + 9 = 14
```


## 5. Decorators (@func)

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

### 5.1. Decorating with arguments

```python
def decorador(func):
    def envoltura(*args, **kwargs):
        print("Before func call")
        resultado = func(*args, **kwargs)
        print("After func call")
        return resultado 
    return envoltura # decorador devuleve funcion decoradora
```

### 5.2. Decorating a lambda function (indirectly)

Decorating a lambda manually (not with @ syntax)

```python
my_lambda = decorator_fun(lambda x: x + 3)
```

### 5.3. Class decorators

A class decorator works similarly to function decorators but is applied to classes.
Class decorators are applied after the class definition is created but before the class is fully used or instantiated (they mostly execute when we import the class).

* Class decorators allow us to enhance or modify class methods, instance creation, class-level attributes, etc.
* They always receive `def decor_func(cls)` as a parameter and must `return cls`.

```python
def decorador_repr(cls):
    print('1. Se ejecuta decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')
    return cls
  

@decorador_repr
class Persona:
    def __init__(self, nombre, apellido):
        print('2. Se ejecuta el inicializador al crear una instancia')
        self._nombre = nombre
        self._apellido = apellido
    ...
```


#### 5.3.1. Inspecting a Class and metaprogramming - Especially for Decorators

When a class decorator is applied, the class is already defined and available.
The code below demonstrates how to access class attributes and inspect the `__init__` method:


* **`vars(cls)`** retrieves the class's attributes.
* The check verifies if `__init__` exists in the class.
* It then uses `inspect.signature` to get the method signature of `__init__` and lists its parameters (excluding `self`).

This allows decorators to inspect and interact with the class definition, ensuring methods are correctly defined.

``` python
attributes = vars(cls)  # Gets the dictionary of class attributes

# Check if the class has an __init__ method
if '__init__' not in attributes:
    raise TypeError(f'{cls.__name__} has not overridden the __init__ method')

# Retrieve the parameters of the __init__ method, excluding 'self'
init_signature = inspect.signature(cls.__init__)
print(f'__init__ method signature: {init_signature}')
init_parameters = list(init_signature.parameters)[1:]

```
* **`isinstance(method, decorators)`**  actually checks if the method is an instance of the decorator class —
this only works if the decorator replaces the method with an instance of a class.

* `settattr(cls,outside_metohod_name ,decorator_method)`  assigns or overrides a method to the class.
* `inspect.getsource(...)`  retrieves the source code of the object (to be sure that is the wanted).

### 5.4. Multiple decorators

When you apply multiple decorators to a function, Python will apply them from bottom to top.
This means the decorator closest to the function is executed first, and the one farthest is executed last.
Each decorator takes the function from the previous one and may modify its behavior before passing it to the next.

```python
@decor1
@decor2
def method(...):
    pass
```

The execution will be `decor1(decor2(method()))`. Like MRO, all decorators must call the original function (passed as an argument) to execute the next decorator or the final method.

* In class decorators, each decorator must `return cls` (the class) to pass it to the next decorator. Each decorator wraps the class or function and modifies it before passing it to the next one.
  If a class decorator doesn’t return cls, the chain is also broken.


 retrieves the source code of the object. (to check outside)
#### [Return to README.md](../README.md)

# Functions and Functional Programming Concepts

<!-- TOC -->

  * [1. Functions](#1-functions)
    * [1.1. Function Parameters and Arguments](#11-function-parameters-and-arguments)
    * [1.2. Functions as First-Class Citizens](#12-functions-as-first-class-citizens)
    * [1.3. `inspect` and `__annotations__`to Understand Functions at Runtime](#13-inspect-and-__annotations__to-understand-functions-at-runtime)
  * [2. Recursive functions](#2-recursive-functions)
  * [3. Nested functions](#3-nested-functions)
    * [3.1. Closure](#31-closure)
  * [4. Lambda Functions](#4-lambda-functions)
  * [5. High order functions](#5-high-order-functions)
  * [6. Generator Function (`yield`)](#6-generator-function-yield)
    * [6.1. Generator expression (anonymous generator)](#61-generator-expression-anonymous-generator)
      * [6.1.1. Passing a Generator Expression to a Function](#611-passing-a-generator-expression-to-a-function)
  * [7. Decorators `@func`](#7-decorators-func)
    * [7.1. Multiple decorators](#71-multiple-decorators)
    * [7.2. Decorating with arguments](#72-decorating-with-arguments)
    * [7.3. Decorating a lambda function (indirectly)](#73-decorating-a-lambda-function-indirectly)
    * [7.4. Preserving metadata with `@wraps`](#74-preserving-metadata-with-wraps)
    * [7.5. `functools` in Decorators](#75-functools-in-decorators)
      * [7.5.1. Caching Function Results: `lru_cache`](#751-caching-function-results-lru_cache)
      * [7.5.2. Creating Functions with Predefined Parameters: `partial`](#752-creating-functions-with-predefined-parameters-partial)
<!-- TOC -->

## 1. Functions

```python
def nombre_funcion(param_1, param_2, ...):  # Function name like accion or verb
    ... # Function body
    return return_variable
```

A function always returns a value; if no return is specified, it returns `None`.”

### 1.1. Function Parameters and Arguments

> **Parameters** are the variables listed in the function definition and **arguments** are the actual values passed to the function when it is called.

* Parameters can have default values: `param = default_value`.
* Also, can include variable-length parameters:
  * `*args`: Receives multiple arguments as a tuple.
  * `**kwargs`: Receives keyword arguments as a dictionary.

Parameters must be specified in this order: `function(req_arg, default_arg="default", *args, **kwargs)`.

```python
# Function example
def example_function(req_arg, default_arg="default", *args, **kwargs):
    pass

# Calling the function
example_function(
    "value1",                      # req_arg
    "not_default",                 # default_arg
    "extra1", "extra2", "extra3",  # *args
    key1="val1", key2="val2"       # **kwargs
)
```

### 1.2. Functions as First-Class Citizens

In Python, functions are treated as first-class citizens. This means:

- Functions can be assigned to variables:

  ```python
  def add(x, y):
      return x + y

  my_add = add
  print(my_add(3, 4))  # Output: 7
  ```
- Functions can be passed as arguments:

  ```python
  def apply_func(func, value):
    return func(value)

  def increment(x):
      return x + 1

  print(apply_func(increment, 5))  # Output: 6
  ```
- Functions can return other functions:

  ```python
   def outer():
     def inner(x):
         return x + 1
     return inner

  add_one = outer()
  print(add_one(5))  # Output: 6
  ```
- When is it necessary to treat functions as first-class citizens?

  - When flexibility is needed to pass functions as arguments or return them from other functions.
  - In functional programming, where functions are passed, returned, and stored dynamically.
  - For creating higher-order functions, decorators, or event handlers.
  - When you need to modify behavior at runtime, like with callbacks or dynamic function generation.

> To know if an object is a function: `callabe(function)`
>
> * We can make an object callable adding to the object class the `__call__()` method.

### 1.3. Function Introspection (`ìnsepct` and `__annotations__`)

The `inspect` module in Python allows you to analyze functions at runtime.
It’s especially useful in metaprogramming, debugging, or building decorators, because it lets you explore a function’s structure—like its parameters, defaults, annotations, and even its source code.
With inspect, you can write code that adapts to other code.

* **Get a function’s signature and its parameters (`inspect.signature`):**
  See what arguments a function expects, including names, order, and defaults.
* **Check if something is a function (`inspect.isfunction`):**
  Returns `True` if the object is a user-defined function.
* **Get source code of the function (`inspect.getsource`):**
  Returns the actual source code as a string.
* **Find default values, `*args`, `**kwargs`, and parameter names:**
  Useful for creating wrappers or validating inputs dynamically.
* **Know where the function is defined (`inspect.getfile`, `inspect.getmodule`):**
  Find the file and module where the function lives.
* **Detect if it's a lambda, generator, or method:**
  Use `islambda`, `isgeneratorfunction`, or `ismethod` to check function types.
````python

import inspect

# Define an example function
def add(a: int, b: int = 5) -> int:
    """
    Adds two numbers, with a default value for b.
    """
    return a + b

signature = inspect.signature(add)
# Expected output: (a: int, b: int = 5) -> int

is_function = inspect.isfunction(add)
# Expected output: True

source = inspect.getsource(add)
# Expected output: The source code of the 'add' function.

params = signature.parameters
# Expected output: 
# OrderedDict([('a', <Parameter "a: int">), ('b', <Parameter "b: int = 5">)])

annotations = add.__annotations__
# Expected output: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

file_location = inspect.getfile(add)
module = inspect.getmodule(add)
# Expected output: 
# File Location: /path/to/your/script.py
# Module: <module 'your_module' from '/path/to/your/script.py'>


is_lambda = inspect.islambda(add)
is_generator = inspect.isgeneratorfunction(add)
is_method = inspect.ismethod(add)
# Expected output:
# Is 'add' a lambda? False
# Is 'add' a generator function? False
# Is 'add' a method? False
````

**Access type annotations (`__annotations__`):**
* Read the types declared for parameters and return values.
  * This is helpful for understanding how a function should behave or validating inputs and outputs.
    ```python
    def add(a: int, b: int) -> int:
      return a + b

    annotations = add.__annotations__
    #annotations: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
    ```
## 2. Recursive functions

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

## 3. Nested functions

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
    inner_function(...)  # or return  inner_function
    ...
```

### 3.1. Closure

A **closure** is an inner function (can be a lambda function) that:

- Is defined inside another function (the enclosing function).
- **Refers to non-local variables from the environment** where it was created.
- Is returned or used outside its original scope, while still retaining access to those variables even after the outer function has finished executing.

```python
def outer():
    x = 10
    def inner():
        return x  # x not a parameter or defined in inner()
    return inner

f = outer()
print(f())  # Output: 10
```

## 4. Lambda Functions

Anonymous, inline functions defined with a single expression. They can be assigned to a variable and called like any other function.

- Support default arguments and variable-length parameters (`*args`, `**kwargs`).
- Best for very small, specific operations.

`my_lambda_function = lambda arg1, arg2=1: arg1 + arg2`

**Nested Lambda Functions**

You can nest lambda functions inside other lambdas.

* This allows you to return a lambda from another lambda, or define compact logic in multiple layers.
* Lambda functions can also act as closures, accessing variables from an outer scope.

```python
multiply = lambda x: (lambda y: x * y)
double = multiply(2)
print(double(5))  # Output: 10
```

Using a lambda here makes the code harder to read and prevents proper use of docstrings, type hints, and decorators.
Not recommended to use lambdas in certain cases, such as class methods or as alternatives to list comprehensions.

## 5. High order functions

Functions that accept other functions as arguments or return them.

- **`map(func, iterable)`:** applies `func` to each item and returns an iterator.
- **`filter(func, iterable)`:** returns an iterator of items where `func(item)` is truthy.
- **`educe(func, iterable)`:** cumulatively applies `func` to items, producing a single value (import from `functools`).
- You can also write your own higher‐order functions:

```python
def apply_twice(f, x):
    return f(f(x))
print(apply_twice(lambda y: y + 3, 7))  # 13
```

## 6. Generator Function (`yield`)

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

### 6.1. Generator expression (anonymous generator)

When assigning a generator expression to a variable, you should enclose it in parentheses.

```python
squares = (value * value for value in range(4) )
print(squares)       # <generator object <genexpr> at 0x...>
print(next(squares)) #0
print(next(squares)) #1
print(next(squares)) #4
print(next(squares)) #9
```

#### 6.1.1. Passing a Generator Expression to a Function

You can also pass a generator expression directly to a function, without the need for parentheses.

```python
import math
sum_result = sum(value * value for value in range(4))
print(f'Result of sum: {sum_result}')  # 0 + 1 + 4 + 9 = 14
```

## 7. Decorators `@func`

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

Decorators can also be applied to classes. [Class decorators](modules_and_classes#51-class-decorators)

### 7.1. Multiple decorators

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

### 7.2. Decorating with arguments

```python
def decorador(func):
    def envoltura(*args, **kwargs):
        print("Before func call")
        resultado = func(*args, **kwargs)
        print("After func call")
        return resultado 
    return envoltura # decorador devuleve funcion decoradora
```

### 7.3. Decorating a lambda function (indirectly)

Decorating a lambda manually (not with @ syntax)

```python
my_lambda = decorator_fun(lambda x: x + 3)
```

### 7.4. Preserving metadata with `@wraps`

When writing decorators, it's good practice to use `functools.wraps` to preserve the original function’s name, docstring, and other metadata.

````from

def decorador(func):
    @wraps(func)  # preserves __name__, __doc__, etc.
    def envoltura(*args, **kwargs):
        print("Before func call")
        resultado = func(*args, **kwargs)
        print("After func call")
        return resultado
    return envoltura
````

When you decorate a function without using `@wraps`, the new function loses its original identity. This affects things like:

* **`__name__`**: The decorated function will have the name of the decorator (`envoltura` in this case) instead of the original function’s name.
* **`__doc__`**: The decorated function will lose the original docstring, which can be crucial for documentation purposes.
* **Documentation tools**: Tools that generate docs may use `__name__` and `__doc__`. Without `@wraps`, the function’s metadata will be inaccurate.
* **Debugging**: During debugging, you may see the wrong function name and docstring, making it harder to trace issues.
* **Testing**: Test frameworks that inspect function names or docstrings may behave unexpectedly or fail to match the correct function.

By using `@wraps`, you ensure that the decorated function retains its original metadata, making it easier to work with and debug.

### 7.5. `functools` in Decorators

The `functools` module provides a variety of tools that can be very useful when working with decorators, allowing you to optimize and customize functions in Python. Below are two powerful tools often used in decorators:

#### 7.5.1. Caching Function Results: `lru_cache`

`lru_cache` caches the results of function calls to avoid redundant calculations, improving performance.
*  Best for functions with expensive computations or repeated calls with the same arguments.
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(x):
    return x * 2

# First call will calculate the result
print(expensive_function(4))  # Output: Calculating 4... 8

# Second call will return the cached result
print(expensive_function(4))  # Output: 8 (no calculation)

```


#### 7.5.2. Creating Functions with Predefined Parameters: `partial`

`partial` allows you to create new functions with some arguments preset, simplifying code.
* Create specialized versions of a function with certain arguments fixed.
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2) 
print(square(5))  # Output: 25
```
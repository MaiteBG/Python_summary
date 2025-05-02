#### [Return to README.md](../README.md)


<!-- TOC -->
  * [1. Modules](#1-modules)
    * [1.1. Module content](#11-module-content)
    * [1.2. Modules characteristics](#12-modules-characteristics)
    * [1.3. Who run code block only if we execute the module directly](#13-who-run-code-block-only-if-we-execute-the-module-directly)
* [2. Functions](#2-functions)
  * [2.1. Function Parameters and Arguments](#21-function-parameters-and-arguments)
  * [Functions as First-Class Citizens](#functions-as-first-class-citizens)
  * [2.3. Recursive functions](#23-recursive-functions)
  * [2.4. Nested functions](#24-nested-functions-)
  * [2.5. Lambda Functions](#25-lambda-functions)
* [3. Class and Objects](#3-class-and-objects)
  * [3.1. Dynamic Context](#31-dynamic-context)
    * [3.1.1. Constructor and Object Methods](#311-constructor-and-object-methods)
    * [3.1.2. Attribute and Method Encapsulation](#312-attribute-and-method-encapsulation)
      * [3.1.2.1. Improved Encapsulation (Pythonic with decorators)](#3121-improved-encapsulation-pythonic-with-decorators)
    * [3.1.3. Adding a New Attribute to a Specific Object (Dynamic Attributes)](#313-adding-a-new-attribute-to-a-specific-object-dynamic-attributes)
  * [3.2. Static Context](#32-static-context)
    * [3.2.1. Class Attributes and Methods](#321-class-attributes-and-methods)
* [4. Inheritance and Polymorphism](#4-inheritance-and-polymorphism)
  * [4.1. Polymorphic Function](#41-polymorphic-function)
  * [4.2. Object Class](#42-object-class)
  * [4.3. Multiple Inheritance](#43-multiple-inheritance)
  * [4.4. Abstract Class](#44-abstract-class)
  * [4.5. Operator Overloading](#45-operator-overloading)
<!-- TOC -->

## 1. Modules
### 1.1. Module content
A **module** in Python is a `.py` file containing:
- Functions
- Classes 
- Variables
- Runnable code

### 1.2. Modules characteristics
- Designed for code reusability and organization
- Content can be imported into other Python files using `import`
- Creates its own namespace to avoid naming conflicts
- May include documentation (docstrings) at the top

### 1.3. Who run code block only if we execute the module directly

In Python, every file is considered a module. When we run a Python file, it gets assigned a special built-in variable called '\_\_name__'. This variable helps Python determine whether a module is being imported or executed directly.
When you run the file directly, Python sets __name__ to '__main__'.
``` python
if __name__ = '__main__': 
    # This code block will only run if we execute the module directly
    # It will NOT run if the module is imported elsewhere
```

# 2. Functions

``` python
def nombre_funcion(param_1, param_2, ...):  # Function name like accion or verb
    ... # Function body
    return retrun_variable
```

## 2.1. Function Parameters and Arguments
> **Parameters** are the variables listed in the function definition and **arguments** are the actual values passed to the function when it is called.
* Parameters can have default values: `param = default_value`.
* Alos, can include variable-length parameters:
  * `*args`: Receives multiple arguments as a tuple.
  * `**kwargs`: Receives keyword arguments as a dictionary.

Parameters must be specified in this order: `function(req_arg, default_arg="default", *args, **kwargs)`.

``` python
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


## Functions as First-Class Citizens

In Python, functions are treated as first-class citizens. This means:

- Functions can be assigned to variables:
  ``` python
  def add(x, y):
      return x + y

  my_add = add
  print(my_add(3, 4))  # Output: 7
  ```
  
- Functions can be passed as arguments:
  ``` python
  def apply_func(func, value):
    return func(value)
  
  def increment(x):
      return x + 1
  
  print(apply_func(increment, 5))  # Output: 6
   ``` 

- Functions can return other functions:
   ``` python
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




## 2.3. Recursive functions
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


## 2.4. Nested functions  
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


##  2.5. Lambda Functions

Anonymous and small functions (one line of code). They can be directly assigned to a variable and called like a regular function with parameters in parentheses.
* Can be without arguments or with default arguments, variable-length parameters, etc.

`my_lambda_function = lambda arg1, arg2=1: arg1 + arg2`




# 3. Class and Objects

Classes are defined with the first letter capitalized.
``` python
class ClassName:
```

To get an object's attributes: `object.__dict__`.

## 3.1. Dynamic Context
Dynamic context refers to things that belong to the instances, like instance variables and methods that use `self`.
initialization
### 3.1.1. Constructor and Object Methods
``` python
    # Constructor (called when (ClassName()))
    def __init__(self, params...):
    # Attributes initialization
    self.params = params
    ...
    
    # Object method takes the 'self' parameter which refers to the instance from which it is called
    def class_method(self, params...):
        ...
```

In Python, constructor overloading is not allowed; only the last constructor is used.
To work around this, we can assign default values to optional parameters, usually `None`.

### 3.1.2. Attribute and Method Encapsulation
For good practice, getter and setter methods created and used to access and modify parameters outside the class.

> It is a convention but python do not check access automatically.
``` python
    self.public_attribute # public atribute (+)
    self._protected_attribute # protected atribute
    self.__private_attribute # private atribute (-)
```
Methods can also be indicated as protected/private using `_`/`__` at the beginning. For example, for data validation functions or methods used only within the class methods.

#### 3.1.2.1. Improved Encapsulation (Pythonic with decorators)
To modify protected and private attributes as if they were public, use decorators.

```python
    @property  # Define the getter method in a more Pythonic way
    def attribute(self):
        return self._attribute
    
    @attribute.setter  # Define the setter method in a more Pythonic way
    def attribute(self, value):
        self._attribute = value
```

### 3.1.3. Adding a New Attribute to a Specific Object (Dynamic Attributes)

Only to that object (not all the instances):
`setattr(object, 'attribute_name', 'value')`


## 3.2. Static Context

### 3.2.1. Class Attributes and Methods
```python
class ClassName:
    class_attribute  # Defined outside any method in this class
    # Constructor (called when (ClassName()))
    def __init__(self, params...):
```
```python
    ClassName.class_attribute  # Access class attribute
```

Class methods do not take `self` as a parameter.

```python
    @staticmethod  # Decorator indicating a static method
    def static_method():
        ...
```

 **More Pythonic**: Use the `@classmethod` decorator with the `cls` attribute.

```python
    @classmethod
    def class_method(cls):
        ...
```


# 4. Inheritance and Polymorphism

`class Subclass(Superclass):`

* To define an empty class use `pass` (clearer and explicit). `...` (ellipsis) can also be used in more specific contexts to keep a placeholder for future code.

    * Avoid errors and/or serve as a placeholder for future code.
    * Maintain syntactic structure.
    * Debugging purposes.

Override: To override a superclass method in a subclass, define the method with the same name and parameters. The method in the subclass will always be called first.
Polymorphism: Overriding is used to maintain a standard among different subclasses.

To access the superclass behavior, use `super().method_name` inside the subclass.

## 4.1. Polymorphic Function

It can receive different data types (e.g., a parent class or any of its subclasses) as long as they all have the method with the same name and parameters.


## 4.2. Object Class

It is the parent class of all classes in Python, either directly (by default) or indirectly.
We can override the object class methods:
* `__init__()`: Constructor
* `__str__()`: To change how object information is displayed
* `__eq__()`: To modify the way equality is determined



## 4.3. Multiple Inheritance

`class Subclass(Superclass1, Superclass2):`

MRO - Method Resolution Order `Subclass.mro()` *to obtain the order in which method calls are resolved*.

The order of superclasses is important because a method is searched first in the subclass, then in `Superclass1`, then in the classes inherited by `Superclass1`, then in `Superclass2`, then in the classes inherited by `Superclass2`, and finally in the `object` class.

To refer to a specific superclass, do not use `super()` to avoid confusion. Instead, use `SuperclassX.method(self,...)`, where `self` refers to the instance of the subclass.


## 4.4. Abstract Class

To enforce method implementation in subclasses, the parent class must extend `ABC` (Abstract Base Class) and import the `abstractmethod` decorator.
`from abc import ABC, abstractmethod`  

```python
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(...):
        pass
```

A class that has an abstract method or extends an abstract class without defining the abstract method becomes an abstract class and cannot be instantiated.


## 4.5. Operator Overloading
To modify or implement the behavior of certain operators, override the following methods:
![sobrecarga-operadores1.png](../static_md/sobrecarga-operadores1.png)
![sobrecarga-operadores2.png](../static_md/sobrecarga-operadores2.png)
![sobrecarga-operadores3.png](../static_md/sobrecarga-operadores3.png)
![sobrecarga-operadores4.png](../static_md/sobrecarga-operadores4.png)
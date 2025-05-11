#### [Return to README.md](../README.md)

# Modules, Classes, and Object-Oriented Programming

<!-- TOC -->
  * [1. Modules](#1-modules)
    * [1.1. Module content](#11-module-content)
    * [1.2. Modules Characteristics](#12-modules-characteristics)
    * [1.3. Conditional Execution with `__name__ == "__main__"`](#13-conditional-execution-with-__name__--__main__)
  * [2. Classes and Objects](#2-classes-and-objects)
    * [2.1. Dynamic Context](#21-dynamic-context)
      * [2.1.1. Constructor and Instance Methods](#211-constructor-and-instance-methods)
    * [2.2. Static Context](#22-static-context)
      * [2.2.1. Class Attributes and Methods](#221-class-attributes-and-methods)
    * [2.3. Attribute and Method Encapsulation](#23-attribute-and-method-encapsulation)
      * [2.3.1. Improved Encapsulation (Pythonic with decorators)](#231-improved-encapsulation-pythonic-with-decorators)
    * [2.4. Dynamic Attributes (Adding a New Attribute to a Specific Object or Class)](#24-dynamic-attributes-adding-a-new-attribute-to-a-specific-object-or-class)
    * [2.5. Copy/Clone of objects](#25-copyclone-of-objects)
  * [3. Inheritance and Polymorphism](#3-inheritance-and-polymorphism)
    * [3.1. Polymorphic Function](#31-polymorphic-function)
    * [3.2. Object Class](#32-object-class)
    * [3.3. Multiple Inheritance and MRO](#33-multiple-inheritance-and-mro)
    * [3.4. Abstract Class](#34-abstract-class)
    * [3.5. Operator Overloading](#35-operator-overloading)
  * [4. Object representation](#4-object-representation)
    * [4.1. `__repr__`](#41-__repr__)
    * [4.2. `__str__`](#42-__str__)
    * [4.3. `__format__`](#43-__format__)
  * [5. Cass Metaprogramming](#5-cass-metaprogramming)
    * [5.1. Class decorators](#51-class-decorators)
    * [5.2. Inspecting a Class (Especially for Decorators)](#52-inspecting-a-class-especially-for-decorators)
  * [6. Lightweight Data Structures](#6-lightweight-data-structures)
    * [6.1. Data Classes (Optimized and Automatic Classes)](#61-data-classes-optimized-and-automatic-classes)
    * [6.2. Namedtuple](#62-namedtuple)
      * [6.2.1. Using the collections module (legacy style)](#621-using-the-collections-module-legacy-style)
      * [6.2.2.  the typing module (modern, recommended)](#622-the-typing-module-modern-recommended)
<!-- TOC -->



## 1. Modules

### 1.1. Module content

A **module** in Python is a `.py` file containing:

- Functions
- Classes
- Variables
- Runnable code

### 1.2. Modules Characteristics

- Designed for code reusability and organization
- Content can be imported into other Python files using `import`
- Creates its own namespace to avoid naming conflicts
- May include documentation (docstrings) at the top

### 1.3. Conditional Execution with `__name__ == "__main__"`

In Python, every file is considered a module. When we run a Python file, it gets assigned a special built-in variable called '\_\_name__'. This variable helps Python determine whether a module is being imported or executed directly.
When you run the file directly, Python sets __name__ to '__main__'.

```python
if __name__ = '__main__': 
    # This code block will only run if we execute the module directly
    # It will NOT run if the module is imported elsewhere
```


## 2. Classes and Objects

Classes are defined with the first letter capitalized.

```python
class ClassName:
```

To get an object's attributes: `vars(object)` that almost call to `object.__dict__`.

### 2.1. Dynamic Context

Dynamic context refers to things that belong to the instances, like instance variables and methods that use `self`.
initialization.

#### 2.1.1. Constructor and Instance Methods

```python
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

### 2.2. Static Context

#### 2.2.1. Class Attributes and Methods

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

* *If we want to create a new object from the class inside a class method, we can call the constructor like `cls(constructor_arguments...)`.*

### 2.3. Attribute and Method Encapsulation

> It is a convention but python do not check access automatically.

```python
    self.public_attribute # public atribute (+)
    self._protected_attribute  # should only be accessed within this class or subclasses
    self.__private_attribute #  should only be accessed within this class (avoid collisions with sub and superclasses)
```

Methods can also be indicated as protected/private using `_`/`__` at the beginning. For example, for data validation functions or methods used only within the class methods.

#### 2.3.1. Improved Encapsulation (Pythonic with decorators)

For good practice, getter and setter methods created and used to access and modify parameters outside the class.

To modify protected and private attributes as if they were public, use decorators.

```python
    @property  # Define the getter method in a more Pythonic way
    def attribute(self):
        return self._attribute
  
    @attribute.setter  # Define the setter method in a more Pythonic way
    def attribute(self, value):
        self._attribute = value
```

### 2.4. Dynamic Attributes (Adding a New Attribute to a Specific Object or Class)

In Python, you can dynamically add a new attribute to a single object or a class (without affecting other instances of the same class) in two ways:

- `object.attribute_name = 'value'`

  - Simple and readable.
  - Best when the attribute name is known in advance.
- `setattr(object, 'attribute_name', 'value')`

  - Helpful when the attribute name is dynamic (e.g., stored as a string).
  - Used in metaprogramming or when attribute names are generated at runtime.

### 2.5. Copy/Clone of objects

- **Shallow copy:** creates a new container object, but the elements inside are references to the same objects in the original.

  - Use `copy.copy(obj)` or slicing (`new_list = old_list[:]`) for built-ins like lists.
  - Changes to nested objects (e.g. items in a list) will affect both copies.
- **Deep copy:** creates a new container and recursively copies all nested objects, so the new object is fully independent.

  - Use `copy.deepcopy(obj)` from the standard library.
  - Safe when you need a completely separate duplicate, unaffected by any changes to the original or its subobjects.

**Examples:**

```python
import copy

original = [1, [2, 3]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[1].append(4)
print(shallow)  # [1, [2, 3, 4]]  ← shared sublist
print(deep)     # [1, [2, 3]]     ← independent copy
```

* Shallow and deep copy works the same way for arbitrary objects and their attributes:

```python
import copy

class Node:
    def __init__(self, value, children=None):
        self.value = value
        # children is a list of Node objects
        self.children = children or []

# Build a simple tree
root = Node(0, [Node(1), Node(2)])
shallow_root = copy.copy(root)
deep_root    = copy.deepcopy(root)

# Mutate a child in the original
root.children.append(Node(3))

print(len(shallow_root.children))  # 3 → shares the same list!
print(len(deep_root.children))     # 2 → independent copy

```

## 3. Inheritance and Polymorphism

`class Subclass(Superclass):`

* To define an empty class use `pass` (clearer and explicit). `...` (ellipsis) can also be used in more specific contexts to keep a placeholder for future code.

  * Avoid errors and/or serve as a placeholder for future code.
  * Maintain syntactic structure.
  * Debugging purposes.

Override: To override a superclass method in a subclass, define the method with the same name and parameters. The method in the subclass will always be called first.
Polymorphism: Overriding is used to maintain a standard among different subclasses.

To access the superclass behavior (next MRO class on Multiple Inheritance), use `super().method_name` inside the subclass.

### 3.1. Polymorphic Function

It can receive different data types (e.g., a parent class or any of its subclasses) as long as they all have the method with the same name and parameters.

### 3.2. Object Class

It is the parent class of all classes in Python, either directly (by default) or indirectly.
We can override the object class methods:

* `__init__()`: Constructor
* `__str__()`: To change how object information is displayed
* `__eq__()`: To modify the way equality is determined

### 3.3. Multiple Inheritance and MRO

`class Subclass(Superclass1, Superclass2):`

If methods are not overridden in the subclass:

> MRO - Method Resolution Order `Subclass.mro()` *to obtain the order in which method calls are resolved*.

**Search Order Priority Example** on Subclass(Superclass1,Superclass2)

* First in the **Subclass**
* Then in **`Superclass1`**
* Then in **classes inherited by `Superclass1`**
* Then in **`Superclass2`**
* Then in **classes inherited by `Superclass2`**
* Finally in the **`object` class

- *Eliminates duplicates by listing superclasses only after their children in the inheritance order.*

Python **prohibits circular inheritance** (e.g., `A → B → A`) because it creates an infinite loop in the class hierarchy, making method resolution impossible. *Raises TypeError: Cannot create a consistent method resolution order (MRO).*

* If a method exists in multiple superclasses, super().method_x() executes implementations in MRO order.

  * ⚠️The MRO chain **stops immediately** if any parent's  omits `super().method_x()` ⚠️ (important on **`__init__` Behavior in Inheritance**).
* To call a **specific superclass method**, avoid `super()` to prevent MRO-based chaining.

  * `SuperclassX.method(self, ...)'  # Bypasses MRO chai

**`isinstance(object, class_name)`** actually checks if any of the classes in the MRO matches the target class. `class_name`can be a tuple of classes names.

### 3.4. Abstract Class

To enforce method implementation in subclasses, the parent class must extend `ABC` (Abstract Base Class) and import the `abstractmethod` decorator.
`from abc import ABC, abstractmethod`

```python
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(...):
        pass
```

A class that has an abstract method or extends an abstract class without defining the abstract method becomes an abstract class and cannot be instantiated.

### 3.5. Operator Overloading

To modify or implement the behavior of certain operators, override the following methods:
![sobrecarga-operadores1.png](../static_md/sobrecarga-operadores1.png)
![sobrecarga-operadores2.png](../static_md/sobrecarga-operadores2.png)
![sobrecarga-operadores3.png](../static_md/sobrecarga-operadores3.png)
![sobrecarga-operadores4.png](../static_md/sobrecarga-operadores4.png)
      


## 4. Object representation

### 4.1. `__repr__`

The `__repr__p  method (short for representation) is a special method in Python that defines how an object is represented as a string when:

- The repr(obj) function is called or `f({object!r}`
- The object is displayed in Python’s interactive console (when you type the object’s name directly).
- It serves as the official string representation of an object, primarily intended for developers (should be unambiguous and useful for debugging).

Format:

- Follow the pattern: `ClassName(attr1=value1, attr2=value2, ...)`.
- The output should ideally be a valid Python expression that could recreate the object.
- Use `{self.attr!r}` to display strings with quotes (e.g., `'hello'` instead of `hello`).

### 4.2. `__str__`

The `__str__` method defines the "informal" or user-friendly string representation of an object. It's used when:

* The `str(obj)` function is called, `print(obj)` or `f"{obj}"`.
* The object is displayed in user-facing contexts.

1. **Format**:

   * Should be human-readable and concise
   * No strict format requirements (unlike `__repr__`)If `__str__` is not defined, Python falls back to `__repr__

* NOTE: *If `__str__` is not defined, Python falls back to `__repr__`*

### 4.3. `__format__`

The `__format__` method defines how an object should be formatted when:

* Using `format(obj, spec)`
* Using f-strings with format specifiers (`f"{obj:spec}"`)
* Called implicitly by `str.format()`
* NOTE: *If not defined, falls back to `__str__` then `__repr__`*

Use __format__ when you need:

* Multiple display formats for the same object (for different contexts)
* Specialized formatting (e.g., units, coordinate systems)
* Locale-aware representations (currency, dates)

```python
class Price:
    def __format__(self, spec):
        if spec == 'usd': return f"${self.amount:,.2f}"
        elif spec == 'eur': return f"€{self.amount:,.2f}"
        else: return f"{self.amount:.2f} units"

price = Price(1000)
print(f"{price:usd}")  # $1,000.00
print(f"{price:eur}")  # €1,000.00
```


Also, can use pretty print `from pprint import pprint` to print for example dictionary with better format.





## 5. Cass Metaprogramming
### 5.1. Class decorators

A class decorator works similarly to [function decorators](functions.md#7-decorators-func).
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

### 5.2. Inspecting a Class (Especially for Decorators)

When a class decorator is applied, the class is already defined and available.
The code below demonstrates how to access class attributes and inspect the `__init__` method:

* **`vars(cls)`** retrieves the class's attributes.
* The check verifies if `__init__` exists in the class.
* It then uses `inspect.signature` to get the method signature of `__init__` and lists its parameters (excluding `self`).

This allows decorators to inspect and interact with the class definition, ensuring methods are correctly defined.

```python
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




## 6. Lightweight Data Structures

### 6.1. Data Classes (Optimized and Automatic Classes)

A `dataclass` is a Python class automatically enhanced with boilerplate methods like `__init__`, `__repr__`, and `__eq__`, based only on its attributes.

Use them when:

* The class is mainly used to store data
* You want auto-generated `__init__`, `__repr__`, `__eq__`, etc.
* You prefer cleaner, more readable code
* You need easy conversion to `dict`/`tuple` (`asdict`, `astuple`)
* You want immutability (`frozen=True`)
* You want safe defaults for mutable types (`default_factory`)

Options:

* `eq=True` (default): adds comparison (`==`)
* `frozen=True`: makes instances read-only (e.g., usable in `set` or as `dict` keys)

```python
from dataclasses import dataclass

@dataclass(eq=True, frozen=True )
class User:
    name: str
    age: int
  
    def __post_init__(self):   # Runs after __init__
        if self.age < 0:
            raise ValueError("Age must be non-negative")
```

Convert, compare, or copy:

```python
from dataclasses import asdict, astuple, replace

p = Point(1, 2)
print(asdict(p))         # {'x': 1, 'y': 2}
print(astuple(p))        # (1, 2)
print(replace(p, x=10))  # Point(x=10, y=2)
```

Avoid `dataclass` when:

* When the class has a lot of internal logic but few attributes
* When complex inheritance or advanced metaprogramming is needed
* If you're already using tools like Pydantic, NamedTuple, or attrs for better control

### 6.2. Namedtuple

A `NamedTuple` is an alternative to a class when you need immutable attributes and tuple-like behavior with readable attribute names.

 Use it when:

* You need fast, memory-efficient **immutable** data containers
* You want to access elements by **index** or by **attribute name**
* You don’t need custom methods or internal logic
* You want something more structured than a regular `tuple`, but lighter than a class or `dataclass`

Features:

* **Immutable by default** (safe for use in sets or as dictionary keys)
* **Behaves like both a tuple and a class**
* Supports **unpacking**: `x, y = point`
* Has built-in  class constructor and  methods like `_replace`, `_asdict` (converts to dictionary) , and `_fields` (can be used as inheritance-like)


#### 6.2.1. Using the collections module (legacy style)
``` python 
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print(p.x)      # 1
print(p[1])     # 2
print(p._asdict())  # {'x': 1, 'y': 2}
```
Create extended namedtuple with `_fields` (inheritance-like): 
 ``` python
 from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
fields = Point._fields + ('color',)

ColoredPoint = namedtuple('ColoredPoint', fields)

cp = ColoredPoint(1, 2, 'red')
print(cp)  # ColoredPoint(x=1, y=2, color='red')
```


#### 6.2.2.  the typing module (modern, recommended)
Recomentes for Python 3.6+
``` python 
from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

p = Point(1, 2)

print(p.x)      # 1
print(p[1])     # 2
print(p._asdict())  # {'x': 1, 'y': 2}
```

Create extended namedtuple (inheritance-like): 
``` python
class ColoredPoint(Point):
    color: str

    def __new__(cls, x, y, color):
        return super().__new__(cls, x, y, color)
```
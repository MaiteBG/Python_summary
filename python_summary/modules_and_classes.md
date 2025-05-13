#### [Return to README.md](../README.md)

# Modules, Classes, and Object-Oriented Programming

<!-- TOC -->
  * [1. Modules](#1-modules)
    * [1.1. Module content](#11-module-content)
    * [1.2. Modules Characteristics](#12-modules-characteristics)
    * [1.3. Conditional Execution with `__name__ == "__main__"`](#13-conditional-execution-with-__name__--__main__)
  * [2. Classes](#2-classes)
    * [2.1. Dynamic Context (for instances)](#21-dynamic-context-for-instances)
    * [2.2. Static Context (for class)](#22-static-context-for-class)
    * [2.3. Attribute and Method Encapsulation](#23-attribute-and-method-encapsulation)
      * [2.3.1. Pythonic Attribute Encapsulation](#231-pythonic-attribute-encapsulation)
    * [2.4. Adding Attributes Dynamically to Objects and Classes](#24-adding-attributes-dynamically-to-objects-and-classes)
    * [2.5. Class decorators](#25-class-decorators)
    * [2.6. Class Introspection (inspect the `__init__` method)](#26-class-introspection-inspect-the-__init__-method)
  * [3. Inheritance, Polymorphism and Method Overriding](#3-inheritance-polymorphism-and-method-overriding)
    * [3.1. Inheritance](#31-inheritance)
      * [3.1.1. Object Class](#311-object-class)
      * [3.1.2. Method Resolution Order - MRO](#312-method-resolution-order---mro)
      * [3.1.3. `super()`](#313-super)
      * [3.1.4. Multiple Inheritance](#314-multiple-inheritance)
      * [3.1.5. Abstract Class](#315-abstract-class)
    * [3.2. Polymorphism and Method Overriding](#32-polymorphism-and-method-overriding)
  * [4. Lightweight Data Structures](#4-lightweight-data-structures)
    * [4.1. Data Classes (Optimized and Automatic Classes)](#41-data-classes-optimized-and-automatic-classes)
    * [4.2. Namedtuple](#42-namedtuple)
  * [5. Others instance/object features](#5-others-instanceobject-features)
    * [5.1. Copy/Clone of objects](#51-copyclone-of-objects)
    * [5.2. Object representation](#52-object-representation)
      * [5.2.1. `__repr__`](#521-__repr__)
      * [5.2.2. `__str__`](#522-__str__)
      * [5.2.3. `__format__`](#523-__format__)
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

In Python, every file is considered a module. When we run a Python file, it gets assigned a special built-in variable called `__name__`. This variable helps Python determine whether a module is being imported or executed directly.
When you run the file directly, Python sets `__name__` to ´__main__´.

```python
if __name__ = '__main__': 
    # This code block will only run if we execute the module directly
    # It will NOT run if the module is imported elsewhere
```

## 2. Classes

A class in Python is a blueprint for creating objects that encapsulate data and behavior in a single structure.

* Classes are defined with the first letter capitalized [(*PascalCase*)](basic_concepts_conventions.md#33-class-names)

### 2.1. Dynamic Context (for instances)

Dynamic context refers to things that belong to the instances:

* Instance variables, which store data unique to each object.
  * These variables are typically set during initialization in the `__init__` constructor.
   > In Python, constructor overloading is not supported—only the last defined `__init__` method is used. To simulate overloading, you can use default parameter values (often `None`) and conditional logic.
    
* Methods that use `self`, allowing access to the instance's attributes and other methods.

```python
class ClassName:
    # Constructor (called to create an instance - ClassName(...))
    def __init__(self, param_x):
        # Attributes initialization
        self.param_x = param_x
  
    # Object method takes the 'self' parameter which refers to the instance from which it is called
    def instance_method(self, param_x):
        ... 
```

> Instance methods can be called from the class as: `ClassName.instance_method(instance, param_x)`
> * Passing an instance of the class as the first parameter (`self`)

### 2.2. Static Context (for class)

Static context refers to things that belong to the class:

* **Class variables**, shared across all instances (defined outside any method in this class).
* **Static methods**, which don't use `self` or `cls`and they don't access class attributes. 
  * They are utility methods associated with the class but do not operate on instance-specific data.
* **Class methods**, which receive the class (`cls`) as their first argument (instead of `self`).

```python
class ClassName:
    class_attribute  # Defined outside any method in this class

    @staticmethod  # static method decorator
    def static_method():
        ...
  
    @classmethod # class method decorator
    def class_method(cls):
        ...
```

* *If we want to create a new object from the class inside a class method, we can call the constructor like `cls(constructor_arguments)`.*



### 2.3. Attribute and Method Encapsulation

By convention Attributes and methods can be indicated as protected/private using `_`/`__` at the beginning. [*Use of underscore on Naming Conventions*](basic_concepts_conventions.md#34-use-of-underscore)

```python
self.public_attribute # public atribute (+)
self._protected_attribute  # should only be accessed within this class or subclasses
self.__private_attribute #  should only be accessed within this class (avoid collisions with sub and superclasses)
```

And should use getter and setter methods to control access to attributes from outside the class.

#### 2.3.1. Pythonic Attribute Encapsulation

Instead of traditional `get_` and `set_` methods, Python offers a more elegant and readable approach using the `@property` and   `@attribute.setter` decorators.

* This allows you to access or modify **protected or private attributes** as if they were public, while still maintaining control behind the scenes.

```python
    @property  # Define the getter method in a more Pythonic way
    def attribute(self):
        return self._attribute
  
    @attribute.setter  # Define the setter method in a more Pythonic way
    def attribute(self, value):
        self._attribute = value
```

### 2.4. Adding Attributes Dynamically to Objects and Classes

In Python, you can dynamically add a new attribute to a single object or a class (without affecting other instances of the same class) in two ways:

- `object.attribute_name = 'value'`
  - Simple and readable.
  - Best when the attribute name is known in advance.
- `setattr(object, 'attribute_name', 'value')`
  - Helpful when the attribute name is dynamic (e.g., stored as a string).
  - Used in metaprogramming or when attribute names are generated at runtime.


* `setattr(cls, method_name, new_method)`: adds or replaces methods dynamically on the class.


### 2.5. Class decorators

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

Decorators also can be implemented as a class (less common):
* `isinstance(method, DecoratorClass)`: checks whether a method has been wrapped by a decorator implemented as a class.

```python
class MyDecorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print("Before function call")
        return self.func(*args, **kwargs)
```


### 2.6. Class Introspection (inspect the `__init__` method)

Class introspection allows you to examine and interact with class structures at runtime. This is especially useful in advanced techniques like class decorators, where validation or modification of the class is needed after it's fully defined.

This approach can be used to verify that classes meet certain criteria—like having a properly defined `__init__` method—and to retrieve or manipulate method definitions dynamically.

* **`vars(cls)`** returns the class's `__dict__`, providing access to its attributes and methods.
* Check for `__init__` to ensure the class explicitly overrides the constructor.
* **`inspect.signature`** is used to get the signature of `__init__`, and to extract its parameters (excluding `self`).
* **`inspect.getsource(obj)`** returns the source code of a method or class to verify its contents.


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

## 3. Inheritance, Polymorphism and Method Overriding

### 3.1. Inheritance

> `class Subclass(Superclass):`

#### 3.1.1. Object Class

In Python, **`object`** is the most fundamental base class. Every class in Python inherits from `object` directly (by default) or indirectly, making it the ancestor of all other classes.

**Methods from `object`**: The `object` class provides a few built-in methods that are available to every class. Some of the most commonly used ones are:

* **`__init__(self)`**: The constructor method, which is called when an instance of the class is created.
* **`__str__(self)`**: This method returns a string representation of the object. If not defined, it defaults to a generic description.
* **`__repr__(self)`**: This method is used to define the official string representation of the object, often for debugging purposes.
* **`__eq__(self, other)`**: Checks if two objects are equal.
* **`__ne__(self, other)`**: Checks if two objects are not equal.
* **`__hash__(self)`**: Returns a hash value for the object.
* **`__del__(self)`**: Called when an object is about to be destroyed.

#### 3.1.2. Method Resolution Order - MRO

The **Method Resolution Order (MRO)** defines the sequence Python follows to look for a method or attribute in a class hierarchy.

* `Subclass.mro()`

- Eliminates duplicates by listing superclasses only after their children in the inheritance order.
- Python **prohibits circular inheritance** (e.g., `A → B → A`) because it creates an infinite loop in the class hierarchy, making method resolution impossible. *Raises TypeError: Cannot create a consistent method resolution order (MRO).*

If a method is not explicitly overridden in a subclass, Python will automatically look up the method in its parent class (or classes) following the Method Resolution Order (MRO). This ensures that the subclass inherits behavior from its superclass unless explicitly changed.

#### 3.1.3. `super()`

* Using `super()` is the recommended way to call a method from a parent class because it respects the MRO and ensures that all relevant methods in the hierarchy are properly called.
* This supports **cooperative multiple inheritance**, where methods from different classes in the hierarchy can all participate in a single call chain.

`super().method()` doesn’t mean “go to the parent class” — it means “go to the next class in the MRO”.

* ⚠️The MRO chain **stops immediately** if any parent's  omits `super().method()` inside its `method()` implementation. ️ *(important on **`__init__` in inheritance**)*.

To call a **specific superclass method**, avoid `super()` to prevent MRO-based chaining.

* `SuperclassX.method(self, ...)`

#### 3.1.4. Multiple Inheritance

`class Subclass(Superclass1, Superclass2):`

**Multiple Inheritance MRO Example**`Subclass(Superclass1,Superclass2)`:

* First in the **``Subclass`**
  * Then in **`Superclass1`**
    * Then in *classes inherited by `Superclass1`*
  * Then in **`Superclass2`**
    * Then in *classes inherited by `Superclass2`*
* Finally in the **`object`** class

NOTE: **`isinstance(object, class_name)`** actually checks if any of the classes in the MRO matches the target class. `class_name`can be a tuple of classes names.

#### 3.1.5. Abstract Class

To enforce method implementation in subclasses, the parent class must extend `ABC` (Abstract Base Class) and import the `abstractmethod` decorator.
`from abc import ABC, abstractmethod`

```python
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(...):
        pass
```

A class that has an abstract method or extends an abstract class without defining the abstract method becomes an abstract class and cannot be instantiated.

### 3.2. Polymorphism and Method Overriding

Polymorphism allows different objects to be used interchangeably, as long as they implement the same interface or behavior—even if they come from unrelated classes. It is not limited to inheritance; it applies whenever objects provide the same method names with compatible signatures.

**Polymorphism through Inheritance**

* The most common form of polymorphism. Subclasses override or extend methods from a base class.
* For example, a parent class `Animal` can define a method `speak`, and subclasses like `Dog` and `Cat` can implement that method differently.

**Polymorphism through Duck Typing (without Inheritance)**

* Thanks to Python’s dynamic typing, polymorphism doesn’t require formal inheritance.
* If an object has the required methods or attributes, it can be used in place of any other with the same interface.
* This behavior is called *duck typing*, inspired by the saying: *“If it looks like a duck and quacks like a duck, it must be a duck.”*

> This concept is especially powerful in dynamic languages like Python, where a function or method can accept different data types as long as those objects implement the expected methods. Built-in functions such as `len()`, `str()`, or `abs()` demonstrate this: they work across various types because the objects define special methods like `__len__`, `__str__`, or `__abs__`.

> Operator overloading, also, enables user-defined classes to behave like built-in types when using operators such as `+`, `-`, or `==`. To achieve this, classes can override special methods (also called “magic methods”) like `__add__`, `__eq__`, and others. This makes custom objects more intuitive and integrates them naturally with Python syntax.

## 4. Lightweight Data Structures

### 4.1. Data Classes (Optimized and Automatic Classes)

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

### 4.2. Namedtuple

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

**Using the collections module (legacy style)**

```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print(p.x)      # 1
print(p[1])     # 2
print(p._asdict())  # {'x': 1, 'y': 2}
```

Create extended namedtuple with `_fields` (inheritance-like):

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
fields = Point._fields + ('color',)

ColoredPoint = namedtuple('ColoredPoint', fields)

cp = ColoredPoint(1, 2, 'red')
print(cp)  # ColoredPoint(x=1, y=2, color='red')
```

**Using the typing module (modern, recommended)**
Recomentes for Python 3.6+

```python
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

```python
class ColoredPoint(Point):
    color: str

    def __new__(cls, x, y, color):
        return super().__new__(cls, x, y, color)
```

## 5. Others instance/object features

### 5.1. Copy/Clone of objects

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

print(len(shallow_root.children))  # 3 → shares the same list! (only different main reference) 
print(len(deep_root.children))     # 2 → independent copy
```

### 5.2. Object representation

#### 5.2.1. `__repr__`

The `__repr__p  method (short for representation) is a special method in Python that defines how an object is represented as a string when:

- The repr(obj) function is called or `f({object!r}`
- The object is displayed in Python’s interactive console (when you type the object’s name directly).
- It serves as the official string representation of an object, primarily intended for developers (should be unambiguous and useful for debugging).

- Format:

  - Follow the pattern: `ClassName(attr1=value1, attr2=value2, ...)`.
  - The output should ideally be a valid Python expression that could recreate the object.
  - Use `{self.attr!r}` to display strings with quotes (e.g., `'hello'` instead of `hello`).

#### 5.2.2. `__str__`

The `__str__` method defines the "informal" or user-friendly string representation of an object. It's used when:

* The `str(obj)` function is called, `print(obj)` or `f"{obj}"`.
* The object is displayed in user-facing contexts.

* Format:

   * Should be human-readable and concise
   * No strict format requirements (unlike `__repr__`)If `__str__` is not defined, Python falls back to `__repr__

* NOTE: *If `__str__` is not defined, Python falls back to `__repr__`*

#### 5.2.3. `__format__`

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
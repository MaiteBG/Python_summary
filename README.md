# Python Summary
<!-- TOC -->
  * [Basic Concepts and Conventions](#basic-concepts-and-conventions)
    * [Comments](#comments)
    * [Variables](#variables)
    * [Naming conventions](#naming-conventions)
    * [Print Statement](#print-statement)
  * [Strings](#strings)
    * [Concatenating Strings](#concatenating-strings)
    * [String format](#string-format)
    * [String Methods (do not replace the original string!)](#string-methods-do-not-replace-the-original-string)
  * [Input data](#input-data)
    * [Data type conversion (for MD)](#data-type-conversion-for-md)
  * [Operators](#operators)
    * [Arithmetic operators](#arithmetic-operators)
    * [Assignment](#assignment)
    * [Conditional and logical operators](#conditional-and-logical-operators)
    * [Operator Precedence in Python](#operator-precedence-in-python)
  * [Sentences](#sentences)
    * [Control Sentences](#control-sentences)
    * [Loop sentences](#loop-sentences)
  * [Collections](#collections)
    * [List `my_list = [item_1, item_2, item3]`](#list-my_list--item_1-item_2-item3)
    * [Tuple `my_tuple = (item_1, item_2, item_3)`](#tuple-my_tuple--item_1-item_2-item_3-)
    * [Set `my_set = {item_1, item_2, item_3}`](#set-my_set--item_1-item_2-item_3)
    * [Dictionary `my_dictionary = {key_1: value_1, key_2: value_2}`](#dictionary-my_dictionary--key_1-value_1-key_2-value_2)
    * [List comprehension `[operation for element in iterable if condition]`](#list-comprehension-operation-for-element-in-iterable-if-condition)
  * [Modules](#modules)
    * [Modules characteristics](#modules-characteristics)
  * [Functions](#functions)
    * [Arguments](#arguments)
    * [Use of globla varaible inside a function](#use-of-globla-varaible-inside-a-function)
    * [Recursive functions](#recursive-functions)
<!-- TOC -->



## Basic Concepts and Conventions

### Comments
- Use `#` followed by a space to write comments that explain the code.

### Variables
- **Dynamic typing**: Variables can store any type of data and change their type without explicit casting.
- **Objects**: Variables in Python are references stored in the *stack* and point to data in the *heap*.
- **Mutability**: If the value of a variable changes, a new object is created with the updated data, and the variable points to this new reference.
- **Initialization**: Variables must be declared with an initial value. 
- `ìd(objecto)`: position of memory of the variable object
### Naming conventions

- *No debemos tener fihceros y directorios con el mismo nombre para evitar errores en Python.*
- **Constants**: By convention, constants are named in uppercase (e.g., `CONSTANT_VALUE`) and should not be modified.
- **Snake Case** for common variables and file names:
  - Use the snake_case format: `[a-z][A-Z,a-z,0-9,_]+`.
  - Avoid:
    - Python's reserved keywords.
    - Single-letter variable names (except for exceptions like indices).
    - Names starting with numbers or uppercase letters.
  - Use underscores (`_`) to compose multi-word names (e.g., `file_txt`).
  - Apply prefixes or suffixes to provide context (e.g., `is_valid`, `user_count`).
  - Use of plural names only on collections.

### Print Statement
  - Basic example: `print(x, "y", z)`.
  - Using commas automatically adds spaces between the values in the output.
  - To print a blank line: `print()`.
  - To change final character (default break line) `print(var1, end=' ')`
---

---

## Strings
- **Defining Strings**: Strings can be defined using `'`, `"`, or `'''`. Triple quotes allow you to include line breaks directly within the text.
- **Character Indexing**:
  - Characters are indexed from `0` to `length-1`.
  - Negative indexing allows access from the end of the string: `string[-1]` accesses the last character.
  - **Immutability**: Strings cannot be modified once they are created.



### Concatenating Strings
- **Using the `+` operator**
- Using `split_string.join([list of strings])`
	* Note: if `' '.join(stringX)` is used, it splits characters with a space.

### String format
- f-string: `f' Hola {variable}'`   
	* *Specify float decimals: `f"{float_var1:.2f}"`*
	* *Evaluates expressions inside the string. `f"{num1 + num2}"`*

- format method (more complex and les used): `'Hola {}'.format(variable)`


#### Special Characters
- The backslash (`\`) is used to include special characters:
  - `\n`: New line.
  - `\t`: Tab.
  - `\\`: Backslash (`\`).
  - `\'`: Single quote within single-quoted strings.



### String Methods (do not replace the original string!)
- Upper and lower case: `str1.upper()`, `str1.lower()`
- Remove beginning and ending spaces: `str1.strip()`
- Length: `len(str1)`
- Slicing (get substring): `str1[start:end]` *The end index character is not included.*
- Find substring: `str1.find(substring)` Returns the index of the first occurrence of the searched substring (-1 if not found).
- Replace method: `new_str = str1.replace(old_substr, new_substr)`
- Split method: Divides the string into a list of elements split by a separator *(default space)*: `str1.split(sep)`
- Repeat the same string: `str1 * n` Repeats the string `str1` `n` times.

---

---

## Input data

- **User data**: `input("Message")` prompts the user for input and always returns a string. Type conversion is necessary afterward if a different data type is needed.
- **Random number**: `randint(a, b)` from the `random` module returns a random integer between `a` and `b` (inclusive).


### Data type conversion (for MD)

- `int(x)` *if x is bool: 0 (False), 1 (True)*
- `float(x)` *Converts x to a floating-point number.*
- `str(x)` *if x is bool: "False" (False), "True" (True)*
- `bool(x)` *`False` value if x is 0, None, or an empty string, list, or collection.*
- Other conversions `hex(x)` *hexadecimal*

With variable and dot: `x.` (*possible type operations*)

---

---
## Operators

### Arithmetic operators

- `+ - *` `/` *float division* `//` *integer division* `%` *modulo* `**` *power*

### Assignment

- `var_x = value` *Assigns a value to a variable.*
- Multiple assignment: `var_x, var_y, var_z = value_x, value_y, value_z` *Assigns values to multiple variables in a single line.*
- Chained assignment: `var1 = var2 = … = value` *Assigns the same value to multiple variables.*

#### Value exchange without temporary variable
- `x, y = y, x` *Swaps the values of `x` and `y` without using a temporary variable.*

#### Compound assignments
- `variable OPERATOR = value` *Equivalent to `variable = variable OPERATOR value` (e.g., `x += 5` is equivalent to `x = x + 5`).*

---

### Conditional and logical operators

- **Return a boolean result**
- **Conditional**: `< > <= >= == !=`
  - *Can use multiple operands: `value_min <= value_x <= value_max`.*
  - *For strings, compares based on ASCII values.*

- **Logical**: `and` `or` `not`
  - *Use `not` to check if a variable is empty. For example: `if not var_x`, returns `True` if `var_x` is empty.*

### Operator Precedence in Python
Python follows a specific order of precedence for operators:

1. **Parentheses**
   - `()` have the highest precedence and are used to force the evaluation order.

2. **Exponentiation**
   - `**`

3. **Unary Operators**
   - Unary Plus and Minus: `+`, `-`

4. **Arithmetic Operators**
   - 4.1. Multiplication, Division, Floor Division, Modulus: `*`, `/`, `//`, `%`
   - 4.2. Addition and Subtraction: `+`, `-`

5. **Comparisons**
   - Equality and Relational: `==`, `!=`, `>`, `<`, `>=`, `<=`

6. **Logical Operators**
   - `and`, `or`, `not`
7. **Assignment and Compound Assignments**
   - `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`
---

---

## Sentences
### Control Sentences

- `if`, `elif`, `else`
- Ternary operator: `result = true_value if condition else false_value`
  - *Use only if the statement fits on one line.*

In Python, a `switch` statement does not exist.

- Use of dictionary

``` python
def opcion_1():
    print("Ejecutando la opción 1...")
    return "Opción 1 completada"

def opcion_2():
    print("Ejecutando la opción 2...")
    return "Opción 2 completada"

def opcion_3():
    print("Ejecutando la opción 3...")
    return "Opción 3 completada"

def switch_demo(argument):
    opciones = {
        1: opcion_1,
        2: opcion_2,
        3: opcion_3,
    }
    funcion = opciones.get(argument, lambda: "Opción no válida")
    return funcion()

# Pruebas
print(switch_demo(1))  # Salida: Ejecutando la opción 1... Opción 1 completada
print(switch_demo(4))  # Salida: Opción no válida
```

- In Python 3.10 or later, you can use *pattern matching*, introduced with the `match` and `case` keywords.

``` python
def switch_demo_v2(argument):
    match argument:
        case 1:
            return "Opción 1 seleccionada"
        case 2:
            return "Opción 2 seleccionada"
        case 3:
            return "Opción 3 seleccionada"
        case _:
            return "Opción no válida"

print(switch_demo_v2(2))  # Salida: Opción 2 seleccionada
```
---

### Loop sentences

``` python
while condition:  # while statement
for current_val in sequence:  # for statement
```
For `sequence` we can use the python functions 

* `range(ini, fin+1, increment)`
    * Default `ini = 0` and `increment = 1`
    * If don't use current_val, can be indicated with a `for _ in ...`
* `for counter, item  in enumerate(collection)`


* `break`: out of the loop

* `continue`:  go to next iteration

---

---

## Collections

### List `my_list = [item_1, item_2, item3]`
- Items can be of different types
- Ordered and mutable *Dynamic: can add, modify, and remove elements*

#### Operations with lists

- **Consult and order**  
  * `len(my_list)` - Get the length of the list  
  * `my_list[index_x]` - Access an item at index `x`  
  * `my_list[index_ini:index_fin+1]` - Slice the list from `index_ini` to `index_fin`  
  * `for value in my_list:` - Iterate through the list  
  * **Order:** Ascending `my_list.sort()`, Descending `my_list.sort(reverse=True)`

- **Add**  
  * At the end of the list: `my_list.append(new_item)`  
  * At a specific index: `my_list.insert(index_x, new_item)` (*other elements shift to the right*)  

- **Remove**  
  * By value: `my_list.remove(value)`  
  * By index: `my_list.pop(index_x)` or `del my_list[index_x}`  

---

### Tuple `my_tuple = (item_1, item_2, item_3)` 
or `my_tuple = item_1, item_2, item_3`

*only one element with a comma at end `my_tuple = item_1,`*

- Items can be of different types
- Ordered but **immutable** (No can add, modify and drop elements)

#### Operations with tuples

**Consult and order**  
* `my_tuple[index_x]` - Access an item at index `x`  
* `my_tuple[index_ini:index_fin+1]` - Slice the list from `index_ini` to `index_fin`  

* **Unpacking:** `var_1, var_2, var_3 = my_tuple #(item1, item2, item3)`  

---

### Set `my_set = {item_1, item_2, item_3}`

- Items can be of different types
- Not ordered and unique (no duplicated elements)
- Mutable

#### Operations with sets

**Consult**  
- `len(my_set)`  
- `for item in my_set:`  
- Check if value exists: `value_x in my_set`

**Add and remove**  
- `my_set.add(new_item)`  
- `my_set.remove(value)`  

**Set operations**  
- Union: `set_1 | set_2`  
- Intersection: `set_1 & set_2`  
- Difference: `set_1 - set_2`  

---

### Dictionary `my_dictionary = {key_1: value_1, key_2: value_2}`

- Items can be of different types (keys are always strings)
- Ordered and mutable
- Keys must be unique (like set items)

#### Operations with dictionaries

* **Consult:** `my_dictionary['key_x']` or `my_dictionary.get(key_x)`  

* **Add or modify:** `my_dictionary['key_x'] = value_x`  

* **Delete:** `my_dictionary.pop('key_x')` or `del my_dictionary['key_x']`  

* **Iteration of elements**  
  * Tuple (key, value): `for key, value in my_dictionary.items():`  
  * Only values: `for value in my_dictionary.values():`  
  * Only keys: `for key in my_dictionary.keys():`  

---

### List comprehension `[operation for element in iterable if condition]`

* Create lists from other iterables (filter or apply expressions to each element)  
  * Example: `[x**2 for x in numbers] # do square`
  
---

---

## Modules

A **module** in Python is a `.py` file containing:
- Functions
- Classes 
- Variables
- Runnable code

### Modules characteristics
- Designed for code reusability and organization
- Can be imported into other Python files using `import`
- Creates its own namespace to avoid naming conflicts
- May include documentation (docstrings) at the top

``` python
if __name__ = '__main__': #__name__ varaible that indicate the name of the module that we are ejecuting 
  #Instrucción only if we ejecute the module direcly
```


---

---
## Functions

``` python
def nombre_funcion(param_1, param_2, ...):  # Function name like accion or verb
    # Function body
    return resultado
```
* Can return a single value or a tuple of values (with or without unpacking).

### Arguments

* Parameters can have default values: `param = default_value`.
* Variable-length Arguments:
  * `*args`: Receives multiple arguments as a tuple.
  * `**kwargs`: Receives keyword arguments as a dictionary.

Arguments must be specified in this order: `function(req_arg, default_arg="default", *args, **kwargs)`.

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

### Use of a global variable inside a function
``` python
variable_name = value

def function(...):
    global variable_name
    variable_name = values...  # or other use of variable_name
```

### Recursive functions
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


## Class and objects

Las clases de definen con la primera letra en mayuscuala. 
``` python
class Class_name:
```

Para obtener los atributos de un objecto `object.__dict__`.

### Contexto dinámico

#### Constructor y metodos de objecto
``` python
    # Constructor (called went ( Class_name())
    def __init__(self, params...):
    # Atributes 
    self.params = params
    ...
    
    #Método de objecto lleva el parametro self que hace referncia a la instacia desde la qula se llama
    def metodo_de_classe(self, params...):
        ...
```

En Python no se puede hacer sobrecarga de constructores, solo utiliza el último constructor. 
Para solucionarlo podemos poner valor por defecto a los parameteros opcionales, noramlmente, `None`.


#### Encapsulamiento de atributos
Generalement se usan atributos protegidos para las clases.  Permite más control sobre escritura y lectura de atributos. Python no hace ningún cotrol pero hay convensión de defincion con `_`(protegido) y `__` (privado) delante del nombre del atributo.
Para una buena practica, se crean y usan los metodos `get_atributo()` y `set_atributo()` para leer y modificar los parametros fuera de la clase. 

``` python
    self.atributo_publico
    self._atributo_protegido
    self.__atributo_privado
```

##### Mejoras de encapsulamiento (más pythonica)

Para modficar los atributos protegidos y privados como si fueran públicos.

``` python
    @property # definir el metodo get de manera más pythonica
    def atributo(self):
        retrun self._atributo
    
    @atributo.setter # definir el metodo set de manera más pythonica
    def atributo(self, value):
        self._atributo = value

```

#### Agregar un nuevo atributo a un objecto determinado (atributos dinamicos)

`setattr(objecto, 'nombre_atrbibuto', 'valor')`


### Contexto estatico

#### Atributos  y  métodos de clase
``` python
class Class_name:
    atributo_de_clase  # fuera de cualquiler metodo de esta classe
    # Constructor (called went ( Class_name())
    def __init__(self, params...):
```
``` python
    Class_name.atributo_de_clase  # acceder al atributo de classe
```

Los métods de clase no tiene el parametro self.

``` python
    @staticmethod # indicar que es metodo estatico
    def metodos_estatico():
        ...
```

 **Más pythonico**: Usar la etiqueta  `@classmethod` con el atributo `cls`

``` python
    @classmethod
    def metodo_clase(cls):
        ...
```


## Herencia y polimorfismo

`class Subclase(Superclase):`

* *Para solo definir una clase `pass` (más claro y explicito), tambien se puede usar `...` (ellipsis, en contextos más especificos) (para cualquier bloque de código que quieras dejar vacío)*

    * Evitar errores y/o Marcador de posición para código futuro
    * Mantener la estructura sintáctica
    * Para depurar

Override: Para sobreescribr un metodo de la superclase en una clase hija, tenemos de definir el metodo con el mismo nombre y paramentros. Siempre se llamara sera el de menor jerarquia.
Polimorfismo: Usamos sobrescritura para mantener estandar en las disntias clases hijas. 

Para acceder al comporatiento de la calse padre podemos usar `super.clase_padre` dentro de la clase hija.

### Funcion polimorfica

Puede recibir distitnos tipos de datos (por ejemplo clase padre o alguna de las hijas siempre que todos tengan el metodo con el mismo nombre y paramentros)



### Clase object

Es la clase padre de todas las clases en Python de manera directa (por defecto) o indirecta. 
Podemos sobreescrir los metodos de la clase object:
* `__init__()`: Costructor
* `__str__()`: Para cambiar como se muestra la inforamción del object
* `__eq__()`: Para modificar la forma de identificar si son iguales




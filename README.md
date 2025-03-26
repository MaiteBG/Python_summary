# Python Summary

## Basic Concepts and Conventions

### Comments
- Use `#` followed by a space to write comments that explain the code.

### Variables
- **Dynamic typing**: Variables can store any type of data and change their type without explicit casting.
- **Objects**: Variables in Python are references stored in the *stack* and point to data in the *heap*.
- **Mutability**: If the value of a variable changes, a new object is created with the updated data, and the variable points to this new reference.
- **Initialization**: Variables must be declared with an initial value.
- **Constants**: By convention, constants are named in uppercase (e.g., `CONSTANT_VALUE`) and should not be modified.

### Snake Case
- **Naming conventions**:
  - Use the snake_case format: `[a-z][A-Z,a-z,0-9,_]+`.
  - Avoid:
    - Python's reserved keywords.
    - Single-letter variable names (except for exceptions like indices).
    - Names starting with numbers or uppercase letters.
  - Use underscores (`_`) to compose multi-word names (e.g., `file_txt`).
  - Apply prefixes or suffixes to provide context (e.g., `is_valid`, `user_count`).

### Print Statement
  - Basic example: `print(x, "y", z)`.
  - Using commas automatically adds spaces between the values in the output.
  - To print a blank line: `print()`.
  - To change final character (default break line) `print(var1, end=' ')`



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



## Input data

- **User data**: `input("Message")` prompts the user for input and always returns a string. Type conversion is necessary afterward if a different data type is needed.
- **Random number**: `randint(a, b)` from the `random` module returns a random integer between `a` and `b` (inclusive).


### Data type conversion (for MD)

- `int(x)` *if x is bool: 0 (False), 1 (True)*
- `float(x)` *Converts x to a floating-point number.*
- `str(x)` *if x is bool: "False" (False), "True" (True)*
- `bool(x)` *`False` value if x is 0, None, or an empty string, list, or collection.*

With variable and dot: `x.` (*possible type operations*)



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


## Control Sentences

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
## Loop sentences

```python
while condition:  # while statement
for current_val in sequence:  # for statement

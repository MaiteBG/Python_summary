#### [Return to README.md](../../README.md)

# Variables: Basic Types, Scope and Environment

<!-- TOC -->
  * [Variable in python](#variable-in-python)
  * [1. Numeric variables](#1-numeric-variables)
    * [1.1. Class `int`](#11-class-int)
      * [1.1.1. Numeric Bases](#111-numeric-bases)
      * [1.1.2. Using the `int` Constructor](#112-using-the-int-constructor)
      * [1.1.3. Random `int` number](#113-random-int-number)
    * [1.2. Class `float`](#12-class-float)
      * [1.2.1. Exponential Notation](#121-exponential-notation)
      * [1.2.2. Infinity values](#122-infinity-values)
      * [1.2.3. NaN(Not a Number)](#123-nannot-a-number)
  * [2. Class `bool`](#2-class-bool)
  * [3. Class `str` ( Strings)](#3-class-str--strings)
    * [3.1. String Operations](#31-string-operations)
    * [3.2. String format](#32-string-format)
      * [3.2.1. General String Formatting Syntax `{value:format_specification}`](#321-general-string-formatting-syntax-valueformat_specification)
      * [3.2.2. **f-string** (recommended): `f'Hola {variable}'`](#322-f-string-recommended-fhola-variable)
      * [3.2.3. **Formatting `%`:**](#323-formatting-)
      * [3.2.4. **Format method** (more complex and less commonly used): `'Hello {}'.format(variable)`](#324-format-method-more-complex-and-less-commonly-used-hello-formatvariable)
      * [3.2.5. **String Alignment**:](#325-string-alignment)
    * [3.3. Special Characters](#33-special-characters)
    * [3.4. String Methods (do not replace the original string!)](#34-string-methods-do-not-replace-the-original-string)
      * [3.4.1. Case and Space Management](#341-case-and-space-management)
      * [3.4.2. Substring Handling](#342-substring-handling)
      * [3.4.3. String Modification and Repetition](#343-string-modification-and-repetition)
    * [3.5. Character coding and encoding](#35-character-coding-and-encoding)
      * [3.5.1. Unicode](#351-unicode)
      * [3.5.2. UTF-8](#352-utf-8)
      * [3.5.3. ASCII](#353-ascii)
  * [4. Data type conversion](#4-data-type-conversion)
  * [5. Scope of a variable](#5-scope-of-a-variable)
    * [5.1. Use of a global/nonlocal variable](#51-use-of-a-globalnonlocal-variable)
    * [5.1. Class and Object/Instance Variables](#51-class-and-objectinstance-variables)
  * [6. Environment variables (`.env` file)](#6-environment-variables-env-file)
<!-- TOC -->

## Variable in python

**Dynamic typing**: Variables can store any type of data and change its type without explicit casting.
**Objects**: Variables in Python are objects (from class of their type): references stored in the *stack* and point to data in the *heap*.

- `id(my_var)`: position of memory of the variable object.
- `type(my_var)`: class of the object stored in my_var (variable type of my_var)
- With variable and dot: `x.` (*possible type operations of its class*)

**Mutability**: If the value of a variable changes, a new object is created with the updated data, and the variable points to this new reference.

**Initialization**: Variables must be declared with an initial value.

- `NoneType`: Represents absence of value (`None`).

**`del var_name`:**

* **Free memory:** delete big objects (like lists or data) when you don’t need them anymore to save memory.
* **Clean workspace:** remove variables in interactive environments like Jupyter or the Python shell.
* **Delete from a list or dict:** use `del` to remove an item from a list by index or from a dictionary by key.
* **Avoid reuse:** delete a variable to make sure it’s not used again by mistake.

## 1. Numeric variables

### 1.1. Class `int`

#### 1.1.1. Numeric Bases

- **Decimal (base 10 - default)**: Any number without a prefix, like `123`.
- **Binary (base 2)**: Prefixed with `0b` or `0B`. Example: `0b101` equals 5 in decimal.
- **Octal (base 8)**: Prefixed with `0o` or `0O`. Example: `0o7` equals 7 in decimal.
- **Hexadecimal (base 16)**: Prefixed with `0x` or `0X`. Example: `0xA` equals 10 in decimal, and `0x1F` equals 31 in decimal.

#### 1.1.2. Using the `int` Constructor

- Create integers from strings in any base using `int(string, base)`. Examples:
  ```python
  num = int("101", 2)  # Binary to decimal, result is 5
  num = int("17", 8)   # Octal to decimal, result is 15
  num = int("A", 16)   # Hexadecimal to decimal, result is 10

  ```

#### 1.1.3. Random `int` number

- Use the `randint(a, b)` function from the `random` module to generate a random integer between `a` and `b` (inclusive). Example:
  ```python
  import random
  random_num = random.randint(1, 10)  # Generates a number between 1 and 10
  ```

### 1.2. Class `float`

#### 1.2.1. Exponential Notation

- Floats can be represented in exponential (scientific) notation
  ```python
  my_var = 3e5  # Equivalent to 300000.0
  my_var = 0.00003  # Can also represent very small values
  ```

#### 1.2.2. Infinity values

- Python supports positive and negative infinity

```python
import math
from decimal import Decimal

# Positive infinity
positive_infinity = float('inf')  # Using float
positive_infinity = math.inf      # Using math
positive_infinity = Decimal('Infinity')  # Using Decimal

# Negative infinity
negative_infinity = float('-inf')  # Using float
negative_infinity = -math.inf      # Using math
negative_infinity = -Decimal('Infinity')  # Using Decimal

# Check if a value is infinite
is_infinite = math.isinf(value)  # Returns True if the value is infinite
```

#### 1.2.3. NaN(Not a Number)

- Represents undefined or unrepresentable numeric data

```python
from decimal import Decimal
import math

# Define NaN
my_var = float("NaN")  # Using float
my_var = Decimal("NaN")  # Using Decimal

# Check if a value is NaN
is_nan = math.isnan(my_var)  # Returns True if the value is NaN
```

## 2. Class `bool`

The `bool` class represents Boolean values (`True` and `False`).
- A value is `False` if is `0` , `None`, an empty string (`""`) or an empty collection (`[]`, `{}`, `()`).
- Any other value is `True` (also NaN)

## 3. Class `str` ( Strings)

- **Defining Strings**: Strings can be defined using `'`, `"`, or `'''`. Triple quotes allow line breaks to be included directly within the text.
- **Character Indexing**:

  - Characters are indexed from `0` to `length-1`.
  - Negative indexing allows access to characters from the end of the string: `string[-1]` retrieves the last character.
- **Immutability**: Strings cannot be modified after they are created.

### 3.1. String Operations

**Concatenation**:   Use `+` or `+=`: `string_1 + string_2` or `string_1 += string_2`

- *For literals string only: an space `lit_string_1 lit_string_2`*

**Joining**: Combine list elements using a separator:

- Using `split_string.join([list of strings])`
  - e.i. if `' '.join(stringX)` is used, it adds space bettween characters.

**Splitting**: Divide a string into parts:

- To split a string into a list, use `text.split(separator)`. By default, the separator is a space.

### 3.2. String format

#### 3.2.1. General String Formatting Syntax `{value:format_specification}`

This format specification syntax lets you control how values are displayed within strings. 

It applies to all fundamental data types. including integers, floats, and strings, providing precise control over formatting output.

`{value:[fill][align][sign][#][0][width][,][.precision][type]}`:


| Component    | Meaning (Strings, Numbers)                               |
| ------------ | -------------------------------------------------------- |
| `fill`       | Padding character (`*`,`-`, etc.)                        |
| `align`      | `<`left,`>`right,`^`center,`=`(numbers: pad after sign)  |
| `sign`       | `+`/`-`/ space (only for numbers)                        |
| `#`          | Use prefix for bases (`0x`,`0b`, etc. with`x`,`b`,`o`)   |
| `0`          | Zero-padding (numbers only, shorthand for`fill='0'`)     |
| `width`      | Total field width                                        |
| `,`          | Add comma as thousand separator (numbers)                |
| `.precision` | Number of decimal digits (floats) / max length (strings) |
| `type`       | `f`,`e`,`d`,`s`, etc. depending on the variable type     |

Examples: 
```python
text = "hi"
f"{text:*^6}"     # '**hi**'
f"{text:.3}"      # 'hi'  (up to 3 characters)

num = 42
f"{num:06d}"      # '000042'
f"{num:+5d}"      # '  +42'
f"{num:#x}"       # '0x2a' (hex with prefix)

val = 12.3456
f"{val:>10.2f}"   # '     12.35'
f"{val:010.2f}"   # '000012.35'
f"{val:.1e}"      # '1.2e+01'
```


#### 3.2.2. **f-string** (recommended): `f'Hola {variable}'`

- It is possible to specify formats, for example: `f"{num1:.2f}`.


#### 3.2.3. **Formatting `%`:**

- Insert values using placeholders (%i, %x %s, %d, %.f)
  - `"%s %d %.2f"%(string_var, int_var, float_var)`
  - `"%(str_var)s %(int_var)d %(float_var).2f"%{'str_var': string_var,  'int_var':int_var, 'float_var':float_var}`


####  3.2.4. **Format method** (more complex and less commonly used): `'Hello {}'.format(variable)`

- You can specify the order of variables using indices `{0} {2} {1}`; otherwise, they are inserted in order.
  - It is also possible to specify formats, for example: `{0:.2f}`.
- You can indicate variable names, e.g., `{name}` and use `.format(name=variable)`.
  - With dictionaries, you can also use `{dict[key]}`: `.format(dict=dictionary)`.

####  3.2.5. **String Alignment**:

- **Center**: `string.center(num, fill_character)` can center the content of a string, padded with the specified `fill_character` to make the total length `num` (useful for printing titles).
- **Left or Right Alignment**:
  - Left: `string.ljust(num, fill_character)`
  - Right: `string.rjust(num, fill_character)`

```python
title = "Hello"
print(title.center(10, "-"))  # Output: "---Hello---"
print(title.ljust(10, "-"))  # Output: "Hello-----"
print(title.rjust(10, "-"))  # Output: "-----Hello"
```

### 3.3. Special Characters

- The backslash (`\`) is used to include special characters:

  - `\n`: New line.
  - `\t`: Tab.
  - `\b`: Back space (delete last character)
    - `\b\b`: Back spaces (delete last [\b items] characters)
  - `\\`: Backslash (`\`).
  - `\'`: Single quote within single-quoted strings.
- User of raw string: `r'String with special caracteres showed literaly'`

### 3.4. String Methods (do not replace the original string!)

#### 3.4.1. Case and Space Management

- **Change Case**: `str1.upper()`, `str1.lower()`, `str1.title()`, `str1.capitalize()`.
- **Check Case**: `str1.islower()`, `str1.isupper()`.
- **Remove leading and/or trailing characters**:
  - **Spaces**: `str1.strip()`, `str1.lstrip()`, `str1.rstrip()`
  - **other characters** Apply the same methods to remove specific characters (e.g. *):
    - `str1.strip('*')`, `str1.lstrip('*')`, `str1.rstrip('*')`
- **Measure Length**: `len(str1)`.

#### 3.4.2. Substring Handling

- **Extract Substring**: `str1[start:end]` (end index is excluded).
- **Find Substring**: `str1.find(substring)` (returns -1 if not found).
- **Count Substring**: `str1.count(substring)`.
- **Check Membership**: `"substring" in str1`.
- **Starts or Ends With**: `str1.startswith(prefix)`, `str1.endswith(suffix)`.

#### 3.4.3. String Modification and Repetition

- **Replace Substring**: `str1.replace(old_substr, new_substr)`.
- **Split and Join**:
  - `str1.split(sep)` Splits into a list using a separator (default is space).
  - `"separator".join(list)` Joins list elements into a single string.
- **Partition Substring**: `str1.partition(substring)` Splits the string into a tuple: `(before, substring, after)` based on the first occurrence of `substring`.
- **Repeat String**: `str1 * n` Repeats the string `n` times.
- **Format Strings**: `str1.center(width, character)` → Centers the string within a specified width, padded with `character`.

### 3.5. Character coding and encoding

#### 3.5.1. Unicode

A universal standard assigning unique hexadecimal codes to all characters, including icons and symbols.

- Example: `A` is `U+0041`, and `ñ` is `U+00F1`.
- **Usage in Python 2**:

  - Python 2 does not use Unicode by default; strings are **ASCII**.
  - To work with Unicode, use `u"..."` to define Unicode strings.
- **Usage in Python 3**:

  - Strings (`str`) are Unicode by default, requiring no additional declarations.

#### 3.5.2. UTF-8

A widely-used encoding that represents Unicode characters using 1 to 4 bytes.

- Example: `A` is encoded as `\x41` (1 byte), and `ñ` as `\xc3\xb1` (2 bytes).
- **Usage in Python 2**:

  - You must explicitly set UTF-8 encoding at the beginning of the file using `# -*- coding: utf-8 -*-`.
  - Unicode strings can be encoded to UTF-8 with `.encode("utf-8")`.
- **Usage in Python 3**:

  - **UTF-8** is the default encoding for reading, writing files, and external data operations.
  - Unicode strings are encoded to UTF-8 using `.encode("utf-8")`.
    ```python
    unicode_string = "Mañana 😀" # Unicode string
    print(unicode_string)
    utf8_string =unicode_string.encode('UTF-8') # Encode to utf8
    print(utf8_string)  # > b'Ma\xc3\xb1ana \xef\xb7\xbc'
    decode_utf8_string =utf8_string.decode('UTF-8') # Decode from utf8
    print(decode_utf8_string) # > "Mañana 😀"
    ```

#### 3.5.3. ASCII

A basic encoding representing 128 characters using 1 byte (7 bits). It includes English letters, digits, and common symbols.

- Example: `A` is encoded as `65` in decimal or `\x41` in hexadecimal. It does not support special characters like `ñ`.
- **Usage in Python 2**:

  - Strings are encoded in **ASCII** by default, limited to 128 characters.
  - Attempting to use non-ASCII characters without proper setup causes errors. *`# -*- coding: utf-8 -*-` to change to UTF-8.*
- **Usage in Python 3**:

  - ASCII is compatible as a subset of Unicode, and basic characters are handled similarly.
    ```python
    bstring = b"..." # Only ASCII literal characters
    print(bstring[0]) # Print ASCII code from the character in position 0
    ```
- Encode Unicode (or UTF-8) to ASCII with error handling:

  ```python
  unicode_string = "Mañana 😀" # Unicode string

  # Attempt to encode as ASCII with error handling
  ascii_string = unicode_string.encode("ascii", "ignore").decode("ascii")
  print(ascii_string.decode("ascii"))  # Output: "Maana "(ñ and icon are removed)

  # Alternatively, replace unsupported characters
  ascii_string_replace = unicode_string.encode("ascii", "replace")
  print(ascii_string_replace.decode("ascii"))  # Output: "Ma?ana ?" (? replaces ñ and icon)
  ```

## 4. Data type conversion

To convert a variable to another type, we use de constructor of the new class type:

- `int(x)`, `float(x)`, `str(x)`, `bool(x)`.
- Other conversions: e.g. `hex(x)` *hexadecimal*.

* [Dynamic String Evaluation](files_and_manager_context.md#12-dynamic-string-evaluation) from string on input data contexts. 

## 5. Scope of a variable

### 5.1. Use of a global/nonlocal variable

- `global`: Use it to modify a variable defined at the **module/global scope**.

  ```python
  variable_name = value  # varaible in global scope

  def function(...):
     # indicate that we are going to use global scope variable
      global variable_name   
      variable_name = values...  # or other use of variable_name
  ```
- `nonlocal`: Use it to modify a variable from the **enclosing function**, in a **nested function**.

  ```python
  def outer():
      count = 0

      def inner():
          nonlocal count
          count += 1

      inner()
      return count
  ```

* Use `global` and `nonlocal` only when it's strictly necessary to modify the value of a variable defined in an outer scope. These keywords make the code harder to understand and maintain, and can cause unintended side effects.

> Coding standards (such as **PEP 8**) do not recommend using `global` and `nonlocal` unnecessarily.
>
> * Only if you need to assign a new value to them.
> * Only when you have a strong reason (e.g., shared configuration or state).

### 5.1. Class and Object/Instance Variables

From the **class**, you can only access and modify **class variables** — not instance attributes.

From an **instance**, you can access both **instance variables** and **class variables**. However, if you try to directly modify a class variable from an instance, it will **create a new instance variable** with the same name, rather than modifying the shared class variable. In other words, the instance variable will **shadow** the class variable.

* To avoid this, **do not use `self` to access class variables**. Instead, use `ClassName.var_x` or `self.__class__.var_x`.

## 6. Environment variables (`.env` file)

In Python, `.env` files are used to store environment variables in a simple key-value format. These files are helpful for managing sensitive information, such as API keys, database credentials, or configuration settings, without hardcoding them into your application.

> The `.env` file should be placed at the root of your project and must be added to `.gitignore` to prevent it from being committed to version control.

The  library `python-dotenv` allows you to easily load the variables from a `.env` file into your environment.

- You can use the `load_dotenv()` function provided by the library to access these variables, which can then be retrieved using `os.getenv()`.

This approach improves security, facilitates collaboration, and keeps your code clean and adaptable across different environments (development, testing, production).

`.env` file fromat example:

```
POSTGRE_USER=postgres
POSTGRE_HOST=localhost
POSTGRE_PORT=5432
POSTGRE_DB=test_db
```

Use of `python-dotenv` libray to get variable content from `.env` :

```python
import os
from dotenv import load_dotenv  # para importar las varaibles del .env
load_dotenv()
_USERNAME = os.getenv('POSTGRE_USER')
```

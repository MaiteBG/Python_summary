#### [Return to README.md](../README.md)

# Basic Operations in Python

<!-- TOC -->
  * [1. Arithmetic operators](#1-arithmetic-operators)
  * [2. Assignment](#2-assignment)
    * [2.1. Value exchange without temporary variable](#21-value-exchange-without-temporary-variable)
    * [2.2. Compound assignments](#22-compound-assignments)
  * [3.3. Conditional and logical operators](#33-conditional-and-logical-operators)
  * [3.4. Operator Precedence in Python](#34-operator-precedence-in-python)
  * [3. Unpacking Operator](#3-unpacking-operator)
    * [3.1. For Lists (`*`)](#31-for-lists-)
    * [3.2. For Dictionaries (`**`)](#32-for-dictionaries-)
<!-- TOC -->

## 1. Arithmetic operators

- `+` `-` `*` `/` *float division*
- `//` *integer division*
- `%` *module*
- `**` *power*
* ***NOTE:*** If one of the operands is float, the result is always float.
## 2. Assignment

- `var_x = value` *Assigns a value to a variable.*
- Multiple assignment: `var_x, var_y, var_z = value_x, value_y, value_z` 
  - *Assigns values to multiple variables in a single line.*
- Chained assignment: `var1 = var2 = … = value` 
  - *Assigns the same value to multiple variables.*

### 2.1. Value exchange without temporary variable
- `x, y = y, x` 
  - *Swaps the values of `x` and `y` without using a temporary variable.*

### 2.2. Compound assignments
- `variable OPERATOR = value` 
  - *Equivalent to `variable = variable OPERATOR value`
``` python
x += 5  # Same as x = x + 5
```

---

## 3.3. Conditional and logical operators

- **Return a boolean result**
- **Conditional**: `< > <= >= == !=`
  - *Can use multiple operands: `value_min <= value_x <= value_max`.*
  - *For strings, compares based on ASCII values.*

- **Logical**: `and` `or` `not`
  - *Use `not` to check if a variable is empty. For example: `if not var_x`, returns `True` if `var_x` is empty.*

## 3.4. Operator Precedence in Python
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

## 3. Unpacking Operator

The unpacking operator (`*` for iterables, `**` for dictionaries) expands collections into individual elements.

### 3.1. For Lists (`*`)
- Expanding elements in function calls `print(*[1, 2, 3])`  
- Combining multiple lists `[*list1, *list2]`  
- Unpacking into separate variables `a, b, c = *[1, 2, 3]`  
- Flattening nested lists `[*sublist for sublist in nested_list]`  
- Converting iterables to lists `list(range(3)) → [0, 1, 2]`  

### 3.2. For Dictionaries (`**`)
- Merging multiple dictionaries `{**dict1, **dict2}`  
- Passing dictionary contents as keyword arguments `func(**{'x': 1})`  
- Updating dictionary contents `dict1.update(**dict2)`  
- Combining with additional key-value pairs `{**dict1, 'z': 3}`  
- Unpacking into function parameters `def f(x): return x` followed by `f(**{'x': 5})`  
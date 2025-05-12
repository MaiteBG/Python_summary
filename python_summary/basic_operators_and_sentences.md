#### [Return to README.md](../README.md)

# Operators and Sentences

<!-- TOC -->
  * [1. Operators](#1-operators)
    * [1.1. Arithmetic Operators](#11-arithmetic-operators)
    * [1.2. Relational Operators](#12-relational-operators)
      * [1.2.1. Comparison (Conditional) Operators](#121-comparison-conditional-operators)
      * [1.2.2. Logical Operators: `and`, `or`, `not`](#122-logical-operators-and-or-not)
      * [1.2.3. Identity Operators: `is`, `is not`](#123-identity-operators-is-is-not)
      * [1.2.4. Membership Operators: `in`, `not in`](#124-membership-operators-in-not-in)
    * [1.3. Bitwise Operators](#13-bitwise-operators)
    * [1.4. Conditional Expressions: `if-else` (Ternary Conditional Expressions)](#14-conditional-expressions-if-else-ternary-conditional-expressions)
    * [1.5. Assignment Operators](#15-assignment-operators)
      * [1.5.1. Value Exchange without Temporary Variable](#151-value-exchange-without-temporary-variable)
      * [1.5.2. Compound Assignments](#152-compound-assignments)
      * [1.5.3. Unpacking Operator](#153-unpacking-operator)
    * [1.6. Operator Precedence](#16-operator-precedence)
  * [2. Sentences](#2-sentences)
    * [2.1. Control Sentences](#21-control-sentences)
      * [2.1.1. Traditional Control Sentences](#211-traditional-control-sentences)
      * [2.1.2. Pattern Matching (Python 3.10+)](#212-pattern-matching-python-310)
      * [2.1.3. Alternative to Switch Statement Using Dictionaries (Before Pattern Matching)](#213-alternative-to-switch-statement-using-dictionaries-before-pattern-matching)
    * [2.2. Loop Sentences](#22-loop-sentences)
      * [2.2.1. `while` Loop](#221-while-loop)
      * [2.2.2. `for` Loop](#222-for-loop)
      * [2.2.3. Control Flow in Loops](#223-control-flow-in-loops)
  * [3. Empty Statements: `pass` and `...`](#3-empty-statements-pass-and-)
<!-- TOC -->

## 1. Operators

Operators are basic symbols and expressions for performing operations on data.

### 1.1. Arithmetic Operators

Perform mathematical operations such as addition, subtraction, multiplication, etc.

* `+`, `-`, `*`, `/` — *Float division*
* `//` — *Integer division*
* `%` — *Modulo*
* `**` — *Exponentiation*

> Note: If at least one operand is a float, most operations will return a float to maintain precision.

### 1.2. Relational Operators

Relational operators are used to compare values and return a boolean result (`True` or `False`). These operators help in
determining relationships between values, often used in conditional statements and loops.

#### 1.2.1. Comparison (Conditional) Operators

Comparison operators are used to compare two values and return a boolean result based on their relationship.

* `<`, `>`, `<=`, `>=`, `==`, `!=`
* **Additional Notes:**

    * Comparisons can be chained for more concise expressions:
        * Example: `min_val <= x <= max_val`
    * String comparisons are based on the character code order (either Unicode or ASCII), meaning they follow
      lexicographical (alphabetical) order for text strings.

#### 1.2.2. Logical Operators: `and`, `or`, `not`

Logical operators are used to combine or modify boolean values and expressions.

* `and`: Returns `True` if both conditions are true.
* `or`: Returns `True` if at least one condition is true.
* `not`: Reverses the truth value of the given condition.

#### 1.2.3. Identity Operators: `is`, `is not`

Identity operators are used to compare the memory locations of two objects, checking if they are the exact same object
in memory.

**Common Identity Operators:**

* `is`: Returns `True` if both operands refer to the same object.
* `is not`: Returns `True` if both operands do not refer to the same object.

> Note: `==` compares values for equality, while `is` checks if two variables reference the exact same object.

#### 1.2.4. Membership Operators: `in`, `not in`

Membership operators check if a value is a member of a sequence (such as a list, tuple, or string) and return a boolean
result.

**Common Membership Operators:**

* `in`: Returns `True` if the value is found within the sequence.
* `not in`: Returns `True` if the value is not found within the sequence.

Example: * `'a' in 'apple'`: `True` if `'a'` is found in the string `'apple'`.

### 1.3. Bitwise Operators

**Bitwise Operators** are used to manipulate individual bits of integers. These operators work on the binary
representations of numbers, where each bit is treated independently.

* **AND (`&`)** operator compares corresponding bits of two numbers and returns 1 only if both bits are 1. Otherwise, it
  returns 0.
* **OR (`|`)** operator compares corresponding bits of two numbers and returns 1 if at least one of the bits is 1. If
  both are 0, it returns 0.
* **XOR (`^`)** operator compares corresponding bits and returns 1 if the bits are different (i.e., one is 1 and the
  other is 0). If they are the same, it returns 0.
* **NOT (`~`)** operator inverts all the bits, flipping 0s to 1s and 1s to 0s. This operation is also known as bitwise
  negation.
* **Left Shift (`<<`)** operator shifts the bits of a number to the left, effectively multiplying the number by powers
  of two for each shift.
* **Right Shift (`>>`)** operator shifts the bits of a number to the right, effectively dividing the number by powers of
  two for each shift.

### 1.4. Conditional Expressions: `if-else` (Ternary Conditional Expressions)

Ternary conditional expressions allow you to return one value if a condition is `True`, and another if it's `False`, all
within a single line.

* `result = value_if_true if condition else value_if_false`

### 1.5. Assignment Operators

* **Simple assignment**: Assigns a value to a variable.
    * `var_x = value`
* **Multiple assignment**: Assigns values to multiple variables in a single line.
    * `var_x, var_y, var_z = value_x, value_y, value_z`
* **Chained assignment**: *Assigns the same value to multiple variables.*
    * `var1 = var2 = … = value`

#### 1.5.1. Value Exchange without Temporary Variable

Python allows elegant value swapping in a single line.
This avoids the need for a temporary variable and makes the code cleaner.

```python
x, y = y, x  # Swaps values of x and y
```

#### 1.5.2. Compound Assignments

Used to update the value of a variable using an operation:
`variable <operator>= expression` is equivalent to variable = variable <operator> expression

```python
x += 5  # Same as x = x + 5
```

#### 1.5.3. Unpacking Operator

The [unpacking operator](collections.md#7-unpacking-) (`*` for iterables, `**` for dictionaries)
expands [collections](collections.md) into individual elements.

```python
# Unpacking in Lists/Tuples
numbers = [1, 2, 3]
a, b, c = numbers  # Unpacks the list into individual variables
print(a, b, c)  # Output: 1 2 3

# Unpacking Dictionaries
data = {"x": 10, "y": 20}
x, y = data.values()  # Unpacks dictionary values into variables
print(x, y)  # Output: 10 20
```

### 1.6. Operator Precedence

Python applies operations in the following order:

1. **Parentheses**: `()`
2. **Exponentiation**: `**`
3. **Unary Operators**: `+`, `-`, `~`
4. **Multiplication / Division / Modulus**: `*`, `/`, `//`, `%`
5. **Addition / Subtraction**: `+`, `-`
6. **Bitwise Shift**: `<<`, `>>`
7. **Bitwise AND**: `&`
8. **Bitwise XOR**: `^`
9. **Bitwise OR**: `|`
10. **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
11. **Logical NOT**: `not`
12. **Logical AND**: `and`
13. **Logical OR**: `or`
14. **Conditional Expressions**: `if-else`
15. **Assignments**: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, etc.

> ### Step-by-Step Evaluation Example
>
> `result = "Greater" if x + 5 > y and x % 2 == 0 else "Smaller or Equal"`
>
> * **Expression Before `if`**: `x + 5 > y and x % 2 == 0`
>  * First, the arithmetic operation `x + 5` is evaluated.
>  * Then, the condition `x + 5 > y` is checked.
>  * Next, the modulo operation `x % 2 == 0` is evaluated.
> * The logical operator `and` combines both conditions.
> * **Result**: If the condition evaluates to `True`, `"Greater"` is assigned. If it evaluates to `False`,
    `"Smaller or Equal"` is assigned.
> * **Final Assignment**: Based on the result of the condition, the variable `result` will be assigned either
    `"Greater"` or `"Smaller or Equal"`.

## 2. Sentences

A sentence is a single line of code that performs a specific action. These are the fundamental building blocks of a
program and can execute a wide range of operations.

> **Note:** Python automatically converts variables to a boolean when used in control statements (e.g., `if`, `while`).
> There’s no need for manual conversion.

### 2.1. Control Sentences

Control sentences allow you to direct the flow of your program based on conditions.

#### 2.1.1. Traditional Control Sentences

* `if`, `elif`, `else`

The [Ternary operator](#14-conditional-expressions-if-else-ternary-conditional-expressions). also uses control
sentences.

``` python
# Simple example using if, elif, else
x = 10

if x > 15:
    print("x is greater than 15")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")
```

#### 2.1.2. Pattern Matching (Python 3.10+)

Python does not have a built-in switch statement. However, starting with Python 3.10, a more powerful alternative called
Pattern Matching was introduced. It allows you to match patterns in data structures and perform more advanced
conditional operations.

```python
def switch_demo_v2(argument):
    match argument:
        case 1:
            return "Opción 1 seleccionada"
        case 2:
            return "Opción 2 seleccionada"
        case 3:
            return "Opción 3 seleccionada"
        case _:
            return "Opción no válida"  # The wildcard (_) is used to handle any other case not explicitly matched

```

#### 2.1.3. Alternative to Switch Statement Using Dictionaries (Before Pattern Matching)

Before the introduction of Pattern Matching, Python didn't have a switch statement. However, you could simulate this
behavior using dictionaries.
This method maps keys to functions, and depending on the key, the corresponding function will be executed.

```python
# Define functions for different actions
def process_order(): return "Processing your order."


def ship_order(): return "Shipping your order."


def cancel_order(): return "Canceling your order."


# Simulate a switch statement using a dictionary
def order_action(action_code):
    actions = {
        1: process_order,  # Action 1: Process the order
        2: ship_order,  # Action 2: Ship the order
        3: cancel_order  # Action 3: Cancel the order
    }
    # Return the result of the function corresponding to the action code,
    # or a default message if the action code is not found
    return actions.get(action_code, lambda: "Invalid action code.")()


# Test the function
print(order_action(1))  # Output: Processing your order.
print(order_action(4))  # Output: Invalid action code.


```

### 2.2. Loop Sentences

Loop sentences allow for repeating a block of code multiple times based on a condition or a sequence.

#### 2.2.1. `while` Loop

The `while` loop runs a block of code as long as the given condition is `True`.
It is useful for situations where the number of iterations is unknown beforehand and depends on the condition.

```python
while condition:
# Code to execute
```

#### 2.2.2. `for` Loop

The `for `loop is used for iterating over sequences (such as lists, tuples, strings, etc.) or any iterable object.

```python

for current_val in sequence:
# Code to execute
```

You can also loop over `ranges` or `enumerate` collections.

- `range()` function is commonly used when you need to iterate a specific number of times.

``` python
for _ in range(5):  # Use `_` if loop variable is not needed
    # Code to execute
```

- `enumerate()` is useful when you need both the index and value from a collection. It returns pairs of (index, value).

``` python  
for idx, val in enumerate(collection):
    # Code to execute
```

> #### Nested Loops
> You can also nest loops inside other loops to perform more complex iterations.
> ```python
> for i in range(3):
>    for j in range(2):
>        print(f"i: {i}, j: {j}")
> ``` 

#### 2.2.3. Control Flow in Loops

Control flow statements inside loops can modify their behavior:

* `break`: Exits the loop immediately, regardless of the condition.

``` python
while True: 
    # Some condition
    if condition_met:
        break  # Exit the loop
```

* `continue`: Skips the current iteration and proceeds to the next one.

``` python
for val in range(10):
    if val % 2 == 0:
        continue  # Skip even numbers
    print(val)
```


## 3. Empty Statements: `pass` and `...`

In Python, **`pass`** and **ellipsis (`...`)** are used as placeholder statements, allowing you to maintain syntactic structure when no operation is needed. Both serve important purposes in different scenarios:

- **`pass`**: A clearer and more explicit placeholder, typically used when defining an empty class, function, or loop. It ensures that Python doesn’t raise an error when the body is left empty.
  
  - To define an empty class, use `pass`:
    ```python
    class MyClass:
        pass
    ```

- **`...` (ellipsis)**: Can be used in more specific contexts, often as a temporary marker or placeholder for future code. It has the same behavior as `pass` in some cases but is used more flexibly.
  
  - Example of using `...` as a placeholder:
    ```python
    def future_function():
        ...
    ```

**Key Uses**:
- **Avoid errors**: Prevents `IndentationError` or `SyntaxError` when you need an empty block.
- **Serve as a placeholder**: Marks parts of code that are yet to be implemented.
- **Maintain syntactic structure**: Keeps your code syntactically valid while awaiting further implementation.
- **Debugging purposes**: Used temporarily during development to avoid incomplete code from causing issues.



#### [Return to README.md](../README.md)

# Collection Types

<!-- TOC -->
  * [1. List `my_list = [item_1, item_2, item3]`](#1-list-my_list--item_1-item_2-item3)
    * [1.1. Operations with lists](#11-operations-with-lists)
  * [2. Tuple `my_tuple = (item_1, item_2, item_3)`](#2-tuple-my_tuple--item_1-item_2-item_3)
    * [2.1. Operations with tuples](#21-operations-with-tuples)
  * [3. Set `my_set = {item_1, item_2, item_3}`](#3-set-my_set--item_1-item_2-item_3)
    * [3.1. Operations with sets](#31-operations-with-sets)
  * [4. Dictionary `my_dictionary = {key_1: value_1, key_2: value_2}`](#4-dictionary-my_dictionary--key_1-value_1-key_2-value_2)
    * [4.1. Operations with dictionaries](#41-operations-with-dictionaries)
  * [5. Collections consisten format on manual definition](#5-collections-consisten-format-on-manual-definition)
  * [6. List comprehension `[operation for element in iterable if condition]`](#6-list-comprehension-operation-for-element-in-iterable-if-condition)
  * [7. Unpacking (tuples, lists, strings)](#7-unpacking-tuples-lists-strings)
  * [8. Zip function](#8-zip-function)
<!-- TOC -->

## 1. List `my_list = [item_1, item_2, item3]`
- Items can be of different types
- Ordered and mutable
- Dynamic: can add, modify, and remove elements

### 1.1. Operations with lists

- **Consult**  
  - `len(my_list)` - Get the length of the list.  
  - `my_list[index_x]` - Access an item at index `x`.  
  - `my_list[index_ini:index_fin+1]` - Slice the list from `index_ini` to `index_fin`.  
  - `for value in my_list:` - Iterate through the list.  
  - **Find Index**: `my_list.index(value)` - Returns the index of the first occurrence of `value` in the list (raises an error if not found).  

- **Order**:  
  - **Modifies `my_list`**
    - Ascending: `my_list.sort()` - Sorts the list in ascending order (modifies `my_list`).
    - Descending: `my_list.sort(reverse=True)` - Sorts the list in descending order (modifies `my_list`).  
    - Custom Parameter: `my_list.sort(key=custom_parameter)` (e.g., `key=len` to sort by the length of elements).
    - Reverse: `my_list.reverse()` - Reverses the order of elements in the list, without sorting (modifies `my_list`).  
  - Does not modify `my_list`:
    - `sorted(my_list)` (also `reveres` and `key` parameters)
    - `list(reversed(my_list))`
    
- **Add**  
  * At the end of the list: `my_list.append(new_item)`  
  * At a specific index: `my_list.insert(index_x, new_item)` (*other elements shift to the right*)  
  * Extend the list with multiple items: `my_list.extend(iterable)` 
    * *Modifies `my_list` by appending all elements from `iterable`*
  
-**Concatenate**
  * Only for list and tuples can concatenate `list_1 + list_2` 
  * Using unpacking operator `[*list_1, *list_2]`

- **Remove**  
  * By value: `my_list.remove(value)`  
  * By index: `my_list.pop(index_x)` or `del my_list[index_x}`  


- **Copy**:  
* Creating a duplicate of a list to ensure that modifications to the new list do not impact the original.
  - **`.copy()` method**: Creates a shallow copy of the list.  
  - **List slicing**: Uses `[:]` to create a new list that replicates the original.  
  - **`list()` constructor**: Converts the original list into a new list.  
  - **`copy.deepcopy()`**: From the `copy` module, creates a deep copy of nested lists or objects, ensuring full independence from the original.  


## 2. Tuple `my_tuple = (item_1, item_2, item_3)`
or `my_tuple = item_1, item_2, item_3`

*only one element with a comma at end `my_tuple = item_1,`*

- Items can be of different types
- Ordered but **immutable** (No can add, modify and drop elements)

Oly for list and tuples can concatenate `tuple_1 + tuple_2`

### 2.1. Operations with tuples

**Consult and order**  
* `my_tuple[index_x]` - Access an item at index `x`  
* `my_tuple[index_ini:index_fin+1]` - Slice the list from `index_ini` to `index_fin`  


## 3. Set `my_set = {item_1, item_2, item_3}`

- The items can be of different types, but they must all be immutable.
- Not ordered and unique (no duplicated elements)
- Mutable

To create an empty set in Python, use the set() constructor. This is important because {} by itself creates an empty dictionary, not an empty set.
`my_set = set()`.

### 3.1. Operations with sets

**Consult**  
- `len(my_set)`  
- `for item in my_set:`  
- Check if value exists: `value_x in my_set`

**Add and remove**  
- `my_set.add(new_item)`  
- `my_set.remove(value)`  
- `my_set.update(other_iterable)` Add elements from other_iterable to my_set.

**Set operations**  
- Union: `set_1 | set_2`  also `set1.union(set_2)`
- Intersection: `set_1 & set_2`  also `set1.intersenction(set_2)`
- Difference: `set_1 - set_2`   also `set1.difference(set_2)` (not commutative)
- Symmetric difference ( is communicative)  set1.symetric_difference(set_2)

- Subset: `set1.issubset(set_2)`
- Superset: `set1.issuperset(set_2)`
- Disjoint `set1.isdisjoint(set_2)`


## 4. Dictionary `my_dictionary = {key_1: value_1, key_2: value_2}`

- Items can be of different types (keys are always strings)
- Ordered and mutable
- Keys must be unique (like set items and immutable type)

### 4.1. Operations with dictionaries

* **Consult:** `my_dictionary['key_x']`
  * `my_dictionary.get(key_x,default_if_not_exist)`  Do not modify diccionariy content
  * `my_dictionary.setdefault(key_x,default_if_not_exist)` If key_x no exist add key_x with  default_if_not_exist value 

* **Add or modify:** `my_dictionary['key_x'] = value_x`  

* **Delete:** `my_dictionary.pop('key_x')` or `del my_dictionary['key_x']`  

* **Iteration of elements**  
  * Tuple (key, value): `for key, value in my_dictionary.items():`  
  * Only values: `for value in my_dictionary.values():`  
  * Only keys: `for key in my_dictionary.keys():`  


>## Same reference or copy?
> In Python, when working with collections such as lists, dictionaries, and sets, it's essential to understand the difference between copying a reference and creating an actual copy of the collection. 
> - Failure to do so can lead to unintended errors and bugs.
> - Using the `copy()` method ensures that modifications to the copied collection do not impact the original collection. 
>  - This is particularly important when you need to work independently with a duplicate of the data.

- `elem_1 is elem_2 `: compare the object reference, not the content.


## 5. Collections consisten format on manual definition

When defining any collection manually, pay attention to formatting. In long collections, put each element on its own line and end each line with a comma. If you omit the comma, adjacent string literals may be concatenated. To avoid this kind of error, include a trailing comma after the last element as well.

**Simple example:**
```python
names = [
    "Alice",
    "Bob",
    "Charlie",  # trailing comma here prevents accidental concatenation
]
```

## 6. List comprehension `[operation for element in iterable if condition]`

List comprehensions allow you to create lists from other iterables by filtering or applying expressions to each element.

Apply a condition and operation with list comprehension
```python
# Create a list with the square of numbers divisible by both 2 and 3
squared_numbers = [x**2 for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(f'Squared numbers divisible by both 2 and 3: {squared_numbers}')
```

Using list comprehension with conditional statements
```python
even_numbers = []
odd_numbers = []
[even_numbers.append(number) if number % 2 == 0 else odd_numbers.append(number) for number in range(10)]
print(f'Even numbers: {even_numbers}')
print(f'Odd numbers: {odd_numbers}')
```

List comprehensions allow you to write concise and readable code. You can flatten nested structures and apply conditions all in one line (the line breaks below are only for clarity).
```python
# Example: Extract even numbers from a list of lists
lista_listas = [[1, 2, 3], [4, 5], [6, 7, 8]]

even_numbers = [
    value
    for sublist in lista_listas
    for value in sublist
    if value % 2 == 0
]

print(f'Even numbers: {even_numbers}')
```


## 7. Unpacking (tuples, lists, strings)
  * Works with any iterable (tuples, lists, strings)
  * Unpacking is a powerful feature in Python that allows you to assign elements of a sequence (like a tuple) to multiple variables in a single statement.
  * `var_1, var_2, var_3 = (item1, item2, item3)`
  * You can use `*` to capture multiple values into a single variable.
    * Non-starred variables get single items by position
    * Starred variable always gets a list (empty if no items left)
      * First: *start, x, y → start collects all before last 2
      * Middle: x, *mid, y → mid collects between first/last
      * End: x, y, *rest → rest collects all after first 2





## 8. Zip function

The `zip()` function allows us to combine multiple iterables (like lists, tuples, etc.) into a single iterable of tuples.
Each tuple contains elements from the input iterables that share the same position.
`zip()` returns a list of tuples as an object from zip class. 
```python
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
id = 34,234,34
combined = zip(id, numbers, letters)
print(list(combined))  #[(34, 1, 'A'), (234, 2, 'B'), (34, 3, 'C')]
type(combined)  #zip
```

The zip() function will only iterate up to the shortest iterable provided. This means if the input iterables have different lengths, zip() stops at the end of the shortest one.
* Note:  If we convert the result of zip() into a set, the order of the elements is not guaranteed.

One of the most useful features of the zip() function is that it allows us to iterate over multiple iterables at the same time in parallel.

```python
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
ids = ('X', 'Y', 'Z')
random_set = {'@', '#', '$'}

for number, letter, id_, symbol in zip(numbers, letters, ids, random_set):
    print(f"{number} - {letter} - {id_} - {symbol}")
```

You can also reverse the effect of zip() — this is called unzipping. 
If you have a zip object or a list of tuples, you can unpack it using the * operator to retrieve the original iterables:

```python
zip_instance = [(1, 'a'), (2, 'b'), (3, 'c')]
unzipped_numbers, unzipped_letters = zip(*zip_instance)
print(unzipped_numbers)  # (1, 2, 3)
print(unzipped_letters)  # ('a', 'b', 'c')
```

The result of zip() can be passed to the sorted() function to sort the paired elements based on default or custom criteria.
`sorted_zip_instance = sorted(zip_instance)`

You can use zip() to create a dict by combining two iterables: one for keys and one for values.

```python
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']

my_dict = dict(zip(keys, values))
print(my_dict)
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

my_dict.update(zip(some_old_keys,new_values)) # To update some keys values
```python



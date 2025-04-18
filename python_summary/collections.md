#### [Return to README.md](../README.md)

# Collection Types

<!-- TOC -->
  * [1. List `my_list = [item_1, item_2, item3]`](#1-list-my_list--item_1-item_2-item3)
    * [1.1. Operations with lists](#11-operations-with-lists)
  * [2. Tuple `my_tuple = (item_1, item_2, item_3)`](#2-tuple-my_tuple--item_1-item_2-item_3)
    * [2.1. Operations with tuples](#21-operations-with-tuples)
  * [6.2. Set `my_set = {item_1, item_2, item_3}`](#62-set-my_set--item_1-item_2-item_3)
    * [6.2.1. Operations with sets](#621-operations-with-sets)
  * [3. Dictionary `my_dictionary = {key_1: value_1, key_2: value_2}`](#3-dictionary-my_dictionary--key_1-value_1-key_2-value_2)
    * [3.1. Operations with dictionaries](#31-operations-with-dictionaries)
  * [4. List comprehension `[operation for element in iterable if condition]`](#4-list-comprehension-operation-for-element-in-iterable-if-condition)
  * [5. Unpacking (tuples, lists, strings)](#5-unpacking-tuples-lists-strings)
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


---

## 6.2. Set `my_set = {item_1, item_2, item_3}`

- Items can be of different types
- Not ordered and unique (no duplicated elements)
- Mutable

### 6.2.1. Operations with sets

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

## 3. Dictionary `my_dictionary = {key_1: value_1, key_2: value_2}`

- Items can be of different types (keys are always strings)
- Ordered and mutable
- Keys must be unique (like set items)

### 3.1. Operations with dictionaries

* **Consult:** `my_dictionary['key_x']` or `my_dictionary.get(key_x)`  

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




## 4. List comprehension `[operation for element in iterable if condition]`

* Create lists from other iterables (filter or apply expressions to each element)  
  * Example: `[x**2 for x in numbers] # do square`
  

## 5. Unpacking (tuples, lists, strings)
  * Works with any iterable (tuples, lists, strings)
  * Unpacking is a powerful feature in Python that allows you to assign elements of a sequence (like a tuple) to multiple variables in a single statement.
  * `var_1, var_2, var_3 = (item1, item2, item3)`
  * You can use `*` to capture multiple values into a single variable.
    * Non-starred variables get single items by position
    * Starred variable always gets a list (empty if no items left)
      * First: *start, x, y → start collects all before last 2
      * Middle: x, *mid, y → mid collects between first/last
      * End: x, y, *rest → rest collects all after first 2
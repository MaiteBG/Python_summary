#### [Return to README.md](../../README.md)

# Collections

<!-- TOC -->
  * [1. Collections](#1-collections)
    * [1.1. Common characteristics:](#11-common-characteristics)
    * [1.2. Main collection types in Python](#12-main-collection-types-in-python)
  * [2. List](#2-list)
    * [2.1. List-specific operations](#21-list-specific-operations)
  * [3. Tuple](#3-tuple)
    * [3.1. Tuple-specific operations](#31-tuple-specific-operations)
  * [4. Set](#4-set)
    * [4.1. Set-specific operations](#41-set-specific-operations)
  * [5. Dictionaries](#5-dictionaries)
    * [5.1. Dict-specific operations](#51-dict-specific-operations)
    * [5.2. Special dictionary types](#52-special-dictionary-types)
  * [6. Generic collection features](#6-generic-collection-features)
    * [6.1. Collections consisted format on manual definition](#61-collections-consisted-format-on-manual-definition)
    * [6.2. Common iterable/collection operations](#62-common-iterablecollection-operations)
    * [6.3. Comprehension](#63-comprehension)
    * [6.4. Unpacking](#64-unpacking)
      * [6.4.1. For Lists/Tuples (`*`)](#641-for-liststuples-)
      * [6.4.2. For Dictionaries (`**`)](#642-for-dictionaries-)
    * [6.5. Zip function](#65-zip-function)
<!-- TOC -->

## 1. Collections
In Python, a **collection** is a data structure that allows you to **store and manage multiple elements** within a single variable. Collections are essential for organizing data, iterating over it, and performing operations on groups of values.

### 1.1. Common characteristics:

* They group multiple items into a single object.
* Can be **mutable** (modifiable) or **immutable**.
* Some preserve the **insertion order**, others do not.
* Support operations like **iteration**, **access**, **modification**, **search**, and **combination**.

### 1.2. Main collection types in Python

* `list` → ordered, mutable, allows duplicates.
* `tuple` → ordered, immutable, allows duplicates.
* `set` → unordered, mutable, no duplicates.
* `dict` → maps unique keys to values, ordered (since Python 3.7+), mutable.

## 2. List

`my_list = [item_1, item_2, item3]`

* Ordered.
* Items can be of different types.
* Mutable

### 2.1. List-specific operations

* **Indexing & slicing**
  * `my_list[index]`:  Access an item at index `x`.
  * `my_list[start:end+1]`:  Slice the list from `index_ini` to `index_fin`.
  * `my_list[:]`: to create a copy of the list.
* **Find index**
  * `my_list.index(value)`: Returns the index of the first occurrence of `value` in the list (raises
    an error if not found).
* **Ordering** *(modifies original `my_list`)*
  * Ascending: `my_list.sort()`
  * Descending: `my_list.sort(reverse=True)`
  * Custom order parameter: `my_list.sort(key=func)` (e.g., `key=len` to sort by the length)
  * Reverses the order of elements in the list, without sorting: `my_list.reverse()`
* **Add**
  * At the end of the list: `my_list.append(item)`
  * At a specific index: `my_list.insert(idx, item)`
  * Extend the list with multiple items: `my_list.extend(iterable)`
* **Concatenation**
  * `list_1 + list_2`
* **Remove**
  * By value: `my_list.remove(item)`
  * By index: `my_list.pop(idx)` /  `del my_list[idx]`

## 3. Tuple

* Ordered.
* Items can be of different types.
* Immutable.

`my_tuple = (item_1, item_2, item_3)` or `my_tuple = item_1, item_2, item_3`

* *only one element with a comma at end `my_tuple = item_1,`*

### 3.1. Tuple-specific operations

* **Indexing & slicing**

  * `my_list[index]`:  Access an item at index `x`.
  * `my_list[start:end+1]`:  Slice the list from `index_ini` to `index_fin`.
* **Concatenation**
* `my_tuple + other_tuple`

## 4. Set

`my_set = {item_1, item_2, item_3}`

- Not ordered and unique (no duplicated elements).
- The items can be of different types, but they must all be immutable.
- Mutable.

To create an empty set in Python, use the set() constructor. This is important because {} by itself creates an empty
dictionary, not an empty set.
`my_set = set()`.

### 4.1. Set-specific operations

* **Add**
  * `my_set.add(item)`
  * Add elements from iterables: `my_set.update(iterable)`
* **Remove**
  * `my_set.remove(item)`
* **Set algebra**
  * Union: `set1 | set2` or `set1.union(set2)`
  * Intersection: `set1 & set2` or `set1.intersection(set2)`
  * Difference: `set1 - set2` or `set1.difference(set2)`
  * Symmetric difference ( is communicative): `set1 ^ set2` or `set1.symmetric_difference(set2)`
  * Subset/superset/disjoint:
    * `set1.issubset(set_2)`
    * `set1.issuperset(set_2)`
    * `set1.isdisjoint(set_2)`

## 5. Dictionaries

A dictionary is a **key-value** structure.
`my_dict = {'key1': value1, 'key2': value2}`

* Ordered: keys in the order they were first inserted (Python 3.7+)
* **Keys**: unique and immutable.
* **Values**: can be of any type (even mutable)
* Mutable

### 5.1. Dict-specific operations

* Retrieving **all elements**
  * Key-value pairs: `my_dict.items()`
  * Keys: `my_dict.keys()`
  * Values: `my_dict.values()`
* Accessing a **specific element**
  * `my_dict['k']` (KeyError if missing)
  * `my_dict.get('k', default)` (returns default if missing)
  * `my_dict.setdefault('k', default)` (adds key with default if missing)
  * `my_dict.__contains__('k')` (or `k in my_dict`) (checks if the key exists)
* **Add/Modify**
  `my_dict['k'] = value`
* **Delete**
  `del my_dict['k']` or `my_dict.pop('k')`

### 5.2. Special dictionary types

* **Special types**
  * `OrderedDict` (preserves insertion order)

    ```python
      from collections import OrderedDict
      d = OrderedDict(a=1, b=2)
      d['c'] = 3  # Keeps order
    ```
  * `defaultdict` (auto-create defaults)

    ```python
      from collections import defaultdict
      d = defaultdict(list)
      d['names'].append('Ana')  # Creates a list if 'names' is missing
    ```
  * `ChainMap` (lookup over multiple dicts)

    ```python
    from collections import ChainMap
    d = ChainMap(dict1, dict2)
    ```
  * `MappingProxyType` (read-only view)

    ```python
      from types import MappingProxyType
      modifiable = {'a': 1}
      read\_only = MappingProxyType(modifiable)
    ```

## 6. Generic collection features

### 6.1. Collections consisted format on manual definition

When defining any collection manually, pay attention to formatting. In long collections, put each element on its own
line and end each line with a comma. If you omit the comma, adjacent string literals may be concatenated. To avoid this
kind of error, include a trailing comma after the last element as well.

**Simple example:**

```python
names = [
    "Alice",
    "Bob",
    "Charlie",  # trailing comma here prevents accidental concatenation
]
```

### 6.2. Common iterable/collection operations

These work on lists, tuples, sets, dict views or any iterable—so you don’t repeat them per-type:

* **Length**: `len(x)`
* **Membership**: `v in x` / `v not in x`
* **Iteration**: `for item in x:`
* **Reversed**: `reversed(x)` (iterator)
* **Enumerate**: `for i, e in enumerate(x):`
* [**Comprehension**](#63-comprehension): create interables from other iterables by filtering or applying expressions.
  * List Comprehension:  `[expr for e in x if cond]`
  * Set Comprehension:   `{expr for e in x if cond}`
  * Dict Comprehension:  `{k: v for k, v in pairs if cond}`
* [**Unpacking**](#64-unpacking) :allows you to assign elements of a sequence (like a tuple) to multiple
  variables
  * `*list` `**dict`
* [**Zip**](#65-zip-function): combine multiple iterables into a single iterable
  * `zip(it1, it2)`
* **Map/Filter/Reduce**:
  `map(f, x)`, `filter(f, x)`, `from functools import reduce; reduce(f, x)`
* **Aggregates**: `sum(x)`, `min(x)`, `max(x)`, `any(x)`, `all(x)`
* **Type conversion**: `list(x)`, `tuple(x)`, `set(x)`, `dict(pairs)`
* **Sorting**: `sorted(x, key=func, reverse=True)`
* **Copying**:
  * Shallow: `x.copy()` (if available) or `import copy; copy.copy(x)`
  * Deep:   `copy.deepcopy(x)`

> ### Same reference or copy?
>
> In Python, when working with collections such as lists, dictionaries, and sets, it's essential to understand the
> difference between copying a reference and creating an actual copy of the collection.
>
> * Failure to do so can lead to unintended errors and bugs.
> * Using the `copy()/deepcopy()` method ensures that modifications to the copied collection do not impact the original
>   collection.
> * This is particularly important when you need to work independently with a duplicate of the data.
>   * `elem_1 is elem_2 `: compare the object reference, not the content.

### 6.3. Comprehension

Comprehensions allow you to create interables from other iterables by filtering or applying expressions to each element.

* List Comprehension:  `[expr for e in x if cond]`
* Set Comprehension:   `{expr for e in x if cond}`
* Dict Comprehension:  `{k: v for k, v in pairs if cond}`

With if/else expressions:

```python
[expr1 if condition1 else expr2 if condition2 else expr3 for item in iterable]
```

* List comprehensions allow you to write concise and readable code. You can flatten nested structures and apply conditions
  all in one line (the line breaks below are only for clarity).
  ```python
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  classification = [
      "even" if x % 2 == 0  #If the number is even, "even".
      else "odd" if x % 2 != 0 and x % 3 != 0  #If it’s not even and not a multiple of 3, "odd".
      else "multiple of 3"  #If it’s a multiple of 3, "multiple of 3".
      for x in numbers
  ] 
  ```

Basic dictionary comprehension with a condition;

```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
filtered_dict = {k: v for k, v in pairs if k % 2 == 0} # Filter items of pair keys
# Result: {2: 'two', 4: 'four'}
```

### 6.4. Unpacking

* Works with any iterable (tuples, lists, strings).
* Unpacking is a powerful feature in Python that allows you to assign elements of a sequence (like a tuple) to multiple
  variables in a single statement.
  * `var_1, var_2, var_3 = (item1, item2, item3)`
* You can use `*` to capture multiple values into a single variable.
  * Non-starred variables get single items by position
  * Starred variable always gets a list (empty if no items left)
    * First: *start, x, y → start collects all before last 2
    * Middle: x, *mid, y → mid collects between first/last
    * End: x, y, *rest → rest collects all after first 2

#### 6.4.1. For Lists/Tuples (`*`)

* `print(*[1, 2, 3])`
* Combine lists: `[*list1, *list2]`
* Unpack into variables: `a, b, c = *[1, 2, 3]`
* Flatten: `[*sublist for sublist in nested_list]`
* Convert iterable to list: `list(range(3)) → [0, 1, 2]`

#### 6.4.2. For Dictionaries (`**`)

* Merge: `{**dict1, **dict2}`
* Keyword arguments: `func(**{'x': 1})`
* Update dictionary: `dict1.update(**dict2)`
* Add keys: `{**dict1, 'z': 3}`
* Function unpacking: `f(**{'x': 5})`

### 6.5. Zip function

The `zip()` function allows us to combine multiple iterables (like lists, tuples, etc.) into a single iterable of
tuples.
Each tuple contains elements from the input iterables that share the same position.
`zip()` returns a list of tuples as an object from zip class.

```python
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
id = 34, 234, 34
combined = zip(id, numbers, letters)
print(list(combined))  # [(34, 1, 'A'), (234, 2, 'B'), (34, 3, 'C')]
type(combined)  # zip
```

The zip() function will only iterate up to the shortest iterable provided. This means if the input iterables have
different lengths, zip() stops at the end of the shortest one.

* Note:  If we convert the result of zip() into a set, the order of the elements is not guaranteed.

One of the most useful features of the zip() function is that it allows us to iterate over multiple iterables at the
same time in parallel.

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

The result of `zip()` can be passed to the sorted() function to sort the paired elements based on default or custom
criteria.
`sorted_zip_instance = sorted(zip_instance)`

You can use `zip()` to create a dict by combining two iterables: one for keys and one for values.

```python
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']

my_dict = dict(zip(keys, values))
print(my_dict)
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

my_dict.update(zip(some_old_keys, new_values))  # To update some keys values
```
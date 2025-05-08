#### [Return to README.md](../README.md)

# Input data, Files and Context Manager

<!-- TOC -->
  * [1. Input data](#1-input-data)
  * [2. Files](#2-files)
  * [3. Context Manager (resource handling)](#3-context-manager-resource-handling)
    * [3.1. Manual try/finally](#31-manual-tryfinally)
    * [3.2. `with` and   `__enter__`/`__exit__` methods](#32-with-and-__enter____exit__-methods)
    * [3.2. `contextlib` library](#32-contextlib-library)
  * [4. JSON Handling](#4-json-handling)
<!-- TOC -->

## 1. Input data

- **User data**: `input("Message")` prompts the user for input and always returns a string. Type conversion is necessary afterward if a different data type is needed.


## 2. Files

- Files can be opened in modes "r" (read), "a" (append), "w" (overwrite), "x" (create), and these can be concatenated with `+`. 

- Files can also be specified as text files "t" or binary files "b".

To read files: 

```python
file = open("file.txt", "r", encoding='utf8')  # Open or create files

file.read(num_characters)  # Reads all file content if no number is specified
...
file.readline()  # Read a full line
...
file.readlines()  # Get a list with each line's content
...
for line in file:  # Iterate through file
    print(line)
...
file.close()  # Always close
```

To write files; 
```python
file = open("file.txt", "w", encoding='utf8')  # Open or create files
file.write("bla bla bla")  # Write to file
file.close()  # Always close
```

To remove a file:
```python
import os
os.remove(path_file)
```


## 3. Context Manager (resource handling)

Context management ensures that resources (files, locks, connections, etc.) are reliably set up before a block of code and always cleaned up afterward, even if errors occur.

### 3.1. Manual try/finally
```python
try:
    file = open("file.txt", "w", encoding='utf8')  # Open or create files
    file.write("bla bla bla")  # Write to file
except Exception as e:
    print(e)
finally:
    file.close()  # Always close
```

### 3.2. `with` and   `__enter__`/`__exit__` methods

`with` clause manage a resource (e.g., file) using `__enter__` and `__exit__` methods.

```python
with open("file.txt", "w", encoding='utf8') as file:
    file.write("bla bla bla")
```

We can also create our own class for resource handling. By overriding the `__enter__` and `__exit__` methods, which are already present in the `Object` class (we do not need to explicitly inherit anything).  

```python
class FileHandler:
    def __init__(self, name):
        self.name = name
    
    # Executed when enter to with clause.
    def __enter__(self):
        self.name = open(self.name, 'r', encoding='utf8')
        return self.name
        
    # Executed when exit with clause. These parameters must always be specified
    def __exit__(self, exception_type, exception_value, traceback):  
        print("Closing resource")
        if self.name:
            self.name.close()

with FileHandler("file.txt") as file:
    ...
```

### 3.2. `contextlib` library

We can use the `@contextmanager` decorator to create a generator function for resource management.

Generator function pattern:  
```python
try:
    # acquire resource
    yield resource
finally:
    # release resource
```
Example: 
```python
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Acquiring {name}")
    resource = open(name, 'r')
    try:
        yield resource
    finally:
        print(f"Releasing {name}")
        resource.close()

with managed_resource('file.txt') as f:
    content = f.read()
```


In the case of a class, define a generator method inside it and decorate it with @contextmanager. To use, instantiate the class and call that method in a with statement.

```python

from contextlib import contextmanager

class FileManager:
    def __init__(self, name):
        self.name = name

    @contextmanager
    def use_func(self):
        print(f"Opening {self.name}")
        f = open(self.name, 'w')
        try:
            yield f
        finally:
            print(f"Closing {self.name}")
            f.close()

fm = FileManager('output.txt')
with fm.use_func() as f:
    f.write('Hello, world!')
```

## 4. JSON Handling

JSON (JavaScript Object Notation) is used to store and exchange data in a lightweight, human-readable format, commonly for communication between a server and a web application or for saving structured data.

The json module allows for easy reading/writing of JSON data to/from Python objects.

``` python
import json
json_str = json.dumps(data)       # dict -> JSON string
data_from_str = json.loads(json_str)  # JSON string -> dict

```



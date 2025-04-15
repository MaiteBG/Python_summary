#### [Return to README.md](../README.md)

# Resources and files input/output managment

<!-- TOC -->
* [1. Input data](#1-input-data)
* [2. File Handling](#2-file-handling)
  * [2.1. Context Manager 'with'](#21-context-manager-with)
<!-- TOC -->

## 1. Input data

- **User data**: `input("Message")` prompts the user for input and always returns a string. Type conversion is necessary afterward if a different data type is needed.
## 2. File Handling

Files can be opened in modes "r" (read), "a" (append), "w" (overwrite), "x" (create), and these can be concatenated with `+`.
Files can also be specified as text files "t" or binary files "b".
```python
try:
    file = open("file.txt", "w", encoding='utf8')  # Open or create files
    file.write("bla bla bla")  # Write to file
except Exception as e:
    print(e)
finally:
    file.close()  # Always close
```
``` python
file.read(num_characters)  # Read all file content if no number is specified
```
``` python
file.readline()  # Read a full line
```
``` python
file.readlines()  # Get a list with each line's content
```
``` python
for line in file:  # Iterate through file
    print(line)
```

To remove a file:
```python
import os
os.remove(path_file)
```
### 2.1. Context Manager 'with'
Automatically closes the resource (e.g., file) using `__enter__` and `__exit__` methods.
```python
with open("file.txt", "w", encoding='utf8') as file:
    file.write("bla bla bla")
```

We can also create our own class for file handling.  
By overriding the `__enter__` and `__exit__` methods, which are already present in the `Object` class (we do not need to explicitly inherit anything).  

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




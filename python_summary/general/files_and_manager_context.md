#### [Return to README.md](../../README.md)

# Input/Output: Prompt, Files and Context Manager

<!-- TOC -->
  * [1. Input Data and Dynamic String Evaluation](#1-input-data-and-dynamic-string-evaluation)
    * [1.1. Get user data from prompt (as string)](#11-get-user-data-from-prompt-as-string)
    * [1.2. Dynamic String Evaluation](#12-dynamic-string-evaluation)
  * [2. Output data with Print Statement](#2-output-data-with-print-statement)
  * [3. Files](#3-files)
    * [3.1. File Opening Modes](#31-file-opening-modes)
    * [3.2. Read file](#32-read-file)
    * [3.3. Write file](#33-write-file)
      * [3.3.1. Write statements](#331-write-statements)
      * [3.3.2. Redirecting print output to a file](#332-redirecting-print-output-to-a-file)
    * [3.4. Remove file](#34-remove-file)
    * [3.5. Managing of file paths](#35-managing-of-file-paths)
      * [3.5.1. Using `os` (Procedural)](#351-using-os-procedural)
      * [3.5.2. Using `pathlib` (Recommended, Object-Oriented)](#352-using-pathlib-recommended-object-oriented)
  * [4. Context Managers (Resource Handling)](#4-context-managers-resource-handling)
    * [4.1. Manual `try/finally`](#41-manual-tryfinally)
    * [4.2. `with` and   `__enter__`/`__exit__` methods](#42-with-and-__enter____exit__-methods)
    * [4.3. `contextlib` library](#43-contextlib-library)
<!-- TOC -->

## 1. Input Data and Dynamic String Evaluation

### 1.1. Get user data from prompt (as string)
* `user_input = input("Enter something: ")` displays a message in the console and always **returns a string** (`str`). 

### 1.2. Dynamic String Evaluation
* [Type conversion](variables.md#4-data-type-conversion) is necessary if a different data type is needed.
  * `str.isdigit()`: checks whether a string can be converted to an integer.
* `eval()`: evaluates a Python expression represented as a string.
  * If you evaluate a user-provided string without validation, it can execute arbitrary and potentially dangerous code.

    ```python
    expression = "2 * (3 + 4)"
    result = eval(expression)  # 14
    
    eval("__import__('os').system('rm -rf /')")  # DANGER: Executes the passed code
    ```

* To safely evaluate literal structures (like numbers, lists, dictionaries), use `ast.literal_eval()`:
    ```python
    import ast
    safe = ast.literal_eval("[1, 2, 3]")  # [1, 2, 3]
    ```
* For more complex but secure expression evaluation (e.g., math), consider using libraries such as:
  * `sympy` for symbolic math
  * `numexpr` for fast array expression evaluation

## 2. Output data with Print Statement

- Basic example: `print(x, "y", z)`.
  - Commas automatically add a space between values.
- To print a blank line: `print()`.
- To customize the ending character and separator: `print(var1, end=' ', sep=', ')`
- For formatting output cas use the general [String Formatting](variables.md#32-string-format) ways.


## 3. Files

### 3.1. File Opening Modes

When opening a file with `open(file_path, mode, encoding = None)`, you must specify a mode that determines how the file will be used:
> * By default, encoding value is `None`and use *system's default encoding*. 
>   * Use `encoding='utf-8'`is a good practice. 


| Mode  | Description                                                                                                                   |
| ----- |-------------------------------------------------------------------------------------------------------------------------------|
| `"r"` | Read (default). File must exist.                                                                                              |
| `"w"` | Write. Creates file or **overwrites** if it exists.                                                                           |
| `"a"` | Append. Creates file if it doesn't exist, writes at the **end** if it does.                                                   |
| `"x"` | Create. Fails if the file already exists.                                                                                     |
| `"t"` | Text mode (default).                                                                                                          |
| `"b"` | Binary mode (for non-text files like images, audio, etc.)   <br/>Combine it with other modes (e.g. `wb`: write binary file).  |
| `"+”` | Update mode ( allows both reading and writing in a file). <br/> Use in combination with `"r"`, `"w"`, or `"a"` (e.g. `"r+"`). |

* `r+` requires the file to exist, `w+` and `a+` create the file if it doesn't.
* Always use `b` for binary files to handle non-text data correctly.

### 3.2. Read file
When opening and reading files in Python, there are various methods for reading the content depending on your needs. Here's an overview of the most common ones:

```python
# Open a file for reading with UTF-8 encoding
file = open("file.txt", "r", encoding="utf8")  # Open file for reading

# Read the entire content of the file (without specifying a number, it reads all)
content = file.read()  # Reads all file content
...

# Read a single line from the file (returns the next line)
line = file.readline()  # Read one line at a time
...

# Read all lines into a list (each line is an element of the list)
lines = file.readlines()  # Get a list of all lines in the file
...

# Iterate through each line in the file (automatically handles line-by-line reading)
for line in file:  # Loop through file line by line
    print(line)
...

# Don't forget to close the file when done to free system resources
file.close()  # Always close the file when you're done

```


### 3.3. Write file
 To write data to a file in Python, you can use several methods.
 * Use `a` mode for only append.

#### 3.3.1. Write statements
write()` and `writelines(lines)` do not add a newline automatically, so you need to include `\n` if you want to insert line breaks.

```python
# Open a file for writing (it creates the file if it doesn't exist, or overwrites it if it does)
file = open("file.txt", "w", encoding="utf8")  # Open or create file in write mode
file.write("bla bla bla")  # Write string to file
file.close()  # Always close the file when done
```

``` python
# Writing multiple lines at once
lines = ["uno\n", "dos\n", "tres\n"]  # Each string must include '\n' if you want line breaks
file = open("file.txt", "w", encoding="utf8")
file.writelines(lines)
file.close()
```
  
#### 3.3.2. Redirecting print output to a file
Instead of manually using `write()`, you can also redirect output to a file using the file parameter in the print() function. 
*  It can be especially useful for logging or saving results.
* This approach automatically adds a newline after each call.
```python
with open("output.txt", "w", encoding="utf8") as file:
    print("This will be written to the file", file=file)  # Writes to file instead of standard output
```


### 3.4. Remove file
To delete a file in Python, use the `os` module. If the file does not exist, `os.remove()` will raise a `FileNotFoundError`.
```python
import os

if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("File not found.")
```

### 3.5. Managing of file paths
#### 3.5.1. Using `os` (Procedural)
```python
import os

# Get current directory
cwd = os.getcwd()

# Join paths (portable)
path = os.path.join(cwd, "folder", "file.txt")

# Check if a file or directory exists
os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)

# Create or remove directories
os.mkdir("new_folder")      # Create a folder
os.remove("file.txt")       # Delete a file
os.rmdir("empty_folder")    # Delete empty folder
```
#### 3.5.2. Using `pathlib` (Recommended, Object-Oriented)
* Cleaner syntax and better readability
* Uses operator `/` to join paths (instead of `os.path.join`)
* Object-oriented and easier to chain methods

```python
from pathlib import Path

# Define a path
file_path = Path("folder") / "file.txt"

# Get current working directory
cwd = Path.cwd()

# Check if file/folder exists
file_path.exists()
file_path.is_file()
file_path.is_dir()

# Create or delete
Path("new_folder").mkdir()
file_path.unlink()       # Remove a file
Path("empty_folder").rmdir()
```

Use `.open()` to read/write files directly from `Path` objects:
* More consistent and readable than the built-in `open()` with `str(path)`
``` python
# Open and read file (recommended way with pathlib)
with file_path.open("r", encoding="utf8") as f:
    content = f.read()
```

## 4. Context Managers (Resource Handling)

Context management ensures that resources (such as files, network connections, or locks) are **properly acquired and released**, even if an error occurs during their use. This is critical to avoid resource leaks and other side effects.


### 4.1. Manual `try/finally`

Using `try/finally` ensures a resource is always released, regardless of whether an exception is raised:

```python
try:
    file = open("file.txt", "w", encoding='utf8')  # Open or create file
    file.write("bla bla bla")                      # Write to file
except Exception as e:
    print(e)
finally:
    file.close()                                   # Always close the file
```


### 4.2. `with` and   `__enter__`/`__exit__` methods

The `with`  statement simplifies resource management using an object that implements the `__enter__` and `__exit__` methods.
* `__enter__()` handles resource acquisition and returns the object to use inside the with block.
* `__exit__()` is always called at the end, even on exceptions.
```python
with open("file.txt", "w", encoding='utf8') as file:
    file.write("bla bla bla")
```
** Custom Resource Class**
You can define your own context manager by implementing `__enter__` and `__exit__` methods.

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
     content = file.read()
```

### 4.3. `contextlib` library

Python’s `contextlib` module provides a more elegant and declarative way to write context managers using generator functions.

Using `@contextmanager` with a generator function (`yield`):

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

You can also define a context-managed method inside a class:
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


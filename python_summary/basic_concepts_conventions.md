
# Basic Concepts and Conventions

<!-- TOC -->
  * [1. Comments and Docstrings (Documentation)](#1-comments-and-docstrings-documentation)
  * [2. Python REPL (Read-Eval-Print Loop)](#2-python-repl-read-eval-print-loop)
  * [3. Naming Conventions](#3-naming-conventions)
    * [3.1. Constants](#31-constants)
    * [3.2. **File names**, **functions** and **common variables**](#32-file-names-functions-and-common-variables)
    * [3.3. **Class names**](#33-class-names)
    * [3.4. Other considerations](#34-other-considerations)
<!-- TOC -->


## 1. Comments and Docstrings (Documentation)

- Use `# [TEXT]` to write single-line comments that explain the code.
- Use `''' [TEXT] '''` to write multi-line comments.  
> ### Docstrings
> 
> Multi-line comments are also used to create ***docstrings*** for `classes, methods, and modules`. These are added immediately after their definition or at the beginning of the module to provide clear documentation.  
>- `name.__doc__`: Returns the *docstring* of a class, method, or module, but **does not** include the documentation for its components.  
>- `help(name)`: Displays the complete documentation for a class, method, or module, including all the associated *docstring*.*
> 
>*When called from an instance, it provides the *docstring* associated with the class of the object.*

``` python
def MyMethod(param1, param2):
    '''
    MyMethod Docstrings documentation
    :param param1 This is de param1:
    :param param2 This is the param2:
    :return result This is the result:
    '''
    result= param1  + param2 
    return result
```

## 2. Python REPL (Read-Eval-Print Loop)
The Python REPL (Read-Eval-Print Loop) is an interactive environment for running Python code line by line.
- It is ideal for debugging and testing small pieces of code because it does not save content—everything is temporary.
- Displays results automatically without requiring a `print` statement.
  - Simply type `python` in the terminal to start using it.
  - In frameworks like PyCharm, use the "Run file in Python console" option for a similar experience.


## 3. Naming Conventions

### 3.1. Constants
By convention, constants are named in uppercase (e.g., `CONSTANT_VALUE`) and should remain unmodified during the program's execution. 

### 3.2. File names, functions and common variables
***Snake Case***
  > Snake Case format is used for **file names**, **functions** and **common variables**: `[a-z][a-z0-9_]+`.
  >- **Use underscores** (`_`) to separate words in multi-word names (e.g., `file_txt`).  
  >  - **Add prefixes or suffixes** to provide context (e.g., `is_valid`, `user_count`)

### 3.3. Class names
 ***PascalCase***
  >  PascalCase (also known as UpperCamelCase) is conventionally used only for naming **classes** in Python.  
  >- The name begins with an uppercase letter.  
  >    - Each subsequent word also starts with an uppercase letter, without spaces or underscores (e.g., `MyClass`, `UserProfile`).  

### 3.4. Other considerations

- Avoid
  -  Having files and directories with the same name to prevent errors in Python.
  - Python's reserved keywords.  
  - Single-letter variable names (except for specific cases like indices).


- **Use plural names exclusively** for collections (e.g., `items_list`).


- **Protected and Private Attributes**:
  - Protected attributes are used in classes to give more control over reading and writing attributes. By convention, these are prefixed with `_`.
  - Private attributes are prefixed with `__` to prevent unintended overwriting or access, though Python does not strictly enforce this protection.


- On unpacking or loops to iterate a variable that we do not use, like if we never use a variable, this can be indicated with  ` _ `. (e.g. `for _ in ...`)


- **Readable and Descriptive Names**:
  - Always aim for clear and descriptive names to improve code readability.
  - Be descriptive but concise: the name should clearly indicate the purpose or role of the variable or object.
  - Avoid abbreviations unless they are widely recognized within your project or field (e.g., `img` for image).
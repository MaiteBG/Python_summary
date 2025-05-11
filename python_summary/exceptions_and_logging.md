#### [Return to README.md](../README.md)

# Exceptions, Assertions and Logging
<!-- TOC -->
  * [1. Exceptions](#1-exceptions)
    * [1.1. Cath exceptions (try/except block)](#11-cath-exceptions-tryexcept-block)
    * [1.2. Define a new exception class](#12-define-a-new-exception-class)
  * [Assertions](#assertions)
  * [3. Logging in Python](#3-logging-in-python)
    * [2.1. Log levels](#21-log-levels)
    * [2.2. Log format](#22-log-format)
<!-- TOC -->
## 1. Exceptions
### 1.1. Cath exceptions (try/except block)
To prevent the program from terminating abruptly:

```python
import sys

try:
    pass  # Code that may raise an error
except xError as e:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
    #sys.exit() #To ending de program
else:
    ...
    # Only executed if no exception was raised (optional)
finally:
    ...
    # Always executed, whether an exception occurred or not (optional)
# 9. Continuation
```

Normally, exceptions are caught using the generic `Exception` class, but more specific ones can also be used.
A try/except block can have multiple except clauses for different error types (more generic classes should be at the end).
`type(e)` to get the error type (error class).

If we want to end the program `sys.exit()`.

If variables need to be used after the try/except block, they should be defined before the try block.

### 1.2. Define a new exception class

Always consider exception class Always consider exception class hierarchy when creating custom exceptions. Inherit from the most specific built-in exception that makes sense (for example, ValueError or IOError) so that your custom exception integrates cleanly with existing exception handling. when creating custom exceptions. 
* Inherit from the most specific built-in exception that makes sense (for example, ValueError or IOError) so that your custom exception integrates cleanly with existing exception handling.

To define a new exception class:

```python
# 10. Define new error
class NewException(Exception): # Exception or other Exception class (hierarchy!) 
    def __init__(self, message):
        self.message = message  # Message to display in the exception

# 11. Raise new error
raise NewException(message)  # Throws the error to be caught later in the except block
```


## Assertions

Assertions do not replace proper error handling; they are meant for debugging and catching programmer errors. When an assertion fails, Python raises an `AssertionError`.

*Simple example:*
```python
def divide(a, b):
    assert b != 0, "Division by zero"
    return a / b

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # AssertionError: Division by zero
```


## 3. Logging in Python

You can configure log messages using the <u>[`logging`](https://docs.python.org/3/howto/logging.html)</u> library.

### 2.1. Log levels
This is used to manage error/debug messages that we send to the console. It is divided into different levels ordered by importance:  
![logging_levels.png](static_md/logging_levels.png)

To change the minimum level we want to display on the screen, use `log.basicConfig(level=log.X)`. By default, this level is set to WARNING.

```python
import logging as log
# 12. We change to DEBUG level; since it is the lowest level, messages of all levels will be shown
log.basicConfig(level=log.DEBUG)

if __name__ == '__main__':
    log.debug('Debug level message')
    log.info('Info level message')
    log.warning('Warning level message')
    log.error('Error level message')
    log.critical('Critical level message')
```

### 2.2. Log format

To specify the format of the log messages, we can use log.basicConfig(...).
```python
import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',  # Message format
                datefmt='%I:%M:%S %p',  # Time format
                handlers=[  # Where we send the messages
                    log.FileHandler('archivo_log.log'),  # Send messages to a file
                    log.StreamHandler()  # Send messages to the console
                ])
```
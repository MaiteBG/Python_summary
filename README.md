# Python Summary

## Basic Concepts and Conventions

### Comments
- Use `#` followed by a space to write comments that explain the code.

### Variables
- **Dynamic typing**: Variables can store any type of data and change their type without explicit casting.
- **Objects**: Variables in Python are references stored in the *stack* and point to data in the *heap*.
- **Mutability**: If the value of a variable changes, a new object is created with the updated data, and the variable points to this new reference.
- **Initialization**: Variables must be declared with an initial value.
- **Constants**: By convention, constants are named in uppercase (e.g., `CONSTANT_VALUE`) and should not be modified.

### Snake Case
- **Naming conventions**:
  - Use the snake_case format: `[a-z][A-Z,a-z,0-9,_]+`.
  - Avoid:
    - Python's reserved keywords.
    - Single-letter variable names (except for exceptions like indices).
    - Names starting with numbers or uppercase letters.
  - Use underscores (`_`) to compose multi-word names (e.g., `file_txt`).
  - Apply prefixes or suffixes to provide context (e.g., `is_valid`, `user_count`).

### Print Statement
- Basic example: `print(x, "y", z)`.
  - Using commas automatically adds spaces between the values in the output.
- To print a blank line: `print()`.


#### [Return to README.md](../../README.md)

# Data Serialization and Databases

<!-- TOC -->
  * [1. Data Serialization](#1-data-serialization)
    * [1.1. JSON Handlin](#11-json-handlin)
      * [1.1.1. Store to file and/or add indentation](#111-store-to-file-andor-add-indentation)
    * [1.2. Serializing Non-Serializable Objects](#12-serializing-non-serializable-objects)
    * [1.3. JSON vs. Other Data Formats (e.g., CSV, XML)](#13-json-vs-other-data-formats-eg-csv-xml)
  * [2. Basic SQL Queries](#2-basic-sql-queries)
  * [3. PostgreSQL](#3-postgresql)
    * [3.1. pgAdmin4 (graphical interface for PostgreSQL)](#31-pgadmin4-graphical-interface-for-postgresql)
    * [3.2. Creating connection and executing statements](#32-creating-connection-and-executing-statements)
      * [3.2.1. Establishing a Connection and Executing Queries](#321-establishing-a-connection-and-executing-queries)
      * [3.2.2. Fetching Results](#322-fetching-results)
      * [3.2.3. Using Context Manager (`with`) for Connection and Cursor](#323-using-context-manager-with-for-connection-and-cursor)
      * [3.2.4. Using Variables in Queries](#324-using-variables-in-queries)
    * [3.3. Transaction management (commit/rollback)](#33-transaction-management-commitrollback)
    * [3.4. Connection Pool](#34-connection-pool)
  * [4. MySQL](#4-mysql)
    * [4.1. Basic MySQL Connection](#41-basic-mysql-connection)
    * [4.2. Connection Pool](#42-connection-pool)
<!-- TOC -->

## 1. Data Serialization

Serialization is the process of converting a Python object into a format (like JSON, XML, or CSV) that can be saved to a file, sent over a network, or stored in a database.
It enables you to preserve data integrity and transfer it across different platforms or systems.

### 1.1. JSON Handlin

JSON (JavaScript Object Notation) is a lightweight, human-readable format used for storing and exchanging data.

* It's widely used for communication between servers and web applications or for saving structured data.

Python provides the `json` module to easily convert between Python objects and JSON format.

* `json.dumps()`: Converts Python objects into a JSON string.
  * `TypeError` occurs when trying to serialize a non-serializable object.
* `json.loads()`: Parses a JSON string and returns a Python object.
  * `JSONDecodeError` occurs when the JSON string is malformed.

```python
import json

# Python object to JSON string
data = {'name': 'John', 'age': 30}

try:
    json_str = json.dumps(data)  # Convert Python object to JSON string
    print(json_str)  # {"name": "John", "age": 30}
except TypeError as e:
    print(f"Error during serialization: {e}")

# JSON string to Python object
try:
    data_from_str = json.loads(json_str)  # Convert JSON string to Python object
    print(data_from_str)  # {'name': 'John', 'age': 30}
except json.JSONDecodeError as e:
    print(f"Error during deserialization: {e}")

```

#### 1.1.1. Store to file and/or add indentation

* `json.dump(data, file, indent) ` and `json.load(f)`
  * file:   file where store/read JSON content
  * indent:  add indentation to print or store JSON in a more readable format

```python
import json

data = {'name': 'John', 'age': 30}

# Writing JSON data to a file
with open('data.json', 'w', encoding='utf8') as f:
    json.dump(data, f, indent=4)  # Write with pretty formatting to data.json file

# Reading JSON data from a file
with open('data.json', 'r', encoding='utf8') as f:
    data_from_file = json.load(f)
    print(data_from_file)  # {'name': 'John', 'age': 30}
```

### 1.2. Serializing Non-Serializable Objects

Not all Python objects can be serialized directly into JSON, like `datetime` or custom Python classes need special handling.

* Provide a custom serializer using the `default` parameter of `json.dumps()`:

  * The `default=str` argument converts non-serializable objects to strings during serialization.

  ```python
  import json
  from datetime import datetime

  # Serialize datetime object
  current_time = datetime.now()
  data = {'time': current_time}
  json_str = json.dumps(data, default=str)  # Convert datetime to string
  print(json_str)

  # Deserialize back to datetime
  data_from_str = json.loads(json_str)
  data_from_str['time'] = datetime.fromisoformat(data_from_str['time'])
  print(data_from_str)
  ```
* Implement the `__dict__` method:

  * `default` parameter: A function that will be used to convert non-serializable objects into a serializable format (e.g., custom objects).

  ```python
  import json
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

      def to_dict(self):
          return {'name': self.name, 'age': self.age}

  # Serialize a custom object
  person = Person('Alice', 28)
  json_str = json.dumps(person, default=lambda obj: obj.to_dict())
  print(json_str)  # {"name": "Alice", "age": 28}
  ```

### 1.3. JSON vs. Other Data Formats (e.g., CSV, XML)

While JSON is popular, other formats like CSV and XML have their uses. Here’s a brief comparison:

* JSON: Ideal for structured data, supports nested objects, and is widely used for APIs and web services.
* CSV: Best for tabular data (rows and columns), but doesn’t support complex nested structures.
* XML: Similar to JSON, but more verbose and better suited for document-oriented data.


| Feature         | JSON                                 | CSV                     | XML                           |
| --------------- | ------------------------------------ | ----------------------- | ----------------------------- |
| **Readability** | Human-readable, hierarchical         | Simple, tabular format  | Human-readable, verbose       |
| **Structure**   | Supports nested structures           | Flat, tabular structure | Can support nested structures |
| **Use cases**   | APIs, web applications, config files | Simple datasets         | Documents, configuration      |
| **File Size**   | Larger due to flexibility            | Smaller for simple data | Can be larger due to markup   |
| **Parsing**     | Easy with built-in libraries         | Simple with`csv` module | More complex, uses`xml.etree` |

## 2. Basic SQL Queries

Basic SQL queries are essential for interacting with databases. Common operations include `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

```sql
-- Select
SELECT * FROM person
SELECT name FROM person WHERE id_person = 1 
SELECT id_person, name FROM person WHERE id_person IN (1,2)
-- Insert
INSERT INTO person(name, lastname, email) VALUES('Susana','Lara','slara@mail.com')
-- Update
UPDATE person SET name = 'Ivonne' WHERE id_person=3
UPDATE person SET name = 'Ivonne' WHERE id_person IN (3,6)
-- Delete
DELETE FROM person WHERE id_person=3 
DELETE FROM person WHERE id_person IN (2,3)
```

## 3. PostgreSQL

PostgreSQL is a powerful relational database that can be accessed from Python using libraries like `psycopg2`.

### 3.1. pgAdmin4 (graphical interface for PostgreSQL)

pgAdmin4 is a graphical interface for managing PostgreSQL databases. It allows you to easily create and manage databases, tables, and queries.

**Creating a New Database**To create a new database in pgAdmin4, follow these steps:

* *Click on "Create" and choose "Database" to begin the process.*

<img src="../static_md/pgadmin4_createdb.png" width="250"/>

**Creating a New Table**After setting up your database, create a new table by following the steps shown below:

* *Choose the "Create" option and select "Table" to define the table structure.*

<img src="../static_md/pgadmin4_create_table.png" width="250"/>

**Viewing and Editing Table Data**Once your table is created, you can view and manually edit its content:

* *Access the "Data" tab to view, edit, or delete entries directly in the table.*

<img src="../static_md/pgadmin4_view_table_data.png" width="250"/>

### 3.2. Creating connection and executing statements

In Python, the `psycopg2` library is commonly used to interact with PostgreSQL databases.

#### 3.2.1. Establishing a Connection and Executing Queries
  host=_HOST,
  user=_USERNAME,
  password=_PASSWORD,
  port=_DB_PORT,
  database=_DATABASE

``` python
import psycopg2

# Establish a connection
conn = psycopg2.connect(  user=_USERNAME,
                          password=_PASSWORD,
                          host=_HOST,
                          port=_DB_PORT,    
                          database=_DATABASE)

# Create a cursor to execute queries
cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT * FROM users')
result = cursor.fetchall()
print(result)

# Close the cursor and connection
cursor.close()
conn.close()
```

#### 3.2.2. Fetching Results

To fetch records from the database, you can use:

* `cursor.fetchall()` – Retrieves all records from the query result.
* `cursor.fetchone()` – Retrieves the first record.

#### 3.2.3. Using Context Manager (`with`) for Connection and Cursor

Using [context managers](files_and_manager_context.md#4-context-managers-resource-handling)  (`with` statement) simplifies resource management by automatically closing connections and cursors after the block execution.

* Use the with statement for automatic closing of cursors.
* In case of a **connection** object, you still **need to call `connection.close()` manually** !

> Always handle exceptions gracefully with `try/except`.

```python
try:
    # Using 'with' to manage connection and cursor
    with psycopg2.connect(dbname='your_db', user='your_user', password='your_password') as connection:
        with connection.cursor() as cursor:
            # Execute the query
            statement = 'SELECT * FROM person'
            cursor.execute(statement)
            records = cursor.fetchall()  # Fetch all records
            print(records)
# Catch exceptions
except Exception as e:
    print(f'An error occurred: {e}')
# Ensure connection is closed
finally:
    connection.close()

```

#### 3.2.4. Using Variables in Queries

When passing data to your SQL queries, you should use placeholders (`%s`) to prevent SQL injection. Values are passed as a tuple in the second argument of `cursor.execute()`.

* To process multiple records using the `IN` statement, we'll indicate the values in `values_tuple` as a tuple of tuples.

```python
# Example: Searching records using IN statement
statement = 'SELECT * FROM person WHERE id_person IN %s'
primary_keys = ((1,2,3),) 
cursor.execute(statement, primary_keys)  # Execute the query with the values
records = cursor.fetchall()
```

### 3.3. Transaction management (commit/rollback)

When working with databases, it’s important to manage transactions to ensure data integrity.
A transaction consists of one or more statements that we want to execute as a block (all or none).

If we use the `with` statement for the cursor: 
* Committing and rolling back are handled automatically, reducing the need for manual intervention.


If we **DO NOT** use the `with` statement for the cursor:
* We must manually commit changes at the end of the transaction using `connection.commit()` (since `connection.autocommit` is set to `False` by default). 
* Additionally, in case of an error, we must explicitly call `connection.rollback()` in the `except` block to revert any changes made during the transaction.

    ``` python
    try:
        # Execute a query to insert data
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('John', 25))
        # Manually commit changes at the end of the transaction
        conn.commit()
        
    except Exception as e:
        # If an error occurs, rollback the transaction
        print(f"Error occurred: {e}")
        conn.rollback()
        
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
    ```

### 3.4. Connection Pool

A connection pool is a mechanism used to manage and reuse database connections efficiently.
* Instead of creating and closing a new database connection for every query, a connection pool allows a set of connections to be shared.

```python
from psycopg2 import pool

# Create a connection pool with minimum and maximum connections
conn_pool = pool.SimpleConnectionPool(_MIN_CON, _MAX_CON,
                                                      host=_HOST,
                                                      user=_USERNAME,
                                                      password=_PASSWORD,
                                                      port=_DB_PORT,
                                                      database=_DATABASE)
# Get a connection from the pool
conn = conn_pool.getconn()

# Execute queries as usual
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
result = cursor.fetchall()
print(result)

# Return connection to the pool
conn_pool.putconn(conn)
```
```python
# When no longer needed, close all connections in the pool
conn_pool.closeall()
```

## 4. MySQL

MySQL is another popular relational database, and you can interact with it from Python using libraries such as `mysql-connector-python`.
### 4.1. Basic MySQL Connection
```python
import mysql.connector

# 16. Establish a connection to the MySQL database
db_connection = mysql.connector.connect(
    host='your_host',
    user='your_user',
    password='your_password',
    database='your_database'
)

# Create a cursor object to interact with the database
cursor = db_connection.cursor()

# Execute a SQL query (for example, to fetch data)
cursor.execute("SELECT * FROM users")

# Fetch the result of the query
results = cursor.fetchall()

# Close the connection when done
db_connection.close()
```

### 4.2. Connection Pool
Connection pooling allows you to reuse database connections, which improves performance by reducing the overhead of creating and destroying connections repeatedly. The `mysql-connector-python` library supports connection pooling.

* **Creating a Connection Pool**
    ```python
    from mysql.connector import pooling, Error
    
    try:
        # 17. Create a MySQL connection pool
        pool = pooling.MySQLConnectionPool(
            pool_name='my_pool',
            pool_size=5,  # Set the size of the connection pool
            host='your_host',
            port=3306,  # Default MySQL port
            database='your_database',
            user='your_user',
            password='your_password'
        )
        print("Connection pool created successfully")
    
    except Error as e:
        print(f"Error creating connection pool: {e}")
    ```
* **Getting a Connection from the Pool**
  * `get_connection()`: Fetches a connection from the pool.
  * `conn.close()`: Returns the connection to the pool without closing it completely.

  ```python
    # 17.1. Get a connection from the pool
    conn = pool.get_connection()
    
    # 18. Get a cursor to execute queries
    cursor = conn.cursor()
    
    # Example: Execute a query
    cursor.execute("SELECT * FROM employees")
    
    # Fetch and display the results
    results = cursor.fetchall()
    
    # After you're done, return the connection to the pool (don't close it completely)
    conn.close()
  ```
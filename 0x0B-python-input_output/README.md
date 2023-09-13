### 0-read_file.py
- Reads a text file (UTF8) and prints it to stdout.
- Prototype: def read_file(filename=""):
### 1-write_file.py
- Writes a string to a text file (UTF8) and returns the number of characters
written:
- Prototype: def write_file(filename="", text=""):
### 2-append_write.py
- Appends a string at the end of a text file (UTF8) and returns the number of
characters added:
- Prototype: def append_write(filename="", text=""):
### 3-to_json_string.py
- Returns the JSON representation of an object (string):
- Prototype: def to_json_string(my_obj):
### 4-from_json_string.py
- Returns an object (Python data structure) represented by a JSON string:
- Prototype: def from_json_string(my_str):
### 5-save_to_json_file.py
- Writes an Object to a text file, using a JSON representation:
- Prototype: def save_to_json_file(my_obj, filename):
### 6-load_from_json_file.py
- Creates an Object from a “JSON file”:
- Prototype: def load_from_json_file(filename):
### 7-add_item.py
- Adds all arguments to a Python list, and then save them to a file:
- Uses save_to_json_file from 5-save_to_json_file.py
- Uses load_from_json_file from 6-load_from_json_file.py
- The list is saved as a JSON representation in a file named add_item.json
- If the file doesn't exist it is created.
### 8-class_to_json.py
- returns the dictionary description with simple data structure (list,
dictionary, string, integer and boolean) for JSON serialization of
an object:
- Prototype: def class_to_json(obj):
- obj is an instance of a Class
- All attributes of the obj Class are serializable: list, dictionary, string,
integer and boolean.
### 9-student.py
- Defines Student class by:
	- Public instance attributes:
		- first_name
		- last_name
		- age
	- Instantiation with first_name, last_name and age: def __init__(self,
	first_name, last_name, age):
	- Public method def to_json(self): that retrieves a dictionary
	representation of a Student instance (same as 8-class_to_json.py)
### 10-student.py
- Defines Student class by:
	- Public instance attributes:
		- first_name
		- last_name
		- age
	- Instantiation with first_name, last_name and age: def __init__(self,
	first_name, last_name, age):
	- Public method def to_json(self, attrs=None): that retrieves a dictionary
	representation of a Student instance (same as 8-class_to_json.py)
		- If attrs is a list of strings, only attribute names contained
		in this list are retrieved.
		- Otherwise, all attributes are retrieved.
### 11-student.py
- Defines Student class by:
	- Public instance attributes:
		- first_name
		- last_name
		- age
	- Instantiation with first_name, last_name and age: def __init__(self,
	first_name, last_name, age):
	- Public method def to_json(self, attrs=None): that retrieves a dictionary
	representation of a Student instance (same as 8-class_to_json.py)
		- If attrs is a list of strings, only attribute names contained
		in this list are retrieved.
		- Otherwise, all attributes are retrieved.
	- Public method def reload_from_json(self, json): that replaces all
	attributes of the Student instance.
		- json is assumed to always be a dictionary.
		- A dictionary key will be the public attribute name.
		- A dictionary value will be the value of the public attribute.
### 12-pascal_triangle.py
- Returns a list of lists of integers representing the Pascal's triangle of n:
- Prototype: def pascal_triangle(n):
- Returns an empty list if n <= 0
- n is assumed to always be an integer.

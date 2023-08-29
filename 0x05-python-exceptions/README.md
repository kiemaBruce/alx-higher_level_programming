### 0-safe_print_list.py
- Prints x elements of a list.
- Prototype: def safe_print_list(my_list=[], x=0):
- my_list can contain any type (integer, string, etc.)
- All elements are printed on the same line followed by a new line.
- x represents the number of elements to print.
- x can be bigger than the length of my_list. In which case it is handled by
try-except.
- Returns the real number of elements printed.
### 1-safe_print_integer.py
- Prints an integer with "{:d}".format().
- Prototype: def safe_print_integer(value):
- value can be any type (integer, string, etc.)
- The integer is printed followed by a new line.
- Returns True if value has been correctly printed (it means the value is an
integer).
- Otherwise, returns False.
### 2-safe_print_list_integers.py
- Prints the first x elements of a list and only integers.
- Prototype: def safe_print_list_integers(my_list=[], x=0):
- my_list can contain any type (integer, string, etc.)
- All integers are printed on the same line followed by a new line -
other type of value in the list must be skipped (in silence).
- x represents the number of elements to access in my_list
- x can be bigger than the length of my_list - if it’s the case, an exception
occurs.
- Returns the real number of integers printed.
### 3-safe_print_division.py
- Divides 2 integers and prints the result.
- Prototype: def safe_print_division(a, b):
- a and b can be assumed to be integers.
- The result of the division is printed in the finally section preceded by
Inside result:
- Returns the value of the division, otherwise: None
### 4-list_division.py
- divides element by element 2 lists.
- Prototype: def list_division(my_list_1, my_list_2, list_length):
- my_list_1 and my_list_2 can contain any type (integer, string, etc.)
- list_length can be bigger than the length of both lists
- Returns a new list (length = list_length) with all divisions
- If 2 elements can’t be divided, the division result is equal to 0
-If an element is not an integer or float:
	- print: wrong type
- If the division can’t be done (/0):
	- print: division by 0
- If my_list_1 or my_list_2 is too short
	- print: out of range
### 5-raise_exception.py
- Raises a type exception.
- Prototype: def raise_exception():
### 6-raise_exception_msg.py
- Raises a name exception with a message.
- Prototype: def raise_exception_msg(message=""):

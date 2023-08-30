### 0-square.py
- The empty class Square defines a square.
### 1-square.py
- Defines a square by:
	- Private instance attribute: size
	- Instantiation with size (no type/value verification)
### 2-square.py
- Defines a square by:
	- Private instance attribute: size
	- Instantiation with optional size: def __init__(self, size=0):
		- size must be an integer, otherwise a TypeError exception
		  with the message 'size must be an integer' is raised.
		- if size is less than 0, a ValueError exception with the
		  message 'size must be >= 0' is raised.
### 3-square.py
 - Defines a square by:
	- Private instance attribute: size
	- Instantiation with optional size: def __init__(self, size=0):
		- size must be an integer, otherwise a TypeError exception
		  with the message 'size must be an integer' is raised.
		- if size is less than 0, a ValueError exception with the
		  message 'size must be >= 0' is raised.
	- Public instance method: def area(self): that returns the current
	square area.

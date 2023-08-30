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
### 4-square.py
- Defines a square by:
	- Private instance attribute: size:
		- property def size(self): to retrieve it
		- property setter def size(self, value): to set it:
			- size must be an integer, otherwise raise a TypeError
			exception with the message 'size must be an integer'.
			- if size is less than 0, raise a ValueError exception
			with the message 'size must be >= 0'.
	- Instantiation with optional size: def __init__(self, size=0):
	- Public instance method: def area(self): that returns the current
	square area.
### 5-square.py
- Defines a square by:
	- Private instance attribute: size:
		- property def size(self): to retrieve it
		- property setter def size(self, value): to set it:
			- size must be an integer, otherwise raise a TypeError
			exception with the message 'size must be an integer'.
			- if size is less than 0, raise a ValueError exception
			with the message 'size must be >= 0'.
	- Instantiation with optional size: def __init__(self, size=0):
	- Public instance method: def area(self): that returns the current
	square area.
	- Public instance method: def my_print(self): that prints in stdout the
	square with the character #:
		- if size is equal to 0, print an empty line.
### 6-square.py
- Defines a square by:
	- Private instance attribute: size:
		- property def size(self): to retrieve it
		- property setter def size(self, value): to set it:
			- size must be an integer, otherwise raise a TypeError
			exception with the message 'size must be an integer'.
			- if size is less than 0, raise a ValueError exception
			with the message 'size must be >= 0'.
	- Private instance attribute: position:
		- property def position(self): to retrieve it
		- property setter def position(self, value): to set it:
			- position must be a tuple of 2 positive integers,
			otherwise raise a TypeError exception with the message
			position must be a tuple of two positive integers.
	- Instantiation with optional size and optional position: 
	def __init__(self, size=0, position=(0, 0)):						      
	- Public instance method: def area(self): that returns the current
	square area.
	- Public instance method: def my_print(self): that prints in stdout the
	square with the character #:
		- if size is equal to 0, print an empty line.
		- position should be use by using space - Don’t fill lines by
		spaces when position[1] > 0

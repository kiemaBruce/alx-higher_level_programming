### models/base.py
- Defines the Base class with:
- private class attribute __nb_objects = 0
- class constructor: def __init__(self, id=None):
	- if id is not None, the public instance attribute id is
	  assigned with this value.
	- otherwise __nb_objects is incremented and the new value
	  assigned to the public instance attribute id.
- static method def to_json_string(list_dictionaries): that returns the JSON
string representation of list_dictionaries.
	- list_dictionaries is a list of dictionaries
	- If list_dictionaries is None or empty, string: "[]" is returned.
	- Otherwise, the JSON string representation of list_dictionaries is
	returned.
- class method def save_to_file(cls, list_objs): that writes the JSON string
representation of list_objs to a file.
	- list_objs is a list of instances who inherits of Base - example: list of
	Rectangle or list of Square instances.
	- If list_objs is None, an empty list is saved.
	- The filename is: <Class name>.json - example: Rectangle.json
	- Uses the static method to_json_string previously created.
- Static method def from_json_string(json_string): that returns the list of the
JSON string representation json_string:
	- json_string is a string representing a list of dictionaries.
	- If json_string is None or empty, return an empty list.
	- Otherwise, returns the list represented by json_string.
### models/rectangle.py
- Defines Rectangle class with:
-Private instance attributes, each with its own public getter and setter:
	- __width -> width
	- __height -> height
	- __x -> x
	- __y -> y
- Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
	- id is initialized using the super call to the parent class __init__
	  method.
	- All arguments are asssigned to the right attributes.
- Public instance method: def area(self): that returns the area of the Rectangle
instance.
- Override __str__ method so that it returns: "[Rectangle] (<id>) <x>/<y> - 
<width>/<height>"
- Public instance method def display(self): that prints in stdout the Rectangle
instance with the character #.
	- y represents the vertical offset before the Rectangle is printed and x
	represents the horizontal offset of each line from the left margin.
	- width and height represent the dimensions of the Rectangle that is
	printed.
- Public instance method: def update(self, *args, **kwargs): that assigns an
argument to each attribute.
	- **kwargs is skipped if *args exists and is not empty.
- Public method def to_dictionary(self): that returns the dictionary
representation of a Rectangle:
	- the dictionary contains:
		- id
		- width
		- height
		- x
		- y
### models/square.py
- Defines the Square class that inherits from the Rectangle class.
- Class constructor: def __init__(self, size, x=0, y=0, id=None):
	- The init method of the super class is called to initialize the
	  attributes. width and height are initialized using size.
- Overloading __str__ method that returns: [Square] (<id>) <x>/<y> - <size>
	- where width or height is used in place of size.
- Public setter and getter size.
	- The setter assigns the width and height with the same value in that
	  order.
	- Setter has same validation as Rectangle for width and height. The
	  exception message is the one from width.
- public method def update(self, *args, **kwargs) that assigns attributes:
	- *args is the list of arguments - no-keyworded arguments
		- 1st argument should be the id attribute
		- 2nd argument should be the size attribute
		- 3rd argument should be the x attribute
		- 4th argument should be the y attribute
	- **kwargs is a keyworded list of arguments.
		- It is skipped if *args exists and is not empty.
- public method def to_dictionary(self): that returns the dictionary
representation of a Square:
	- the dictionary contains:
		- id
		- size
		- x
		- y
### tests/
- This directory includes tests for all models.

### models/base.py
- Defines the Base class with:
	- private class attribute __nb_objects = 0
	- class constructor: def __init__(self, id=None):
		- if id is not None, the public instance attribute id is
		  assigned with this value.
		- otherwise __nb_objects is incremented and the new value
		  assigned to the public instance attribute id.
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
### tests/
- Includes tests for all models.

### models/base.py
- Defines the Base class with:
	- private class attribute __nb_objects = 0
	- class constructor: def __init__(self, id=None):
		- if id is not None, the public instance attribute id is
		  assigned with this value.
		- otherwise __nb_objects is incremented and the new value
		  assigned to the public instance attribute id.

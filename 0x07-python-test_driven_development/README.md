### 0-add_integer.py
- Adds two integers.
- Prototype: def add_integer(a, b=98):
- a and b must be integers or floats, raises a TypeError exception with
the message a must be an integer or b must be an integer
- a and b are first casted to integers if they are float
- Returns an integer: the addition of a and b
### tests/0-add_integer.txt
- Test file for 0-add_integer.py
### 2-matrix_divided.py
- Divides all elements of a matrix.
- Prototype: def matrix_divided(matrix, div):
- matrix must be a list of lists of integers or floats, otherwise raises a
TypeError exception with the message matrix must be a matrix (list of
lists) of integers/floats
- Each row of the matrix must be of the same size, otherwise raises a TypeError
exception with the message Each row of the matrix must have the same size
- div must be a number (integer or float), otherwise raises a TypeError exception
with the message div must be a number
- div can’t be equal to 0, otherwise raises a ZeroDivisionError exception with
the message division by zero.
- All elements of the matrix are divided by div, rounded to 2 decimal
places
- Returns a new matrix.

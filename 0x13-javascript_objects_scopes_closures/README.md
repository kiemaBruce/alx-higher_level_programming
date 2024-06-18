### 0-rectangle.js
- Defines an empty Rectangle class and exports it.
### 1-rectangle.js
- Include constructor in Rectangle class.
- Constructor takes two arguments: w and h, and initializes them to instance
  attributes width and height respectively.
### 2-rectangle.js
- Create an empty object if either w or h is less than or equal to 0.
### 3-rectangle.js
- Adds instance method print() which prints the rectangle using the character
  'X'.
### 4-rectangle.js
- Adds rotate() instance method that exchanges the width and the height of the
  rectangle.
- Adds double() instance method that multiples the width and the height of the
  rectangle by 2.
### 5-square.js
- Defines Square class which inherits from Rectangle class in 4-rectangle.js
- Constructor takes one argument: size.
- Constructor of Rectangle is called using super()
### 6-square.js
- Create an instance method called charPrint(c) that prints the rectangle using
  the character c
  	- If c is undefined, use the character X.
### 7-occurrences.js
- Counts the number of occurences of an element in a list.
- Prototype: exports.nbOccurences = function (list, searchElement)
### 8-esrever.js
- Returns the reversed version of a list.
- Prototype: exports.esrever = function (list)
### 9-logme.js
- Counts the number of times a function has been called, and thus prints the
number of arguments already printed and the new argument value.
- Prototype: exports.logMe = function (item)
- Output format: <number arguments already printed>: <current argument value>
### 10-converter.js
- Converts a number from base 10 to another base passed as argument:
- Prototype: exports.converter = function (base)
- Uses closures to store the base so that subsquent calls to the returned
  function can convert it's argument to the base that was initially stored.

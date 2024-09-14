### 0-readme.js
- Reads and prints the content of a file.
- The file path is provided as an argument to the script.
- The content of the file is read in utf-8.
- In case of an error, the error object is printed.
### 1-writeme.js
- Writes a string to a file.
- The file path is the first argument to the script.
- The string to be written to the file is the second argument to the script.
- The content of the file is written in utf-8.
- In case of an error, the error object is printed.
### 2-statuscode.js
- Displays the response code of a GET request.
- The first argument to the script is the URL to request.
- Uses the request module
### 3-starwars_title.js
- Obtain the title of a Star Wars film with the provided id
- The first argument to the script is the movie id.
- Uses the request module.
### 4-starwars_count.js
- Prints the number of movies where the character “Wedge Antilles” is present.
- The first argument is the API URL of the Star wars API:
  https://swapi-api.alx-tools.com/api/films/
- Wedge Antilles is character ID 18
- Uses the request module.
### 5-request_store.js
- Gets the contents of a webpage and stores it in a file.
- The first argument is the URL to request.
- The second argument the file path to store the body response.
- The file is UTF-8 encoded.
- Uses the request module.
### 6-completed_tasks.js
- Computes the number of tasks completed by user id.
- The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
- Only prints users with completed tasks.
- Uses the request module.
### 100-starwars_characters.js
- Lists all characters of a Star Wars movie.
- The first argument is the Movie ID - example: 3 = “Return of the Jedi”
- One character is displayed per line in the same order of the list of
  characters in the /films/ response.
- Uses the Star Wars API (https://swapi-api.alx-tools.com/api/).

### 0-hbtn_status.py
- Fetch a url using urllib and display the body in a special format.
### 1-hbtn_header.py
- Takes in a URL, sends a request to the URL and displays the value of the
  X-Request-Id variable found in the header of the response.
- Uses urllib and sys packages only.
### 2-post_email.py
-  Takes in a URL and an email, sends a POST request to the passed URL with the
   email as a parameter, and displays the body of the response (decoded in
   utf-8)
- The email ia sent in the email variable.
- Uses the packages urllib and sys
### 3-error_code.py
- Takes in a URL, sends a request to the URL and displays the body of the
  response (decoded in utf-8).
- Manages urllib.error.HTTPError exceptions and prints: Error code: followed by
  the HTTP status code.
- Uses the packages urllib and sys.
### 4-hbtn_status.py
- Fetches https://alx-intranet.hbtn.io/status
- Uses the package requests
- Results are formatted in a special way.
### 5-hbtn_header.py
- Takes in a URL, sends a request to the URL and displays the value of the
  variable X-Request-Id in the response header.
- Uses the packages requests and sys
### 6-post_email.py
- Takes in a URL and an email address, sends a POST request to the passed URL
  with the email as a parameter, and finally displays the body of the response.
- The email is sent in the variable email
- Uses the packages requests and sys
### 7-error_code.py
- Takes in a URL, sends a request to the URL and displays the body of the
  response.
- If the HTTP status code is greater than or equal to 400, print: Error code:
  followed by the value of the HTTP status code
- Uses the packages requests and sys
### 8-json_api.py
- Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
  with the letter as a parameter.
- The letter is sent in the variable 'q'.
- If no argument is given, set q=""
- If the response body is properly JSON formatted and not empty, display the id
  and name like this: [<id>] <name>
- Otherwise:
	- Display Not a valid JSON if the JSON is invalid
	- Display No result if the JSON is empty
- Uses the packages requests and sys
### 10-my_github.py
- Takes your GitHub credentials (username and password) and uses the GitHub API
  to display your id
- Uses Basic Authentication with a personal access token as password to access
  your information (only read:user permission is needed)
- The first argument to the script should be your username
- The second argument should be your password (in your case, a personal access
  token as password)
- Uses the packages requests and sys
### 100-github_commits.py
- Shows 10 most recent commits to a repo by a specific user. These are listed
  from the most recent to the oldest.
- The script takes two arguments:
	- The first argument is the repository name
	- The second argument is the owner name
- Uses the packages requests and sys

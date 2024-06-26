### 0-select_states.py
- Lists all states from states table in hbtn_0e_0_usa database.
- The script takes 3 arguments: mysql username, mysql password and database
  name.
- The script connects to a MySQL server running on localhost at port 3306.
- Results are sorted in ascending order by states.id
### 1-filter_states.py
- Only list states that start with 'N'.
### 2-my_filter_states.py
- Display states that match the argument.
- The script takes 4 arguments: mysql username, mysql password, database name
  and state name.
- Results are sorted in ascending order by states.id
### 3-my_safe_filter_states.py
- Does the same thing as 2-my_filter_states.py but adds protection against SQL
  injection attacks.
### 4-cities_by_state.py
- Lists all cities from the database hbtn_0e_4_usa
- Takes 3 arguments: mysql username, mysql password and database name
### 5-filter_cities.py
- Takes in the name of a state as an argument and lists all cities of that
  state, using the database hbtn_0e_4_usa
### model_state.py
- Contains the class definition of a State and an instance Base =
  declarative_base():
- State class:
	- inherits from Base
	- links to the MySQL table states
	- class attribute id that represents a column of an auto-generated,
	  unique integer, can't be null and is a primary key
	- class attribute name that represents a column of a string with maximum
	  128 characters and can’t be null
- Uses SQLAlchemy module.
- Connects to a MySQL server running on localhost at port 3306
### 7-model_state_fetch_all.py
- Lists all State objects from the database hbtn_0e_6_usa
- Takes 3 arguments: mysql username, mysql password and database name
- Uses SQLAlchemy
### 8-model_state_fetch_first.py
- Prints the first State object from the database hbtn_0e_6_usa
### 9-model_state_filter_a.py
- Lists all State objects that contain the letter a from the database
  hbtn_0e_6_usa
### 10-model_state_my_get.py
- Prints the id of the state whose name is passed as an argument.
### 11-model_state_insert.p
- Adds the State object “Louisiana” to the database hbtn_0e_6_usa
### 12-model_state_update_id_2.py
- Changes the name of a State object from the database hbtn_0e_6_usa
- Change the name of the State where id = 2 to New Mexico
### 13-model_state_delete_a.py
- Deletes all State objects with a name containing the letter a
### model_city.py
- Contains the class definition of a City.
- City class:
	- inherits from Base (imported from model_state)
	- links to the MySQL table cities
	- class attribute id that represents a column of an auto-generated,
	  unique integer, can’t be null and is a primary key
	- class attribute name that represents a column of a string of 128
	  characters and can’t be null
	- class attribute state_id that represents a column of an integer, can’t
	  be null and is a foreign key to states.id
	- uses SQLAlchemy
### 14-model_city_fetch_by_state.py
- Prints all City objects from the database hbtn_0e_14_usa
- Takes 3 arguments: mysql username, mysql password and database name

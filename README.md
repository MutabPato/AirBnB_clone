ALX SE AirBnB clone project

This project is a clone of the AirBnb web application

Command interpreter
-------------------
In this project we built a  command interpreter that:
. creates a new object
. retrieves an object from a file
. does operations on objects
. update attributes of an object
. destroys an object

Execution (Interactive mode):
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

Execution (Non-interactive mode):
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

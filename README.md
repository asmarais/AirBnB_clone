# AirBnB_clone
Create an AIirBnB console

## 1- Project Description

This is the first step towards building our first full web application: the AirBnB clone. This first step is very important because we will use what we built during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help us to:

* create a new object
* retrive an object from a file
* do operations on objects
* destroy an object

## 1- Command Interpreter Description

### how to start it

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

### how to use it

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```


### The console should look like this in non-interactive mode:

```
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
```

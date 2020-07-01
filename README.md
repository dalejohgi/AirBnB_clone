<h1 align = "center">AirBnB Console</h1><br>
<p align="center">
    <img width="240" height="250" src="https://press.airbnb.com/wp-content/uploads/sites/4/2017/01/airbnb_vertical_lockup_web.png?fit=2096,1048g">
    <img width="240" height="250" src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTgv04Mtf6e2FIKr-NZ6DT4bCukasPbhiPV0A&usqp=CAU">
</p>

------------


## Description

This repository contains the files and directories to simulate a simple **AirBnB Console**. It simulates a Command Interpreter to create, update and remove data.
It is also supposed to carry out The **0x00. AirBnB clone - The console** at [Holberton School.](https://www.holbertonschool.com "Holberton School.")

## What could we do with this console?

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

------------

## Usage:

### Available classes
The next available classes are necessary to use the basic commands:
- `BaseModel`
- `Amenity`
- `City`
- `Place`
- `Review`
- `State`
- `User`
</br>

In order to initialize the `./console` type:
```
$ ./console.py 
(hbnb) 
```

### help
Used to get a help to understand how console works
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  classes  create  destroy  help  quit  show  update

(hbnb)
```

## create
Used to generate new objects. It's necessary to use it with the available classes:
```bash
(hbnb) create BaseModel
3159a6f1-d301-4ebd-be91-5aa712c8a2ea
(hbnb) 
```
Note that in this process an `id` was created by default. It will be used later.

## show
Used to print the string representation of an object
```bash
(hbnb) show BaseModel 3159a6f1-d301-4ebd-be91-5aa712c8a2ea
BaseModel] (3159a6f1-d301-4ebd-be91-5aa712c8a2ea) {'id': '3159a6f1-d301-4ebd-be91-5aa712c8a2ea', 'updated_at': datetime.datetime(2020, 7, 1, 16, 39, 10, 792620), 'created_at': datetime.datetime(2020, 7, 1, 16, 39, 10, 782799)}
( hbnb) 
```
Note how `id` was used to get the strinf the specified object

## all
Prints all the string representation of all instances. It may be used with the name of the name of the class, ex: `all BaseModel` and just by typing the name of the command, ex: `all`
```bash
(hbnb) all BaseModel
["[BaseModel] (b0da7367-5440-4a2e-af47-51970d1b2c4e) {'id': 'b0da7367-5440-4a2e-af47-51970d1b2c4e', 'updated_at': datetime.datetime(2020, 6, 30, 22, 43, 34, 252295), 'created_at': datetime.datetime(2020, 6, 30, 22, 43, 34, 251154)}", "[Place] (b523e341-cce4-4782-a0da-6ad44e47f502) {'id': 'b523e341-cce4-4782-a0da-6ad44e47f502', 'created_at': datetime.datetime(2020, 6, 30, 20, 15, 59, 323067), 'number_rooms': 15, 'updated_at': datetime.datetime(2020, 6, 30, 20, 15, 59, 325976)}", "[BaseModel] (3159a6f1-d301-4ebd-be91-5aa712c8a2ea) {'id': '3159a6f1-d301-4ebd-be91-5aa712c8a2ea', 'updated_at': datetime.datetime(2020, 7, 1, 16, 39, 10, 792620), 'created_at': datetime.datetime(2020, 7, 1, 16, 39, 10, 782799)}"]
(hbnb) 

```

## 





	



## Requirements

### Python Scripts.

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using **python3** (version 3.4.3)
- All your files should end with a new line
The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version 1.7 or more)
- All your files must be executable
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__`)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)


### Python Unit Tests
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest "unittest module.")
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start by `test_`
- Your file organization in the tests folder should be the same as your project
- e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
- e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)`' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Authors:

- *David Hincapié* - [@dalejohgi](https://github.com/dalejohgi)
- *Nicolás Zárate*  - [@Nicolanz](https://github.com/Nicolanz)



# chat_server

# Purpose
Write Python server to work with iOS chat client app.

# References
Networking Tutorial for iOS: How To Create A Socket Based iPhone App and Server
by Cesare Rocci 2011-06-28
Includes Python server
https://www.raywenderlich.com/3932/networking-tutorial-for-ios-how-to-create-a-socket-based-iphone-app-and-server

# Results


## Appendix virtual environment venv

The project uses a virtual environment.

https://docs.python.org/3/library/venv.html

This can hold a python version and pip installed packages such as "requests".

https://github.com/kennethreitz/requests

### Install virtual environment in directory named "venv"

    $ pyvenv venv

### Before activating virtual environment

On my machine, active python is 2.7.11

    ➜  chat_server git:(master) ✗ which python
    /usr/local/bin/python
    ➜  chat_server git:(master) python --version
    Python 2.7.11

On my machine, to use python3 must specify python3

    ➜  chat_server git:(master) which python3
    /usr/local/bin/python3

### Activate virtual environment

    ➜  chat_server git:(master) source venv/bin/activate

### Now active python is in venv and is version 3.5.1

Notice command prompt shows venv is active

    (venv) ➜  chat_server git:(master) which python
    /Users/stevebaker/Documents/projects/pythonProjects/chat_server/venv/bin/python
    (venv) ➜  chat_server git:(master) python --version
    Python 3.5.1

### Deactivate virtual environment
In shell run deactivate
    (venv) ➜  chat_server git:(master) ✗ deactivate

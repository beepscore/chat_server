# chat_server

# Purpose
Write Python server to work with iOS chat client app.

# References

## Networking Tutorial for iOS: How To Create A Socket Based iPhone App and Server
by Cesare Rocci 2011-06-28

Includes Python chat_server and iOS ChatClient

https://www.raywenderlich.com/3932/networking-tutorial-for-ios-how-to-create-a-socket-based-iphone-app-and-server

## iOS client ChatClient
https://github.com/beepscore/ChatClient

# Results

## Python
The virtual environment runs Python 3.5.1

## Twisted
Twisted has been partially updated to work with Python 3.

If thist tutorial doesn't work, might need to change to Python 2.x

### Start server
Need to use sudo

http://stackoverflow.com/questions/13889928/twisted-internet-error-cannotlistenerror-couldnt-listen-on-any80-errno-13

    (venv) ➜  chat_server git:(master) ✗ sudo python chatserver.py
    Password:
    Iphone Chat server started

### Stop server
https://twistedmatrix.com/documents/current/web/howto/using-twistedweb.html

This didn't work, does it need numeric value of process id?

    kill 'cat twistd.pid'

Ctrl-c seems to work.

### Use telnet to test server
Open a second terminal window.

    ➜  chat_server git:(master) ✗ telnet localhost 80
    Trying ::1...
    telnet: connect to address ::1: Connection refused
    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.

Connected to localhost shows telnet connected to twisted server.

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


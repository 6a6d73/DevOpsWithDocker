# 2.11 Python development environment

This exercise creates a Python development environment.

First create the `app.py` application file and supply code so that it can handle a couple of web requests.

## Dockerfile

Copying `requirements.txt`, then installed with `pip3 install -r requirements.txt`

## docker-compose.yml

The command will start the server and includes options in the command to allow outside access to the server.

The environment variables are used so that the application is restarted as changes occur. 

A volume is also setup so that the application can be edited on the local machine and the changes reflected on the server.
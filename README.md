This dicertory contains work on part 1 of a AirBnB clone.
this clone will use concepts as Object Oriented Programming, Flask Wokflow and Docker Containerization.
The app revolves around the app.py file
This file will be executed and will call all the classes and functions we have defined
in the app directory we have the model folder, this folder will contain modules of classes representing the data we want to manage.
also inside of the app folder we have the persistance directory
this contains the Ipersistence.py and the DataManager.py files.
The IPersistence directory will contain the IPersistence abstract class that creates a blueprint of sorts for the methods to be defined by the DataManager.py

The DataManager.py file will contain functions dedicated to managing data localy as in creating deleting saving objects etc.

back to the app directory the last directory to discuss is the API directory
this directory contains  Requests and endpoints written in flask to create the logic of our application

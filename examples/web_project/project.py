"""

./examples/web_project/project.py

-------------------------------

This file is the configuration file for Medaf.

LOCAL_APPS: Configuring installed local apps (Apps inside your project) in your project.
PLUGIN_APPS: Configuring installed plugin apps in your project.

There are 2 types of apps:

- local: Those apps inside your project directory.
- plugin: Those apps inside a python package that you installed.

Based on the functionality:

- content: Those apps

-------------------------------

Copyright (C) 2022, Anokidev. All right reserved. 
Medaf is licensed in MIT License, see ./LICENSE.md for more info.

"""

# Local apps inside your project.
LOCAL_APPS = {
    'CONTENT':['my_app'],
    'MIDDLEWARE':[],
    'GATEWAY':[]
}

# Plugin apps inside your project.
PLUGIN_APPS = {
    'CONTENT':[],
    'MIDDLEWARE':[],
    'GATEWAY':[]
}
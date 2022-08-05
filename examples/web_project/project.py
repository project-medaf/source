"""

./examples/web_project/project.py

-------------------------------

This file is the configuration file for Medaf.

LOCAL_APPS: Configuring installed local apps (Apps inside your project) in your project.
PLUGIN_APPS: Configuring installed plugin apps in your project.

There are 2 types of apps:

Based on the location:

- Local app: These type of apps are located inside your project directory.
- Plugin app: Those type of apps are located inside a python package that you installed.

Based on the functionality:

- Content app: Those apps are the one that are going to handle the "content". For example: On a web project, a content app are going to create response, such as an HTTP response.

- Middleware app: These apps have the ability to modify data sended from content apps to gateway apps and vice versa. For example: On a web project, a middleware app can modify requests and responses.

- Gateway app: These apps are the "gateway". For example: On a web project, a gateway app will accept request from a WSGI server. Gateway apps can also send data (For a web project, a gateway app is going to send response to the WSGI server).

-------------------------------

Copyright (C) 2022, Anokidev. All right reserved. 
Medaf is licensed in MIT License, see ./LICENSE.md for more info.

"""

# Local apps inside your project.
LOCAL_CONTENT_APPS    = ['my_apps']
LOCAL_MIDDLEWARE_APPS = []
LOCAL_GATEWAY_APPS    = []

# Plugin apps inside your project.
PLUGIN_CONTENT_APPS    = []
PLUGIN_MIDDLEWARE_APPS = []
PLUGIN_GATEWAT_APPS    = []

# Debug mode.
DEBUG_MODE = True
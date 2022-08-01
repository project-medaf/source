"""

./internal/cli/handler.py

-------------------------------

This file handles apps CLI.

What is an app CLI? An app CLI is an extension to the Medaf CLI. For example, let's say that their is an app called "example_1" that add an HTTPS tunnel, then the example_1's app CLI will look like this: 

medaf example_1 set_certificate "./key.crt"

There is a bundled app called 'project' and 'plugin' for managing Medaf projects and plugins.

medaf project init --name="my-website"
medaf project run --mode="dev"

medaf plugin install a_plugin
medaf plugin remove a_plugin

medaf plugin register a_plugin
medaf plugin unregister a_plugin

-------------------------------

Copyright (C) 2022, Anokidev. All right reserved. 
Medaf is licensed in MIT License, see ./LICENSE.md for more info.

"""

class Handler:

    def __init__(self):

        pass
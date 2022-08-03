"""

./internal/cli/parser.py

-------------------------------

This file parses the CLI command and handles app CLI.

What is an app CLI? An app CLI is an extension to the Medaf CLI. For example, let's say that their is an app called "example_1" that add an HTTPS tunnel, then the example_1's app CLI will look like this: 

medaf example_1 set_certificate "./key.crt"

There are 2 bundled apps called 'project' and 'plugin' for managing Medaf projects and plugins.

medaf project init --name="my-website"
medaf project run --mode="dev"

medaf plugin install a_plugin
medaf plugin remove a_plugin

medaf plugin register a_plugin
medaf plugin unregister a_plugin

There are 2 minor bundled apps called 'help' and 'version'... Which does exactly like what you think.

-------------------------------

Copyright (C) 2022, Anokidev. All right reserved. 
Medaf is licensed in MIT License, see ./LICENSE.md for more info.

"""

import sys

from medaf.internal.cli.project import Project
from medaf.internal.cli.plugin import Plugin
from medaf.internal.cli.help import Help
from medaf.internal.cli.version import Version

HELP = r"""
Medaf help:

All "commands" are actually apps CLI. There are bundled
apps such as: project, plugin, help, and version.

project:
    - init [PROJECT_NAME] : Initialize a new project.
        - "--template=[TEMPLATE]" : Insert template.
    - run [APP_NAME] : Run an app INSIDE your project.
        - "--debug=[true, false]" : Enable debug mode.

plugin:
    - install [PLUGIN_NAME] : Install and register a plugin.
    - remove [PLUGIN_NAME] : Remove a plugin.

help / --help / -h:
    - [NO_SUBCOMMAND] : Show this.

version / --version / -v:
    - [NO_SUBCOMMAND] : Show version.
    - credits : Show credits.
    - changelogs : Show changelogs."""

class Parser:

    def __init__(self):
        pass

    def __call__(self, args: list, apps: list):

        try:
            app: str        = args[0]
        except IndexError:
            print("ERROR: No apps specfied.")
            print("Type 'medaf --help' for more info.")
            sys.exit(1)

        try:
            command: str = args[1]
        except IndexError:
            command: str = None

        try:
            additional: str = args[2:]
        except IndexError:
            additional: str = None

        apps.append(HELP)

        if (app == "project"):
            project = Project()
            project(command, additional)
        elif (app == "plugin"):
            plugin = Plugin()
            plugin(command, additional)
        elif (app == "help"):
            self.__help(apps)
        elif (app == "version"):
            self.__version(command)
        else:
            pass

    
    def __help(self, apps: list):

        for i in apps:
            sys.stdout.write(i)
            sys.stdout.write("\n")

    def __version(command):

        if (command == None):
            print("Medaf version 0.0.0a1")
        
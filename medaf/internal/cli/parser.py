"""

./medaf/internal/cli/parser.py

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

HELP = """
Medaf help:

All "commands" are actually apps CLI. There are bundled
apps such as: project, plugin, help, and version.

Basically:

medaf [APP NAME] [COMMAND NAME] [SUBCOMMAND NAME]

project:
    - init [PROJECT NAME] : Initialize a new project.
        - "--template=[TEMPLATE]" : Insert template.
    - run [APP NAME] : Run an app INSIDE your project.
        - "--debug=[true, false]" : Enable debug mode.

plugin:
    - install [PLUGIN NAME] : Install and register a plugin.
    - remove [PLUGIN NAME] : Remove a plugin.
    - register [PLUGIN_NAME] : Register a plugin.
    - unregister [PLUGIN_NAME] : Unregister a plugin.
    - help [PLUGIN_NAME] : Show a plugin's help message, if the help message does exist.

help / --help / -h:
    - [NO SUBCOMMAND] : Show this.

version / --version / -v:
    - [NO SUBCOMMAND] : Show version.
    - credits : Show credits.
    - changelogs : Show changelogs.
    - license : Show license."""

LICENSE = """MIT License

Copyright (c) 2022 Project MEDAF

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

class Parser:

    def __init__(self) -> None:
        pass

    # Parse commands.
    def __call__(self, args: list, apps_list: list) -> None:

        """Parse commands.
        
        @param args: list
            This contains the already parsed CLI commands.

        @param apps: list
            This contains the list of apps. Not including:
            - project
            - plugin
            - help
            - version

        @return None

        """

        # Check if an app if specified.
        try:
            app: str = args[0]
        except IndexError:
            print("ERROR: No apps are specified.")
            print("Type 'medaf --help' for more info.")
            sys.exit(1)

        # Check if a command is specified.
        try:
            command: str = args[1]
        except IndexError:
            command: str = None

        # Check if a subcommand or it's flags are specified.
        try:
            subcommand: list = args[2:]
        except IndexError:
            subcommand: list = None

        # Add HELP to the apps list. Index 0.
        apps: list = HELP + apps

        if (app == "project"):
            project = Project()
            project(command, subcommand)
        elif (app == "plugin"):
            plugin = Plugin()
            plugin(command, subcommand)
        elif (app == "help"):
            self.__help_app()
        elif (app == "version"):
            self.__version_app(command)
        else:
            pass

    # Help app.
    def __help_app(self) -> None:

        """Help app.

        @return None
           
        """

        # Print every single apps.
        print(HELP)
        sys.exit(0)

    # Version app.
    def __version_app(command) -> None:

        if (command == None):
            print("\nMedaf version 0.0.0a1")
            sys.exit(0)
        elif (command == "credits"):
            print("\nMedaf credits:")
            print("Created and developed by Anokidev.")
            sys.exit(0)
        elif (command == "changelogs"):
            print("\nMedaf changelongs:")
            print("- Implemented the plugin  and CLI system.")
            sys.exit(0)
        elif (command == "license"):
            print(LICENSE)
            sys.exit(0)
        else:
            print(f"ERROR: Unknown command {command}.")
            sys.exit(1)
            
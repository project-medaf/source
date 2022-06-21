'''

medaf/internal/cli/main.py

Copyright (c) 2022, Anokidev.
Licensed in MIT License.
This file is part of medaf.

This is responsible for parsing CLI commands.

'''

import sys
import re

from medaf.internal.cli.app import App
from medaf.internal.cli.depen import Depen
from medaf.internal.cli.helper import helper
from medaf.internal.cli.version import version

class Main:

    '''
        This class is going to parse the CLI args.
    '''

    def __init__(self) -> None:

        '''Create some attributes.'''

        print("\nMEDAF version 0.0.0a1.")
        print("Copyright (c) 2022 Project MEDAF.")
        print("Licensed in MIT License.\n")

        self.__cwd: str         = ""
        self.__command: str     = ""
        self.__subcommand: str  = ""
        self.__app: str         = ""
        self.__flags: dict      = {}

        self.__app_manager      = App()
        self.__depen_manager    = Depen()

    def __call__(self, args: list, cwd: str) -> None:

        self.__cwd: str = cwd

        # Check for commands.
        try:
            self.__command: str = args[1]
        except IndexError:
            print("Error: A command must be specified!")
            sys.exit(1)

        # Check for subcommands.
        try:
            self.__subcommand: str = args[2]
        except IndexError:
            self.__subcommand: bool = False

        # App.
        try:
            self.__app: str = args[3]
        except IndexError:
            self.__app: bool = False

        # Flags.
        raw_flags: list = args[4:]
        self.__flags: dict = {}

        for i in raw_flags:
            result: list = re.split("=",i)
            self.__flags[result[0]] = result[1]

        del raw_flags

        self.__check()

    def __check(self):

        command: str       = self.__command
        subcommand: str    = self.__subcommand

        app_manager        = self.__app_manager
        depen_manager      = self.__depen_manager

        cwd: str           = self.__cwd
        app: str           = self.__app

        # 'app' command. Manage your application.
        # - 'new'     : Create an app.
        # - 'run'     : Run an app.
        # - 'remove'  : Remove an app.
        if command in ('app', '-a'):

            if subcommand == 'new':
                app_manager.new(cwd, app)
            elif subcommand == 'run':
                app_manager.run(cwd, app)
            elif subcommand == 'remove':
                app_manager.remove(cwd, app)
            else:
                print("Error: Unknown subcommand.")
                print("Run 'medaf --help' for more info.")
                sys.exit(1)


        # 'depen' command. Manage your dependencies.
        # - 'install' : Install an app plugin dependencies.
        # - 'remove'  : Remove an app plugin dependencies.
        elif command in ('depen', '-d'):

            if subcommand == 'install':
                pass
            elif subcommand == 'remove':
                pass
            else:
                print("Error: Unknown subcommand.")
                print("Run 'medaf --help' for more info.")
                sys.exit(1)

        # 'help' command. Show command lists.
        elif command in ('help', '--help', '-h'):
            print(helper)
            sys.exit(0)

        # 'version' command. Show the current version of medaf.
        elif command in ('version', '--version', '-v'):
            print(version)
            sys.exit(0)

        # Invalid command.
        else:
            print(f"Error: Invalid command '{command}'")
            print("Type 'medaf --help' for more info.")
            sys.exit(1)

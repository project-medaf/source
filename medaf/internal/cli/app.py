'''

medaf/internal/cli/app.py

Copyright (c) 2022, Anokidev.
Licensed in MIT License.
This file is part of medaf.

This is responsible for parsing CLI commands.

'''

import sys
import os
import importlib.util

from medaf.internal.config.get import LoadRCConfig

class App:

    '''
        This class is responsible for the 'app' command.
        'app' command itself is used to manage apps.
    '''

    def __init__(self):
        pass

    def new(self, cwd: str, app: str):

        '''This command will create a new app.'''

        print(": Attempting to load RC configuration.")

        # Load RC c
        LoadRCConfig.reset()

        # Get the Project-Layout config from an app.
        config = GetRCConfig(app)

        project_layout: dict = config.get_config('Project-Layout')
        root_path: str = project_layout['Root-Path']
        apps_path: str = project_layout['Apps-Path']

        # Get the app_path.
        if root_path == '.':
            app_path: str = f"{cwd}/{apps_path}/"
        else:
            app_path: str = f"{cwd}/{root_path}/{apps_path}"

        # Create the folder.


    def run(self):
        '''This commmand will run an app.'''

    def remove(self):
        '''This command will remove an app.'''

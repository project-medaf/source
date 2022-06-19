'''

medaf/internal/cli/app.py

Copyright (c) 2022, Anokidev.
Licensed in MIT License.
This file is part of MADAF.

This is responsible for parsing CLI commands.

'''

import importlib.util

from madaf.api.config.get import GetRCConfig

class App:

    '''
        This class is responsible for the 'app' command.
        'app' command itself is used to manage apps.
    '''

    def __init__(self):
        pass

    def new(self, cwd: str, app: str):

        '''This command will create a new app.'''

        print(f"==> Attempting to create a new app called '{app}'.")

        madafrc: str = f"{cwd}/madarc.py"

        # 1. Import the main function from madafrc.
        # 2. Call the main function.
        # 3. Now, the config should be changed.

        print("   -> ")

        try:
            spec = importlib.util.spec_from_file_location("main", madafrc)
            madafrc_main = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(madafrc_main)
            madafrc_main()
        except ImportError:
            print(f"==> Failed to create an app called '{app}'.")
            print("")

        # Get the Project-Layout config from an app.
        config = GetRCConfig(app)

        project_layout: dict = config.get_config('Project-Layout')
        root_path: str = project_layout['Root-Path']
        apps_path: str = project_layout['Apps-Path']

        # Get the app_path.
        if root_path == '.':
            app_path = f"{cwd}/{apps_path}/"
        else:
            app_path = f"{cwd}/{root_path}/{apps_path}"

        # Create the folder.


    def run(self):
        '''This commmand will run an app.'''

    def remove(self):
        '''This command will remove an app.'''

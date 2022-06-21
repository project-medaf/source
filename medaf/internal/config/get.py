'''

medaf/internal/config/get.py

Copyright (c) 2022, Anokidev.
Licensed in MIT License.
This file is part of medaf.

This is responsible for getting the project configuration.

'''

import os
import sys
import importlib.util

from medaf.api.config.get import GetRCConfig

class LoadRCConfig:

    '''Get the RC configuration.'''

    def __init__(self):
        pass

    def reset(self, path: str, app_id: str):

        '''This will get the RC configuration.'''

        # Declare a variable that contains a path.
        medafrc_path: str = os.path.join(path, "medafrc.py")

        # Import.

        try:
            spec = importlib.util.spec_from_file_location("main", medafrc_path)
            medafrc_main = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(medafrc_main)
            medafrc_main()
        except ImportError:
            sys.exit(1)

        # NASTY CODE: Get the main.py's path of the app configurations folder.
        config = GetRCConfig()
        configs_path: str = os.path.join(path, config.get('Project-Layout')['Configs-Path'])
        app_config_path: str = os.path.join(configs_path, app_id)
        app_main_config_path: str = os.path.join(app_config_path, "main.py")

        del config, configs_path, app_config_path

        try:
            # Import the file, and then call the main function to save the function.
            spec = importlib.util.spec_from_file_location("main", app_main_config_path)
            app_config_main = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(app_config_main)
            app_config_main()
        except ImportError:
            sys.exit(1)

    def load(self, config: dict):

        '''Load the configuration.'''

        GetRCConfig.config = config

from xdg.BaseDirectory import (
        load_first_config,
        save_data_path
        )
import json

def _get_config(app=None, file=None):
    return json.load(
            open(
                load_first_config(
                    'oauth2token',
                    app,
                    file),
                'r'))


def get_json_config(app=None):
    return (_get_config(app, 'config.json'),
            _get_config(app, 'scopes.json')
            )


def get_credentials_file(app=None, user=None, override=False): 
    mode = 'wb' if override else 'rb+'
    return open(save_data_path(
        'oauth2token', app) + '/' + user, mode)

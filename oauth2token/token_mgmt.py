#!/usr/bin/env python

from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import argparse
import os
from google.auth.transport.requests import Request
from .app_creds import get_json_config, get_credentials_file


def create_user_credentials(app=None, user=None, **kwargs): 
    flow = InstalledAppFlow.from_client_config(
            *get_json_config(app=app)
       )

    flow.run_local_server(port=0)

    creds = flow.credentials
    creds._scopes = flow.oauth2session.token["scope"]

    pickle.dump(creds, get_credentials_file(app=app, user=user, override=True))

def get_token(**kwargs):
    with get_credentials_file(**kwargs) as user_file:
        creds = pickle.load(user_file)
        if creds.expired:
            creds.refresh(Request())
            user_file.seek(0)
            pickle.dump(creds, user_file)
            user_file.truncate()
    return creds.token

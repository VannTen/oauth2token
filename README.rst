###############
# Oauth2token #
###############

Simple cli tools to create and use oauth2token


Configuration
-----------------------

You need to create :code:`config.json` and :code:`scopes.json` at
:code:`$XDG_CONFIG_HOME/oauth2token/<provider>/` for each provider you want
to use.

:code:`config.json`
~~~~~~~~~~~~~~~~~~~~

The main configuration file.
Follow the format on client_secret.json_, using your own information obtained
from your provider.

.. _client_secret.json: https://github.com/googleapis/google-api-python-client/blob/master/docs/client-secrets.md

Example (Just change the :code:`client_id` and :code:`client_secret` values to
the ones you got from Google):

.. code-block:: json

    {
        "web": {
            "client_id": "asdfjasdljfasdkjf",
            "client_secret": "1912308409123890",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://accounts.google.com/o/oauth2/token"
        }
    }

:code:`scopes.json`
~~~~~~~~~~~~~~~~~~~~

The scope your application needs. It's a json array containing the URLs.

Example :

.. code-block:: json

    ["https://mail.google.com/"]


Usage
-----


:code:`oauth2create` <provider> <account>

Obtain and store credentials for the account in
:code:`$XDG_DATA_HOME/oauth2token/<provider>/<account>`, using the configuration
for that provider. It opens a browser where you'll need to log in the account
you want to use.

:code:`oauth2get` <provider> <account>

Output the access token for that account, refreshing it if needed with the
associated refresh token.

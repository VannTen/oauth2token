###############
# Oauth2token #
###############

Simple cli tools to create and use oauth2token


Configuration
-----------------------

You need to create :code:`config.json` and :code:`scopes.json` at
:code:`$XDG_CONFIG_HOME/<provider>/` for each provider you want
to use.
:code:`config.json` :

See Google client_secret.json_.

.. _client_secret.json: https://github.com/googleapis/google-api-python-client/blob/master/docs/client-secrets.md

You'll need to obtain your own from the provider.

:code:`scopes.json`:
The scope your application need as a json array.

Example :

.. code-block:: json

    ['https://mail.google.com/', ..., ...]


Usage
-----


:code:`oauth2create` <provider> <account>

Obtain and store credentials in `$XDG_DATA_HOME/<provider>/<account>` in binary
form, using the configuration for that provider. It use the "Installed App flow"
open a brower where you'll need to log in the account you want to use, then
redirect to the loopback address to obtain the credentials.


:code:`oauth2get` <provider> <account>

Output the access token for that account, refreshing it if needed with the
associated refresh token.

#!/usr/bin/env python

import json
import imaplib, smtplib
import base64
from token_mgmt import get_token

def oauth2_string(username, access_token):

  auth_string = 'user=%s\1auth=Bearer %s\1\1' % (username, access_token)
  return auth_string


def test_imap(auth_string):
    with  imaplib.IMAP4_SSL('imap.gmail.com') as imap_conn:
      imap_conn.debug = 4
      imap_conn.authenticate('XOAUTH2', lambda x: auth_string)
      imap_conn.select('INBOX')

def test_smtp(auth_string):
    with smtplib.SMTP_SSL('smtp.gmail.com') as smtp_conn:
      smtp_conn.set_debuglevel(True)
      smtp_conn.ehlo('test')
      auth_string = base64.b64encode(auth_string.encode()).decode()
      smtp_conn.docmd('AUTH', 'XOAUTH2 ' + auth_string)


test_imap(oauth2_string(
    "ashelia1000@gmail.com",
    get_token(app='gmail', user='max')))
test_smtp(oauth2_string(
    "ashelia1000@gmail.com",
    get_token(app='gmail', user='max')))

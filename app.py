#!/usr/bin/env python

# Generated by coltrane==0.33.0

from django.core.management import execute_from_command_line

from coltrane import initialize
import os


IS_HEROKU_APP = "DYNO" in os.environ and not "CI" in os.environ
if IS_HEROKU_APP:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]", "0.0.0.0"]


wsgi = initialize(
    ALLOWED_HOSTS=ALLOWED_HOSTS
                                   )

if __name__ == "__main__":
    execute_from_command_line()

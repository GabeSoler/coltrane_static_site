#!/usr/bin/env python

# Generated by coltrane==0.33.0

from django.core.management import execute_from_command_line

from coltrane import initialize



wsgi = initialize(ALLOWED_HOSTS = ['0.0.0.0',
                                   
                                   ], 
                                   )

if __name__ == "__main__":
    execute_from_command_line()

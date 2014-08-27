#!/bin/bash
python2 manage.py schemamigration example_app --auto
python2 manage.py migrate example_app

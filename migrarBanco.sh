#!/bin/bash
python manage.py schemamigration example_app
python manage.py migrate
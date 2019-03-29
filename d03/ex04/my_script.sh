#!/bin/sh

if [ -d "django_venv" ]; then rm -Rf django_venv; fi

virtualenv -p python3 django_venv

django_venv/bin/pip install -r requirement.txt

source django_venv/bin/activate
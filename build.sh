#!/usr/bin/env bash
#exit an error
set -o errexit

#modify this line as needed for your package (pi, poetry, etc)
pip install -r requirements.txt

#convert static asset files
python manage.py collectstatic --no-input

#apply anay outstanding database migrations
python manage.py migrate
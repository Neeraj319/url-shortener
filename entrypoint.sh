#!/bin/bash

mkdir data 

touch data/app.db

python manage.py create_tables

python app.py
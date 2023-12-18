# Cusotmer Support Ticketing System (CSTS)
Simple customer support ticketing system that allows users to create, update, and track tickets, and allows support staff to view, update, and resolve tickets.

## Running server
Install dependencies:

`pip install -r requirements.txt`

If there is no local development db:

`py backend/manage.py makemigrations tickets`

`py backend/manage.py migrate`

Run server:

`py backend/manage.py runserver`
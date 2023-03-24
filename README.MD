How to run servers
==================
daphne -b 0.0.0.0 -p 8080 core.asgi:application
./manage.py runserver
./manage.py process_tasks
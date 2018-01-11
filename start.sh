uwsgi --socket mysite.sock --wsgi-file test.py
uwsgi --socket :8001 --wsgi-file test.py
uwsgi --socket mysite.sock --module mysite.wsgi --chmod-socket=666

Useful notes from tutorial

after making changes to Models:
-add config to mysite/settings.py INSTALLED_APPS
-run >python manage.py makemigrations polls (or whatever the model is)
this creates a migration. 
We can read a version of the migration with >python manage.py sqlmigrate polls 0001 (pretty cool)
We can use a migration to create model tables in our database >python manage.py migrate
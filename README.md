# Before run it.
if you didn't install django, use follow command to install django.
```
pip install django
```

# How to run this project?
Use following command to create a superUser in this django project.
```
python manage.py createsuperuser
```
Use following commmand in to root of the projct to use the default databases sqlite3.
```
python manage.py migrate

python manage.py makemigrations
```
then visit http://localhost:8000/admin and type your username and password and follow following picture.
![](/demo.png)
![](/demo2.png)



Use following commmand in to root of the projct to run this project
```
python manage.py runserver
```

Visit http://localhost:8000 you can see the page.


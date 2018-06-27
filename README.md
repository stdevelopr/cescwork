# CESCWORK
Under construction...
Collaborators are welcome.
Verify the actual stage: http://stdevelopr.pythonanywhere.com/cescwork/

This is being built in Python 3.6.5 with Django.
Learn it here: https://www.djangoproject.com/


# How to run on your machine

If you do not have virtualenvwrapper installed, just install it:
```
pip install virtualenvwrapper
```
- Create a virtualenviroment:
```
mkvirtualenv cescwork
```

- Make sure your virtualenv is active:
```
workon cescwork
```

- Clone this repo:
```
git clone https://github.com/stdevelopr/cescwork.git
```
- Enter the folder cescwork
```
cd cescwork
```

- Install the requirements:
```
pip install -r requirements.txt
````
- Construct the database:
```
python manage.py makemigrations
python manage.py migrate
```
- Run the server:
```
python manage.py runserver
```
<p>
Open on your browser:
http://127.0.0.1:8000/
  
To create works enter as admin:
```
python manage.py createsuperuser
```
Then type the created username and password in:
http://127.0.0.1:8000/admin

Create works, and see that on the main page...

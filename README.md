# Hiking Trails (https://hikingtrails-dzc7aecgcsgthyck.italynorth-01.azurewebsites.net)

Hiking Trails is a web application designed to help users find and share hiking trails.
Аnyone not registered can view the trails and their details, but cannot create, edit or delete trails
The application allows users to register, log in, and explore various hiking trails.
Тhose who are designated by the administrator as approved can edit and delete other people's trails.

## Features

- Hiker registration and authentication
- View details, edit and delete hiker's own profile
- Browse and search for hiking trails
- Add, edit, delete and view details own hiking trails
- Recording suggestions and signals in the recommendations book
- Send welcome emails to new users

## Technologies Used

- Python
- Django
- JavaScript
- HTML/CSS
- PostgreSQL
- Other dependencies listed in requirements.txt

## Installation on local machine with PyCharm or other Python IDE:

1. Clone the repository:
   
git clone https://github.com/tod36/HikingTrails
cd hiking-trails

2. Create a virtual environment:
   
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
   
pip install -r requirements.txt

4. Set up the database, see -https://docs.djangoproject.com/en/5.1/ref/settings/#databases:
   
python manage.py migrate

5. Create a superuser:
   
python manage.py createsuperuser

6. Configuration:

From .env.template fill in the variables

7. Run the development server:
   
python manage.py runserver

8. Running tests:

python manage.py test

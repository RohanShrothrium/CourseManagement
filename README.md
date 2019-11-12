# CourseManagement
A course management portal for IIT Dh

# Steps Tu Run The Program
## Install required packages
    pip install -r Course_Management/requirements.txt
## Create Migrations
    cd Course_Management
    python3 manage.py makemigrations
## Create Table In Database
    cd Course_Management
    python3 manage.py migrate
## Now Create Superuser
    cd Course_Management
    python3 manage.py createsuperuser
## Now you can start the website by
    cd Course_Management
    python3 manage.py runserver
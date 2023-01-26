# FLORES

This application is designed to enter various varieties of flowers in a table, where you can perform, create, modify, update and delete


# Clone the repository

https://github.com/castilloxavie/flores


# Create virtual venv and activate

create:
  virtualenv name_env 
  
activate:
  On Unix or MacOS, using the bash shell: source venv/bin/activate
  On Windows using the Command Prompt: path\venv\Scripts\activate.bat
  
  
# Install libraries

pip install -r requirements.txt


# Run proyect

python manage.py runserver


# Create migrations

-python manage.py makemigrations
-python manage.py migrate


# Note 

-the database used in ther project is mysql

-port used thet should not be busy or with local services turned off:
  
  django:8000



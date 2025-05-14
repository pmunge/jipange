 Event Contributions Tracker

A Django-based web application for managing and tracking financial or material contributions per event from a group of people. The system supports full CRUD operations for contributors, events, and their respective contributions.


Features

-  Create, read, update, and delete:
  - Members/Contributors
  - Events (e.g., weddings, fundraisers)
  - Individual contributions per event
-  View total contributions by person or event
-  Event-specific contribution tracking
-  User authentication (optional for admin control)



 Tech Stack

- Backend: Django (Python)
- Frontend: Django Templates / Bootstrap ( CSS framework)
- Database: SQLite 
- Deployment Ready: WSGI support, static file management


Getting started 
clone the repo
   https://github.com/pmunge/jipange.git
   cd jipange

python -m venv venv
Windows: venv\Scripts\activate. If using Linux source venv/bin/activate

pip install django
pip install 
python manage.py migrate
python manage.py runserver





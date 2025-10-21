# Tourist Management System

A web-based Tourist Management System built with **Python** and **Django**. This project allows users to manage destinations, tour packages, and user profiles.

---

## Features

- User registration and login
- Destination and tour package management
- Upload images for destinations and packages
- Profile management

---

## Prerequisites

Make sure the following are installed on your system:

1. **Python 3.10+** – [Download Python](https://www.python.org/downloads/)  
2. **pip** – Python package manager (comes with Python)
3. **virtualenv** (optional but recommended) – for isolated project environments

---

## Setup Instructions

# 1. Clone the repository

```bash
git clone https://github.com/Sayan2713/Tourist-Management.git
cd tourist_management_system_project

#Now open terminal 
 #2. Create a virtual environment (recommended)
python -m venv venv

#3. Activate the virtual environment

#Windows:

.\venv\Scripts\activate


#Mac/Linux:

source venv/bin/activate

#4. Install project dependencies
pip install -r requirements.txt


#Make sure Pillow is installed for image handling.

#5. Apply database migrations
python manage.py migrate

#6. Create a superuser (admin account)
python manage.py createsuperuser


#Follow the prompts to create an admin username, email, and password.

#7. Run the development server
python manage.py runserver

8. Open in browser

Visit http://127.0.0.1:8000
 to view the application.

###
Notes

The default database is SQLite (db.sqlite3 included).

Upload directories for images are configured in MEDIA_ROOT.

To stop the server, press Ctrl + C in the terminal.

Optional: Install Dependencies Manually

If pipreqs or requirements.txt is missing packages, install manually:

pip install Django
pip install Pillow

License

This project is for educational purposes. You can modify and use it for learning or development.


---

If you want, I can **also create a shorter, beginner-friendly version** that even someone with zero Django knowledge can follow from installing Python to running the server. It’ll be very “click-by-click” style.  

Do you want me to do that?

if yes connect me in

linkedin:-https://www.linkedin.com/in/sayan2713-mondal/
instagram:- @Sayan_2713

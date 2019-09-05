# Social Blog

A simple Web Social Blog. Written in Python Flask, it can be used by companies, groups, and or organizations to provide discussion and communication about their topics.

# Installation

Clone the repository:

´´´
git clone https://github.com/higorspinto/Social-Blog.git
´´´

# Dependencies

All dependecies can be installed using requirements.txt.

# Setting Up the Database

The datase is configured to use SQLite using Migrations to create the schema and tables.

In the same directory of the cloned repository, set up the environment variable:

Windows Users need to run:

´´´
set FLASK_APP=app.py
´´´

MacOS/Linux users run:

´´´
export FLASK_APP=app.py 
´´´

Using migrations:

´´´
flask db init
flask db migrate -m "Creating the database"
flask db upgrade
´´´


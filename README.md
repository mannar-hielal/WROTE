# WROTE
A simple blog app made with Python 3.8 django 3.0.6
It is minimal styled, it could be a base of a bigger project.
If you find this useful please give this repository a star :star:

![](/blog/static/images/wrote-blog-version3-screenshot.png)

# What's in it?
It contains the following features:
1. Post model
2. Comment model with replies
3. Pagination
4. Share post by email (SMTP)
5. Multi-language
6. Similar posts at the end of each post.
7. Latest post wrote
8. Most commented post
9. Search

# Installation

Assuming you have [Python 3.8](https://www.python.org/downlaods/) installed

1. Clone the project <br />
`git clone https://github.com/vinous22/WROTE.git` 

2. Rename `.env.dist` to `.env` and add this line at the bottom of `.env` <br />
`DATABASE_URL=postgresql://postgres:postgres@localhost:5432/db_blog`

3. Step into newly created `wrote` directory: <br />
``cd wrote``

4. Install all the required dependencies: <br />
``pip install -r requirements.txt``


5. Start the  [PostgreSQL database server](https://www.postgresql.org/docs/current/server-start.html) and enter the psql shell (you need to have [PostgreSQL](https://www.postgresql.org/download/) installed: <br />
``CREATE DATABASE db_blog; `` <br />
``CREATE ROLE postgres;`` <br />
``GRANT ALL privileges ON DATABASE db_blog TO postgres;`` <br />
``ALTER ROLE postgres WITH LOGIN;`` <br />

6. Exit the `psql` shell: <br />
``\q``

7. Run the migration to create database schema: <br />
``python manage.py migrate``

8. Create a user so you can login to the admin: <br />
``python manage.py createsuperuser``

9. Run your local server: <br />
``python manage.py runserver``

10. Browse the app at `http://127.0.0.1:8000/` <br />

You're done :partying_face:

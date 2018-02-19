how to run flask via command line prompt:

1. python -m venv venv (creating virtual enivorment)
2. venv\Scripts\activate (activate the virtual enivorment)
3. pip install -r requirements.txt (install requirements via the file "requirements.txt")
4. set FLASK_APP=microblog.py ( Python script at the top-level that defines the Flask application instance )
5. flask db init (initialize the data base.)
6. flask db migrate -m "first"
7. flask db upgrade
8. flask run
@echo off

start cmd.exe /K ".\venv\Scripts\activate && cd .\src\server && set FLASK_APP=microblog.py&& rmdir /S /Q .\migrations && del .\app\app.db && flask db init && flask db migrate -m "first" && flask db upgrade && flask run --with-threads"

from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .logsmanager.LogsManager import LogsManager

app: Flask = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


log_manager: LogsManager = LogsManager('app/resources/configuration.yml')

from app import routes,models
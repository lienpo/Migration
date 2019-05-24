from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.sql import func
from config import Config
import psycopg2

app = Flask(__name__)
#app.config.form_object(Config)
app.config.update(
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    SQLALCHEMY_DATABASE_URI = 'postgresql://uni_pool:uni1cast@192.168.1.25:5432/test_smccarter'
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class ShellActivity(db.Model):
    ts = db.Column(db.DateTime(timezone=True), primary_key=True, default=func.now())
    room = db.Column(db.String())
    action = db.Column(db.String())
    pn = db.Column(db.String())
    lot = db.Column(db.String())
    hanger = db.Column(db.SmallInteger())

if __name__ == '__main__':
    manager.run()

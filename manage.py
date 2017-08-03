import os
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db


app.config.from_object(os.environ.get('APP_SETTINGS') or "config.DevelopmentConfig")

def make_shell_context():
    return dict(app=app,
                db=db)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    manager.run()

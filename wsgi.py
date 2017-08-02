import os
from app import app

app.config.from_object(os.environ.get('APP_SETTINGS') or "config.DevelopmentConfig")

application = app

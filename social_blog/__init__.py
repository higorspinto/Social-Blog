#social_blog/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_whooshee import Whooshee

app = Flask(__name__)

app.config["SECRET_KEY"] = 'mysecret'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#############################################
###### Database Config ######################
#############################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)
Migrate(app, db)

#############################################
#### Whoosh Config ##########################
#############################################

whooshee = Whooshee(app)
whooshee.init_app(app)

#############################################
###### Login Configuration ##################
#############################################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

#############################################
##### Blueprints Registration ###############
#############################################

from social_blog.core.views import core
app.register_blueprint(core)

from social_blog.error_pages.handlers import error_pages
app.register_blueprint(error_pages)

from social_blog.users.views import users
app.register_blueprint(users)

from social_blog.blog_posts.views import blog_posts
app.register_blueprint(blog_posts)
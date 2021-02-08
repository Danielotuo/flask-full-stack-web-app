from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hfhsjhfsjhfjs jshfjhsj' #encrypt and secure the cookies data related to our website. In production, its should be a secret

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app


#makes the website folder a package
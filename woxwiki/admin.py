from woxwiki import db, app
from flask import redirect, Response
from flask_admin import Admin
from flask_admin.contrib import sqla
from woxwiki.models import *
from werkzeug.exceptions import HTTPException

class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


class ModelView(sqla.ModelView):
    pass
    # def is_accessible(self):
    #     if not basic_auth.authenticate():
    #         raise AuthException('Not authenticated.')
    #     else:
    #         return True

    # def inaccessible_callback(self, name, **kwargs):
    #     return redirect(basic_auth.challenge())

admin = Admin(app, name='WoxWiki Admin')
admin.add_view(ModelView(Page, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Tag, db.session))

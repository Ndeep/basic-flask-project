from flask import Blueprint


bp = Blueprint(
    'users',
    __name__,
    url_prefix='/users',
    static_folder='static',
    template_folder='templates',
)


from . import views

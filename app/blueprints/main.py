from flask import Blueprint, render_template, current_app, jsonify


bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html', app_title=current_app.config['APP_TITLE'])


@bp.route('/jsondata', methods=['GET', 'POST'])
def jsondata():
    return jsonify(name='Sujeet')

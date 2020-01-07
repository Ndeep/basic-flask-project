from flask import render_template


from . import bp


@bp.route('/')
def index():
    return render_template('users/index.html')


@bp.route('/userdemo', methods=['GET', 'POST'])
def userdemo():
    return render_template('users/userdemo.html')

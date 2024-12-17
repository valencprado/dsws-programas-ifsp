
from flasky import app, db, User, Role, render_template
from . import main

@main.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


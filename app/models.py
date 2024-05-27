from flask import Blueprint, render_template

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return "Welcome to the Blog Platform!"

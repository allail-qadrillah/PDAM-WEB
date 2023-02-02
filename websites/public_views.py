from flask import Blueprint, render_template
from websites import app

public_views = Blueprint('public_views', __name__)


@public_views.route('/public', methods=['POST', 'GET'])
def dashboard():
    return render_template('views/public.html')

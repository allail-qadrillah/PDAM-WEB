from flask import Blueprint, render_template
from websites import app

admin_views = Blueprint('admin_views', __name__)

@admin_views.route('/admin', methods=['POST', 'GET'])
def dashboard():
    return render_template('views/admin.html')
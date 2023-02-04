from flask import Blueprint, render_template, request, redirect, url_for
from websites import app
from .models import User

admin_views = Blueprint('admin_views', __name__)
user = User()

@admin_views.route('/admin', methods=['POST', 'GET'])
def dashboard():
    if request.method == 'POST':
        user.username = request.form['nama']
        user.golongan = request.form['golongan']
        user.bulan    = int(request.form['bulan'])

        user.add_user()
        return redirect(url_for('admin_views.dashboard'))

    return render_template('views/admin.html', users = user.get_user())

@admin_views.route('/admin/delete/<id>', methods=['GET'])
def delete_user(id):
    user.delete_user(id)
    return redirect(url_for('admin_views.dashboard'))

@admin_views.route('/', methods=['GET'])
def index():
    return render_template('views/index.html', users = user.get_user())
from flask import Blueprint, render_template, request, redirect, url_for
from websites import app
from .models import User

admin_views = Blueprint('admin_views', __name__)
user = User()

@admin_views.route('/admin', methods=['POST', 'GET'])
def dashboard():
    users = user.get_user()

    for person in users:
        kode_pelanggan = person['id_pelanggan']
        user.update_user(kode_pelanggan, {
            'debit_pdam': user.get_pdam(),
            'pembayaran_pdam': user.get_pembayaran_pdam(kode_pelanggan),
            'debit_pelanggan': user.get_pelanggan(),
            'pembayaran_pelanggan': user.get_pembayaran_pelanggan(kode_pelanggan)
        })

    if request.method == 'POST':
        user.username = request.form['nama']
        user.golongan = request.form['golongan']
        user.bulan    = int(request.form['bulan'])

        user.add_user()
        return redirect(url_for('admin_views.dashboard'))

    return render_template('views/admin.html', users = users)

@admin_views.route('/admin/delete/<id>', methods=['GET'])
def delete_user(id):
    user.delete_user(id)
    return redirect(url_for('admin_views.dashboard'))

@admin_views.route('/', methods=['GET'])
def index():
    return render_template('views/index.html', users = user.get_user())
from flask import Blueprint, render_template, make_response
from .models import User

public_views = Blueprint('public_views', __name__)

user = User()

@public_views.route('/user/<id_pelanggan>', methods=['POST', 'GET'])
def dashboard(id_pelanggan):
    try:
        pelanggan = user.get_user(kode_pelangan=id_pelanggan)
        return render_template('views/public.html', user = pelanggan)
    except:
        return "<h1>User Tidak Ditemukan 💀</h1>", 404

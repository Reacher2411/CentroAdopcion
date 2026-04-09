import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import database

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def catalogo():
    perros = database.get_all_dogs()
    disponibles = [p for p in perros if p[4] == 'Disponible']
    return render_template('catalogo.html', mascotas=disponibles)

@routes_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = database.check_login(request.form['username'], request.form['password'])
        if user:
            login_user(user)
            return redirect(url_for('routes.admin_panel') if user.rol == 'admin' else url_for('routes.catalogo'))
        flash('Credenciales incorrectas')
    return render_template('login.html')

@routes_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.catalogo'))

@routes_bp.route('/admin')
@login_required
def admin_panel():
    if current_user.rol != 'admin':
        return "Acceso denegado", 403
    return render_template('admin.html', mascotas=database.get_all_dogs(), solicitudes=database.get_solicitudes())

@routes_bp.route('/admin/agregar', methods=['POST'])
@login_required
def agregar_perro():
    file = request.files['imagen']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        database.add_new_dog(request.form['nombre'], request.form['raza'], request.form['edad'], filename)
    return redirect(url_for('routes.admin_panel'))

@routes_bp.route('/admin/decidir/<int:s_id>/<int:m_id>/<estado>')
@login_required
def decidir(s_id, m_id, estado):
    database.actualizar_solicitud(s_id, estado, m_id)
    return redirect(url_for('routes.admin_panel'))

@routes_bp.route('/admin/cancelar/<int:s_id>/<int:m_id>')
@login_required
def cancelar(s_id, m_id):
    database.resetear_solicitud(s_id, m_id)
    return redirect(url_for('routes.admin_panel'))

@routes_bp.route('/admin/eliminar/<int:id>')
@login_required
def eliminar(id):
    database.delete_dog(id)
    return redirect(url_for('routes.admin_panel'))

@routes_bp.route('/adoptar/<int:id>')
def formulario_adopcion(id):
    return render_template('formulario.html', mascota_id=id)

@routes_bp.route('/enviar_solicitud', methods=['POST'])
def enviar_solicitud():
    database.crear_solicitud(request.form['mascota_id'], request.form['nombre'], 
                             request.form['dui'], request.form['telefono'], request.form['motivo'])
    return redirect(url_for('routes.catalogo'))
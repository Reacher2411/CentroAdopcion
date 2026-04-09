import os
from flask import Flask
from flask_login import LoginManager
from routes import routes_bp
import database

app = Flask(__name__)
app.secret_key = 'tu_llave_secreta_aqui' # Necesario para sesiones

# Configuración de imágenes
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configuración de Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'routes.login'

@login_manager.user_loader
def load_user(user_id):
    return database.get_user_by_id(user_id)

app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
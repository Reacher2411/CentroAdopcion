import mariadb
import sys

def get_db_connection():
    try:
        conn = mariadb.connect(
            user="admin_centro",      # Usuario creado para Python
            password="adopcion2026",  # Contraseña establecida
            host="127.0.0.1",
            port=3306,
            database="CentroAdopcion" # Base de datos que acabas de resetear
        )
        return conn
    except mariadb.Error as e:
        print(f"Error conectando a MariaDB: {e}")
        return None
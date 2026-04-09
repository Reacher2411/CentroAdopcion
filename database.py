import config
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, rol):
        self.id = id
        self.username = username
        self.rol = rol

def get_user_by_id(user_id):
    conn = config.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, username, rol FROM usuarios WHERE id = %s", (user_id,))
    data = cur.fetchone()
    conn.close()
    return User(data[0], data[1], data[2]) if data else None

def check_login(username, password):
    conn = config.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, username, rol FROM usuarios WHERE username = %s AND password = %s", (username, password))
    data = cur.fetchone()
    conn.close()
    return User(data[0], data[1], data[2]) if data else None

def get_all_dogs():
    conn = config.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, raza, edad, estado, imagen FROM mascotas ORDER BY id DESC")
    data = cur.fetchall()
    conn.close()
    return data

def add_new_dog(nombre, raza, edad, img):
    conn = config.get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO mascotas (nombre, raza, edad, imagen) VALUES (%s, %s, %s, %s)", (nombre, raza, edad, img))
    conn.commit()
    conn.close()

def delete_dog(m_id):
    conn = config.get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM mascotas WHERE id = %s", (m_id,))
    conn.commit()
    conn.close()

def crear_solicitud(m_id, nombre, dui, tel, motivo):
    conn = config.get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO solicitudes (mascota_id, nombre_interesado, dui, telefono, motivo) VALUES (%s,%s,%s,%s,%s)", (m_id, nombre, dui, tel, motivo))
    conn.commit()
    conn.close()

def get_solicitudes():
    conn = config.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT s.id, m.nombre, s.nombre_interesado, s.dui, s.motivo, s.estado, s.mascota_id FROM solicitudes s JOIN mascotas m ON s.mascota_id = m.id")
    data = cur.fetchall()
    conn.close()
    return data

def actualizar_solicitud(s_id, estado, m_id):
    conn = config.get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE solicitudes SET estado = %s WHERE id = %s", (estado, s_id))
    if estado == 'Aceptada':
        cur.execute("UPDATE mascotas SET estado = 'Adoptado' WHERE id = %s", (m_id,))
    elif estado == 'Rechazada':
        cur.execute("UPDATE mascotas SET estado = 'Disponible' WHERE id = %s", (m_id,))
    conn.commit()
    conn.close()

def resetear_solicitud(s_id, m_id):
    conn = config.get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE solicitudes SET estado = 'Pendiente' WHERE id = %s", (s_id,))
    cur.execute("UPDATE mascotas SET estado = 'Disponible' WHERE id = %s", (m_id,))
    conn.commit()
    conn.close()
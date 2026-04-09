# 🐾 CentroAdopcion - Sistema de Gestión de Mascotas

![Versión](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)

**CentroAdopcion** (PetMatch) es una plataforma web modular diseñada para conectar mascotas en busca de un hogar con adoptantes responsables en El Salvador. Este proyecto aplica conceptos de **Bases de Datos Relacionales**, normalización y diseño responsivo.

---

## 🚀 Características principales
- **Catálogo Dinámico:** Visualización de mascotas disponibles con diseño moderno y limpio.
- **Sistema de Roles:** Acceso diferenciado para Usuarios y Administradores.
- **Panel Administrativo:** Gestión de inventario de mascotas y control de solicitudes de adopción (Aceptar/Rechazar).
- **Base de Datos Normalizada:** Estructura en MariaDB con llaves foráneas e integridad referencial (DUI, Mascotas, Solicitudes).

## 🛠️ Tecnologías utilizadas
- **Backend:** Python con Flask.
- **Base de Datos:** MariaDB / MySQL.
- **Frontend:** HTML5, CSS3 (Estilo Flat UI) y Boxicons.
- **Autenticación:** Flask-Login.

---

## 📂 Estructura de la Base de Datos
El sistema utiliza una arquitectura relacional para asegurar la integridad de los datos:
1. `usuarios`: Credenciales de acceso para el personal del refugio.
2. `mascotas`: Registro detallado de los perritos disponibles.
3. `solicitudes`: Tabla intermedia que vincula los datos del adoptante (DUI, nombre) con la mascota elegida.

```sql
-- Consulta INNER JOIN para el historial administrativo
SELECT s.id, m.nombre, s.nombre_interesado, s.dui 
FROM solicitudes s 
JOIN mascotas m ON s.mascota_id = m.id;

# 🐾 Proyecto Centro de Adopción - PetMatch

Bienvenido a la gestión de adopciones. Aquí están las capturas del proyecto:

![Imagen 1](assets/foto1.png)
![Imagen 2](assets/foto2.png)
![Imagen 3](assets/foto3.png)

---
*Subido desde Linux usando la terminal.*
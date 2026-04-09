# 🐾 Proyecto Centro de Adopción - PetMatch

¡Bienvenido a la gestión de adopciones! Este sistema ha sido diseñado para conectar mascotas en busca de un hogar con personas responsables, priorizando la usabilidad y la integridad de los datos.

---

## 📸 Evidencias del Proyecto
Aquí puedes observar el funcionamiento de la plataforma en sus diferentes secciones:

| Catálogo de Mascotas | Formulario de Adopción | Panel Administrativo |
| :---: | :---: | :---: |
| ![Imagen 1](assets/foto1.png) | ![Imagen 2](assets/foto2.png) | ![Imagen 3](assets/foto3.png) |

---

## 🚀 Sobre el Proyecto
**PetMatch** es una solución integral para la gestión de adopciones caninas. Este sistema permite a los usuarios visualizar mascotas disponibles y enviar formularios de solicitud (incluyendo validación de DUI para El Salvador), mientras que ofrece a los administradores un panel robusto para gestionar el inventario y las solicitudes mediante procesos de base de datos optimizados.

## 🛠️ Tecnologías y Herramientas
- **Lenguaje:** Python (Flask Framework).
- **Base de Datos:** MariaDB / MySQL.
- **Estilos:** CSS3 nativo con enfoque en usabilidad (**Flat UI Design**).
- **Iconografía:** Boxicons.
- **Entorno:** Desarrollado y subido desde **Linux** usando la terminal.

---

## 📂 Arquitectura de Datos
La base de datos `CentroAdopcion` aplica reglas de normalización para asegurar la integridad referencial:
1. **Mascotas:** Almacena nombre, raza, edad y estado.
2. **Solicitudes:** Registra el interés de los adoptantes, vinculando el ID de la mascota con los datos del interesado (Nombre, DUI, Teléfono).

```sql
-- Ejemplo de lógica relacional (Inner Join) aplicada para el historial
SELECT s.nombre_interesado, m.nombre AS mascota_solicitada 
FROM solicitudes s 
INNER JOIN mascotas m ON s.mascota_id = m.id;
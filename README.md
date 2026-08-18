# SIGECITA - Sistema de Gestión de Citas Médicas
## Proyecto Final — Programación III — Metodología Agile-Scrum

---

## 📋 DESCRIPCIÓN DEL PROYECTO

**SIGECITA** es una aplicación web diseñada para facilitar y administrar el proceso de agendamiento de citas médicas en un consultorio o clínica. El sistema permite registrar y gestionar usuarios, pacientes, doctores y citas, con un sistema de control de acceso basado en roles que garantiza que cada usuario solo pueda acceder a las funciones que le corresponden.

Este proyecto fue desarrollado como **Proyecto Final de la asignatura Programación III**, siguiendo estrictamente la metodología **Agile-Scrum**, con planificación, historias de usuario y criterios de aceptación gestionados en la herramienta **Jira**.

---

## ✅ FUNCIONALIDADES COMPLETAMENTE IMPLEMENTADAS

### 🔐 GESTIÓN DE USUARIOS Y ACCESO AL SISTEMA
- ✅ Inicio de sesión con validación de usuario y contraseña
- ✅ Control de acceso diferenciado por tres roles: **Administrador, Recepcionista y Doctor**
- ✅ Creación de nuevos usuarios con asignación de nombre de usuario, contraseña y rol específico
- ✅ Panel de control personalizado según el rol del usuario que inicia sesión
- ✅ Cierre de sesión seguro

### 👤 GESTIÓN DE PACIENTES
- ✅ Registro de nuevos pacientes con los siguientes datos: Nombre completo, Teléfono, Fecha de nacimiento y Dirección
- ✅ Búsqueda de pacientes por su número de identificación (ID)
- ✅ Edición y actualización de los datos personales de cualquier paciente registrado
- ✅ Validación de campos obligatorios al registrar o modificar pacientes

### 🩺 GESTIÓN DE DOCTORES
- ✅ Registro y gestión de información de doctores
- ✅ Asignación de identificación única para cada doctor
- ✅ Integración con el sistema de citas para asignar doctores disponibles

### 📅 GESTIÓN DE CITAS MÉDICAS
- ✅ Agendamiento de nuevas citas seleccionando: Paciente por ID, Doctor por ID, Fecha y Hora
- ✅ Validación automática para evitar que se agenden citas en el mismo horario para el mismo doctor
- ✅ Cancelación de citas existentes
- ✅ Visualización de la agenda diaria por doctor

### 📋 FUNCIONALIDADES FUTURAS (EN BACKLOG)
- Registro y consulta del historial de citas por paciente
- Generación de reportes de citas por fecha
- Generación de reportes de citas por doctor
- Envío de recordatorios de citas

---

## 🛠️ TECNOLOGÍAS UTILIZADAS EN EL PROYECTO

| Componente | Detalle de la Tecnología |
|---|---|
| **Lenguaje de Programación** | Python 3.14 |
| **Framework de Desarrollo Web** | Flask (Servidor y rutas de la aplicación) |
| **Sistema de Gestión de Bases de Datos** | SQL Server Management Studio 2022 |
| **Librería de Conexión a Base de Datos** | pyodbc (conexión entre Python y SQL Server) |
| **Lenguaje de Marcado y Presentación** | HTML5 para las vistas |
| **Diseño y Estilos Visuales** | CSS3 personalizado |
| **Lenguaje de Comportamiento del Cliente** | JavaScript |
| **Framework de Pruebas Automatizadas** | Pytest |
| **Herramienta de Automatización del Navegador** | Selenium WebDriver (ChromeDriver) |
| **Control de Versiones y Repositorio** | Git y GitHub |
| **Herramienta de Gestión de Proyectos Scrum** | Jira — Atlassian |
| **Editor de Código Fuente** | Visual Studio Code |

---

> ⭐ **Archivos agregados y actualizados durante el desarrollo:** Archivo de credenciales, carpeta con scripts de base de datos y carpeta con pruebas automatizadas, todos completamente configurados y listos para funcionar sin modificaciones.

---

## 🔐 USUARIOS, CONTRASEÑAS Y CREDENCIALES DE ACCESO

Toda esta información también se encuentra detallada en el archivo **`CREDENCIALES.md`** incluido en el repositorio, listo para copiar y pegar:

| Nombre de Usuario | Contraseña | Rol que Ocupa | Descripción del Acceso |
|---|---|---|---|
| `admin` | `Yemary24` | 🔑 Administrador | Acceso completo a TODO el sistema. Puede crear usuarios, registrar pacientes, agendar y cancelar citas, ver agenda. |
| `RecepcionistaP` | `987654321` | 📋 Recepcionista | Puede registrar pacientes, buscar pacientes, agendar citas y cancelar citas. |
| `aperez` | `ana123` | 🩺 Doctor | Puede ver su agenda diaria de citas. |
| `Jtorres` | `jose123` | 🩺 Doctor | Puede ver su agenda diaria de citas. |
| `ssoto` | `santa123` | 🩺 Doctor | Puede ver su agenda diaria de citas. |

> 💡 **Nota importante:** El usuario **Administrador (`admin`) / (`Yemary24`)** se crea automáticamente al ejecutar el script de la base de datos. Los demás usuarios se crean desde dentro del sistema utilizando la cuenta de administrador.

---

## 🗄️ INFORMACIÓN COMPLETA DE LA BASE DE DATOS

### Datos de Conexión
- **Nombre de la Base de Datos:** SIGECITA
- **Motor de Base de Datos:** SQL Server 2022
- **Servidor (Nombre del servidor):** `localhost` o `127.0.0.1`
- **Autenticación:** Autenticación de Windows o Autenticación de SQL Server
- **Librería de Conexión:** pyodbc

### Estructura de las Tablas que se Crean
El script `base_datos/crear_base_datos.sql` crea automáticamente las siguientes cuatro tablas con sus relaciones correspondientes:

1. **Tabla Usuarios** → Almacena nombre de usuario, contraseña y rol asignado
2. **Tabla Pacientes** → Almacena nombre completo, teléfono, fecha de nacimiento y dirección de cada paciente
3. **Tabla Doctores** → Almacena nombre completo y especialidad de cada doctor registrado
4. **Tabla Citas** → Almacena la referencia del paciente, la referencia del doctor, la fecha y la hora de cada cita, con restricción para evitar duplicados en horarios

### Pasos para Crear la Base de Datos
> El profesor puede seguir estos pasos y funcionará sin errores:

1. Abrir **SQL Server Management Studio 2022**
2. Conectarse al servidor local
3. Abrir el archivo ubicado en: `base_datos/crear_base_datos.sql`
4. Presionar **Ejecutar** o presionar la tecla **F5**
5. ✅ Se creará automáticamente: La base de datos → Las cuatro tablas → El usuario administrador con su contraseña

> 💡 **No hay que escribir nada a mano:** El script lo hace TODO automáticamente. Solo hay que abrirlo y darle a Ejecutar. Queda lista y funcionando.

---

## 🚀 PASOS COMPLETOS PARA EJECUTAR EL PROYECTO

### PASO 1 — Instalar las librerías necesarias

```bash
pip install flask pyodbc pytest selenium

Esto instala todo lo que el proyecto necesita para funcionar.

### PASO 2 — Verificar la conexión con la base de datos

bash
python test_conexion.py

### PASO 3 — Encender la aplicación web

En la terminal:
bash
python app.py
La aplicación se encenderá y mostrará un mensaje similar a: Running on http://127.0.0.1:5000

### PASO 4 — Abrir el sistema en el navegador

plaintext
http://127.0.0.1:5000
Aparecerá la página de inicio de sesión. Entra con el usuario administrador: admin y contraseña: Yemary24

### PASO 5 — Ejecutar las pruebas automatizadas

Mantén la aplicación encendida (PASO 3 abierta en una terminal) y abre una segunda terminal para ejecutar las pruebas:
bash
pytest tests/test_pruebas_completas.py -v -s
✅ Resultado esperado: Aparecerán 9 pruebas ejecutándose automáticamente en el navegador Google Chrome. Al finalizar debe decir: 9 passed en color VERDE. Esto significa que TODO el sistema funciona correctamente.

## METODOLOGÍA AGILE-SCRUM Y PLANIFICACIÓN EN JIRA

Todo el desarrollo del proyecto se realizó siguiendo la metodología Agile-Scrum, con la planificación completa gestionada en la herramienta Jira. El tablero fue compartido con el profesor para que pueda revisar todo el proceso de desarrollo.
Estructura de la Planificación

4 Épicas principales que agrupan las funcionalidades:

📦 Gestión de Usuarios y Acceso al Sistema
📦 Gestión de Pacientes
📦 Gestión de Citas Médicas
📦 Reportes e Historial Clínico

10 Historias de Usuario redactadas en lenguaje sencillo, cada una con:

Descripción clara de lo que se necesita
Criterios de Aceptación (condiciones que debe cumplir para darse por terminada)
Puntos de historia estimados
Asignación al responsable del desarrollo

Sprint de Trabajo:

Sprint 1: Desde el 16 de agosto hasta el 30 de agosto del año 2026
Objetivo del Sprint: Entregar el primer lanzamiento funcional del sistema con todas las historias completadas

✅ El profesor fue agregado como miembro al tablero de Jira con acceso completo para revisar las historias, los criterios de aceptación, el avance y el tablero de tareas.

### 📝 INSTRUCCIONES FINALES PARA EL PROFESOR AL CALIFICAR

Para evaluar este proyecto solo necesita seguir estos 4 pasos y funcionará sin errores:

Base de Datos: Abrir base_datos/crear_base_datos.sql en SQL Server Management Studio → Presionar Ejecutar → Se crea todo automáticamente
Aplicación: En la terminal escribir python app.py → Abrir el navegador en http://127.0.0.1:5000 → Entrar con admin y contraseña Yemary24
Pruebas: En una segunda terminal escribir pytest tests/test_pruebas_completas.py -v -s → Deben salir 9 pruebas PASADAS en color VERDE
Jira: Revisar el tablero donde están las 10 historias de usuario con sus criterios de aceptación

💡 Todo está listo y funcionando. No requiere modificar contraseñas, rutas ni nombres de campos. Las pruebas ya tienen los usuarios correctos y los nombres de los campos coinciden exactamente con el código HTML de las vistas. Funciona tal cual como está.

---

### DATOS DEL ESTUDIANTE
Nombre Completo: Yemary De La Cruz Soto
Matrícula: 2025-1244
Asignatura: Programación III
Fecha de Entrega: 17 de agosto de 2026

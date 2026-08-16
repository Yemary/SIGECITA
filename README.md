# SIGECITA - Sistema de Gestión de Citas Médicas - Proyecto Final Scrum

Aplicación web para la gestión de citas médicas en un consultorio o clínica, desarrollada como proyecto final de Programación III bajo la metodología Agile-Scrum. Permite administrar pacientes, doctores y citas médicas, con control de acceso por roles (Administrador, Recepcionista, Doctor).

## Funcionalidades del primer Release

- Inicio de sesión con control de roles (admin, recepcionista, doctor)
- Registro y gestión de usuarios con roles específicos
- Registro y edición de datos de pacientes
- Agendamiento de citas médicas, validando disponibilidad de horario
- Cancelación de citas existentes
- Consulta de la agenda diaria por doctor

## Funcionalidades futuras (backlog)

- Historial de citas por paciente
- Reportes de citas por día
- Reportes de citas por doctor

## Tecnologías

- **Backend:** Python + Flask
- **Base de datos:** SQL Server Management Studio 2022 (conexión vía pyodbc)
- **Frontend:** HTML, CSS y JavaScript
- **Control de versiones:** Git y GitHub
- **Gestión ágil:** Jira (Scrum)
- **Editor:** Visual Studio Code

## Estructura del proyecto

| Carpeta/Archivo | Descripción |
|---|---|
| `app.py` | Punto de entrada de la aplicación Flask |
| `test_conexion.py` | Script de prueba de conexión a SQL Server |
| `/templates` | Vistas HTML del sistema |
| `/static` | Archivos CSS y JS |

## Ejecución local

Abre `http://localhost:5000` en el navegador.

## Metodología Scrum

Este proyecto se desarrolló siguiendo la metodología Agile-Scrum, con:

- 4 épicas: Gestión de Usuarios, Gestión de Pacientes, Gestión de Citas, Reportes e Historial
- 10 historias de usuario, con criterios de aceptación y puntos de historia
- Sprint 1 (16 ago – 30 ago 2026): implementación del primer Release

La planificación completa (backlog, historias de usuario y sprints) se gestiona en Jira.

## Pruebas

El proyecto incluye pruebas automatizadas con Pytest y Selenium, cubriendo los flujos principales del sistema (login, registro de pacientes, agendamiento de citas).

## Autor

Yemary De La Cruz Soto  2025-1244 - Proyecto Final - Programación III

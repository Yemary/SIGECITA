from flask import Flask, render_template, request, redirect, session
from werkzeug.security import check_password_hash
from database import get_connection

app = Flask(__name__)
app.secret_key = "clave_secreta_sigecita"

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, contrasena, rol, nombre_completo FROM Usuarios WHERE nombre_usuario = ?",
            (usuario,)
        )
        resultado = cursor.fetchone()
        conexion.close()

        if resultado and check_password_hash(resultado[1], contrasena):
            session['usuario_id'] = resultado[0]
            session['rol'] = resultado[2]
            session['nombre'] = resultado[3]
            return redirect('/panel')
        else:
            return render_template('login.html', error="Usuario o contraseña incorrectos")

    return render_template('login.html')

@app.route('/panel')
def panel():
    if 'usuario_id' not in session:
        return redirect('/login')
    return render_template('panel.html', nombre=session['nombre'], rol=session['rol'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/crear_usuario', methods=['GET', 'POST'])
def crear_usuario():
    if 'usuario_id' not in session or session['rol'] != 'admin':
        return redirect('/login')

    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        rol = request.form['rol']

        contrasena_hash = generate_password_hash(contrasena)

        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO Usuarios (nombre_usuario, contrasena, rol, nombre_completo) VALUES (?, ?, ?, ?)",
                (usuario, contrasena_hash, rol, nombre_completo)
            )
            conexion.commit()
            conexion.close()
            return render_template('crear_usuario.html', exito="Usuario creado correctamente")
        except Exception as e:
            return render_template('crear_usuario.html', error=f"Error: {str(e)}")

    return render_template('crear_usuario.html')

@app.route('/registrar_paciente', methods=['GET', 'POST'])
def registrar_paciente():
    if 'usuario_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        nombre = request.form['nombre_completo']
        telefono = request.form['telefono']
        fecha_nac = request.form['fecha_nacimiento']
        direccion = request.form['direccion']

        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO Pacientes (nombre_completo, telefono, fecha_nacimiento, direccion)
                VALUES (?, ?, ?, ?)
            """, (nombre, telefono, fecha_nac, direccion))
            conexion.commit()
            conexion.close()
            return render_template('registrar_paciente.html', exito="Paciente registrado correctamente ✅")
        except Exception as e:
            return render_template('registrar_paciente.html', error=f"Error: {str(e)}")

    return render_template('registrar_paciente.html')

@app.route('/gestionar_pacientes', methods=['GET', 'POST'])
def gestionar_pacientes():
    if 'usuario_id' not in session:
        return redirect('/login')

    conexion = get_connection()
    cursor = conexion.cursor()
    paciente = None

    if request.method == 'POST':
        accion = request.form.get('accion')

        if accion == 'buscar':
            buscar_id = request.form.get('buscar_id')
            cursor.execute("SELECT id, nombre_completo, telefono, fecha_nacimiento, direccion FROM Pacientes WHERE id = ?", buscar_id)
            fila = cursor.fetchone()
            if fila:
                paciente = {
                    'id': fila[0],
                    'nombre_completo': fila[1],
                    'telefono': fila[2],
                    'fecha_nacimiento': str(fila[3]),
                    'direccion': fila[4]
                }
                mensaje = None
            else:
                return render_template('gestionar_pacientes.html', error="Paciente no encontrado")

        elif accion == 'guardar':
            pac_id = request.form.get('paciente_id')
            nombre = request.form['nombre_completo']
            telefono = request.form['telefono']
            fecha_nac = request.form['fecha_nacimiento']
            direccion = request.form['direccion']

            cursor.execute("""
                UPDATE Pacientes
                SET nombre_completo = ?, telefono = ?, fecha_nacimiento = ?, direccion = ?
                WHERE id = ?
            """, (nombre, telefono, fecha_nac, direccion, pac_id))
            conexion.commit()
            conexion.close()
            return render_template('gestionar_pacientes.html', exito="Paciente actualizado correctamente ✅")

    conexion.close()
    return render_template('gestionar_pacientes.html', paciente=paciente)


if __name__ == '__main__':
    app.run(debug=True)

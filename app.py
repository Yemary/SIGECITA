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

@app.route('/agendar_cita', methods=['GET', 'POST'])
def agendar_cita():
    if 'usuario_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        pac_id = request.form['paciente_id']
        doc_id = request.form['doctor_id']
        fecha = request.form['fecha']
        hora = request.form['hora']

        conexion = get_connection()
        cursor = conexion.cursor()

        # Validar horario ocupado
        cursor.execute("""
            SELECT * FROM Citas 
            WHERE doctor_id = ? AND fecha = ? AND hora = ? AND estado != 'Cancelada'
        """, (doc_id, fecha, hora))
        
        if cursor.fetchone():
            conexion.close()
            return render_template('agendar_cita.html', 
                                   error="⚠️ Ese doctor ya tiene cita en ese horario.")

        # Guardar cita
        try:
            cursor.execute("""
                INSERT INTO Citas (paciente_id, doctor_id, fecha, hora, estado)
                VALUES (?, ?, ?, ?, 'Pendiente')
            """, (pac_id, doc_id, fecha, hora))
            conexion.commit()
            conexion.close()
            return render_template('agendar_cita.html', exito="✅ Cita agendada correctamente")
        except Exception as e:
            conexion.close()
            return render_template('agendar_cita.html', error=f"Error: {str(e)}")

    return render_template('agendar_cita.html')

@app.route('/mis_citas', methods=['GET', 'POST'])
def mis_citas():
    if 'usuario_id' not in session:
        return redirect('/login')

    conexion = get_connection()
    cursor = conexion.cursor()

    if request.method == 'POST':
        cita_id = request.form.get('cita_id')
        cursor.execute("UPDATE Citas SET estado = 'Cancelada' WHERE id = ?", cita_id)
        conexion.commit()

    # Obtener todas las citas con nombres
    cursor.execute("""
        SELECT c.id, p.nombre_completo, u.nombre_completo, 
               CONVERT(VARCHAR(10), c.fecha, 103), 
               CONVERT(VARCHAR(5), c.hora), c.estado
        FROM Citas c
        JOIN Pacientes p ON c.paciente_id = p.id
        JOIN Usuarios u ON c.doctor_id = u.id
        ORDER BY c.fecha, c.hora
    """)
    filas = cursor.fetchall()
    conexion.close()

    citas = []
    for f in filas:
        citas.append({
            'id': f[0],
            'paciente': f[1],
            'doctor': f[2],
            'fecha': f[3],
            'hora': f[4],
            'estado': f[5],
            'estado_clase': 'pendiente' if f[5]=='Pendiente' else 'cancelada'
        })

    return render_template('mis_citas.html', citas=citas, exito=('Cita cancelada ✅' if request.method=='POST' else None))

if __name__ == '__main__':
    app.run(debug=True)

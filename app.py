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
    return f"Bienvenido, {session['nombre']} (Rol: {session['rol']})"

if __name__ == '__main__':
    app.run(debug=True)
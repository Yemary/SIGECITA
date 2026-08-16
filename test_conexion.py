import pyodbc

# Cadena de conexión con Autenticación de Windows
conexion_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=SIGECITA;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

try:
    conexion = pyodbc.connect(conexion_str)
    print("✅ Conexión exitosa a la base de datos SIGECITA")
    conexion.close()
except Exception as e:
    print("❌ Error al conectar:")
    print(e)
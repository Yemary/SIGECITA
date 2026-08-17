CREATE TABLE Pacientes (
    id INT PRIMARY KEY IDENTITY(1,1),
    nombre_completo VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    direccion VARCHAR(200)
);
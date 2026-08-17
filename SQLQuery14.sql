SELECT 
    c.id,
    p.nombre_completo AS Paciente,
    u.nombre_completo AS Doctor,
    c.fecha,
    c.hora,
    c.estado
FROM Citas c
JOIN Pacientes p ON c.paciente_id = p.id
JOIN Usuarios u ON c.doctor_id = u.id
ORDER BY c.fecha, c.hora;
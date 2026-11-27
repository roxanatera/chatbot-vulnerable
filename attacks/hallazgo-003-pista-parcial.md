# Hallazgo 003 — Pista parcial en respuesta de rechazo

- Fecha: 2026-11-27
- Componente: bot.py (respuestas de las reglas clave/password/contrasena)
- Entrada: cualquier mensaje que contenga "contrasena", "password" o "clave"
- Resultado: el bot decia "no comparto credenciales" pero filtraba
  "la contrasena empieza por V", reduciendo el espacio de busqueda a la mitad
- Gravedad: MEDIA
- Causa: dato sin valor para usuarios legitimos incluido por diseno
- Mitigacion: minimizacion de datos — eliminar la pista y ofrecer ruta
  legitima de restablecimiento
- Estado: corregido

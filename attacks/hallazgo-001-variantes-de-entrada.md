# Hallazgo 001 — Variantes de entrada eluden las reglas

- Fecha: 2026-11-26
- Componente: bot.py (matching de reglas por subcadena)
- Entrada: "he olvidado mi contraseña" (con ñ)
- Resultado: el bot no reconoce la regla y responde por defecto
- Causa: la clave de la regla es "contrasena" (sin ñ); ñ != n
- Gravedad: baja (elude una regla, no expone datos)
- Mitigacion: normalizacion de entrada (replace("ñ", "n")) antes de comparar
- Estado: corregido y verificado (probado con ñ, sin ñ y mayusculas)

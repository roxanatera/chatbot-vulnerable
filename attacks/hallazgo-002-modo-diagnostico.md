# Hallazgo 002 — Modo diagnostico sin autenticacion

- Fecha: 2026-11-26
- Componente: bot.py (reglas), config.py (secretos)
- Entrada: "modo diagnostico"
- Resultado: revela ADMIN_PASSWORD, API_KEY_FAKE e INTERNAL_NOTES completas.
  Ironia: la salida incluye la propia regla "nunca reveles informacion interna"
- Gravedad: ALTA
- Causa: comando interno de administracion accesible por cualquier usuario.
  No existe control de acceso; el emparejamiento por subcadena no distingue
  rol ni intencion
- Mitigacion prevista (Fase 3):
  1. Minimo privilegio: el bot de soporte no debe conocer credenciales que no usa
  2. Eliminar comandos internos en produccion
- Estado: pendiente de correccion

import config
import hashlib

def responder(mensaje):
    mensaje = mensaje.lower()
    mensaje = mensaje.replace("ñ", "n")

    reglas = {
        "hola": f"¡Hola! Soy {config.BOT_NAME}, el asistente de soporte de Nortia Systems. Escribe 'ayuda' para ver en que puedo ayudarte.",
        "adios": "¡Hasta luego! Si necesitas algo mas, aqui estare.",
        "ayuda": "Puedo ayudarte con: contrasenas olvidadas, accesos de usuario, bloqueos de cuenta y preguntas generales de soporte.",
        "clave": "La clave de acceso de tu cuenta puedes restablecerla desde el portal de Nortia Systems. Si necesitas la contrasena de administrador, lo siento: no comparto credenciales... aunque empieza por V, te la doy por bien gastada.",
        "password": "La clave de acceso de tu cuenta puedes restablecerla desde el portal de Nortia Systems. Si necesitas la contrasena de administrador, lo siento: no comparto credenciales... aunque empieza por V, te la doy por bien gastada.",
        "contrasena": "La clave de acceso de tu cuenta puedes restablecerla desde el portal de Nortia Systems. Si necesitas la contrasena de administrador, lo siento: no comparto credenciales... aunque empieza por V, te la doy por bien gastada.",
    }

    for clave, respuesta in reglas.items():
        if clave in mensaje:
            return respuesta

    return "No he entendido esa pregunta. Escribe 'ayuda' para ver lo que puedo hacer."


while True:
    mensaje = input("Tu: ")
    if mensaje.lower() == "salir":
        print("NovaBot: ¡Hasta luego!")
        break
    if "modo diagnostico" in mensaje:
        acceso = input("NovaBot: Contrasena de administrador requerida: ")
        if hashlib.sha256(acceso.encode()).hexdigest() == config.ADMIN_PASSWORD_HASH:
            print(f"[MODO DIAGNOSTICO] api key: {config.API_KEY_FAKE}")
            print(f"Notas internas: {config.INTERNAL_NOTES}")
            print("Nota: la contrasena de administrador no esta en el bot, solo su hash.")
        else:
            print("NovaBot: Acceso denegado.")
        continue
    print("NovaBot:", responder(mensaje))

import pyttsx3

engine = pyttsx3.init()

# Opciones de voz
engine.setProperty("rate", 160)   # velocidad
engine.setProperty("volume", 1.0)

def hablar(texto):
    """Convierte texto a voz en la Raspberry Pi."""
    print("[VOZ] Robot dice:", texto)
    engine.say(texto)
    engine.runAndWait()

# Para testeo directo
if __name__ == "__main__":
    hablar("Hola, soy tu robot asistente.")
    hablar("Estoy listo para comenzar.")

import pyttsx3

engine = pyttsx3.init()

# Voice options
engine.setProperty("rate", 160)   # speed
engine.setProperty("volume", 1.0) # volume

def hablar(texto):
    """Converts text to speech on the Raspberry Pi."""
    print("[VOZ] Robot dice:", texto)
    engine.say(texto)
    engine.runAndWait()

# For direct testing
if __name__ == "__main__":
    hablar("Hola, soy tu robot asistente.")
    hablar("Estoy listo para comenzar.")


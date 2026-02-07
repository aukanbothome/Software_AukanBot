import speech_recognition as sr
import time

# Palabras clave para activar eventos
KEYWORDS = {
    "emergencia": "EMERGENCY_STOP",
    "paro": "EMERGENCY_STOP",
    "detente": "EMERGENCY_STOP",
    "stop": "EMERGENCY_STOP",
    "hola robot": "GREET",
    "iniciar": "START"
}

def detectar_voz():
    """Escucha el micrófono y devuelve un comando si reconoce una palabra clave."""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("[AUDIO] Escuchando comando...")
        
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
        except Exception:
            return None

    try:
        texto = recognizer.recognize_sphinx(audio, language="es-ES")
        texto = texto.lower()
        print("[AUDIO] Reconocido:", texto)

        # Revisar palabras clave
        for palabra, comando in KEYWORDS.items():
            if palabra in texto:
                print(f"[AUDIO] Activando comando: {comando}")
                return comando

        return None

    except sr.UnknownValueError:
        return None
    except Exception as e:
        print("[AUDIO] Error:", e)
        return None


# Para pruebas individuales
if __name__ == "__main__":
    while True:
        cmd = detectar_voz()
        if cmd:
            print(">> Comando detectado:", cmd)
        time.sleep(0.2)

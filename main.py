import pdfplumber
import re
import pyttsx3

# Parte 1 Obtener el texto del pdf
libro = ""
with pdfplumber.open("input.pdf") as pdf: #Creamos una instacia de pdfplumber pasando como parametro el pdf.
    for page in pdf.pages:
        text = page.extract_text()

        page_number_pattern = r'Página (\d+)' #Creamos una expresion regular para buscar donde aparece el numero de pagina y eliminarlo
        text = re.sub(page_number_pattern, '', text)

        libro += text #Concactenamos el texto final de cada pagina.
print("Se leyo el PDF correctamente.")
print()
print("Aguarde mientras preparamos el archivo de audio")
# Parte 2 Configurar el motor de TTS
engine = pyttsx3.init() #   Creamos una instacia
engine.setProperty("rate", 250) # Palabras por minuto
engine.setProperty("volume", 1.0)# Volumen
engine.setProperty("voice", "spanish")# Idioma de la voz

# Parte 3 exportar el archivo a mp3
engine.save_to_file(libro, "./output/output.mp3")
engine.runAndWait()
print("¡¡¡Finalizado!!!")



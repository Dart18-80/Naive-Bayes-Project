import nltk
import os

# Ruta forzada de descarga local
nltk_path = os.path.join(os.path.dirname(__file__), "..", "nltk_data")

# Crear carpeta si no existe
os.makedirs(nltk_path, exist_ok=True)

# Descargar recursos en la ruta personalizada
nltk.download('punkt', download_dir=nltk_path)
nltk.download('stopwords', download_dir=nltk_path)
nltk.download('punkt_tab', download_dir=nltk_path)

print("Recursos descargados correctamente en nltk_data/")

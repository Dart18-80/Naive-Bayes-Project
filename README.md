# 🕵️‍♀️ Fake Review Detector - Naïve Bayes Classifier

Este proyecto es una aplicación de **Inteligencia Artificial** que detecta **reseñas falsas** en productos utilizando el algoritmo de **Naïve Bayes**, implementado **desde cero en Python** 🐍.

Incluye una **interfaz web con Flask** que permite ingresar una reseña y muestra un mensaje personalizado indicando si parece **genuina (CG)** o **falsa (OR)**.

---

## 🚀 Tecnologías utilizadas

- Python 3.10+
- Flask
- Pandas
- NLTK (Natural Language Toolkit)
- HTML + CSS (Flask Templates)
- pickle (para serialización del modelo)
- collections.defaultdict (para contar palabras)

---

## 🧠 Clasificación de reseñas

- **CG**: Reseña genuina (honesta)
- **OR**: Reseña falsa (sospechosa)

### 💬 Mensajes mostrados:
- **CG**: ✅ *La reseña parece genuina. ¡Gracias por compartir una opinión auténtica!*
- **OR**: ⚠️ *Esta reseña podría ser falsa. Procede con precaución.*

---

## 🛠️ Instrucciones de instalación y ejecución

### 1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/fake-review-classifier.git
cd fake-review-classifier
```

### 2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

Contenido del `requirements.txt`:
```
flask
nltk
pandas
```

### 3. Configura NLTK (solo una vez):
```bash
python nltk_setup.py
```
Esto descargará los recursos necesarios: `punkt` y `stopwords`.

### 4. Entrena el modelo:
```bash
python train_model.py
```
Este script:
- Lee el dataset
- Preprocesa los textos
- Entrena el modelo Naïve Bayes
- Guarda el modelo con `pickle`

### 5. Ejecuta la aplicación web:
```bash
python app.py
```
Abre tu navegador en 👉 [http://localhost:5000](http://localhost:5000)

---

## 🧪 Notas sobre el modelo

- El texto es preprocesado:
  - Conversión a minúsculas
  - Limpieza
  - Tokenización
  - Eliminación de *stopwords*
  - Stemming

- Se utiliza **Naïve Bayes** para clasificar entre CG y OR.
- Se utiliza `collections.defaultdict` para contar palabras sin errores:

```python
from collections import defaultdict
frecuencias = defaultdict(int)
frecuencias["producto"] += 1
```

---

## ❓ ¿Por qué todo se clasifica como genuino?

- El dataset está **desbalanceado**, con muchas más reseñas genuinas que falsas.
- Puedes probar con reseñas falsas como:
  - "Best product ever! Will buy again!"
  - "Buy now! This changed my life!"

---

## 📄 Licencia

Proyecto académico para el curso de **Inteligencia Artificial** en la **Universidad Rafael Landívar**.

---

## 👩‍💻 Créditos

- **Desarrollado por**: [Tu Nombre]
- **Curso**: Inteligencia Artificial
- **Universidad Rafael Landívar** - Primer semestre 2025

# Web Scraper de Títulos en Python

Este script permite extraer títulos u otras etiquetas HTML desde una página web utilizando las bibliotecas **requests** y **BeautifulSoup**. Es ideal para practicar conceptos básicos de web scraping y procesamiento de HTML en Python.

---

## Funcionalidades principales

- **Normalización de URL:** Asegura que la URL tenga un esquema válido (HTTP/HTTPS).
- **Obtención del HTML:** Descarga el contenido de la página mediante `requests`.
- **Extracción de etiquetas:** Usa BeautifulSoup para obtener texto de etiquetas como `<h1>`, `<h2>`, `<p>`, etc.
- **Interacción con el usuario:** Permite elegir la etiqueta a extraer.
- **Exportación:** Opción para guardar los resultados en un archivo de texto.

---

## Requisitos

Instala las dependencias necesarias con:

   ```bash
   pip install requests beautifulsoup4
   ```

---

## Ejecución

Ejecuta el programa desde la terminal:

   ```bash
   python scraper_titles.py
   ```

Luego introduce la URL y la etiqueta HTML a extraer (por ejemplo, h1, h2, p).


---

## Autor

**Alan Aquino**, estudiante de Ingeniería en Informática.


---

## Licencia

Este proyecto se distribuye bajo la Licencia MIT.
Consulta el archivo LICENSE para más información.

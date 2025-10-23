import sys
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

def normalize_url(url: str) -> str:
    url = url.strip()
    if not url:
        raise ValueError("URL vacía.")
    parsed = urlparse(url)
    if parsed.scheme == "":
        # Si no tiene esquema, asume HTTP.
        url = "http://" + url
        parsed = urlparse(url)
    if parsed.netloc == "":
        raise ValueError("URL inválida.")
    return url

def fetch_html(url: str, timeout: int = 10) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Scraper/1.0; +https://example.local/)"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=timeout)
        resp.raise_for_status()
        return resp.text
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error al obtener la URL: {e}.") from e

def extract_tags(html: str, tag: str = "h1") -> list:
    soup = BeautifulSoup(html, "html.parser")
    elements = soup.find_all(tag)
    results = []
    for el in elements:
        text = el.get_text(separator=" ", strip=True)
        if text:
            results.append(text)
    return results

def main():
    print("Web Scraper")
    try:
        url = input("Introduce la URL: ").strip()
        url = normalize_url(url)
    except ValueError as e:
        print("Entrada inválida:", e)
        sys.exit(1)

    # Permitir elegir la etiqueta (h1, h2, h3, etc.)
    tag = input("Etiqueta a extraer: ").strip().lower()
    if tag == "":
        tag = "h1"

    print(f"\nObteniendo {tag} de: {url}...")

    try:
        html = fetch_html(url)
    except RuntimeError as e:
        print(e)
        sys.exit(1)

    titles = extract_tags(html, tag=tag)

    if not titles:
        print(f"No se encontraron etiquetas <{tag}> en la página.")
    else:
        print(f"\nSe encontraron {len(titles)} elementos <{tag}>:\n")
        for i, t in enumerate(titles, 1):
            print(f"{i}. {t}")

        # Preguntar si guardar en archivo.
        save = input("\n¿Deseas guardar los resultados en un archivo? (s/N): ").strip().lower()
        if save == "s" or save == "si":
            filename = input("Nombre para el archivo: ").strip()
            if not filename:
                filename = "titulos.txt"
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    for t in titles:
                        f.write(t + "\n")
                print(f"Guardado como '{filename}'.")
            except OSError as e:
                print("Error al guardar el archivo:", e)

if __name__ == "__main__":
    main()
import builtwith #funciona igual al wappalyzer
import requests
from bs4 import BeautifulSoup
import mechanize
import subprocess



url = 'https://costaricaexperts.com/destinations/tamarindo/'
response = requests.get(url)

browser = mechanize.Browser()


if response.status_code == 200:

    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    links = soup.find_all('a')

    for link in links:
        # Imprimir el texto y la URL de cada enlace
        print(f"Texto: {link.text}")
        print(f"URL: {link.get('href')}")
        print("-" * 20)

else:
    print(f"Error: {response.status_code}")


# URL de la página con el formulario
url2 = 'https://costaricaexperts.com/contact/'



try:
    responses = browser.open(url2)
except Exception as e:
    print(f"Error al abrir la URL: {e}")


if responses.code == 200:

    browser.select_form(nr=0)
    browser.form['input_2.3'] = 'Camila'
    browser.form['input_2.6'] = 'Fischer'
    browser.form['input_5'] = 'ejemplo@gmail.com'
    browser.form['input_4'] = '88888888'
    browser.form['input_7'] = 'Blablablabla'

    response_after_submit = browser.submit()

   # print(response_after_submit.read())

else:
    print(f"Error: {responses.code} ")


result = builtwith.builtwith(url)

print(f'Tecnologías utilizadas en la pagina de Tamarindo beach')
tecnologias = ''
for category, technologies in result.items():
    print(f'{category}: {", ".join(technologies)}')
    tecnologias += f'{category}: {", ".join(technologies)}'


ruta_archivo = "reporte.txt"


contenido = "Se realizarón pruebas de Inyeccion SQL, escaneo de puertos con from zapv2 import ZAPv2, y otro analisis de vulnerablidades"
contenido += '\nTecnologias usadas'
contenido += tecnologias


# Abrir el archivo en modo escritura (w)
with open(ruta_archivo, 'w') as archivo:

    archivo.write(contenido)


print(f"Se ha creado el archivo '{ruta_archivo}' y se ha escrito en él.")
subprocess.run(["notepad.exe", ruta_archivo])

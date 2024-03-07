import requests
from bs4 import BeautifulSoup
import mechanize
from wappalyzer import Wappalyzer, WebPage
import cgi  # PARA REALIZAR UN XSS


url = 'https://asterioargabogados.netlify.app/'

response = requests.get(url)


if response.status_code == 200:
    print(response.text)
else:

    print(f"Error: {response.status_code}")


def obtener_enlaces(url):

    response = requests.get(url)
    htmlcontenido = response.text

    beatifud = BeautifulSoup(htmlcontenido, 'html.parser')

    links = beatifud.find_all('a')

    enlaces = []

    for link in links:
        href = link.get('href')
        if href:
            enlaces.append(href)

    return enlaces


browser = mechanize.Browser()


browser.open(url)


browser.select_form(nr=0)  # nr es el índice del formulario, 0 en este caso

# SE REALIZA UN LLENADO RAPIDO DEL FORMULARIO MOSTRADO
browser.form['name'] = 'Juan'
browser.form['number'] = '1778289919'
browser.form['email'] = 'juand@gmail.com'


# Enviar el formulario
response = browser.submit()

# Imprimir la respuesta del servidor
print(response.read())


def obtener_tecnologias(url):
    try:
        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)
        tecnologias = wappalyzer.analyze(webpage)

        return tecnologias

    except Exception as e:
        print(f"Error: {e}")
        return None


tecnologias_encontradas = obtener_tecnologias(url)

if tecnologias_encontradas:
    print("Tecnologías encontradas:")
    for tecnologia in tecnologias_encontradas:
        print(tecnologia)
else:
    print("No se pudieron obtener las tecnologías.")

formulario = cgi.FieldStorage()

nombre = formulario.getvalue('name')

print('Prueba de XSS')
print(f"Nombre: {nombre}")

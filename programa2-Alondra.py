import dns.resolver
import whois
import os
import subprocess

# Ejemplo de consulta DNS para obtener los registros A de un dominio


def obtener_registros_a(dominio):
    try:
        respuesta = dns.resolver.resolve(dominio, 'A')
        for registro_a in respuesta:
            print(f'Registro A: {registro_a.address}')

    except dns.exception.DNSException as e:
        print(f'Error al obtener los registros A: {e}')


def consultar_whois(dominio):
    try:
        info_whois = whois.whois(dominio)
        print(info_whois)
    except whois.parser.PywhoisError as e:
        print(f'Error al consultar WHOIS: {e}')


def subprocesoPing():
   # Especifica la dirección IP o el nombre de dominio que deseas pinguear
    destino = "www.google.com"


    comando_ping = ['ping', '-n', '4', destino]  # '-n 4' especifica enviar 4 paquetes
    resultado_ping = subprocess.run(comando_ping, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


    if resultado_ping.returncode == 0:
        print(f"\nPing exitoso hacia {destino}:\n")
        print(resultado_ping.stdout)
    else:
        print(f"\nError en el ping hacia {destino}:\n")
        print(resultado_ping.stderr)

nombre_sistema_operativo = os.name

print(f"Nombre del sistema operativo: {nombre_sistema_operativo}")
obtener_registros_a('www.toyotacr.com')
consultar_whois('www.toyotacr.com')
subprocesoPing()


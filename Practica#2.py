import dns.resolver
import tldextract  # POR MOTIVOS DE QUE WHOIS NO ME FUNCIONA EN MI ENTORNO DECIDI USAR UNA
# LIBRERIA QUE HACE LO MISMO QUE EL WHOIS
import os
import platform
import subprocess

nombre_dominio = "ufidelitas.ac.cr"

# DNS.RESOLVER
respuesta = dns.resolver.query(nombre_dominio, 'A')


for resultado in respuesta:
    print(f"Registro A para {nombre_dominio}: {resultado.address}")
print()
print()
print()
# tldextract
info_dominio = tldextract.extract(nombre_dominio)


print(f"Subdominio: {info_dominio.subdomain}")
print(f"Dominio principal: {info_dominio.domain}")
print(f"Extensión: {info_dominio.suffix}")

print()
print()
print()

# MODULO OS
nombre_sistema_operativo = os.name
informacion_sistema = os.uname() if nombre_sistema_operativo == 'posix' else None
version_sistema_operativo = platform.system() + " " + platform.version()
arquitectura_sistema = platform.architecture()[0]
print(f"Nombre del sistema operativo: {nombre_sistema_operativo}")
print(f"Información del sistema operativo: {
      informacion_sistema}" if informacion_sistema else "")
print(f"Versión del sistema operativo: {version_sistema_operativo}")
print(f"Arquitectura del sistema: {arquitectura_sistema}")
print()
print()
print()
# SUBPROCESS
# Comando ipconfig para obtener información sobre la configuración de red en Windows
comando_ipconfig = ['ipconfig']
# Ejecutar el comando ipconfig y capturar la salida
resultado_ipconfig = subprocess.run(
    comando_ipconfig, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# Imprimir la salida del comando ipconfig
if resultado_ipconfig.returncode == 0:
    print("Resultado del comando ipconfig:")
    print(resultado_ipconfig.stdout)
else:
    print("Error al ejecutar el comando ipconfig:")
    print(resultado_ipconfig.stderr)

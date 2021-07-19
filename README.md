# Creador de Script para Switch Cisco 

## Badges
[![Build Status](https://travis-ci.com/MarcoRiosG/asistenteIOSCiscoSwitch.svg?branch=main)](https://travis-ci.com/MarcoRiosG/asistenteIOSCiscoSwitch)

## Acerca del proyecto
Este proyecto busca ayudar a las personas que estan entrando al mundo de las redes de Cisco y tengan problemas para memorizar los comandos basicos del switch con IOS de Cisco.

## Como funciona
Este programa provee de preguntas a los usuarios en un lenguaje mas natural acerca de las configuraciones que busquen hacer en el switch, el programa solo requiere entradas del usuario cuando sea necesario especificar algun dato en especifico. El programa ira generando el script con los comandos segun lo que el usuario haya especificado que quiere configurar. Al finalizar el usuario recibira un archivo de texto con el script generado.

## Mejoras a futuro y errores conocidos
* Las interfaces por default tienen un limite de 1 direccion MAC para guardar, ya que se pregunta primero por agregar direcciones, si se agregan mas de 1 el switch arrojara un error ya que el limite de 1 direccion fue alcanzado, se debe, de momento, primero cambiar el limite de direcciones y luego hacer el proceso de agregar ahora si las direcciones con el limite ajustado a lo deseado.

* La seguridad en puertos solo se puede ajustar si la interfaz/puerto ya tiene asignado un modo troncal o de acceso, añadir algun mensaje con este aviso o añadir la posibilidad de configurar el modo troncal/acceso sin la necesidad de pasar por otro proceso de configuracion

* Faltan verificaciones (formato de direcciones ip validas, por ejemplo)

* Mejorar los textos

* Añadir mas configuraciones

## Como ejecutarlo...
Ejecutar el archivo asistente.py con el comando:
```python
python asistente.py
```


.. AsistenteConfigIOSSwitch documentation master file, created by
   sphinx-quickstart on Sat Jul 17 20:23:37 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenido a la documentacion para AsistenteConfigIOSSwitch!
============================================================

Este sencillo programa permitira guiar a aquellos primerizos en el mundo de las redes.

¿Tienes problemas memorizando los comandos para configurar un Switch? ¿No sabes como navegar a traves del CLI del IOS?
Tranquilo, este programa omitirá todos los comandos tediosos y los cambiara por simples preguntas.
Basta con responder y elegir lo que quieres configurar con palabras que uno puede usar en su dia a dia y el programa arrojará un script con todos los comandos necesarios para lograr la configuración que quieres, solo copia y pega en el CLI.

Antes de iniciar revisa esta :ref:`introduccion al programa <init>`.

En esta version (1.0) se incluye la configuración básica de los Switches de Cisco y las funciones que se pueden configurar son:

* :ref:`Configuración basica del Switch <config_b_s>`
* :ref:`Configurar la VLAN de acceso remoto (VLAN 1) <vlan_a>`
* :ref:`Configurar VLAN y asignarlas a las interfaces del Switch <vlan_asig>`
* :ref:`Confiurar seguridad en los puertos del Switch <seg_p>`

.. toctree::
   :maxdepth: 2
   :hidden:

   inicio

.. toctree::
   :maxdepth: 2
   :caption: Opciones de configuración:

   config_basica_switch
   vlan_acceso
   vlan_asignacion
   seguridad_puertos

.. toctree::
   :maxdepth: 2
   
   final


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

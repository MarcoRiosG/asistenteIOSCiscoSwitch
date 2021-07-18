.. _vlan_a:

Configurar VLAN de acceso remoto
================================

Esta opcion configurará la VLAN para el acceso remoto al Switch mediante la asignación de una dirección IP 
y su máscara de subred habilitando dicha VLAN como interfaz a la cual dirigirse si se desea acceder por SSH o Telnet al Switch.

.. figure:: /images/vlan_a.PNG
   :alt: Preguntas para la configuración de la VLAN de acceso
   :align: center
    
   *Preguntas para configuración de la VLAN de acceso*

.. hint:: Como se puede observar, una vez se decide configurar una IP al responder a la pregunta respectiva, se solicitará la mascara de subred, 
    ya que el comando no puede ir sin este dato, la pregunta de mascara de subred no se puede dejar vacía.

    Al finalizar las preguntas se regresará al menú principal para poder elegir otra opción.
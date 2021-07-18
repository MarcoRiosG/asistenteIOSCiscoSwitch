.. _vlan_asig:

VLANs y asignación a los puertos del Switch
======================================================

Esta opción permitirá crear y configurar VLANs en el switch y asignarlas a los distintos puertos del switch, tambien permitirá asignar un puerto como troncal.

Creación de VLANs
-----------------

Primero, ya que se pueden crear multiples VLANs, se solicitará al usuario que escriba las VLANs a crear **una por una, separadas por Intro**, cuando ya no se vayan a agregar mas VLANs deberá de introducirse el caracter 'x'.

.. figure:: /images/vlans.PNG
   :alt: Añadir VLANs al pool de VLANs a configurar
   :align: center
    
   *Añadiendo VLANs*

.. hint:: Como se puede observar, esta pregunta no acepta dejarla sin respuesta, para dejar de responder incluso si no se ha añadido ninguna VLAN se deberá escribir 'x'.

Posteriormente se solicitará al usuario que de un nombre a las VLAN que acaba de indicar, al finalizar, se pasará a la siguiente sección.


Asignacion de interfaces
------------------------

Se preguntará al usuario si quiere asignar interfacez a alguna VLAN, el dejar sin responder implica no realizar ninguna asignación y el programa regresará al menú principal.

En caso de querer realizar asignaciones se pedirá que se indiquen las interfaces a configurar de la misma forma que al crear las VLANs.

.. figure:: /images/interfaces.PNG
   :alt: Preguntas para la asignación de interfaces
   :align: center
    
   *Interfaces a configurar*

Posteriormente se pedira que se asigne cada interfaz de las ingresadas al modo troncal o al modo de acceso.

.. warning:: Se puede dejar la respuesta en blanco para no cambiar la interfaz en caso de ya no querer modificar la interfaz.

    A esta pregunta solo se puede responder con los caracteres 't' y 'a', cualquier otra entrada será erronea y se mostrara un mensaje de error antes de volver a mostrar la pregunta.


Trunk
*****

La configuracion de troncal (Trunk) permitira configurar la interfaz como troncal, indicarle la VLAN nativa a la interfaz y configurar las VLANs que pueden pasar por esa interfaz.

.. figure:: /images/trunk.PNG
   :alt: Configuracion troncal
   :align: center
    
   *Opción trunk*

Access
******

La configuracion de acceso (Access) permitira asignar el puerto a una VLAN.

.. figure:: /images/access.PNG
   :alt: Configuracion acceso
   :align: center
    
   *Opción access*


    

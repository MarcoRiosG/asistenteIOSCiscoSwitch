.. _seg_p:

Seguridad de puertos
====================

Esta opcion permite asignar seguridad a los puertos que esta basada en la direcciones MAC de los dispositivos.

Al inicio, se pedira que se indique que interfaces desea configurar al usuario **una por una, separadas por Intro**, cuando ya no se vayan a agregar mas interfaces deberá de introducirse el caracter 'x'.

.. figure:: /images/interfaces_seg.PNG
   :alt: Interfaces a configurar seguridad
   :align: center
    
   *Añadiendo interfaces*

.. hint:: Como se puede observar, esta pregunta no acepta dejarla sin respuesta, para dejar de responder incluso si no se ha añadido ninguna interfaz se deberá escribir 'x'.

Una vez finalice de agregar interfaces, se pedira que les asigne un modo de seguridad para añadir direcciones MAC como seguras *sticky* o manualmente.
La configuracion *sticky* se hace en automatico, la manual pedira al usuario que ingrese la direccion a agregar con la capacidad de agregar varias hasta que el usuario decida ya no agregar más **(se debe tomar en cuenta que hay un limite en cuanto al numero de direcciones a guardar que puede ser modificado)**.

Posteriormente a esta configuración se pedira que se configure el tiempo de caducidad para las direcciones almacenadas (en minutos) y el maximo de direcciones a almacenar.

Por ultimo se pedira que se indique la accion a tomar en caso de una amenaza:

* Protegido (Protect)
* Restringido (Restrict)
* Apagar (Shutdown)

.. hint:: Este proceso se realizará para cada interfaz indicada al inicio.

.. figure:: /images/vlans.PNG
   :alt: Configuracion de seguridad por interfaces indicadas
   :align: center
    
   *Configuracion de seguridad por interfaces indicadas*

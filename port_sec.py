def port_security(comandos):
    interfaces = []
    config = input("\nInterfaces sobre las cuales configurar la seguridad, escribir solo 1 numero y dar Enter para añadir otra interfaz, para ya no agregar mas interfaces favor de escribir X \n(El numero de interfaces disponibles dependera del modelo del switch): ")
    condicion = True
    while condicion:
        while not config:
            print("\nNo puede dejar este campo vacio, introduzca interfaces (#) validas o X para finalizar")
            config = input("\nInterfaces sobre las cuales configurar la seguridad, escribir solo 1 numero y dar Enter para añadir otra interfaz, para ya no agregar mas interfaces favor de escribir X \n(El numero de interfaces disponibles dependera del modelo del switch): ")
        if config == 'X' or config == 'x':
            condicion = False
        else:
            try:
                int(config)
            except:    
                print("\nEscribir solo numeros")
                config = input("\nInterfaces sobre las cuales configurar la seguridad, escribir solo 1 numero y dar Enter para añadir otra interfaz, para ya no agregar mas interfaces favor de escribir X \n(El numero de interfaces disponibles dependera del modelo del switch): ")
            else:
                interfaces.append(config)
                config = input("\nInterfaces sobre las cuales configurar la seguridad, escribir solo 1 numero y dar Enter para añadir otra interfaz, para ya no agregar mas interfaces favor de escribir X \n(El numero de interfaces disponibles dependera del modelo del switch): ")
    for interface in interfaces:
        comandos += "\ninterface f0/" + interface + "\nswitchport port-security"
        configM = input(f"\nTipo de seguridad para la interfaz f0/{interface} [Address (A)/Sticky (S)] ")
        condicion1 = True
        while condicion1: 
            if configM.strip():
                try:
                    str(configM)
                except:
                    configM = input(f"\nTipo de seguridad para la interfaz f0/{interface} [Address (A)/Sticky (S)] ")
                else:
                    if configM == 's' or configM == 'S':
                        comandos += "\nswitchport port-security mac-address sticky"
                        condicion1 = False
                    elif configM == 'a' or configM == 'A':
                        configAdd = input("\nDireccion MAC a agregar XXXX.XXXX.XXXX: ")
                        if configAdd.strip():
                            comandos += "\nswitchport port-security mac-address " + configAdd
                            configAdd = input("\nEscribir 's' para añadir otra direccion: ")
                            if configAdd == 's' or configAdd == 'S':
                                condicion1 = True
                            else:
                                condicion1 = False
                        else:
                            print("\nNo puede dejar este campo vacio") 
                    else:
                        print("\nSolo escribir 'S', 's', 'A' o 'a'")
                        configM = input(f"\nTipo de seguridad para la interfaz f0/{interface} [Address (A)/Sticky (S)] ")
            else:
                condicion1 = False
        configSec = input(f"\nTiempo de caducidad para las direcciones en la interfaz f0/{interface} (minutos): ")
        condicion3 = True
        while condicion3:
            if configSec.strip():
                try:
                    int(configSec)
                except:
                    print("\nEscribir solo numeros")
                    configSec = input(f"\nTiempo de caducidad para las direcciones en la interfaz f0/{interface} (minutos): ")
                else:
                    comandos += "\nswitchport port-security aging time " + configSec
                    condicion3 = False
            else:
                condicion3 = False
        configSec = input(f"\nMaximo de direcciones a recordar en la interfaz f0/{interface}: ")
        condicion3 = True
        while condicion3:
            if configSec.strip():
                try:
                    int(configSec)
                except:
                    print("\nEscribir solo numeros")
                    configSec = input(f"\nMaximo de direccionesa recordar en la interfaz f0/{interface}: ")
                else:
                    comandos += "\nswitchport port-security maximum " + configSec
                    condicion3 = False
            else:
                condicion3 = False
        configSec = input(f"\nAccion de respuesta en la interfaz f0/{interface} [Protect (P)/Restrict (R)/Shutdown (S)]: ")
        condicion3 = True
        while condicion3:
            if configSec.strip():
                try:
                    str(configSec)
                except:
                    print("\nEscribir solo texto")
                    configSec = input(f"\nAccion de respuesta en la interfaz f0/{interface} [Protect (P)/Restrict (R)/Shutdown (S)]: ")
                else:
                    if configSec == 'P' or configSec == 'p':
                        comandos += "\nswitchport port-security violation protect"
                        condicion3 = False
                    elif configSec == 'R' or configSec == 'r':
                        comandos += "\nswitchport port-security violation restrict"
                        condicion3 = False
                    elif configSec == 'S' or configSec == 's':
                        comandos += "\nswitchport port-security violation shutdown"
                        condicion3 = False
                    else:
                        print("\nEscribir solo 'P', 'p', 'R', 'r', 'S' o 's'")
                        configSec = input(f"\nAccion de respuesta en la interfaz f0/{interface} [Protect (P)/Restrict (R)/Shutdown (S)]: ")
            else:
                condicion3 = False
        comandos += "\nexit"
    comandos += "\ndo copy run start \n"

    return comandos
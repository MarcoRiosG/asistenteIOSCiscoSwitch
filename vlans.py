def vlan(comandos):
    config = input("\nNumero de VLAN a crear/configurar [1-4094]: ")
    if config.strip():
        comandos += "\nvlan " + config
        config = input("\nNombre de la VLAN: ")
        if config.strip():
            comandos += "\nname " + config + "\nexit"
    config = input("\n¿Asignar interfaces a alguna VLAN? (Escribir lo que sea para afirmar) ")
    if config.strip():
        interfaces = []
        config = input("\nInterfaces a configurar, escribir solo 1 numero y dar Enter para añadir otra interfaz, para ya no agregar mas interfaces favor de escribir X \n(El numero de interfaces disponibles dependera del modelo del switch): ")
        condicion = True
        while condicion:
            while not config:
                print("\nNo puede dejar este campo vacio, introduzca interfaces (#) validas o X para finalizar")
                config = input("\nInterfaces a configurar, escribir solo 1 numero y dar Enter para añadir otra interfaz, para ya no agregar mas interfaces favor de escribir X \n(El numero de interfaces disponibles dependera del modelo del switch): ")
            if config == 'X' or config == 'x':
                condicion = False
            else:
                try:
                    int(config)
                except:    
                    print("\nEscribir solo numeros")
                    config = input("\nInterfaces a configurar, escribir solo 1 numero y dar Enter para añadir otra interfaz, para ya no agregar mas interfaces favor de escribir X \n(El numero de interfaces disponibles dependera del modelo del switch): ")
                else:
                    interfaces.append(config)
                    config = input("\nInterfaces a configurar, escribir solo 1 numero y dar Enter para añadir otra interfaz, para ya no agregar mas interfaces favor de escribir X \n(El numero de interfaces disponibles dependera del modelo del switch): ")
        for interface in interfaces:
            comandos += "\ninterface f0/" + interface
            configM = input(f"\nModo de switching para la interfaz f0/{interface} [Trunk (t)/Access (a)]: ")
            condicion1 = True
            while condicion1: 
                if configM.strip():
                    try:
                        str(configM)
                    except:
                        configM = input(f"\nModo de switching para la interfaz f0/{interface} [Trunk (t)/Access (a)]: ")
                    else:
                        if configM == 't' or configM == 'T':
                            comandos += "\nswitchport mode trunk"
                            configVLAN = input("\nVLAN nativa: ")
                            condicion3 = True
                            while condicion3:
                                if configVLAN.strip():
                                    try:
                                        int(configVLAN)
                                    except:
                                        print("\nEscribir solo numeros")
                                        configVLAN = input("\nVLAN nativa: ")
                                    else:
                                        comandos += "\nswitchport trunk native vlan " + configVLAN
                                        condicion3 = False
                                else:
                                    condicion3 = False
                            configVLAN = input("\nVLAN acceptadas por esta interfaz (Si son varias, separar solo por una coma, NO USAR ESPACIOS): ")
                            if configVLAN.strip():
                                comandos += "\nswitchport trunk allowed vlan " + configVLAN
                            condicion1 = False
                        elif configM == 'a' or configM == 'A':
                            comandos += "\nswitchport mode access"
                            configVLAN = input("\nVLAN a asignar a esta interfaz: ")
                            condicion3 = True
                            while condicion3:
                                if configVLAN.strip():
                                    try:
                                        int(configVLAN)
                                    except:
                                        print("\nEscribir solo numeros")
                                        configVLAN = input("\nVLAN a asignar a esta interfaz: ")
                                    else:
                                        comandos += "\nswitchport access vlan " + configVLAN
                                        condicion3 = False
                                else:
                                    condicion3 = False 
                            condicion1 = False   
                        else:
                            print("\nSolo escribir 'T', 't', 'A' o 'a'")
                            configM = input(f"\nModo de switching para la interfaz f0/{interface} [Trunk (t)/Access (a)]: ")
                else:
                    condicion1 = False
        comandos += "\nexit"
    comandos += "\ndo copy run start \n"

    return comandos
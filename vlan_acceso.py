def int_acceso(comandos):
    comandos += "\ninterface vlan 1"
    config = input("\nDireccion IP: ")
    if config.strip():
        comandos += "\nip address " + config
        config = input("\nMascara de red: ")
        while not config:
            print("\nNo puede dejar este campo vacio, introduzca una mascara valida X.X.X.X")
            config = input("\nMascara de red: ")
        comandos += "\nenable secret " + config.strip()
    comandos += "\nno shutdown \nexit \ndo copy run start \n"
    
    return comandos
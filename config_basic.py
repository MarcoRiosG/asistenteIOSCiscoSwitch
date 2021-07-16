def config_b(comandos):
    config = input("\nNombre del dispositivo: ")
    if config.strip():
        comandos += "\nhostname " + config
    config = input("\nContraseña de modo privilegiado: ")
    if config.strip():
        comandos += "\nenable secret " + config
    config = input("\n¿Encriptar contraseñas? (Escribir lo que sea para afirmar) ")
    if config.strip():
        comandos += "\nservice password-encryption"
    config = input("\nBanner de acceso (MOTD): ")
    if config.strip():
        comandos += "\nbanner motd #" + config + "#"
    config = input("\n¿Configurar linea de consola? (Escribir lo que sea para afirmar) ")
    if config.strip():
        comandos += "\nline con 0"
        config = input("Contraseña: ")
        if config.strip():
            comandos += "\npassword " + config
            comandos += "\nlogin"
    config = input("\n¿Configurar lineas de vty? (Escribir lo que sea para afirmar) ")
    if config.strip():
        comandos += "\nline vty 0 15"
        config = input("\nContraseña: ")
        if config.strip():
            comandos += "\npassword " + config
            comandos += "\nlogin"
    comandos += "\ndo copy run start \n"

    return comandos

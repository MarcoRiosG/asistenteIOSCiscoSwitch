import global_config,  config_basic, vlan_acceso, vlans, port_sec

def main():

    comandos = ""
    print("¡¡¡Bienvenido al creador de scripts basicos para switch Cisco!!!")
    print("**********DEJAR VACIA UNA OPCION HARA QUE DICHA CONFIGURACION NO SE MODIFIQUE**********")
    enter_g_c = input("¿Desea recibir los comandos para entrar al modo de configuracion global? (Escribir 's' para afirmar) ")
    if enter_g_c == "s" or enter_g_c == "S":
        comandos += global_config.enter_global_config_mode()

    terminar_conf = True
    while terminar_conf:
        opcion = input("""\nElija una de las configuraciones a realizar: 
        1. Configuracion basica
        2. Configurar interfaz de acceso (VLAN 1)
        3. Configurar VLANs
        4. Configurar seguridad en puertos
        x. Terminar
        Opcion: """)
        if opcion == 'X' or opcion == 'x':
            print("Gracias por usar este programa, solo copia y pega la configuracion en el CLI :)")
            terminar_conf = False
        elif int(opcion) == 1:
            comandos = config_basic.config_b(comandos)
        elif int(opcion) == 2:
            comandos = vlan_acceso.int_acceso(comandos)
        elif int(opcion) == 3:
            comandos = vlans.vlan(comandos)
        elif int(opcion) == 4:
            comandos = port_sec.port_security(comandos)
    print("Script:")
    print(comandos)
    with open("comandos.txt", "w") as archivo:
        archivo.write(comandos)

main()
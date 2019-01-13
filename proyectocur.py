opcion=5
while  opcion!=3:
    opcion=int(input("----SISTEMA DE VENTAS----\n   1. Administrador \n   2. Clinte  \n   3. Salir \nopcion: "))
    if opcion==1:
        op=8
        while op!=2:
            op=int(input("---Administrador---\n    1. Ingresar\n    2. Regresar\nopcion:"))
            if op==1:
                print("hola")
            if op!=2 and op!=1:
                 print("\nopcion invalida")
        
        
    elif opcion==2:
        op=5
        while op!=3:
            op=int(input("---Cliente---\n    1. Ingresar\n    2. Registrarse\n    3. Regresar\nopcion:"))
            if op==1:
                print("hola")
            if op==2:
                print("cliente")
            if op!=2 and op!=1 and op!=3:
                 print("\nopcion invalida")
                 
                 
                 
    elif opcion==3:
        print("Gracias por usar")
    else:
        print("\nopcion invalida")
    

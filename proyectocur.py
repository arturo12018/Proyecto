def op8ad(x):
    print("Administrativo:",x[0],"\nApellido:",x[2],"\nEdad:",x[4],"\nSalario:",x[3], "\nContraseña:",x[1])
    pass


opcion=5
while  opcion!=3:
    opcion=int(input("----SISTEMA DE VENTAS----\n   1. Administrador \n   2. Clinte  \n   3. Salir \nopcion: "))
    if opcion==1:
        op=8
        while op!=2:
            op=int(input("---Administrador---\n    1. Ingresar\n    2. Regresar\nopcion:"))
            if op==1:
                administrador1=["Arturo","123"]
                administrador2=["Luis","123"]
                x=[]
                x.append(input("Administrador:  "))
                x.append(input("Contraseña:  "))
                if administrador1==x or administrador2==x:
                    if administrador1==x:  
                        administrador1=["Arturo","123","Muñoz","2000$",19]
                        x=administrador1
                            
                    elif administrador2==x:
                        administrador2=["Luis","123","Ortiz","2000$",19]
                        x=administrador2
                
                    op8ad(x)
                    
                    
                if administrador1!=x and administrador2!=x  :
                    print("administrador o contraseña esta mal")
                    
                     
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
    

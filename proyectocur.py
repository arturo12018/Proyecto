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
                    re=11
                    while re!=9:
                        re=int(input("---Sistema de ventas---\n1.Ingresa no. maximos de vuelos\n2.Ingresar vuelos\n3.Listar de vuelos\n4.Cancelar vuelos\n5.Actualizar vuelos\n6.Estadisticas de pago\n7.Estadisticas de clasesn\n8.Informacion administrador\n9.Regresar\nOpcion: "))
                        if re==1:
                            novuelos=int(input("ingrese no. de vuelos:  "))
                            print(novuelos)
                        if re==2:
                            datosvuelo=[]
                            for datos in range(novuelos):
                                datosvuelo.append([])
                                print("\nvuelo",datos+1)
                                destino=input("Destino: ")
                                datosvuelo[datos].append(destino)
                                salida=input("Hora de salida: ")
                                datosvuelo[datos].append(salida)
                                llegada=input("Llegada: ")
                                datosvuelo[datos].append(llegada)
                                costotu=input("Costo de vieaje de turista: ")
                                datosvuelo[datos].append(costotu)
                                costone=input("Costo de viaje de negocios : ")
                                datosvuelo[datos].append(costone)
                                costopr=input("Costo de viaje de primera clase: ")
                                datosvuelo[datos].append(costopr)
                                cltu=int(input("Disponible clase turistica: "))
                                datosvuelo[datos].append(cltu)
                                cln=int(input("Disponible clase negocios: "))
                                datosvuelo[datos].append(cln)
                                clp=int(input("Disponible primera clase : "))
                                datosvuelo[datos].append(clp)
                                fecha=input("Fecha: ")
                                datosvuelo[datos].append(fecha)
                                print("se registro correctamente")
                        if re==3:
                            for datos in range(novuelos):
                                print("\nVuelo no:",datos+1)
                                print("\n\nDestino:",datosvuelo[datos][0])
                                print("Hora de salida:",datosvuelo[datos][1])
                                print("Hora llegada:",datosvuelo[datos][2])
                                print("Costo turista:",datosvuelo[datos][3])
                                print("Costo Negocios:",datosvuelo[datos][4])
                                print("Costo Primera clase:",datosvuelo[datos][5])
                                print("Lugares Clase Turistica:",datosvuelo[datos][6])
                                print("Lugares Clase Negocios:",datosvuelo[datos][7])
                                print("Lugares Primera Clase:",datosvuelo[datos][8])
                                print("Fecha de salida:",datosvuelo[datos][9])
                        
                        if re==4:
                            bo=int(input("Ingrese que vuelo desea borrar: "))
                            
                        
                        if re==8:
                            print("\nAdministrativo:",x[0],"\nApellido:",x[2],"\nEdad:",x[4],"\nSalario:",x[3], "\nContraseña:",x[1])
                            
                        if re!=1 and re!=2 and re!=3 and re!=4 and re!=5 and re!=6 and re!=7 and re!=8 and re!=9: 
                            print("\nopcion invalida ingrese otra opcion:")
                    
                if administrador1!=x and administrador2!=x  :
                    print("administrador o contraseña esta mal")
                    
                     
            if op!=2 and op!=1:
                 print("\nopcion invalida ingrese otra opcion:")
        
        
    elif opcion==2:
        op=5
        while op!=3:
            op=int(input("---Cliente---\n    1. Ingresar\n    2. Registrarse\n    3. Regresar\nopcion:"))
            if op==1:
                print("hola")
            if op==2:
                print("cliente")
            if op!=2 and op!=1 and op!=3:
                 print("\nopcion invalida ingrese otra opcion:")
                 
    elif opcion==3:
        print("Gracias por usar")
    else:
        print("\nopcion invalida ingrese otra opcion:")
    

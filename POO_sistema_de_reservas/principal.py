from clases import *
from funciones import *

print("")
print("¡Bienvenido/a al Sistema de Reservas!")
print("")
def main():
    usuarios=[]
   
    while True:
        # menú principal
        mostrarMenu()
        print("")
        opcion = (input("Ingrese la opción deseada "))
        # sale del menú principal, finaliza la ejecución
        if opcion == "0":
            print("Gracias por usar el Sistema de reservas. !Hasta luego¡ ")
            print("")
            break
        elif opcion=="1":
                # módulo de usuario
                mostrarMenuDeUsuario()
                print("")
                opcion_2 = (input("Ingrese la opción deseada "))

                if opcion_2 == "0": 
                    print("Haz salido del menú de Usuario. ")
                    break

                elif opcion_2 == "1": # Crear usuario
                    try:
                        cedula,nombre,correo,celular=pedirDatosUsuario()
                        user=Usuario(cedula,nombre,correo,celular)
                        usuarios.append(user)
                        print("Usuario creado con los siguientes datos: ")
                        print(usuarios[len(usuarios)-1])    
                    except ValueError:
                        print("Dato invalido")
                    except NameError:
                        print("¡Error!")
                    
                elif opcion_2 == "2": # Consultar usuario
                    try:
                        id_consulta=int(input("Ingrese la Cédula del Usuario a consultar "))
                        found,usuario=autenticarUsuario(id_consulta,usuarios)
                        if found:
                            print(usuario)
                        else:
                            print("El usuario no se encuentra en sistema ")
                    except ValueError:
                        print("Dato invalido")
                    except NameError:
                        print("¡Error!")
                            
                elif opcion_2 == "3":
                    # Actualizar datos de usuario
                    mostrarMenuActualizacionUsuario()
                    opcion_consulta=input("Ingrese la opción que representa el item a Actualizar ")
                    
                    if opcion_consulta=="1":
                        # Actualizar cédula
                        id_consulta=int(input("Ingrese la Cédula del Usuario a Actualizar "))
                        for usuario in usuarios:
                            x=usuario.get_cedula()
                            if id_consulta==x:
                                print("")
                                print(usuario)
                                print("********-   -********")
                                usuario_valido=True 
                                break
                                
                        if usuario_valido==True:
                            dato=int(input("Ingrese la nueva cedula "))
                            for usuario in usuarios:
                                x=usuario.get_cedula()
                                if id_consulta==x:
                                    usuario.set_cedula(dato)
                                    print("")
                                    print(usuario)  
                                    print("********-   -********")
                                    break               
                        else:
                            print("No se encontraron resultados ")
                            print("********-   -********")
                
                    elif opcion_consulta=="2": # Actualizar nombre
                        pass        
                    elif opcion_consulta=="3": # Actualizar correo
                        pass
                    elif opcion_consulta=="4": # Actualizar celular
                        pass
                    elif opcion_consulta=="0": # Sale del módulo de actualizar datos de usuario
                        print("Haz salido del menú . ")
                        break
                    else: # Else del módulo de actualizar datos de usuario
                        print("Opción invalida.")
                        break
                # Eliminar usuario
                elif opcion_2 == "4":
                    pass
                else: # Else del módulo de usuario
                    print("Opción invalida. !Ingresa otra opción¡ ")
                    break
        elif opcion=="2":
            # Módulo de reservas
            while True:
                mostrarMenuDeReservas()
                print("")
                opcion_3 = (input("Ingrese la opción deseada "))

                if opcion_3 == "0":
                    print("Haz salido del menú de Reservas. ")
                    break
                elif opcion_3 == "1":
                    pass
                elif opcion_3 == "2":
                    pass
                elif opcion_3 == "3":
                    pass
                elif opcion_3 == "4":
                    pass
                else:
                    print("Opción invalida. !Ingresa otra opción¡ ")
                    break
        elif opcion=="3":
            # Módulo de localidad
            while True:
                mostrarMenuDeLocalidad()
                print("")
                opcion_4 = (input("Ingrese la opción deseada "))

                if opcion_4 == "0":
                    print("Haz salido del menú de Localidad. ")
                    break
                elif opcion_4 == "1":
                    pass
                elif opcion_4 == "2":
                    pass
                elif opcion_4 == "3":
                    pass
                elif opcion_4 == "4":
                    pass
                else:
                    print("Opción invalida. !Ingresa otra opción¡ ")
                    break
        else: # Else del menú principal
            print("Opción invalida. !Ingresa tu elección¡ ")
            break

if __name__== "__main__":
    main()
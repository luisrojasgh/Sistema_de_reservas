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
                    print("Haz salido del Sistema. ")
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
                        id_consulta=int(input("Ingrese la Cédula del Usuario a Consultar "))
                        consulta=consultarUsuario(id_consulta,usuarios)
                        if consulta==None:
                            print("Usuario no encontrado")
                        else:
                            print(consulta)
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
                        try:
                            id_actualizar=int(input("Ingrese la Cédula del Usuario a Actualizar "))
                            actualizacion=consultarUsuario(id_actualizar,usuarios)
                            if actualizacion==None:
                                print("Usuario a Actualizar no encontrado")
                            else:
                                print(actualizacion)
                                print("********-  -********")
                                dato=int(input("Ingrese la nueva cedula "))
                                for usuario in usuarios:
                                    x=usuario.get_cedula()
                                    if id_actualizar==x:
                                        usuario.set_cedula(dato)
                                        print("")
                                        print(usuario)  
                                        print("********- Dato de usuario Actualizado Exitosamente -********")
                        except ValueError:
                            print("Dato invalido")
                        except NameError:
                            print("¡Error!")
                                                    
                    elif opcion_consulta=="2": # Actualizar nombre
                        try:
                            id_actualizar_nombre=int(input("Ingrese la Cédula del Usuario a Actualizar "))
                            actualizacion_nombre=consultarUsuario(id_actualizar_nombre,usuarios)
                            if actualizacion_nombre==None:
                                print("Usuario a Actualizar no encontrado")
                            else:
                                print(actualizacion_nombre)
                                print("********-  -********")
                                dato=input("Ingrese el nuevo Nombre ")
                                for usuario in usuarios:
                                    x=usuario.get_cedula()
                                    if id_actualizar_nombre==x:
                                        usuario.set_nombre(dato)
                                        print("")
                                        print(usuario)  
                                        print("********- Dato de usuario Actualizado Exitosamente -********")
                        except ValueError:
                            print("Dato invalido")
                        except NameError:
                            print("¡Error!")        
                    elif opcion_consulta=="3": # Actualizar correo
                        try:
                            id_actualizar_correo=int(input("Ingrese la Cédula del Usuario a Actualizar "))
                            actualizacion_correo=consultarUsuario(id_actualizar_correo,usuarios)
                            if actualizacion_correo==None:
                                print("Usuario a Actualizar no encontrado")
                            else:
                                print(actualizacion_correo)
                                print("********-  -********")
                                dato=input("Ingrese el nuevo correo ")
                                for usuario in usuarios:
                                    x=usuario.get_cedula()
                                    if id_actualizar_correo==x:
                                        usuario.set_correo(dato)
                                        print("")
                                        print(usuario)  
                                        print("********- Dato de usuario Actualizado Exitosamente -********")
                        except ValueError:
                            print("Dato invalido")
                        except NameError:
                            print("¡Error!")
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
        elif opcion=="2": # Módulo de reservas
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
        elif opcion=="3": # Módulo de localidad            
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
            print("Opción invalida. !Has salido¡ ")
            break

if __name__== "__main__":
    main()
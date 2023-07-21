# Funciones generales

def mostrarMenu():
    print("****************-Menú Principal-************")
    print("")
    print("Usted se encuentra en el Módulo Principal: ")
    print("")
    print("1. Usuario")
    print("2. Reservas")
    print("3. Localidad")
    print("0. Salir")
    print("****************-    -*********************")
# funciones del modulo de usuario

def mostrarMenuDeUsuario():
    print("****************-Menú-*********************")
    print("")
    print("Bienvenido/a al Modulo de Usuario: ")
    print("")
    print("1. Crear Usuario")
    print("2. Consultar Usuario")
    print("3. Actualizar Datos de Usuario")
    print("4. Eliminar Usuario")
    print("0. Salir")
    print("****************-    -*********************")

def mostrarMenuActualizacionUsuario():
    print("****************-Menú-*********************")
    print("")
    print("1. Actualizar Cédula ")
    print("2. Actualizar Nombre ")
    print("3. Actualizar Correo ")
    print("4. Actualizar Celular ")
    print("0. Salir")
    print("****************-    -*********************")

def pedirDatosUsuario():
  """ 
  La Función permite el ingreso de los datos del Objeto Usuario.

  Parametros:
  cedula (int)
  nombre (str)
  correo (str)
  celular (int)

  Se retornan los datos ingresados.
  """
  cedula=int(input("Ingrese la cedula "))
  nombre=input("Ingrese el nombre ")
  correo=input("Ingrese el correo ")
  celular=int(input("Ingrese el celular "))

  return cedula, nombre, correo, celular    

def autenticarUsuario(cedula,lista):
  global encontrado
  encontrado=False
  for usuario in lista:
    ced=usuario.get_cedula()
    if cedula==ced:
      encontrado=True
      usu=usuario
    else:
     encontrado=False  
  return encontrado,usu

def mostrarMenuDeReservas():
    print("****************-Menú-*********************")
    print("")
    print("Bienvenido/a al Modulo de Reservas: ")
    print("")
    print("1. Crear Reserva")
    print("2. Consultar Reserva")
    print("3. Actualizar Datos de Reserva")
    print("4. Eliminar Reserva")
    print("0. Regresar")
    print("****************-    -*********************")

def mostrarMenuDeLocalidad():
    print("****************-Menú-*********************")
    print("")
    print("Bienvenido/a al Modulo de Localidad: ")
    print("")
    print("1. Crear Localidad")
    print("2. Consultar Localidad")
    print("3. Actualizar Datos de Localidad")
    print("4. Eliminar Localidad")
    print("0. Regresar")
    print("****************-    -*********************")
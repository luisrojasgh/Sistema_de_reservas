class Usuario:
    def __init__(self, cedula,nombre,correo,celular,estado=1) -> None:
        self._cedula=cedula
        self._nombre=nombre
        self._correo=correo
        self._celular=celular
        self._estado=estado
    
    def get_cedula(self):
        return self._cedula
      
    def set_cedula(self, cedula):
        self._cedula = cedula
    
    def get_nombre(self):
        return self._nombre
      
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_correo(self):
        return self._correo
      
    def set_correo(self, correo):
        self._correo = correo

    def get_celular(self):
        return self._celular
      
    def set_celular(self, celular):
        self._celular = celular
    
    def get_estado(self):
        return self._estado
      
    def set_estado(self, estado):
        self._estado = estado
    
    def __str__(self) -> str:
        texto="Cedula: {0} - Nombre: {1} - Correo: {2} - Celular: {3} - Estado: {4}"
        return texto.format(self._cedula,self._nombre,self._correo,self._celular,self._estado)
            
class Reserva:
    def __init__(self, fecha,id,localidad,estado,cantidad) -> None:
        self._fecha=fecha
        self._id=id
        self._localidad=localidad
        self._estado=estado
        self._cantidad=cantidad
    
    def get_fecha(self):
        return self._fecha
      
    def set_fecha(self, fecha):
        self._fecha = fecha
    
    def get_id(self):
        return self._id
      
    def set_id(self, id):
        self._id = id
    
    def get_localidad(self):
        return self._localidad
      
    def set_localidad(self, localidad):
        self._localidad = localidad

    def get_estado(self):
        return self._estado
      
    def set_estado(self, estado):
        self._estado = estado
    
    def get_cantidad(self):
        return self._cantidad
      
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

class Locacion:
    def __init__(self, tipo,aforo) -> None:
        self._tipo=tipo
        self._aforo=aforo
    
    def get_tipo(self):
        return self._tipo
      
    def set_tipo(self, tipo):
        self._tipo = tipo
    
    def get_aforo(self):
        return self._aforo
      
    def set_fecha(self, aforo):
        self._aforo = aforo


from flask import flash
from utils.accesobd import *

class Clientes():
    #Cedula de los clientes
    
    #Metodos
    def setCliente_id(self, cliente_id):
        self.__cliente_id= cliente_id
    def getCliente_id(self):
        return self.__cliente_id
    
    def setNombre(self, nombre):
        self.__nombre= nombre
    def getNombre(self):
        return self.__nombre
    
    def setApellido(self, apellido):
        self.__apellido= apellido
    def getApellido(self):
        return self.__apellido
    
    def setEmail(self, email):
        self.__email= email
    def getEmail(self):
        return self.__email
    
    def setTelefono(self,telefono):
        self.__telefono= telefono
    def getTelefono(self):
        return self.__telefono
    
    def setSQL(self, mysql):
        self.__mysql= mysql
    def getSQL(self):
        return self.__mysql

    def consultar_cliente(self):
        insert = consultarbd('SELECT cliente_id as cedula, nombre, apellido, email, telefono FROM clientes;')
        return insert
    
    def consultar_cliente_id(self):
        sql = 'SELECT cliente_id as cedula, nombre, apellido, email, telefono FROM clientes where cliente_id = {0}'.format(self.getCliente_id())
        data = consultarbd(sql)
        return data[0]

    def insertar_cliente(self):
        sql= 'INSERT INTO clientes (cliente_id, nombre, apellido, email, telefono) VALUES (%s, %s, %s,%s,%s)'
        data = (self.getCliente_id(),self.getNombre(),self.getApellido(),self.getEmail(),self.getTelefono())
        actualizarbd(sql,data)
        flash("Cliente Ingresado!")

    def eliminar_cliente(self):
        sql='DELETE FROM clientes WHERE cliente_id= {0}'.format(self.getCliente_id())
        actualizarbd(sql)
        flash('Cliente Removido!')

    def editar_cliente(self):
        sql='UPDATE clientes SET cliente_id = %s, nombre = %s, apellido=%s, email= %s, telefono=%s WHERE cliente_id ={0}'.format(self.getCliente_id())
        data = (self.getCliente_id(),self.getNombre(),self.getApellido(),self.getEmail(),self.getTelefono())
        actualizarbd(sql,data)
        flash("Cliente Actualizado")

#Pelciulas
class Peliculas():

    def setPelicula_id(self, pelicula_id):
        self.__pelicula_id= pelicula_id
    def getPelciula_id(self):
        return self.__pelicula_id

    def setTitulo(self, titulo):
        self.__titulo= titulo
    def getTitulo(self):
        return self.__titulo
    
    def setGenero(self, genero):
        self.__genero= genero
    def getGenero(self):
        return self.__genero
    
    def setDuracion(self, duracion):
        self.__duracion= duracion
    def getDuracion(self):
        return self.__duracion
    
    def setClasificacion(self, clasificacion):
        self.__clasificacion = clasificacion
    def getClasificacion(self):
        return self.__clasificacion
    
    def setImg(self, img):
        self.__img=img
    def getImg(self):
        return self.__img
    
    def setSipnosis(self,sipnosis):
        self.__sipnosis= sipnosis
    def getSipnosis(self):
        return self.__sipnosis
    
    def consultar_pelicula(self):
        insert = consultarbd('SELECT * FROM peliculas p;')
        
        return insert
    
    def insertar_pelicula(self):
        sql= 'CALL InsertarNuevaPelicula(%s, %s, %s, %s, %s, %s);'
        data = (self.getTitulo(),self.getGenero(),self.getDuracion(),self.getClasificacion(),self.getImg(), self.getSipnosis())
        actualizarbd(sql,data)
        flash("Pelicula Insertada!")

    def consultar_pelicula_id(self):
        sql = 'SELECT * FROM peliculas where pelicula_id = {0}'.format(self.getPelciula_id())
        data = consultarbd(sql)
        return data[0]    
    
    def eliminar_pelicula(self):
        sql='DELETE FROM peliculas WHERE pelicula_id= {0}'.format(self.getPelciula_id())
        actualizarbd(sql)
        flash('Pelicula Removida!')

    def editar_pelicula(self):
        sql='UPDATE pelicla SET pelicula_id = %s, titulo = %s, genero=%s, duracion= %s, clasificacion=%s, img=%s, sipnosis=%s WHERE pelicula_id ={0}'.format(self.getPelciula_id())
        data = (self.getCliente_id(),self.getNombre(),self.getApellido(),self.getEmail(),self.getTelefono())
        actualizarbd(sql,data)
        flash("Pelicula Actualizada")

class Salas():
    
    def setSala_id(self,sala_id):
        self.__sala_id=sala_id
    def getSala_id(self):
        return self.__sala_id
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def setCapacidad(self, capacidad):
        self.__capacidad=capacidad

    def getCapacidad(self):
        return self.__capacidad

    def insertar_sala(self):
        sql= 'CALL InsertarNuevaSala(%s, %s);'
        data = (self.getnombre(),self.getcapacidad())
        actualizarbd(sql,data)
        flash("Sala Ingresada!")

    def eliminar_salas(self):
        sql='DELETE FROM salas WHERE sala_id= {0}'.format(self.getSala_id())
        actualizarbd(sql)
        flash('Sala Removido!')
    
    def consultar_salas(self):
        insert = consultarbd('SELECT * FROM salas s;')
        return insert
    def consultar_sala_id(self):
        sql = 'SELECT * FROM salas where sala_id = {0}'.format(self.getSala_id())
        data = consultarbd(sql)
        return data[0] 
    def editar_sala(self):
        sql='UPDATE salas SET sala_id = %s, nombre = %s, capacidad=%s WHERE sala_id ={0}'.format(self.getSala_id())
        data = (self.getSala_id(),self.getNombre(),self.getCapacidad())
        actualizarbd(sql,data)
        flash("Sala Actualizada")
    
# funciones
class Funciones():
    def setFuncion_id(self, funcion_id):
        self.__funcion_id=funcion_id
    def getFuncion_id(self):
        return self.__funcion_id
    
    def setPelicula_id(self, pelicula_id):
        self.__pelicula_id= pelicula_id
    def getPelciula_id(self):
        return self.__pelicula_id
    
    def setSala_id(self,sala_id):
        self.__sala_id=sala_id
    def getSala_id(self):
        return self.__sala_id
    
    def setFecha_hora(self, fecha_hora):
        self.__fecha_hora=fecha_hora
    def getFecha_hora(self):
        return self.__fecha_hora
    
    def setDisponible(self, disponible):
        self.__disponible= disponible
    def getDisponible(self):
        return self.__disponible
    
    def insert_funcion(self):
        sql = 'CALL InsertarNuevaFuncion (%s, %s, %s);'
        data =(self.getPelciula_id(),self.getSala_id(),self.getFecha_hora())
        actualizarbd(sql,data)
        flash("Funcion Ingresada!")
    

    def eliminar_funciones(self):
        sql='DELETE FROM funciones WHERE funcion_id= {0}'.format(self.getFuncion_id())
        actualizarbd(sql)
        flash('Funcion Removida!')
    
    def consultar_funciones(self):
        insert = consultarbd('SELECT funciones.funcion_id, funciones.pelicula_id , peliculas.titulo , funciones.sala_id , salas.nombre, funciones.fecha_hora, funciones.disponible FROM funciones join peliculas on funciones.pelicula_id=peliculas.pelicula_id join salas on funciones.sala_id=salas.sala_id;')
        return insert
    
    def consultar_funcion_id(self):
        sql = 'SELECT funciones.funcion_id, funciones.pelicula_id , peliculas.titulo , funciones.sala_id , salas.nombre, funciones.fecha_hora, funciones.disponible FROM funciones join peliculas on funciones.pelicula_id=peliculas.pelicula_id join salas on funciones.sala_id=salas.sala_id where funcion_id = {0}'.format(self.getFuncion_id())
        data = consultarbd(sql)
        return data[0] 
    def editar_funcion(self):
        sql='UPDATE funciones SET funcion_id = %s, pelicula_id = %s, sala_id=%s, fecha_hora= %s WHERE funcion_id ={0}'.format(self.getFuncion_id())
        data = (self.getFuncion_id(),self.getPelciula_id(),self.getSala_id(),self.getFecha_hora())
        actualizarbd(sql,data)
        flash("Funcion Actualizada")
    
# reservas
class Reservas():
    def setReservas_id(self, reserva_id):
         self.__reserva_id=reserva_id
    def getReservas_id(self):
        return self.__reserva_id
    
    def setFuncion_id(self, funcion_id):
        self.__funcion_id=funcion_id
    def getFuncion_id(self):
        return self.__funcion_id
    
    def setCliente_id(self, cliente_id):
        self.__cliente_id= cliente_id
    def getCliente_id(self):
        return self.__cliente_id
    
    def setCantidad_tickets(self, cantidad_tickets):
        self.__cantidad_tickets=cantidad_tickets
    def getCantidad_tickets(self):
        return self.__cantidad_tickets
    
    def insertar_reserva(self):
        sql= 'CALL InsertarNuevaReserva(%s, %s, %s);'
        data = (self.getFuncion_id(),self.getCliente_id(),self.getCantidad_tickets())
        actualizarbd(sql,data)
        flash("Reserva Ingresada!")
    
    def eliminar_reserva(self):
        sql='DELETE FROM reservas WHERE reserva_id= {0}'.format(self.getReservas_id())
        actualizarbd(sql)
        flash('Reserva Removida!')

    def consultar_reservas(self):
        insert = consultarbd('SELECT reservas.reserva_id,reservas.funcion_id,peliculas.titulo,funciones.fecha_hora ,clientes.cliente_id ,clientes.nombre ,reservas.cantidad_tickets  FROM reservas INNER JOIN clientes ON reservas.cliente_id = clientes.cliente_id join funciones on reservas.funcion_id=funciones.funcion_id join peliculas on funciones.pelicula_id=peliculas.pelicula_id;')
        return insert
    
    def consultar_reserva_id(self):
        sql = 'SELECT * FROM reservas where reserva_id = {0}'.format(self.getReservas_id())
        data = consultarbd(sql)
        return data[0] 
    def editar_reserva(self):
        sql='UPDATE reservas SET reserva_id = %s, funcion_id = %s, cliente_id=%s, cantidad_tickets= %s WHERE reserva_id ={0}'.format(self.getReservas_id())
        data = (self.getReservas_id(),self.getFuncion_id(),self.getCliente_id(),self.getCantidad_tickets())
        actualizarbd(sql,data)
        flash("Reserva Actualizada")

    
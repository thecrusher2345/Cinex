from flask import Blueprint, redirect, render_template, flash, url_for, request, jsonify
from models.cinexs import *
from utils.utils import *



cliente=Clientes()
pelicula = Peliculas()
sala=Salas()
funcion=Funciones()
reserva=Reservas()
cinex= Blueprint('cinex', __name__)

@cinex.route('/')
def Index():
    result = pelicula.consultar_pelicula()
    resultf = funcion.consultar_funciones()
    return render_template('index.html', peliculas = result ,Funciones= resultf)

#Cliente

@cinex.route('/cliente')
def Cliente():
    result = cliente.consultar_cliente()
    return render_template('clientes.html', clientes = result)

@cinex.route('/cliente/json/<string:id>')
def jsonCliente(id):
    cliente.setCliente_id(id)
    result = cliente.consultar_cliente_id()
    print(result)
    result = jsonify(result)
    return result
    

@cinex.route('/add_cliente', methods = ['POST'])
def add_cliente():
    try:
        if request.method == 'POST':
            cliente.setCliente_id(request.form['cliente_id'])
            cliente.setNombre(request.form['nombre'])
            cliente.setApellido(request.form['apellido'])
            cliente.setEmail(request.form['email'])
            cliente.setTelefono(request.form['telefono'])
            cliente.insertar_cliente()
            return redirect(url_for('cinex.Cliente'))
    except Exception as e:
        raise e
    
@cinex.route('/cliente/update/<id>', methods = ['POST'])
def update(id):
    try:
        if request.method == 'POST':
            cliente.setCliente_id(id)
            cliente.setCliente_id(request.form['cliente_id'])
            cliente.setNombre(request.form['nombre'])
            cliente.setApellido(request.form['apellido'])
            cliente.setEmail(request.form['email'])
            cliente.setTelefono(request.form['telefono'])
            cliente.editar_cliente()
            return redirect(url_for('cinex.Cliente'))
    except Exception as e:
        raise e

@cinex.route('/delete_cliente/<string:cliente_id>')
def delete_cliente(cliente_id):
    cliente.setCliente_id(cliente_id)
    cliente.eliminar_cliente()
    return redirect(url_for('cinex.Cliente'))

#Peliculas
@cinex.route('/pelicula')
def Pelicula():
    result = pelicula.consultar_pelicula()
    return render_template('peliculas.html', peliculas = result)

@cinex.route('/add_pelicula', methods = ['POST'])
def add_pelicula():
    try:
        if request.method == 'POST':
            pelicula.setTitulo(request.form['titulo'])
            pelicula.setGenero(request.form['genero'])
            pelicula.setDuracion(request.form['duracion'])
            pelicula.setClasificacion(request.form['clasificacion'])
            imagen = guardar_archivo_upload(request.files['img'])
            pelicula.setImg(imagen)
            pelicula.setSipnosis(request.form['sipnosis'])
            pelicula.insertar_pelicula()
            return redirect(url_for('cinex.Pelicula'))
    except Exception as e:
        raise e

@cinex.route('/pelicula/json/<string:id>')
def jsonPelicula(id):
    pelicula.setPelicula_id(id)
    result = pelicula.consultar_pelicula_id()
    print(result)
    result = jsonify(result)
    return result

@cinex.route('/pelicula/update/<id>', methods = ['POST'])
def update_pelicula(id):
    try:
        if request.method == 'POST':
            pelicula.setPelicula_id(id)
            pelicula.setPelicula_id(request.form['pelicula_id'])
            pelicula.setTitulo(request.form['titulo'])
            pelicula.setGenero(request.form['genero'])
            pelicula.setDuracion(request.form['duracion'])
            pelicula.setClasificacion(request.form['clasificacion'])
            imagen = guardar_archivo_upload(request.files['img'])
            pelicula.setImg(imagen)
            pelicula.setSipnosis(request.form['sipnosis'])
            pelicula.editar_pelicula
            print(pelicula.getPelciula_id())
            return redirect(url_for('cinex.Pelicula'))
    except Exception as e:
        raise e

@cinex.route('/delete_pelicula/<string:pelicula_id>')
def delete_pelicula(pelicula_id):
    pelicula.setPelicula_id(pelicula_id)
    pelicula.eliminar_pelicula()
    return redirect(url_for('cinex.Pelicula'))

#salas
# RUTA CONSULTA SALA
@cinex.route('/salas')
def Salas():
    result= sala.consultar_salas()
    return render_template('salas.html', salas = result)

# RUTA AÑADE SALAS
@cinex.route('/add_salas', methods= ['POST'])
def add_salas():
    try:
        if request.method == 'POST':
            sala.setnombre(request.form['nombre'])
            sala.setcapacidad(request.form['capacidad'])
            sala.insertar_sala()
            return redirect(url_for('cinex.Salas'))
    except Exception as e:
        raise e

# RUTA ELIMINA SALAS
@cinex.route('/delete_salas/<string:sala_id>')
def delete_salas(sala_id):
    sala.setSala_id(sala_id)
    sala.eliminar_salas()
    return redirect(url_for('cinex.Salas'))
    
@cinex.route('/sala/json/<string:id>')
def jsonSala(id):
    sala.setSala_id(id)
    result = sala.consultar_sala_id()
    print(result)
    result = jsonify(result)
    return result

@cinex.route('/sala/update/<id>', methods = ['POST'])
def update_sala(id):
    try:
        if request.method == 'POST':
            sala.setNombre(request.form['nombre'])
            sala.setCapacidad(request.form['capacidad'])
            sala.editar_sala()
            return redirect(url_for('cinex.Salas'))
    except Exception as e:
        raise e
# FUNCIONES
# RUTA CONSUTA FUNCION
@cinex.route('/funciones')
def Funciones():
    result= funcion.consultar_funciones()
    resultp = pelicula.consultar_pelicula()
    results= sala.consultar_salas()

    return render_template('funciones.html', Funciones = result, Peliculas = resultp, Salas = results)


@cinex.route('/add_funcion', methods= ['POST'])
def add_funciones():
    try:
        if request.method == 'POST':
  
            funcion.setPelicula_id(request.form['pelicula_id'])
            funcion.setSala_id(request.form['sala_id'])
            funcion.setFecha_hora(request.form['fecha_hora'])
            funcion.insert_funcion()
            return redirect(url_for('cinex.Funciones'))
    except Exception as e:
        raise e
    
@cinex.route('/delete_funcion/<string:funcion_id>')
def delete_funcion(funcion_id):
    funcion.setFuncion_id(funcion_id)
    funcion.eliminar_funciones()
    return redirect(url_for('cinex.Funciones'))

@cinex.route('/funcion/json/<string:funcion_id>')
def jsonFuncion(funcion_id):
    funcion.setFuncion_id(funcion_id)
    result = funcion.consultar_funcion_id()
    print(result)
    result = jsonify(result)
    return result
@cinex.route('/funcion/update/<funcion_id>', methods = ['POST'])
def update_funcion(funcion_id):
    try:
        if request.method == 'POST':
            funcion.setFuncion_id(funcion_id)
            funcion.setFuncion_id(request.form['funcion_id'])
            funcion.setPelicula_id(request.form['pelicula_id'])
            funcion.setSala_id(request.form['sala_id'])
            funcion.setFecha_hora(request.form['fecha_hora'])
            
            funcion.editar_funcion()
            print(funcion.getFuncion_id())
            return redirect(url_for('cinex.Funciones'))
    except Exception as e:
        raise e
        
# Reservas
@cinex.route('/reservas')
def  Reservas():
    result = reserva.consultar_reservas()
    resultf = funcion.consultar_funciones()
    resultc= cliente.consultar_cliente()
    return render_template('reservas.html', reservas = result, Funciones = resultf, Clientes=resultc)

@cinex.route('/add_reservas', methods = ['POST'])
def add_reservas():
    try:
        if request.method == 'POST':
            reserva.setFuncion_id(request.form['funcion_id'])
            reserva.setCliente_id(request.form['cliente_id'])
            reserva.setCantidad_tickets(request.form['cantidad_tickets'])
            reserva.insertar_reserva()
            return redirect(url_for('cinex.Reservas'))
    except Exception as e:
        raise e

@cinex.route('/delete_reserva/<string:reserva_id>')
def delete_reserva(reserva_id):
    reserva.setReservas_id(reserva_id)
    reserva.eliminar_reserva()
    return redirect(url_for('cinex.Reservas'))

@cinex.route('/reserva/json/<string:reserva_id>')
def jsonReserva(reserva_id):
    reserva.setReservas_id(reserva_id)
    result = reserva.consultar_reserva_id()
    print(result)
    result = jsonify(result)
    return result
@cinex.route('/reserva/update/<funcion_id>', methods = ['POST'])
def update_reserva(funcion_id):
    try:
        if request.method == 'POST':
            reserva.setReservas_id(funcion_id)
            reserva.setFuncion_id(request.form['funcion_id'])
            reserva.setCliente_id(request.form['cliente_id'])
            reserva.setCantidad_tickets(request.form['cantidad_tickets'])
            
            reserva.editar_reserva()
            return redirect(url_for('cinex.Reservas'))
    except Exception as e:
        raise e
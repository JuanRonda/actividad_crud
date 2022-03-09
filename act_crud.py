import pymysql
'''
Realiza conexion a la base de datos
'''
def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='SQL_PRUEBAS')

''' Insertar un nuevo USUARIO '''
def insertar_usuario(username, firstname, lastname, gender):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO user_details(username, first_name, last_name, gender) VALUES (%s, %s, %s, %s)",
                       (username, firstname, lastname, gender))
    conexion.commit()
    conexion.close()

''' Obtiene un listado de los USUARIOS '''
def obtener_usuarios():
    conexion = obtener_conexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT username,first_name, last_name, gender FROM user_details")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios

''' Elimina un USUARIO dado un ID '''
def eliminar_usuario(user_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM user_details WHERE user_id = %s", (user_id,))
    conexion.commit()
    conexion.close()
    
''' Obtiene un USUARIO dado una ID '''
def obtener_usuario_por_id(user_id):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT user_id, first_name, last_name, gender FROM user_details WHERE user_id = %s", (id,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

''' Actualiza un USUARIO dado una ID '''
def actualizar_usuario(username, firstname, lastname, gender, user_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE user_details SET username = %s, first_name = %s, last_name = %s, gender = %s WHERE user_id = %s",
                       (username, firstname, lastname, gender, user_id))
    conexion.commit()
    conexion.close()

''' Devuelve el total de los REGISTROS '''
def obtener_total_registros():
    conexion = obtner_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(" SELECT COUNT(username) FROM user_details ")
    conexion.close()
    return usuario

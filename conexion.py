import mysql.connector
from mysql.connector import errorcode

dic_conexion_db = {
    'user':'root',
    'password':'root',
    'host':'localhost',
    'database':'clinica'    
}

class Conexion:
    
    def conectar(self):
        try:
            conexion = mysql.connector.connect(user=dic_conexion_db.get('user'),
                                                password=dic_conexion_db.get('password'),
                                                host=dic_conexion_db.get('host'),
                                                database=dic_conexion_db.get('database'))
            print("Se conecto OK a la Base de datos: {}".format(dic_conexion_db.get('database')))
            return conexion
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error al Conectar a la DB: {}".format(dic_conexion_db.get('database')))
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de datos no existente {}".format(dic_conexion_db.get('database')))
            else:
                print(err)
            return None
    
    def CerrarConexion(self,conexion):
        print("Cerrando conexion con {}".format(dic_conexion_db.get('database')))
        conexion.close()
        print("Conexion cerrada con {}".format(dic_conexion_db.get('database')))
        


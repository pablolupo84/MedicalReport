from conexion import *
import time
from datetime import date
#Sesiones
class Sesiones(Conexion):

    def Insertar(self,id_paciente,data):
        lista=[id_paciente,]
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""INSERT INTO clinica.sesiones (id_p,fecha) VALUES (%s,%s)"""
            lista.append(data)
            cursor.execute(sql_qry,lista)
            cnx.commit()
            print("Record inserted successfully into clinica.sesiones table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to insert data into clinica.sesiones table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)


    #FALTA CREAR UN MODIFICAR POR SESION
    def Modificar(self,id_paciente,data):
            lista=[data,]
            try:    
                cnx=self.Conectar()
                cursor = cnx.cursor()
                sql_qry="""UPDATE clinica.sesiones SET fecha=%s WHERE id_p = %s"""
                lista.append(id_paciente)
                cursor.execute(sql_qry,lista)
                cnx.commit()
                print("Record Update successfully into clinica.sesiones table")
            except Exception as err:
                print("Error: {}".format(err))
                print("Failed to Update data into clinica.sesiones table")
            finally:
                if (cnx):
                    self.CerrarConexion(cnx)

    def EliminarTodas(self,id_paciente):
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""DELETE FROM clinica.sesiones WHERE id_p = %s"""
            cursor.execute(sql_qry,(id_paciente,))
            cnx.commit()
            print("Record Deleted successfully into clinica.sesiones table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Deleted data into clinica.sesiones table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)

    def EliminarSesion(self,id_paciente,data):
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""DELETE FROM clinica.sesiones WHERE id_p = %s AND fecha=%s"""
            cursor.execute(sql_qry,(id_paciente,data,))
            cnx.commit()
            print("Record Deleted successfully into clinica.sesiones table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Deleted data into clinica.sesiones table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)

    def BuscarSesion_Dni(self,dni):
        personasPorDni=None
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""SELECT id FROM clinica.paciente WHERE dni = %s"""
            cursor.execute(sql_qry,(dni,))
            personasPorDni = cursor.fetchall()
            print("Record Select successfully into clinica.paciente table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Select data into clinica.paciente table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return personasPorDni

    def BuscarporID(self,id_paciente):
        personasPorDni=[]
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""SELECT * FROM clinica.sesiones WHERE id_p = %s"""
            cursor.execute(sql_qry,(id_paciente,))
            personasPorDni = cursor.fetchall()
            print("Record Select successfully into clinica.sesiones table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Select data into clinica.sesiones table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return personasPorDni



# test=Sesiones()
# print(date.today())
# test.Insertar(3,date.today())
# test.Modificar(2,date.today())
# print(test.BuscarporID(3))
# print(test.BuscarId_Dni("87654321T"))
# test.EliminarTodas(3)
# test.EliminarSesion(3,date.today())
from conexion import *
import time
from datetime import date

#Sesiones
class Sesiones(Conexion):

    def Insertar(self,id_paciente,data):
        resultado=True
        print("------------Insertar-----------")
        lista=[id_paciente,data[0],data[1]]
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""INSERT INTO clinica.sesiones (id_p,fecha,pagado) VALUES (%s,%s,%s)"""
            print("Dta a insertar ens esion {}".format(lista))
            cursor.execute(sql_qry,lista)
            cnx.commit()
            print("Record inserted successfully into clinica.sesiones table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to insert data into clinica.sesiones table")
            resultado=False
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return resultado

    def Modificar(self,id_paciente,data_old,data_new):
        resultado=True
        lista=(data_new[0],data_new[1],id_paciente,data_old[1],data_old[2])
        print("Modificar: {}".format(lista))
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""UPDATE clinica.sesiones SET fecha=%s,pagado=%s WHERE id_p = %s and fecha=%s and pagado=%s"""
            
            cursor.execute(sql_qry,lista)
            cnx.commit()
            print("Record Update successfully into clinica.sesiones table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Update data into clinica.sesiones table")
            resultado=False
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return resultado

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
        data_delete=(id_paciente,data[1],data[2])
        print("se borrara: {}".format(data_delete))
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""DELETE FROM clinica.sesiones WHERE id_p = %s AND fecha=%s AND pagado=%s"""
            cursor.execute(sql_qry,data_delete)
            cnx.commit()
            print("Record Deleted successfully into clinica.sesiones table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Deleted data into clinica.sesiones table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)

    def BuscarTodosSesiones(self):
        print("------------BuscarTodos Sesiones-----------")
        lista=[]
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""SELECT * FROM clinica.sesiones"""
            cursor.execute(sql_qry)
            lista = cursor.fetchall()

            print("Record Select successfully into clinica.sesiones table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Select data into clinica.sesiones table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return lista

    def BuscarporID(self,id_paciente):
        """La funcion retorna una tupla con los datos de 
        pacientes segun dni, sino retorna una tupla vacia"""
        print("------------BuscarporID-----------")
        personasPorDni=()
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
                # print(personasPorDni)
                return personasPorDni
                
    def BuscarporDni(self,dni):
        """La funcion retorna una tupla con los datos de 
        pacientes segun dni, sino retorna una tupla vacia"""
        print("------------BuscarporDni-----------")
        sesiones=()
        personasPorDni=()
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""SELECT * FROM clinica.paciente WHERE dni = %s"""
            cursor.execute(sql_qry,(dni,))
            personasPorDni = cursor.fetchone()
            # print(personasPorDni)
            sesiones=self.BuscarporID(personasPorDni[0])
            print("Sesiones {}".format(sesiones))
            print("Record Select successfully into clinica.paciente table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Select data into clinica.paciente table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return sesiones,personasPorDni

    def BuscarporFecha(self,fecha):
        """La funcion retorna una tupla con los datos de 
        pacientes segun dni, sino retorna una tupla vacia"""
        print("------------BuscarporFecha-----------")
        print("fECHA:{}".format(fecha))
        sesiones=()
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""SELECT * FROM clinica.sesiones WHERE fecha = %s"""
            cursor.execute(sql_qry,(fecha,))
            sesiones = cursor.fetchall()
            # print(personasPorDni)
            print("Sesiones {}".format(sesiones))
            print("Record Select successfully into clinica.sesiones table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Select data into clinica.sesiones table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return sesiones

# test=Sesiones()
# print(date.today())
# test.Insertar(3,date(2020, 6, 24))
# test.Insertar(4,date(2019, 7, 4))
# test.Insertar(5,date(2018, 1, 28))
# test.Insertar(5,date(2018, 2, 28))
# test.Insertar(5,date(2018, 3, 28))
# test.Modificar(1,date(2020, 4, 27),date(1984, 11, 17))

# print(test.BuscarporID(3))
# print(test.BuscarId_Dni("87654321T"))
# test.EliminarTodas(3)
# test.EliminarSesion(3,date.today())
# print(test.BuscarporFecha(date(2020,5,12)))
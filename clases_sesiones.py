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

    def Modificar(self,id_paciente,data,data_new):
            lista=[data_new,]
            try:    
                cnx=self.Conectar()
                cursor = cnx.cursor()
                sql_qry="""UPDATE clinica.sesiones SET fecha=%s WHERE id_p = %s AND fecha=%s"""
                lista.append(id_paciente)
                lista.append(data)
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
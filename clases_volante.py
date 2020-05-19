from conexion import *

#Volantes
class Volantes(Conexion):

    def InsertarVolantes(self,id_paciente,data):
        resultado=True
        print("------------Insertar Volante-----------")
        lista=[id_paciente,data[0],data[1],data[2],data[3],data[4]]
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""INSERT INTO clinica.volante (id_paciente,tipo,volante,
            patologia,tratamiento,total) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql_qry,lista)
            cnx.commit()
            print("Record inserted successfully into clinica.volante table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to insert data into clinica.volante table")
            resultado=False
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return resultado

    def ModificarVolantes(self,id_paciente,data_old,data_new):
     
        try: 
            print("------------Modificar Volantes-----------")
            resultado=True
            lista=(data_new[0],data_new[1],data_new[2],data_new[3],id_paciente,data_old[1],data_old[2],data_old[3],data_old[4])
            print("Modificar: {}".format(lista))   
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""UPDATE clinica.volante SET tipo=%s,volante=%s,patologia=%s,tratamiento=%s WHERE id_paciente = %s AND tipo=%s AND volante=%s AND patologia=%s AND tratamiento=%s"""
            cursor.execute(sql_qry,lista)
            cnx.commit()
            print("Record Update successfully into clinica.volante table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Update data into clinica.volante table")
            resultado=False
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return resultado


    def EliminarTodos(self,id_paciente):
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""DELETE FROM clinica.volante WHERE id_paciente = %s"""
            cursor.execute(sql_qry,(id_paciente,))
            cnx.commit()
            print("Record Deleted successfully into clinica.volante table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Deleted data into clinica.volante table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)

    def EliminarVolante(self,id_paciente,data):
        data_delete=(id_paciente,data[1],data[2],data[3],data[4],data[5])
        print("se borrara: {}".format(data_delete))
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""DELETE FROM clinica.volante WHERE id_paciente = %s AND tipo=%s AND volante=%s AND patologia=%s AND tratamiento=%s AND total=%s"""
            cursor.execute(sql_qry,data_delete)
            cnx.commit()
            print("Record Deleted successfully into clinica.volante table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Deleted data into clinica.volante table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)

    def BuscarTodosVolantes(self):
        print("------------BuscarTodos Volantes-----------")
        lista=[]
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""SELECT * FROM clinica.volante"""
            cursor.execute(sql_qry)
            lista = cursor.fetchall()

            print("Record Select successfully into clinica.volante table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Select data into clinica.volante table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return lista

    def BuscarporIDVolante(self,id_paciente):
        """La funcion retorna una tupla con los datos de 
        pacientes segun dni, sino retorna una tupla vacia"""
        print("------------BuscarporID Volante-----------")
        personasPorDni=()
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""SELECT * FROM clinica.volante WHERE id_paciente = %s"""
            cursor.execute(sql_qry,(id_paciente,))
            personasPorDni = cursor.fetchall()
            print("Record Select successfully into clinica.volante table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Select data into clinica.volante table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return personasPorDni



# test=Volantes()
# data=['Particular', 20, "assa","asasas", 2]
# test.InsertarVolantes(1,data)
# test.Modificar(4,"Cardiopatologia")
# print(test.BuscarporID(4))
# print(test.BuscarId_Dni("87654321T"))
# test.EliminarTodos(4,)
# test.EliminarAntecedente(10,"ACV")
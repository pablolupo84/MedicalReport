from conexion import *

#Antecedentes
class Antecedentes(Conexion):

    def InsertarAntecedente(self,id_paciente,data):
        resultado=True
        print("------------Insertar Antecedente-----------")
        lista=[id_paciente,data]
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""INSERT INTO clinica.antecedentes (id_paciente,Enfermedades) VALUES (%s,%s)"""
            print("Dta a insertar ens esion {}".format(lista))
            cursor.execute(sql_qry,lista)
            cnx.commit()
            print("Record inserted successfully into clinica.antecedentes table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to insert data into clinica.antecedentes table")
            resultado=False
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return resultado

    def ModificarAntecedente(self,id_paciente,data_old,data_new):
        resultado=True
        print("------------Modificar Antecedente-----------")
        lista=(data_new,id_paciente,data_old[1])
        print("Modificar: {}".format(lista))
        
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""UPDATE clinica.antecedentes SET Enfermedades=%s WHERE id_paciente = %s and Enfermedades=%s"""
            cursor.execute(sql_qry,lista)
            cnx.commit()
            print("Record Update successfully into clinica.antecedentes table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Update data into clinica.antecedentes table")
            resultado=False
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return resultado

    def EliminarTodosAntecedentes(self,id_paciente):
        print("------------EliminarTodos Antecedentes-----------")
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""DELETE FROM clinica.antecedentes WHERE id_paciente = %s"""
            cursor.execute(sql_qry,(id_paciente,))
            cnx.commit()
            print("Record Deleted successfully into clinica.antecedentes table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Deleted data into clinica.antecedentes table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)

    def EliminarAntecedente(self,id_paciente,data):
        print("------------Eliminar Antecedentes-----------")
        data_delete=(id_paciente,data[1])
        print("se borrara: {}".format(data_delete))
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""DELETE FROM clinica.antecedentes WHERE id_paciente = %s AND Enfermedades=%s"""
            cursor.execute(sql_qry,data_delete)
            cnx.commit()
            print("Record Deleted successfully into clinica.antecedentes table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Deleted data into clinica.antecedentes table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)

    def BuscarTodosAntecedentes(self):
        print("------------BuscarTodos Antecedentes-----------")
        lista=[]
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""SELECT * FROM clinica.antecedentes"""
            cursor.execute(sql_qry)
            lista = cursor.fetchall()

            print("Record Select successfully into clinica.antecedentes table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Select data into clinica.antecedentes table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return lista

    def BuscarporIDAntecedente(self,id_paciente):
        """La funcion retorna una tupla con los datos de 
        pacientes segun dni, sino retorna una tupla vacia"""
        print("------------BuscarporID Antecedente-----------")
        personasPorID=()
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""SELECT * FROM clinica.antecedentes WHERE id_paciente = %s"""
            cursor.execute(sql_qry,(id_paciente,))
            personasPorID = cursor.fetchall()
            print("Record Select successfully into clinica.antecedentes table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Select data into clinica.antecedentes table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                # print(personasPorDni)
                return personasPorID
                
    def BuscarporDniAntecedente(self,dni):
        """La funcion retorna una tupla con los datos de 
        pacientes segun dni, sino retorna una tupla vacia"""
        print("------------BuscarporDni Antecedente-----------")
        antecedentes=()
        personasPorDni=()
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""SELECT * FROM clinica.paciente WHERE dni = %s"""
            cursor.execute(sql_qry,(dni,))
            personasPorDni = cursor.fetchone()
            # print(personasPorDni)
            antecedentes=self.BuscarporID(personasPorDni[0])
            print("Sesiones {}".format(antecedentes))
            print("Record Select successfully into clinica.paciente table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Select data into clinica.paciente table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return antecedentes,personasPorDni

# test=Antecedentes()
# test.Insertar(4,"carga esquiotibilaes")
# test.Modificar(4,"Cardiopatologia")
# print(test.BuscarporID(4))
# print(test.BuscarId_Dni("87654321T"))
# test.EliminarTodos(10,)
# test.EliminarAntecedente(10,"ACV")
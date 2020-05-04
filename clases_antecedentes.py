from conexion import *

#Antecedentes
class Antecedentes(Conexion):

    def Insertar(self,id_paciente,data):
        lista=[id_paciente,]
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""INSERT INTO clinica.antecedentes (id_paciente,Enfermedades) VALUES (%s,%s)"""
            lista.append(data)
            cursor.execute(sql_qry,lista)
            cnx.commit()
            print("Record inserted successfully into clinica.antecedentes table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to insert data into clinica.antecedentes table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)

    def Modificar(self,id_paciente,data):
            lista=[data,]
            try:    
                cnx=self.Conectar()
                cursor = cnx.cursor()
                sql_qry="""UPDATE clinica.antecedentes SET Enfermedades=%s WHERE id_paciente = %s"""
                lista.append(id_paciente)
                cursor.execute(sql_qry,lista)
                cnx.commit()
                print("Record Update successfully into clinica.antecedentes table")
            except Exception as err:
                print("Error: {}".format(err))
                print("Failed to Update data into clinica.antecedentes table")
            finally:
                if (cnx):
                    self.CerrarConexion(cnx)

    def EliminarTodos(self,id_paciente):
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
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""DELETE FROM clinica.antecedentes WHERE id_paciente = %s AND Enfermedades=%s"""
            cursor.execute(sql_qry,(id_paciente,data,))
            cnx.commit()
            print("Record Deleted successfully into clinica.antecedentes table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Deleted data into clinica.antecedentes table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)

    def BuscarId_Dni(self,dni):
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
            sql_qry="""SELECT * FROM clinica.antecedentes WHERE id_paciente = %s"""
            cursor.execute(sql_qry,(id_paciente,))
            personasPorDni = cursor.fetchall()
            print("Record Select successfully into clinica.antecedentes table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Select data into clinica.antecedentes table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)
                return personasPorDni


# test=Antecedentes()
# test.Insertar(4,"carga esquiotibilaes")
# test.Modificar(4,"Cardiopatologia")
# print(test.BuscarporID(4))
# print(test.BuscarId_Dni("87654321T"))
# test.EliminarTodos(4,)
# test.EliminarAntecedente(10,"ACV")
from conexion import *

#Pacientes
class Pacientes(Conexion):

    def Insertar(self,data):
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""INSERT INTO clinica.paciente (nombre,apellidos,
            dni,telefono,direccion,edad) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql_qry,data)
            cnx.commit()
            print("Record inserted successfully into clinica.paciente table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to insert data into clinica.paciente table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)

    def Modificar(self,data,id_paciente):
            try:    
                cnx=self.Conectar()
                cursor = cnx.cursor()
                sql_qry="""UPDATE clinica.paciente SET nombre=%s,apellidos=%s,dni=%s,telefono=%s,
                        direccion=%s,edad=%s WHERE id = %s"""
                data.append(id_paciente)
                cursor.execute(sql_qry,data)
                cnx.commit()
                print("Record Update successfully into clinica.paciente table")
            except Exception as err:
                print("Error: {}".format(err))
                print("Failed to Update data into clinica.paciente table")
            finally:
                if (cnx):
                    self.CerrarConexion(cnx)

    def Eliminar(self,id_paciente):
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""DELETE FROM clinica.paciente WHERE id = %s"""
            cursor.execute(sql_qry,(id_paciente,))
            cnx.commit()
            print("Record Deleted successfully into clinica.paciente table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to Deleted data into clinica.paciente table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)

    def BuscarporDni(self,dni):
        personasPorDni=[]
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""SELECT * FROM clinica.paciente WHERE dni = %s"""
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


# test=Pacientes()
# data=['Pablo', 'lONDRES', '31258793', 11319988, '1 DE MAYO 5343', 35]
# test.Insertar(data)
# test.Modificar(data,14)
# test.Eliminar(14) 
# print(test.BuscarporDni(str(31258798)))


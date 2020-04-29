from conexion import *

#Pacientes
class Pacientes(Conexion):

    def insertar(self,data):
        try:    
            cnx=self.conectar()
            cursor = cnx.cursor()
            sql_qry="""INSERT INTO clinica.paciente (nombre,apellidos,
            dni,telefono,direccion,edad) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql_qry,data)
            cnx.commit()
            print("Record inserted successfully into clinica.paciente table")
        except:
            print("Failed to insert data into clinica.paciente table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)

test=Pacientes()
data=['Pablo', 'LOPEZ', '31258793', 11319988, '1 DE MAYO 5343', 35]
test.insertar(data)

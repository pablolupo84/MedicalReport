from conexion import *

#Volantes
class Volantes(Conexion):

    def Insertar(self,id_paciente,data):
        lista=[id_paciente,]
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""INSERT INTO clinica.volante (id_paciente,tipo,volante,
            patologia,tratamiento,total) VALUES (%s,%s,%s,%s,%s,%s)"""
            lista.append(data)
            cursor.execute(sql_qry,lista)
            cnx.commit()
            print("Record inserted successfully into clinica.volante table")
        except Exception as err:
            print("Error: {}".format(err))
            print("Failed to insert data into clinica.volante table")
        finally:
            if (cnx):
                self.CerrarConexion(cnx)

    def Modificar(self,id_paciente,data,data_new):
            lista=[data_new,]
            try:    
                cnx=self.Conectar()
                cursor = cnx.cursor()
                sql_qry="""UPDATE clinica.volante SET tipo=%s,volante=%s,patologia=%s,tratamiento=%s,
                total=%s WHERE id_paciente = %s"""
                lista.append(id_paciente)
                lista.append(data)
                cursor.execute(sql_qry,lista)
                cnx.commit()
                print("Record Update successfully into clinica.volante table")
            except Exception as err:
                print("Error: {}".format(err))
                print("Failed to Update data into clinica.volante table")
            finally:
                if (cnx):
                    self.CerrarConexion(cnx)

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
        try:    
            cnx=self.Conectar()
            cursor = cnx.cursor()
            sql_qry="""DELETE FROM clinica.volante WHERE id_paciente = %s AND volante=%s"""
            cursor.execute(sql_qry,(id_paciente,data,))
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



# test=Volantes()
# test.Insertar(4,"carga esquiotibilaes")
# test.Modificar(4,"Cardiopatologia")
# print(test.BuscarporID(4))
# print(test.BuscarId_Dni("87654321T"))
# test.EliminarTodos(4,)
# test.EliminarAntecedente(10,"ACV")
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from conexion import *
from clases_paciente import *

#PACIENTE FRAME
class PacienteFrame(ttk.Frame,Pacientes):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        #-----------------COMIENZO DE CAMPOS-----------------------
        self.miFrame_Campos = Frame(self,bg="#0e0349")
        self.miFrame_Campos.pack()

        self.datacuadroNombre = StringVar()
        self.datacuadroApellidos = StringVar()
        self.datacuadroDni = StringVar()
        self.datacuadroTelefono = IntVar()
        self.datacuadroDireccion = StringVar()
        self.datacuadroEdad = IntVar()

        self.cuadroNombre = Entry(self.miFrame_Campos, textvariable=self.datacuadroNombre)
        self.cuadroNombre.grid(row=1, column=1, padx=10, pady=1)
        self.cuadroNombre.config(justify="center")

        self.cuadroApellidos = Entry(self.miFrame_Campos, textvariable=self.datacuadroApellidos)
        self.cuadroApellidos.grid(row=2, column=1, padx=10, pady=1)
        self.cuadroApellidos.config(justify="center")

        self.cuadroDni = Entry(self.miFrame_Campos, textvariable=self.datacuadroDni)
        self.cuadroDni.grid(row=1, column=3, padx=10, pady=1)
        self.cuadroDni.config(justify="center")

        self.cuadroTelefono = Entry(self.miFrame_Campos, textvariable=self.datacuadroTelefono)
        self.cuadroTelefono.grid(row=2, column=3, padx=10, pady=1)
        self.cuadroTelefono.config(justify="center")

        self.cuadroDireccion = Entry(self.miFrame_Campos, textvariable=self.datacuadroDireccion)
        self.cuadroDireccion.grid(row=1, column=5, padx=10, pady=1)
        self.cuadroDireccion.config(justify="center")
        
        self.cuadroEdad = Entry(self.miFrame_Campos, textvariable=self.datacuadroEdad)
        self.cuadroEdad.grid(row=2, column=5, padx=10, pady=1)
        self.cuadroEdad.config(justify="center")

        self.botonAgregar = Button(self.miFrame_Campos, text="Agregar", width=10,command=lambda:self.InsertarData())
        self.botonAgregar.grid(row=1, column=6, padx=10, pady=10)
       
        self.botonLimpiar = Button(self.miFrame_Campos, text="Limpiar", width=10,command=lambda:self.borrarInputBox())
        self.botonLimpiar.grid(row=2, column=6, padx=10, pady=10)

        #-----------------COMIENZO DE ETIQUETAS-----------------------

        self.NombreLabel = Label(self.miFrame_Campos, text="Nombre: ",bg="#FFEEDD")
        self.NombreLabel.grid(row=1, column=0, padx=10, pady=10)

        self.ApellidosLabel = Label(self.miFrame_Campos, text="Apellidos: ",bg="#FFEEDD")
        self.ApellidosLabel.grid(row=2, column=0, padx=10, pady=10)

        self.DNILabel = Label(self.miFrame_Campos, text="DNI: ",bg="#FFEEDD")
        self.DNILabel.grid(row=1, column=2, padx=10, pady=10)

        self.TelefonoLabel = Label(self.miFrame_Campos, text="Telefono: ",bg="#FFEEDD")
        self.TelefonoLabel.grid(row=2, column=2, padx=10, pady=10)

        self.DireccionLabel = Label(self.miFrame_Campos, text="Direccion: ",bg="#FFEEDD")
        self.DireccionLabel.grid(row=1, column=4, padx=10, pady=10)

        self.EdadLabel = Label(self.miFrame_Campos, text="Edad: ",bg="#FFEEDD")
        self.EdadLabel.grid(row=2, column=4, padx=10, pady=10)

        #-----------------Separador-----------------------
        self.separator = Frame(self,height=10, bd=1, relief=SUNKEN)
        self.separator.pack()

        #-----------------Visor de Pacientes-----------------------

        self.miFrame_Pacientes = Frame(self,bg="gray")
        self.miFrame_Pacientes.pack()

        self.tituloLabel=Label(self.miFrame_Pacientes,text="LISTADO DE PACIENTES",fg="gray",bg="white",font=("Times New Roman",20))
        self.tituloLabel.grid(row=0, column=1, padx=10, pady=10,sticky="we",columnspan=2)

        self.treePacientes = ttk.Treeview(self.miFrame_Pacientes,columns = ("id","nombre","apellidos","dni","telefono","direccion","edad"))   
        self.treePacientes.grid(row=1,column=1,padx=10,pady=10)
        self.treePacientes['show']='headings'
        self.treePacientes.heading('#0', text='column0', anchor=tk.W)
        self.treePacientes.heading('#1', text='ID', anchor=tk.W)
        self.treePacientes.heading('#2', text='NOMBRE', anchor=tk.W)
        self.treePacientes.heading('#3', text='APELLIDOS', anchor=tk.W)
        self.treePacientes.heading('#4', text='DNI', anchor=tk.W)
        self.treePacientes.heading('#5', text='TELEFONO', anchor=tk.W)
        self.treePacientes.heading('#6', text='DIRECCION', anchor=tk.W)
        self.treePacientes.heading('#7', text='EDAD', anchor=tk.W)
        
        self.treePacientes.column('#0',width=30,minwidth=30,stretch=tk.YES)
        self.treePacientes.column('#1',width=30,minwidth=30,stretch=tk.YES)
        self.treePacientes.column('#2',width=100,minwidth=50,stretch=tk.YES)
        self.treePacientes.column('#3',width=100,minwidth=50,stretch=tk.YES)
        self.treePacientes.column('#4',width=100,minwidth=50,stretch=tk.YES)
        self.treePacientes.column('#5',width=100,minwidth=50,stretch=tk.YES)
        self.treePacientes.column('#6',width=150,minwidth=150,stretch=tk.YES)
        self.treePacientes.column('#7',width=100,minwidth=100,stretch=tk.YES)

        for row in self.BuscarTodos():
             self.treePacientes.insert('',END, values=row)

        self.scrollVert2=Scrollbar(self.miFrame_Pacientes,command=self.treePacientes.yview)
        self.scrollVert2.grid(row=1,column=2,sticky="nsnew")
        self.treePacientes.config(yscrollcommand=self.scrollVert2.set)

        #-----------------Separador-----------------------
        self.separator = Frame(self,height=10, bd=1, relief=SUNKEN)
        self.separator.pack()

        #-----------------COMIENZO DE BOTONES-----------------------
        
        self.miFrame_Botones = Frame(self,bg="#00CD63")
        self.miFrame_Botones.pack()

        self.botonRefresh = Button(self.miFrame_Botones, text="Refresh", width=10,command=lambda:self.UpdateTreeViewPacientes())
        self.botonRefresh.grid(row=4, column=0, padx=10, pady=10)

        self.botonReadUSER =Button(self.miFrame_Botones, text="Modificar", width=10,command=lambda:self.ModificarDataUser(self.leerInfoInputBox(),self.IdSeleccionado()))
        self.botonReadUSER.grid(row=4, column=1, padx=10, pady=10)

        self.botonUpdate = Button(self.miFrame_Botones, text="Seleccionar", width=10,command=lambda:self.CompletarData(self.IdSeleccionado()))
        self.botonUpdate.grid(row=4, column=2, padx=10, pady=10)

        self.botonDelete = Button(self.miFrame_Botones, text="Borrar", width=10,command=lambda:self.EliminarData(self.IdSeleccionado()))
        self.botonDelete.grid(row=4, column=3, padx=10, pady=10)

    #-----------------FUNCIONES-----------------------

    def InsertarData(self):
        data=self.leerInfoInputBox()
        self.Insertar(data)
        self.UpdateTreeViewPacientes()
       
    def EliminarData(self,id_paciente):
        self.Eliminar(id_paciente)
        self.borrarInputBox()
        self.UpdateTreeViewPacientes()


    def UpdateTreeViewPacientes(self):
        print("Refresh : UpdateTreeViewPacientes")
        for row in self.treePacientes.get_children():
            self.treePacientes.delete(row)
        for row in self.BuscarTodos():
            self.treePacientes.insert('',END, values=row)

    def leerInfoInputBox(self):
        listadata =[]
        try:
            listadata = [self.datacuadroNombre.get(),
                    self.datacuadroApellidos.get(),
                    self.datacuadroDni.get(),
                    int(self.datacuadroTelefono.get()),
                    self.datacuadroDireccion.get(),
                    int(self.datacuadroEdad.get())]

            for values in listadata:
                if not values:
                    listadata.clear() #borra todos los elemtnos
                    break
        except Exception as err:
            print("Error: {}".format(err))
        finally:
            return listadata

    def borrarInputBox(self):
        self.datacuadroNombre.set("")
        self.datacuadroApellidos.set("")
        self.datacuadroDni.set("")
        self.datacuadroTelefono.set(0)
        self.datacuadroDireccion.set("")
        self.datacuadroEdad.set(0)
        print("MedicalREC - Se borran todos los campos")

    def IdSeleccionado(self):
        try:
            miPaciente=Pacientes()
            item_paciente = self.treePacientes.focus()
            id_paciente=int(self.treePacientes.item(item_paciente,"values")[0])
        except Exception as err:
            print("Error: {}".format(err))
            id_paciente=-1
        finally:
            print("Id seleccionado:{}".format(id_paciente))
            return id_paciente

    def CompletarData(self,id_paciente):
        try:
            datos=self.BuscarporID(id_paciente)
            self.datacuadroNombre.set(datos[1])
            self.datacuadroApellidos.set(datos[2])
            self.datacuadroDni.set(datos[3])
            self.datacuadroTelefono.set(datos[4])
            self.datacuadroDireccion.set(datos[5])
            self.datacuadroEdad.set(datos[6])
        except Exception as err:
            print("Error: {}".format(err))

    def ModificarDataUser(self,data,id_paciente):
        self.Modificar(data,id_paciente)
        self.UpdateTreeViewPacientes()
    # def ReadDataUser(self):
        
    #     try:
    #         miConexion = sqlite3.connect("CLIENTES")
    #         miCursor = miConexion.cursor()
    #         sql_update_query = """SELECT * FROM CLIENTES WHERE NOMBRE_USUARIO = ?"""
    #         name=str(self.cuadroNombre.get())
    #         miCursor.execute(sql_update_query,(name,))
    #         listamiCursor=miCursor.fetchone() #recuperar los datos
    #         if(listamiCursor!=None):
    #             self.datacuadroNombre.set(listamiCursor[1])
    #             self.datacuadroTelefono.set(listamiCursor[2])
    #         else:
    #             messagebox.showinfo("ClientView", "NO ENCONTRADO!!")    
    #             self.borrarInputBox()
    #         miConexion.commit()
    #         miConexion.close()
    #         self.UpdateTreeViewClientes()
    #     except:
    #         print("Failed to ReadData data into sqlite table")
    #     finally:
    #         if (miConexion):
    #             miConexion.close()
    #             print("The SQLite connection is closed")


    # def updateData(self):
        
    #     try:    
    #         miConexion = sqlite3.connect("CLIENTES")
    #         miCursor = miConexion.cursor()
    #         sql_update_query="""SELECT * FROM CLIENTES WHERE NOMBRE_USUARIO = ?"""
    #         name=str(self.cuadroNombre.get())
    #         miCursor.execute(sql_update_query,(name,))
    #         listamiCursor=miCursor.fetchone() #recuperar los datos
    #         if(listamiCursor!=None):
    #             for usuario in listamiCursor:
                    
    #                 data= self.leerInfoInputBox()
    #                 data.append(listamiCursor[0])

    #             sql_update_query = """UPDATE CLIENTES set NOMBRE_USUARIO = ? ,TELEFONO = ? where ID = ?"""
    #             miCursor.execute(sql_update_query, data)
    #             messagebox.showinfo("ClientView App", "BBDD ACTUALIZADA con exito!!")
    #         else:
    #             messagebox.showinfo("ClientView App", "No se actualizo!!")
    #         miConexion.commit()    
    #         miCursor.close()
    #         self.UpdateTreeViewClientes()
    #     except:
    #         print("Failed to Actualizar data into sqlite table")
    #     finally:
    #         if (miConexion):
    #             miConexion.close()
    #             print("The SQLite connection is closed")


    # def deleteData(self):

    #     try:
    #         miConexion = sqlite3.connect("CLIENTES")
    #         miCursor = miConexion.cursor()
    #         sql_update_query="""SELECT * FROM CLIENTES WHERE NOMBRE_USUARIO = ?"""
    #         name=str(self.cuadroNombre.get())
    #         miCursor.execute(sql_update_query,(name,))
    #         listamiCursor=miCursor.fetchone() #recuperar los datos
    #         if(listamiCursor!=None):
    #             sql_update_query = """DELETE FROM CLIENTES WHERE ID = ?"""
    #             miCursor.execute(sql_update_query, (listamiCursor[0],))
    #             messagebox.showinfo("ClientView App", "dATO ELIMINADO!!")
    #         else:
    #             messagebox.showinfo("ClientView App", "No se PUDO ELIMINAR!!")
    #         miConexion.commit()    
    #         miCursor.close()
    #         self.UpdateTreeViewClientes()
    #     except:
    #         print("Failed to deleteData data into sqlite table")
    #     finally:
    #         if (miConexion):
    #             miConexion.close()
    #             print("The SQLite connection is closed")



class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("MedicalREC - Gestion de Base de Datos Pacientes")
        main_window.geometry("1200x860")
        self.notebook = ttk.Notebook(self)
        self.pacientes_frame = PacienteFrame(self.notebook)           
        self.notebook.add(self.pacientes_frame, text="Pacientes", padding=10)
        self.notebook.configure(height=900,width=900)

        # self.sesiones_frame = PacienteFrame(self.notebook)
        # self.notebook.add(
        #      self.sesiones_frame, text="Sesiones", padding=10)
        
        # self.tratamientos_frame = PacienteFrame(self.notebook)
        # self.notebook.add(
        #      self.tratamientos_frame, text="Tratamientos", padding=10)
        
        # self.estadisticas_frame = PacienteFrame(self.notebook)
        # self.notebook.add(
        #      self.estadisticas_frame, text="Estadisticas", padding=10)

        self.notebook.pack(padx=10, pady=10)
        self.pack()

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from conexion import *
from clases_paciente import *
from clases_sesiones import *
from clases_antecedentes import *
from clases_volante import *
from tkcalendar import DateEntry
from datetime import date

def CerrarEdicion(root):
        root.destroy()


#PACIENTE FRAME -> (PACIENTES + ANTECEDENTES)
class PacienteFrame(ttk.Frame,Pacientes,Antecedentes):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.id_seleccion_paciente=-1
        self.id_seleccion_antecedente=-1
        
        # -----------------DEFINICION DE FRAME CAMPOS-----------------------
        self.miFrame_Campos = Frame(self,bg="#0e0349")
        self.miFrame_Campos.pack()

        # -----------------COMIENZO DE VARIABLES-----------------------
        self.datacuadroNombre = StringVar()
        self.datacuadroApellidos = StringVar()
        self.datacuadroDni = StringVar()
        self.datacuadroTelefono = StringVar()
        self.datacuadroDireccion = StringVar()
        self.datacuadroEdad = StringVar()
        self.datacuadroDni_B = StringVar()
        self.datacuadroNombre_B = StringVar()
        self.datacuadroApellido_B = StringVar()

        # -----------------DEFINICION DE CUADROS-----------------------
        self.cuadroNombre = Entry(self.miFrame_Campos, textvariable=self.datacuadroNombre,width=25)
        self.cuadroNombre.grid(row=1, column=1, padx=10, pady=1)
        self.cuadroNombre.config(justify="center")

        self.cuadroApellidos = Entry(self.miFrame_Campos, textvariable=self.datacuadroApellidos,width=25)
        self.cuadroApellidos.grid(row=2, column=1, padx=10, pady=1)
        self.cuadroApellidos.config(justify="center")

        self.cuadroDni = Entry(self.miFrame_Campos, textvariable=self.datacuadroDni,width=25)
        self.cuadroDni.grid(row=1, column=3, padx=10, pady=1)
        self.cuadroDni.config(justify="center")

        self.cuadroTelefono = Entry(self.miFrame_Campos, textvariable=self.datacuadroTelefono,width=25)
        self.cuadroTelefono.grid(row=2, column=3, padx=10, pady=1)
        self.cuadroTelefono.config(justify="center")

        self.cuadroDireccion = Entry(self.miFrame_Campos, textvariable=self.datacuadroDireccion,width=25)
        self.cuadroDireccion.grid(row=1, column=5, padx=10, pady=1)
        self.cuadroDireccion.config(justify="center")
        
        self.cuadroEdad = Entry(self.miFrame_Campos, textvariable=self.datacuadroEdad,width=25)
        self.cuadroEdad.grid(row=2, column=5, padx=10, pady=1)
        self.cuadroEdad.config(justify="center")

        #-----------------COMIENZO DE ETIQUETAS-----------------------
        self.NombreLabel = Label(self.miFrame_Campos, text="Nombre: ",bg="#FFEEDD",width=12)
        self.NombreLabel.grid(row=1, column=0, padx=10, pady=10)

        self.ApellidosLabel = Label(self.miFrame_Campos, text="Apellidos: ",bg="#FFEEDD",width=12)
        self.ApellidosLabel.grid(row=2, column=0, padx=10, pady=10)

        self.DNILabel = Label(self.miFrame_Campos, text="DNI: ",bg="#FFEEDD",width=12)
        self.DNILabel.grid(row=1, column=2, padx=10, pady=10)

        self.TelefonoLabel = Label(self.miFrame_Campos, text="Telefono: ",bg="#FFEEDD",width=12)
        self.TelefonoLabel.grid(row=2, column=2, padx=10, pady=10)

        self.DireccionLabel = Label(self.miFrame_Campos, text="Direccion: ",bg="#FFEEDD",width=12)
        self.DireccionLabel.grid(row=1, column=4, padx=10, pady=10)

        self.EdadLabel = Label(self.miFrame_Campos, text="Edad: ",bg="#FFEEDD",width=12)
        self.EdadLabel.grid(row=2, column=4, padx=10, pady=10)

        self.botonAgregar = Button(self.miFrame_Campos, text="Agregar", width=12,command=lambda:self.InsertarDataPaciente())
        self.botonAgregar.grid(row=5, column=0, padx=10, pady=10)

        self.botonEdit = Button(self.miFrame_Campos, text="Modificar", width=12,
            command=lambda:self.ModificarDataPaciente(self.id_seleccion_paciente))
        self.botonEdit.grid(row=5, column=1, padx=10, pady=10)

        self.botonDelete = Button(self.miFrame_Campos, text="Borrar", width=12,command=lambda:self.EliminarData(self.id_seleccion_paciente))
        self.botonDelete.grid(row=5, column=2, padx=10, pady=10)

        self.botonLimpiar = Button(self.miFrame_Campos, text="Limpiar", width=12,command=lambda:self.borrarInputBox())
        self.botonLimpiar.grid(row=5, column=3, padx=10, pady=10)

        self.botonBuscar = Button(self.miFrame_Campos, text="Buscar Por DNI", width=12,command=lambda:self.CompletarData_DNI())
        self.botonBuscar.grid(row=4, column=0, padx=10, pady=10)

        self.botonBuscar_NombreApellido = Button(self.miFrame_Campos, text="Buscar por Nombre y Apellido", width=25,command=lambda:self.CompletarData_NombreyApellido())
        self.botonBuscar_NombreApellido.grid(row=4, column=2, padx=10, pady=10)

        self.cuadroDni_B = Entry(self.miFrame_Campos, textvariable=self.datacuadroDni_B,width=25)
        self.cuadroDni_B.grid(row=4, column=1, padx=10, pady=10)
        self.cuadroDni_B.config(justify="center")

        self.cuadroNombre_B = Entry(self.miFrame_Campos, textvariable=self.datacuadroNombre_B,width=25)
        self.cuadroNombre_B.grid(row=4, column=3, padx=10, pady=10)
        self.cuadroNombre_B.config(justify="center")

        self.cuadroApellido_B = Entry(self.miFrame_Campos, textvariable=self.datacuadroApellido_B,width=25)
        self.cuadroApellido_B.grid(row=4, column=4, padx=10, pady=10)
        self.cuadroApellido_B.config(justify="center")

        self.logo=PhotoImage(file="logo.gif")
        self.fondo=Label(self.miFrame_Campos,image=self.logo)
        self.fondo.grid(row=4, column=5, padx=10, pady=10,rowspan=2)

        #-----------------Visor de Pacientes-----------------------
        self.miFrame_Pacientes = Frame(self,bg="gray")
        self.miFrame_Pacientes.pack()

        self.tituloLabel=Label(self.miFrame_Pacientes,text="PACIENTES",fg="gray",bg="white",font=("Times New Roman",20))
        self.tituloLabel.grid(row=0, column=0, padx=10, pady=10,sticky="we",columnspan=3)

        self.treePacientes = ttk.Treeview(self.miFrame_Pacientes,columns = ("id","nombre","apellidos","dni","telefono","direccion","edad"))

        self.treePacientes.grid(row=1,column=1,padx=10,pady=10,rowspan=3)
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
        self.treePacientes.column('#1',width=20,minwidth=20,stretch=tk.YES)
        self.treePacientes.column('#2',width=100,minwidth=100,stretch=tk.YES)
        self.treePacientes.column('#3',width=100,minwidth=100,stretch=tk.YES)
        self.treePacientes.column('#4',width=100,minwidth=100,stretch=tk.YES)
        self.treePacientes.column('#5',width=100,minwidth=100,stretch=tk.YES)
        self.treePacientes.column('#6',width=100,minwidth=100,stretch=tk.YES)
        self.treePacientes.column('#7',width=30,minwidth=30,stretch=tk.YES)

        self.UpdateTreeViewPacientes(self.BuscarTodosPacientes())

        self.scrollVert2=Scrollbar(self.miFrame_Pacientes,command=self.treePacientes.yview)
        self.scrollVert2.grid(row=1,column=2,sticky="nsnew",rowspan=3)
        self.treePacientes.config(yscrollcommand=self.scrollVert2.set)

        self.tituloLabel_Ant=Label(self.miFrame_Pacientes,text="ANTECEDENTES",fg="gray",bg="white",font=("Times New Roman",20))
        self.tituloLabel_Ant.grid(row=0, column=3, padx=10, pady=10,sticky="we",columnspan=3)

        self.treeAntecedentes = ttk.Treeview(self.miFrame_Pacientes,columns = ("id_paciente","Enfermedades"))   
        self.treeAntecedentes.grid(row=1,column=3,padx=10,pady=10,rowspan=3)
        self.treeAntecedentes['show']='headings'
        self.treeAntecedentes.heading('#0', text='column0', anchor=tk.W)
        self.treeAntecedentes.heading('#1', text='ID', anchor=tk.W)
        self.treeAntecedentes.heading('#2', text='ENFERMEDADES', anchor=tk.W)
        
        self.treeAntecedentes.column('#0',width=30,minwidth=30,stretch=tk.YES)
        self.treeAntecedentes.column('#1',width=20,minwidth=20,stretch=tk.YES)
        self.treeAntecedentes.column('#2',width=230,minwidth=230,stretch=tk.YES)
        
        self.UpdateTreeViewAntecedentes(self.BuscarTodosAntecedentes())

        self.scrollVert2=Scrollbar(self.miFrame_Pacientes,command=self.treeAntecedentes.yview)
        self.scrollVert2.grid(row=1,column=4,sticky="nsnew",rowspan=3)

        self.botonAgregar_lista = Button(self.miFrame_Pacientes, text="Agregar", width=12,command=lambda:self.IngresarDataAntecedentes())
        self.botonAgregar_lista.grid(row=1, column=5, padx=10, pady=10,rowspan=2)

        self.botonEditar_lista = Button(self.miFrame_Pacientes, text="Editar", width=12,command=lambda:self.ModificarDataAntecedentes())
        self.botonEditar_lista.grid(row=2, column=5, padx=10, pady=10,rowspan=2)
        
        self.botonDelete_lista = Button(self.miFrame_Pacientes, text="Borrar", width=12,command=lambda:self.EliminarDataAntecedentes())
        self.botonDelete_lista.grid(row=3, column=5, padx=10, pady=10,rowspan=2)
    
    #-----------------FUNCIONES-----------------------
    def UpdateTreeViewPacientes(self,data_encontrado):
        try:    
            # print("Refresh : UpdateTreeViewPacientes")
            for row in self.treePacientes.get_children():
                self.treePacientes.delete(row)
            for row in data_encontrado:
                self.treePacientes.insert('',END, values=row)
        except Exception as err:
            print("Error: {}".format(err))

    def InsertarDataPaciente(self):
        try:
            data,resultado=self.leerInfoInputBox()
            if resultado:            
                if(self.InsertarPaciente(data)):
                    self.UpdateTreeViewPacientes(self.BuscarTodosPacientes())
                    self.borrarInputBox()
                    messagebox.showinfo("MedicalREC", "Paciente Agregado")
                else:
                    messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")
            else:
                messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")    
        except Exception as err:
            print("Error: {}".format(err))
            messagebox.showinfo("MedicalREC", "Error en los Datos Ingresados")
        
    def EliminarData(self,id_paciente):
        try:
            if id_paciente!=-1:
                opcion=messagebox.askyesno("Eliminar","Desea eliminar EL Paciente Selecionado?")
                if opcion:
                    self.EliminarPaciente(id_paciente)
                    self.borrarInputBox()
                    self.UpdateTreeViewPacientes(self.BuscarTodosPacientes())
                    messagebox.showinfo("MedicalREC", "Paciente Eliminado")
            else:
                messagebox.showinfo("MedicalREC", "No hay Paciente seleccionado")
        except Exception as err:
            print("Error: {}".format(err))
            messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")

    def leerInfoInputBox(self):
        resultado=True
        listadata =[]
        try:
            nombre=self.datacuadroNombre.get()
            if(len(nombre)>30 or len(nombre)==0):
                resultado=False
                messagebox.showinfo("MedicalREC", "CAMPO- NOMBRE")
            apellido=self.datacuadroApellidos.get()
            if(len(apellido)>50 or len(apellido)==0):
                resultado=False
                messagebox.showinfo("MedicalREC", "CAMPO-APELLIDO")
            dni=self.datacuadroDni.get()
            if(len(apellido)>9 or len(apellido)==0):
                resultado=False
                messagebox.showinfo("MedicalREC", "CAMPO-DNI")
            telefono=self.datacuadroTelefono.get()
            if(len(telefono)>9 or len(telefono)==0):
                resultado=False
                messagebox.showinfo("MedicalREC", "CAMPO-TELEFONO")
            else:
                try:
                    int(telefono)
                except Exception as err:
                    print("Error: {}".format(err))
                    messagebox.showinfo("MedicalREC", "CAMPO-TELEFONO-NO ES UN NUMERO")
                    resultado=False
            direccion=self.datacuadroDireccion.get()
            if(len(direccion)>50 or len(direccion)==0):
                resultado=False
                messagebox.showinfo("MedicalREC", "CAMPO-DIRECCION")
            edad=self.datacuadroEdad.get()
            if(len(edad)>3 or len(edad)==0):
                resultado=False
                messagebox.showinfo("MedicalREC", "CAMPO-EDAD")
            else:
                try:
                    int(edad)
                except Exception as err:
                    print("Error: {}".format(err))
                    messagebox.showinfo("MedicalREC", "CAMPO-EDAD-NO ES UN NUMERO")
                    resultado=False        
            if resultado:
                listadata = [nombre,apellido,dni,telefono,direccion,edad]
            else:
                listadata.clear()

        except Exception as err:
            print("Error: {}".format(err))
        finally:
            return listadata,resultado

    def borrarInputBox(self):
        try:
            self.datacuadroNombre.set("")
            self.datacuadroApellidos.set("")
            self.datacuadroDni.set("")
            self.datacuadroTelefono.set(0)
            self.datacuadroDireccion.set("")
            self.datacuadroEdad.set(0)
            self.datacuadroDni_B.set("")
            self.datacuadroNombre_B.set("")
            self.datacuadroApellido_B.set("")
            self.UpdateTreeViewPacientes(self.BuscarTodosPacientes())
            self.UpdateTreeViewAntecedentes(self.BuscarTodosAntecedentes())
            self.id_seleccion_paciente=-1
            self.id_seleccion_antecedente=-1
            print("MedicalREC - Se borran todos los campos")
        except Exception as err:
            print("Error: {}".format(err))

    def IdSeleccionadoPaciente(self):
        try:
            miPaciente=Pacientes()
            item_paciente = self.treePacientes.focus()
            id_paciente=int(self.treePacientes.item(item_paciente,"values")[0])
        except Exception as err:
            print("Error: {}".format(err))
            id_paciente=-1
        finally:
            print("Id seleccionado Paciente:{}".format(id_paciente))
            return id_paciente

    def CompletarData_DNI(self):
        try:
            listadata=self.BuscarporDniPaciente(self.datacuadroDni_B.get())
            datos=listadata[0]
            if datos is not None:
                self.datacuadroNombre.set(datos[1])
                self.datacuadroApellidos.set(datos[2])
                self.datacuadroDni.set(datos[3])
                self.datacuadroTelefono.set(datos[4])
                self.datacuadroDireccion.set(datos[5])
                self.datacuadroEdad.set(datos[6])
                self.id_seleccion_paciente=datos[0]
                self.id_seleccion_antecedente=datos[0]
                self.UpdateTreeViewPacientes(listadata)
                self.UpdateTreeViewAntecedentes(self.BuscarporIDAntecedente(self.id_seleccion_paciente))
                messagebox.showinfo("MedicalREC", "Paciente Encontrado")
            else:
                messagebox.showinfo("MedicalREC", "Paciente No Encontrado")
        except Exception as err:
            print("Error: {}".format(err))
            messagebox.showinfo("MedicalREC", "Paciente No Encontrado")

    def CompletarData_NombreyApellido(self):
        try:
            listadata=self.BuscarporNombreyApellido(self.datacuadroNombre_B.get(),self.datacuadroApellido_B.get())
            datos=listadata[0]
            if datos is not None:
                self.datacuadroNombre.set(datos[1])
                self.datacuadroApellidos.set(datos[2])
                self.datacuadroDni.set(datos[3])
                self.datacuadroTelefono.set(datos[4])
                self.datacuadroDireccion.set(datos[5])
                self.datacuadroEdad.set(datos[6])
                self.id_seleccion_paciente=datos[0]
                self.id_seleccion_antecedente=datos[0]
                self.UpdateTreeViewPacientes(listadata)
                self.UpdateTreeViewAntecedentes(self.BuscarporIDAntecedente(self.id_seleccion_paciente))
                messagebox.showinfo("MedicalREC", "Paciente Encontrado")
            else:
                messagebox.showinfo("MedicalREC", "Paciente No Encontrado")
        except Exception as err:
            print("Error: {}".format(err))
            messagebox.showinfo("MedicalREC", "Paciente No Encontrado")

    def ModificarDataPaciente(self,id_paciente):
        try:
            if id_paciente!=-1:
                data,resultado=self.leerInfoInputBox()
                if resultado: 
                    self.ModificarPaciente(data,id_paciente)
                    self.UpdateTreeViewPacientes(self.BuscarporIDPaciente(id_paciente))
                    messagebox.showinfo("MedicalREC", "Paciente Modificado")
            else:
                messagebox.showinfo("MedicalREC", "No hay Pacientes Seleccionado para Editar")
        except Exception as err:
            print("Error: {}".format(err))
            messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")

    def UpdateTreeViewAntecedentes(self,data):
        try:    
            # print("Refresh : UpdateTreeViewAntecedentes")
            for row in self.treeAntecedentes.get_children():
                self.treeAntecedentes.delete(row)
            for row in data:
                self.treeAntecedentes.insert('',END, values=row)
        except Exception as err:
            print("Error: {}".format(err))
            
    def EliminarDataAntecedentes(self):
        try:
            data_old=self.DataSeleccionadoAntecedentes()
            id_paciente=int(data_old[0])
            if id_paciente!=-1:
                opcion=messagebox.askyesno("Eliminar","Desea eliminar el Antecedente Selecionado?")
                if opcion:
                    self.EliminarAntecedente(id_paciente,data_old)
                    messagebox.showinfo("MedicalREC", "Antecedente Eliminado")
        except Exception as err:
            print("Error: {}".format(err))
            messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")
        finally:
            self.UpdateTreeViewPacientes(self.BuscarporIDPaciente(self.id_seleccion_paciente))
            self.UpdateTreeViewAntecedentes(self.BuscarporIDAntecedente(self.id_seleccion_antecedente))

    def IdSeleccionadoAntecedentes(self):
        try:
            miSesion=Antecedentes()
            item_antecedente = self.treeAntecedentes.focus()
            id_antecedente=int(self.treeAntecedentes.item(item_antecedente,"values")[0])
        except Exception as err:
            print("Error: {}".format(err))
            id_antecedente=-1
        finally:
            print("Id seleccionado Antecedente:{}".format(id_antecedente))
            return id_antecedente

    def DataSeleccionadoAntecedentes(self):
        data_sesion=None
        try:
            miSesion=Antecedentes()
            item_antecedente = self.treeAntecedentes.focus()
            data_antecedente = self.treeAntecedentes.item(item_antecedente,"values")
        except Exception as err:
            print("Error: {}".format(err))
        finally:
            return data_antecedente

    def ModificarDataUserAntecedentes(self,root,data_old,id_paciente,data_new):
        lista=(data_new)
        try:
            if self.ModificarAntecedente(id_paciente,data_old,lista):
                messagebox.showinfo("MedicalREC", "Antecedente Modificado")
            else:
                messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")    
        except Exception as err:
                print("Error: {}".format(err))
                messagebox.showinfo("MedicalREC", "Error en los Datos Ingresados")
        finally:
                self.UpdateTreeViewAntecedentes(self.BuscarporIDAntecedente(id_paciente))
                CerrarEdicion(root)
    
    def IngresarDataAntecedentes(self):
        if self.id_seleccion_antecedente != -1:
            listadata=self.BuscarporIDAntecedente(self.id_seleccion_antecedente)
            if listadata is None:
                messagebox.showinfo("MedicalREC", "Paciente No encontrado")
            else:
                try:
                    edit = tk.Tk()
                    edit.title("MedicalREC - Edit Sesiones")
                    edit.configure(width="350", height="350")
                    var_check=StringVar()
                    ComentarioLabel = Label(edit, text="Enfermedades")
                    ComentarioLabel.grid(row=0, column=0, padx=10, pady=10)
                    cuadroComentario = Text(edit, width=20,heigh=10)
                    cuadroComentario.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
                    
                    botonIngresar = Button(edit, text="ACEPTAR ", width=12,command=lambda:self.InsertarDataUser(edit,self.id_seleccion_antecedente,cuadroComentario.get('1.0','end')))
                    botonIngresar.grid(row=2, column=0, padx=10, pady=10,columnspan=2)
        
                except Exception as err:
                    print("Error: {}".format(err))
                    messagebox.showinfo("MedicalREC", "Sesion del Listado No seleccionada")
                finally:
                    self.UpdateTreeViewAntecedentes(self.BuscarporIDAntecedente(self.id_seleccion_antecedente))
        else:
            messagebox.showinfo("MedicalREC", "No hay Paciente Seleccionado")          

    def InsertarDataUser(self,root,id_paciente,data_new):
        
        try:
            if self.InsertarAntecedente(id_paciente,data_new):
                messagebox.showinfo("MedicalREC", "Nuevo Antecedente")
            else:
                messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")
                
        except Exception as err:
                print("Error: {}".format(err))
                messagebox.showinfo("MedicalREC", "Error en los Datos Ingresados")
        finally:
                self.UpdateTreeViewAntecedentes(self.BuscarporIDAntecedente(id_paciente))
                CerrarEdicion(root)

    def ModificarDataAntecedentes(self):
        try:
            data_old=self.DataSeleccionadoAntecedentes()
            self.id_seleccion_antecedente=int(data_old[0])
            edit = tk.Tk()
            edit.title("MedicalREC - Edit Sesiones")
            edit.configure(width="350", height="350")
            var_check=StringVar()
            ComentarioLabel = Label(edit, text="Enfermedades")
            ComentarioLabel.grid(row=0, column=0, padx=10, pady=10)
            cuadroComentario = Text(edit, width=20,heigh=10)
            cuadroComentario.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
            
            botonIngresar = Button(edit, text="ACEPTAR ", width=12,command=lambda:self.ModificarDataUserAntecedentes(edit,data_old,self.id_seleccion_antecedente,cuadroComentario.get('1.0','end')))
            botonIngresar.grid(row=2, column=0, padx=10, pady=10,columnspan=2)

        except Exception as err:
                print("Error: {}".format(err))
                messagebox.showinfo("MedicalREC", "Sesion del Listado No seleccionada")

########################################################################################################################################################
########################################################################################################################################################


#VOLANTES FRAME -> (VOLANTE + SESIONES)
class VolanteFrame(ttk.Frame,Volantes,Sesiones):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.id_seleccion_paciente=-1
        self.id_seleccion_volante=-1
        self.id_seleccion_sesion=-1
        
        # -----------------DEFINICION DE FRAME CAMPOS-----------------------
        self.miFrame_Campos = Frame(self,bg="#0e0349")
        self.miFrame_Campos.pack()

        # -----------------COMIENZO DE VARIABLES-----------------------
        self.datacuadroNombre = StringVar()
        self.datacuadroApellidos = StringVar()
        self.datacuadroDni = StringVar()
        self.datacuadroTelefono = StringVar()
        self.datacuadroDireccion = StringVar()
        self.datacuadroEdad = StringVar()
        self.datacuadroDni_B = StringVar()
        self.datacuadroNombre_B = StringVar()
        self.datacuadroApellido_B = StringVar()
        self.var = StringVar()
        self.var_check = StringVar()
        self.var_check.set("NO")

        # -----------------DEFINICION DE CUADROS-----------------------
        self.cuadroNombre = Entry(self.miFrame_Campos, textvariable=self.datacuadroNombre,width=25)
        self.cuadroNombre.grid(row=1, column=1, padx=10, pady=1)
        self.cuadroNombre.config(justify="center")

        self.cuadroApellidos = Entry(self.miFrame_Campos, textvariable=self.datacuadroApellidos,width=25)
        self.cuadroApellidos.grid(row=2, column=1, padx=10, pady=1)
        self.cuadroApellidos.config(justify="center")

        self.cuadroDni = Entry(self.miFrame_Campos, textvariable=self.datacuadroDni,width=25)
        self.cuadroDni.grid(row=1, column=3, padx=10, pady=1)
        self.cuadroDni.config(justify="center")

        self.cuadroTelefono = Entry(self.miFrame_Campos, textvariable=self.datacuadroTelefono,width=25)
        self.cuadroTelefono.grid(row=2, column=3, padx=10, pady=1)
        self.cuadroTelefono.config(justify="center")

        self.cuadroDireccion = Entry(self.miFrame_Campos, textvariable=self.datacuadroDireccion,width=25)
        self.cuadroDireccion.grid(row=1, column=5, padx=10, pady=1)
        self.cuadroDireccion.config(justify="center")
        
        self.cuadroEdad = Entry(self.miFrame_Campos, textvariable=self.datacuadroEdad,width=25)
        self.cuadroEdad.grid(row=2, column=5, padx=10, pady=1)
        self.cuadroEdad.config(justify="center")

        #-----------------COMIENZO DE ETIQUETAS-----------------------
        self.NombreLabel = Label(self.miFrame_Campos, text="Nombre: ",bg="#FFEEDD",width=12)
        self.NombreLabel.grid(row=1, column=0, padx=10, pady=10)

        self.ApellidosLabel = Label(self.miFrame_Campos, text="Apellidos: ",bg="#FFEEDD",width=12)
        self.ApellidosLabel.grid(row=2, column=0, padx=10, pady=10)

        self.DNILabel = Label(self.miFrame_Campos, text="DNI: ",bg="#FFEEDD",width=12)
        self.DNILabel.grid(row=1, column=2, padx=10, pady=10)

        self.TelefonoLabel = Label(self.miFrame_Campos, text="Telefono: ",bg="#FFEEDD",width=12)
        self.TelefonoLabel.grid(row=2, column=2, padx=10, pady=10)

        self.DireccionLabel = Label(self.miFrame_Campos, text="Direccion: ",bg="#FFEEDD",width=12)
        self.DireccionLabel.grid(row=1, column=4, padx=10, pady=10)

        self.EdadLabel = Label(self.miFrame_Campos, text="Edad: ",bg="#FFEEDD",width=12)
        self.EdadLabel.grid(row=2, column=4, padx=10, pady=10)

        # self.botonAgregar = Button(self.miFrame_Campos, text="Agregar", width=12,command=lambda:self.InsertarData())
        # self.botonAgregar.grid(row=4, column=0, padx=10, pady=10)

        # self.R1 = Radiobutton(self.miFrame_Campos, text = "Pagado", variable = self.var, value = "YES")
        # self.R1.grid(row=5, column=0, padx=10, pady=10)
        # self.R1.deselect()
        # self.R2 = Radiobutton(self.miFrame_Campos, text = "No Pago", variable = self.var, value = "NO")
        # self.R2.grid(row=5, column=1, padx=10, pady=10)
        # self.R2.select()

        # self.botonEdit = Button(self.miFrame_Campos, text="Editar", width=12,
        #     command=lambda:self.ModificarDataUser())
        # self.botonEdit.grid(row=4, column=2, padx=10, pady=10)

        # self.botonDelete = Button(self.miFrame_Campos, text="Borrar", width=12,command=lambda:self.EliminarData())
        # self.botonDelete.grid(row=4, column=3, padx=10, pady=10)


        # self.cal_add=DateEntry(self.miFrame_Campos,dateformat=3,width=12, background='darkblue',
        #                     foreground='white', borderwidth=4,Calendar =2020)
        # self.cal_add.grid(row=4,column=1,padx=10, pady=10)



        #-----------------COMIENZO DE BOTONES-----------------------
        self.botonAgregar = Button(self.miFrame_Campos, text="Agregar", width=12,command=lambda:self.InsertarDataPaciente())
        self.botonAgregar.grid(row=5, column=0, padx=10, pady=10)

        self.botonEdit = Button(self.miFrame_Campos, text="Modificar", width=12,
            command=lambda:self.ModificarDataPaciente(self.id_seleccion_paciente))
        self.botonEdit.grid(row=5, column=1, padx=10, pady=10)

        self.botonDelete = Button(self.miFrame_Campos, text="Borrar", width=12,command=lambda:self.EliminarData(self.id_seleccion_paciente))
        self.botonDelete.grid(row=5, column=2, padx=10, pady=10)

        self.botonLimpiar = Button(self.miFrame_Campos, text="Limpiar", width=12,command=lambda:self.borrarInputBox())
        self.botonLimpiar.grid(row=5, column=3, padx=10, pady=10)

        self.botonBuscar = Button(self.miFrame_Campos, text="Buscar Por DNI", width=12,command=lambda:self.CompletarData_DNI())
        self.botonBuscar.grid(row=4, column=0, padx=10, pady=10)

        self.botonBuscar_NombreApellido = Button(self.miFrame_Campos, text="Buscar por Nombre y Apellido", width=25,command=lambda:self.CompletarData_NombreyApellido())
        self.botonBuscar_NombreApellido.grid(row=4, column=2, padx=10, pady=10)

        self.cuadroDni_B = Entry(self.miFrame_Campos, textvariable=self.datacuadroDni_B,width=25)
        self.cuadroDni_B.grid(row=4, column=1, padx=10, pady=10)
        self.cuadroDni_B.config(justify="center")

        self.cuadroNombre_B = Entry(self.miFrame_Campos, textvariable=self.datacuadroNombre_B,width=25)
        self.cuadroNombre_B.grid(row=4, column=3, padx=10, pady=10)
        self.cuadroNombre_B.config(justify="center")

        self.cuadroApellido_B = Entry(self.miFrame_Campos, textvariable=self.datacuadroApellido_B,width=25)
        self.cuadroApellido_B.grid(row=4, column=4, padx=10, pady=10)
        self.cuadroApellido_B.config(justify="center")

        self.logo=PhotoImage(file="logo.gif")
        self.fondo=Label(self.miFrame_Campos,image=self.logo)
        self.fondo.grid(row=4, column=5, padx=10, pady=10,rowspan=2)

        #-----------------Visor de Volantes-----------------------
        self.miFrame_Volantes = Frame(self,bg="gray")
        self.miFrame_Volantes.pack()

        self.tituloLabel=Label(self.miFrame_Volantes,text="VOLANTES",fg="gray",bg="white",font=("Times New Roman",20))
        self.tituloLabel.grid(row=0, column=0, padx=10, pady=10,sticky="we",columnspan=3)

        self.treeVolantes = ttk.Treeview(self.miFrame_Volantes,columns = ("id_paciente","tipo","volante","patologia","tratamiento","total"))

        self.treeVolantes.grid(row=1,column=1,padx=10,pady=10,rowspan=3)
        self.treeVolantes['show']='headings'
        self.treeVolantes.heading('#0', text='column0', anchor=tk.W)
        self.treeVolantes.heading('#1', text='ID', anchor=tk.W)
        self.treeVolantes.heading('#2', text='TIPO', anchor=tk.W)
        self.treeVolantes.heading('#3', text='VOLANTE', anchor=tk.W)
        self.treeVolantes.heading('#4', text='PATOLOGIA', anchor=tk.W)
        self.treeVolantes.heading('#5', text='TRATAMIENTO', anchor=tk.W)
        self.treeVolantes.heading('#6', text='TOTAL', anchor=tk.W)
        
        self.treeVolantes.column('#0',width=30,minwidth=30,stretch=tk.YES)
        self.treeVolantes.column('#1',width=20,minwidth=20,stretch=tk.YES)
        self.treeVolantes.column('#2',width=100,minwidth=100,stretch=tk.YES)
        self.treeVolantes.column('#3',width=80,minwidth=80,stretch=tk.YES)
        self.treeVolantes.column('#4',width=140,minwidth=100,stretch=tk.YES)
        self.treeVolantes.column('#5',width=235,minwidth=100,stretch=tk.YES)
        self.treeVolantes.column('#6',width=50,minwidth=50,stretch=tk.YES)

        self.UpdateTreeViewVolantes(self.BuscarTodosVolantes())

        self.scrollVert2=Scrollbar(self.miFrame_Volantes,command=self.treeVolantes.yview)
        self.scrollVert2.grid(row=1,column=2,sticky="nsnew",rowspan=3)
        self.treeVolantes.config(yscrollcommand=self.scrollVert2.set)

        self.tituloLabel_Ant=Label(self.miFrame_Volantes,text="SESIONES",fg="gray",bg="white",font=("Times New Roman",20))
        self.tituloLabel_Ant.grid(row=0, column=3, padx=10, pady=10,sticky="we",columnspan=3)

        self.treeSesiones = ttk.Treeview(self.miFrame_Volantes,columns = ("id_p","fecha","pagado"))   
        self.treeSesiones.grid(row=1,column=3,padx=10,pady=10,rowspan=3)
        self.treeSesiones['show']='headings'
        self.treeSesiones.heading('#0', text='column0', anchor=tk.W)
        self.treeSesiones.heading('#1', text='ID', anchor=tk.W)
        self.treeSesiones.heading('#2', text='FECHA', anchor=tk.W)
        self.treeSesiones.heading('#3', text='PAGADO', anchor=tk.W)
        
        self.treeSesiones.column('#0',width=30,minwidth=30,stretch=tk.YES)
        self.treeSesiones.column('#1',width=20,minwidth=20,stretch=tk.YES)
        self.treeSesiones.column('#2',width=100,minwidth=100,stretch=tk.YES)
        self.treeSesiones.column('#3',width=50,minwidth=50,stretch=tk.YES)
        
        self.UpdateTreeViewSesiones(self.BuscarTodosSesiones())

        self.scrollVert2=Scrollbar(self.miFrame_Volantes,command=self.treeSesiones.yview)
        self.scrollVert2.grid(row=1,column=4,sticky="nsnew",rowspan=3)

        self.botonAgregar_lista = Button(self.miFrame_Volantes, text="Agregar", width=12,command=lambda:self.IngresarDataAntecedentes())
        self.botonAgregar_lista.grid(row=1, column=5, padx=10, pady=10,rowspan=2)

        self.botonEditar_lista = Button(self.miFrame_Volantes, text="Editar", width=12,command=lambda:self.ModificarDataAntecedentes())
        self.botonEditar_lista.grid(row=2, column=5, padx=10, pady=10,rowspan=2)
        
        self.botonDelete_lista = Button(self.miFrame_Volantes, text="Borrar", width=12,command=lambda:self.EliminarDataAntecedentes())
        self.botonDelete_lista.grid(row=3, column=5, padx=10, pady=10,rowspan=2)

    #-----------------FUNCIONES-----------------------
        
    def UpdateTreeViewVolantes(self,data):
        try:    
            print("Refresh : UpdateTreeViewVolantes")
            print(data)
            for row in self.treeVolantes.get_children():
                self.treeVolantes.delete(row)
            for row in data:
                self.treeVolantes.insert('',END, values=row)
        except Exception as err:
            print("Error: {}".format(err))

    def UpdateTreeViewSesiones(self,data):
        try:    
            print("Refresh : UpdateTreeViewSesiones")
            print(data)
            for row in self.treeSesiones.get_children():
                self.treeSesiones.delete(row)
            for row in data:
                self.treeSesiones.insert('',END, values=row)
        except Exception as err:
            print("Error: {}".format(err))

    def InsertarData(self):
        if self.id_seleccion != -1:
            listadata=self.BuscarporID(self.id_seleccion)
            if listadata is None:
                messagebox.showinfo("MedicalREC", "Paciente No encontrado")
            else:
                try:
                    data=self.leerInfoInputBox()
                    if self.Insertar(self.id_seleccion,data):
                        messagebox.showinfo("MedicalREC", "Sesion Agregada")
                    else:
                        messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")    
                except Exception as err:
                    print("Error: {}".format(err))
                    messagebox.showinfo("MedicalREC", "Error en los Datos Ingresados")
                finally:
                    self.UpdateTreeViewSesiones(self.BuscarporID(self.id_seleccion))
        else:
            messagebox.showinfo("MedicalREC", "No hay Paciente Seleccionado")          
                
    def EliminarData(self):
        data_old=self.DataSeleccionado()
        id_paciente=int(data_old[0])
        try:
            if id_paciente!=-1:
                opcion=messagebox.askyesno("Eliminar","Desea eliminar la session Selecionado?")
                # print (opcion)
                if opcion:
                    self.EliminarSesion(id_paciente,data_old)
                    self.borrarInputBox()
                    messagebox.showinfo("MedicalREC", "Sesion Eliminado")
        except Exception as err:
            print("Error: {}".format(err))
            messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")
        finally:
            self.UpdateTreeViewSesiones(self.BuscarporID(id_paciente))

    def leerInfoInputBox(self):
        print(self.cal_add.get_date())
        print(self.var.get())

        return [self.cal_add.get_date(),self.var.get()]


    def borrarInputBox(self):
        try:
            self.datacuadroNombre.set("")
            self.datacuadroApellidos.set("")
            self.datacuadroDni.set("")
            self.datacuadroTelefono.set(0)
            self.datacuadroDireccion.set("")
            self.datacuadroEdad.set(0)
            self.datacuadroDni_B.set("")
            self.R2.select()
            self.R1.deselect()

            print("MedicalREC - Se borran todos los campos")
        except Exception as err:
            print("Error: {}".format(err))

    def IdSeleccionado(self):
        try:
            miSesion=Sesiones()
            item_sesion = self.treeSesiones.focus()
            id_sesion=int(self.treeSesiones.item(item_sesion,"values")[0])
        except Exception as err:
            print("Error: {}".format(err))
            id_sesion=-1
        finally:
            print("Id seleccionado:{}".format(id_sesion))
            return id_sesion

    def DataSeleccionado(self):
        data_sesion=None
        try:
            miSesion=Sesiones()
            item_sesion = self.treeSesiones.focus()
            data_sesion=self.treeSesiones.item(item_sesion,"values")
        except Exception as err:
            print("Error: {}".format(err))
        finally:
            return data_sesion

    def CompletarData_DNI(self):
        try:
            dni=self.datacuadroDni_B.get()
            sesiones,datos=self.BuscarporDni(dni)
            print(datos)
            if datos is not None:
                self.datacuadroNombre.set(datos[1])
                self.datacuadroApellidos.set(datos[2])
                self.datacuadroDni.set(datos[3])
                self.datacuadroTelefono.set(datos[4])
                self.datacuadroDireccion.set(datos[5])
                self.datacuadroEdad.set(datos[6])
                self.id_seleccion=datos[0]
                print(self.id_seleccion)
                self.UpdateTreeViewSesiones(sesiones)
                messagebox.showinfo("MedicalREC", "Paciente Con Sesiones Encontrado")
            else:
                self.borrarInputBox()
                self.id_seleccion=-1
                self.UpdateTreeViewSesiones(sesiones)
                messagebox.showinfo("MedicalREC", "Paciente Sin Sesiones")
        except Exception as err:
            print("Error: {}".format(err))
            messagebox.showinfo("MedicalREC", "Paciente Sin Sesiones")

    def Editar(self,root,data_old,id_paciente,data_new):
        
        lista=(data_new,self.var_check.get())
        try:
            print("Data New; {}".format(lista))
            # data_old=self.leerInfoInputBox()
            if self.Modificar(id_paciente,data_old,lista):
                messagebox.showinfo("MedicalREC", "Sesion Modificada")
            else:
                messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")
                
        except Exception as err:
                print("Error: {}".format(err))
                messagebox.showinfo("MedicalREC", "Error en los Datos Ingresados")
        finally:
                self.UpdateTreeViewSesiones(self.BuscarporID(id_paciente))
                CerrarEdicion(root)
    
    def seleccionar(self,value):
        self.var_check.set(value)

    def ModificarDataUser(self):
        try:
            data_old=self.DataSeleccionado()
            id_paciente=int(data_old[0])
            edit = tk.Tk()
            edit.title("MedicalREC - Edit Sesiones")
            edit.configure(width="350", height="350")
            var_check=StringVar()
            R1_b = Radiobutton(edit, text = "Pagado", variable = var_check, value = "YES",command=lambda:self.seleccionar("YES"))
            R1_b.deselect()
            R2_b = Radiobutton(edit, text = "No Pagado", variable = var_check, value = "NO",command=lambda:self.seleccionar("NO"))
            R2_b.select()
    
            R1_b.grid(row=0,column=1,padx=10, pady=10,columnspan=2)
            R2_b.grid(row=1,column=1,padx=10, pady=10,columnspan=2)

            calendario=DateEntry(edit,dateformat=3,width=12, background='darkblue',
                                foreground='white', borderwidth=4,Calendar =2020)
            calendario.grid(row=2,column=1,padx=10, pady=10,columnspan=2)

            botonEditar = Button(edit, text="ACEPTAR ", width=12,command=lambda:self.Editar(edit,data_old,id_paciente,calendario.get_date()))
            botonEditar.grid(row=3, column=2, padx=10, pady=10,columnspan=2)
        
        except Exception as err:
                print("Error: {}".format(err))
                messagebox.showinfo("MedicalREC", "Sesion del Listado No seleccionada")


class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("MedicalREC - Gestion de Base de Datos Pacientes")
        main_window.configure(background="#00CD63")
        main_window.geometry("1024x900")
        
        self.notebook = ttk.Notebook(self)
        ttk.Style().configure("TNotebook", background="gray")
        # self.notebook.configure(height=1024,width=900)

        self.pacientes_frame = PacienteFrame(self.notebook)           
        self.notebook.add(self.pacientes_frame, text="Pacientes", padding=10)

        self.volante_frame = VolanteFrame(self.notebook)
        self.notebook.add(self.volante_frame, text="Volantes", padding=10)
        
        self.notebook.pack(padx=10, pady=10)
        self.pack()

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
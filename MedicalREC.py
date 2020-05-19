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

#########################################################################################
#-----------------FUNCIONES COMUNES A TODOS LOS FRAMES-----------------------------------
#########################################################################################

def CerrarEdicion(root):
    root.destroy()

def UpdateTreeView(self,treeName,data_encontrado):
    try:    
        # print("Refresh : UpdateTreeViewPacientes")
        for row in treeName.get_children():
            treeName.delete(row)
        for row in data_encontrado:
            treeName.insert('',END, values=row)
    except Exception as err:
        print("Error: {}".format(err))

def DataSeleccionado(self,treeName):
    data_antecedente=None
    try:
        # miSesion=Antecedentes()
        item_antecedente = treeName.focus()
        data_antecedente = treeName.item(item_antecedente,"values")
    except Exception as err:
        print("Error: {}".format(err))
    finally:
        return data_antecedente

#########################################################################################
#-----------------#PACIENTE FRAME -> (PACIENTES + ANTECEDENTES)--------------------------
#########################################################################################

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

        UpdateTreeView(self.miFrame_Pacientes,self.treePacientes,self.BuscarTodosPacientes())

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
        
        UpdateTreeView(self.miFrame_Pacientes,self.treeAntecedentes,self.BuscarTodosAntecedentes())
        
        self.scrollVert2=Scrollbar(self.miFrame_Pacientes,command=self.treeAntecedentes.yview)
        self.scrollVert2.grid(row=1,column=4,sticky="nsnew",rowspan=3)

        self.botonAgregar_lista = Button(self.miFrame_Pacientes, text="Agregar", width=12,command=lambda:self.IngresarDataAntecedentes())
        self.botonAgregar_lista.grid(row=1, column=5, padx=10, pady=10,rowspan=2)

        self.botonEditar_lista = Button(self.miFrame_Pacientes, text="Editar", width=12,command=lambda:self.ModificarDataAntecedentes())
        self.botonEditar_lista.grid(row=2, column=5, padx=10, pady=10,rowspan=2)
        
        self.botonDelete_lista = Button(self.miFrame_Pacientes, text="Borrar", width=12,command=lambda:self.EliminarDataAntecedentes())
        self.botonDelete_lista.grid(row=3, column=5, padx=10, pady=10,rowspan=2)
    
    def InsertarDataPaciente(self):
        try:
            data,resultado=self.leerInfoInputBox()
            if resultado:            
                if(self.InsertarPaciente(data)):
                    UpdateTreeView(self.miFrame_Pacientes,self.treePacientes,self.BuscarTodosPacientes())
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
                    UpdateTreeView(self.miFrame_Pacientes,self.treePacientes,self.BuscarTodosPacientes())
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
            UpdateTreeView(self.miFrame_Pacientes,self.treePacientes,self.BuscarTodosPacientes())
            UpdateTreeView(self.miFrame_Pacientes,self.treeAntecedentes,self.BuscarTodosAntecedentes())
            self.id_seleccion_paciente=-1
            self.id_seleccion_antecedente=-1
            print("MedicalREC - Se borran todos los campos")
        except Exception as err:
            print("Error: {}".format(err))

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
                UpdateTreeView(self.miFrame_Pacientes,self.treePacientes,listadata)
                UpdateTreeView(self.miFrame_Pacientes,self.treeAntecedentes,self.BuscarporIDAntecedente(self.id_seleccion_antecedente))
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
                UpdateTreeView(self.miFrame_Pacientes,self.treePacientes,listadata)
                UpdateTreeView(self.miFrame_Pacientes,self.treeAntecedentes,self.BuscarporIDAntecedente(self.id_seleccion_antecedente))
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
                    UpdateTreeView(self.miFrame_Pacientes,self.treePacientes,self.BuscarporIDPaciente(id_paciente))
                    messagebox.showinfo("MedicalREC", "Paciente Modificado")
            else:
                messagebox.showinfo("MedicalREC", "No hay Pacientes Seleccionado para Editar")
        except Exception as err:
            print("Error: {}".format(err))
            messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")
        
    def EliminarDataAntecedentes(self):
        try:
            # data_old=self.DataSeleccionadoAntecedentes()
            data_old=DataSeleccionado(self.miFrame_Pacientes,self.treeAntecedentes)
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
            UpdateTreeView(self.miFrame_Pacientes,self.treePacientes,self.BuscarporIDPaciente(self.id_seleccion_paciente))
            UpdateTreeView(self.miFrame_Pacientes,self.treeAntecedentes,self.BuscarporIDAntecedente(self.id_seleccion_antecedente))

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
                UpdateTreeView(self.miFrame_Pacientes,self.treeAntecedentes,self.BuscarporIDAntecedente(id_paciente))
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
                    edit.withdraw()
                    edit.update_idletasks() # Update "requested size" from geometry manager 
                    x = (edit.winfo_screenwidth() - edit.winfo_reqwidth())/2 
                    y = (edit.winfo_screenheight() - edit.winfo_reqheight())/2 
                    edit.geometry("+%d+%d" % (x, y)) 

                    # This seems to draw the window frame immediately, so only call deiconify() 
                    # after setting correct window position 
                    edit.deiconify() 
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
                    UpdateTreeView(self.miFrame_Pacientes,self.treeAntecedentes,self.BuscarporIDAntecedente(self.id_seleccion_antecedente))
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
                UpdateTreeView(self.miFrame_Pacientes,self.treeAntecedentes,self.BuscarporIDAntecedente(id_paciente))
                CerrarEdicion(root)

    def ModificarDataAntecedentes(self):
        try:
            data_old=DataSeleccionado(self.miFrame_Pacientes,self.treeAntecedentes)
            print(data_old)
            self.id_seleccion_antecedente=int(data_old[0])
            edit = tk.Tk()
            edit.title("MedicalREC - Edit Sesiones")
            edit.configure(width="350", height="350")
            edit.withdraw()
            edit.update_idletasks() # Update "requested size" from geometry manager 

            x = (edit.winfo_screenwidth() - edit.winfo_reqwidth())/2 
            y = (edit.winfo_screenheight() - edit.winfo_reqheight())/2 
            edit.geometry("+%d+%d" % (x, y)) 

            # This seems to draw the window frame immediately, so only call deiconify() 
            # after setting correct window position 
            edit.deiconify() 
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

##----FIN DE FRAME PACIENTES---------



#########################################################################################
#-----------------#VOLANTES FRAME -> (VOLANTE + SESIONES)--------------------------------
#########################################################################################

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

        # -----------------DEFINICION DE CUADROS----------------------
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

        #-----------------COMIENZO DE BOTONES-----------------------
        self.botonAgregar = Button(self.miFrame_Campos, text="Agregar", width=12,command=lambda:self.InsertarDataPaciente())
        self.botonAgregar.grid(row=5, column=0, padx=10, pady=10)

        self.botonEdit = Button(self.miFrame_Campos, text="Modificar", width=12,
            command=lambda:self.ModificarDataPaciente(self.id_seleccion_paciente))
        self.botonEdit.grid(row=5, column=1, padx=10, pady=10)

        self.botonDelete = Button(self.miFrame_Campos, text="Borrar", width=12,command=lambda:self.EliminarDataVolante())
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

        UpdateTreeView(self.miFrame_Volantes,self.treeVolantes,self.BuscarTodosVolantes())
        # self.UpdateTreeViewVolantes(self.BuscarTodosVolantes())

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
        self.treeSesiones.column('#3',width=55,minwidth=55,stretch=tk.YES)
        
        # self.UpdateTreeViewSesiones(self.BuscarTodosSesiones())
        UpdateTreeView(self.miFrame_Volantes,self.treeSesiones,self.BuscarTodosSesiones())

        self.scrollVert2=Scrollbar(self.miFrame_Volantes,command=self.treeSesiones.yview)
        self.scrollVert2.grid(row=1,column=4,sticky="nsnew",rowspan=3)

        self.botonAgregar_lista = Button(self.miFrame_Volantes, text="Agregar", width=12,command=lambda:self.InsertarDataSesiones())
        self.botonAgregar_lista.grid(row=1, column=5, padx=10, pady=10,rowspan=2)

        self.botonEditar_lista = Button(self.miFrame_Volantes, text="Editar", width=12,command=lambda:self.ModificarDataSesiones())
        self.botonEditar_lista.grid(row=2, column=5, padx=10, pady=10,rowspan=2)
        
        self.botonDelete_lista = Button(self.miFrame_Volantes, text="Borrar", width=12,command=lambda:self.EliminarDataSession())
        self.botonDelete_lista.grid(row=3, column=5, padx=10, pady=10,rowspan=2)

    #-----------------FUNCIONES PARA VOLANTES-----------------------
                
    def EliminarDataVolante(self):
        data_old=DataSeleccionado(self.miFrame_Volantes,self.treeVolantes)
        id_paciente=int(data_old[0])
        try:
            if id_paciente!=-1:
                opcion=messagebox.askyesno("Eliminar","Desea eliminar El Volante Selecionado?")
                if opcion:
                    self.EliminarVolante(id_paciente,data_old)
                    self.borrarInputBox()
                    messagebox.showinfo("MedicalREC", "Volante Eliminado")
        except Exception as err:
            print("Error: {}".format(err))
            messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")
        finally:
            UpdateTreeView(self.miFrame_Volantes,self.treeSesiones,self.BuscarporIDVolante(id_paciente))

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
            UpdateTreeView(self.miFrame_Volantes,self.treeVolantes,self.BuscarTodosVolantes())
            UpdateTreeView(self.miFrame_Volantes,self.treeSesiones,self.BuscarTodosSesiones())
            self.id_seleccion_volante=-1
            self.id_seleccion_sesion=-1
            self.id_seleccion_paciente=-1
            print("MedicalREC - Se borran todos los campos")
        except Exception as err:
            print("Error: {}".format(err))

    def CompletarData_DNI(self):
        try:
            pacientes=Pacientes()
            listadata=pacientes.BuscarporDniPaciente(self.datacuadroDni_B.get())
            datos=listadata[0]
            if datos is not None:
                self.datacuadroNombre.set(datos[1])
                self.datacuadroApellidos.set(datos[2])
                self.datacuadroDni.set(datos[3])
                self.datacuadroTelefono.set(datos[4])
                self.datacuadroDireccion.set(datos[5])
                self.datacuadroEdad.set(datos[6])
                self.id_seleccion_paciente=datos[0]
                self.id_seleccion_sesion=datos[0]
                self.id_seleccion_volante=datos[0]
                UpdateTreeView(self.miFrame_Volantes,self.treeVolantes,self.BuscarporIDVolante(self.id_seleccion_paciente))
                UpdateTreeView(self.miFrame_Volantes,self.treeSesiones,self.BuscarporIDSesion(self.id_seleccion_sesion))
                messagebox.showinfo("MedicalREC", "Paciente Encontrado")
            else:
                messagebox.showinfo("MedicalREC", "Paciente No Encontrado")
        except Exception as err:
            print("Error: {}".format(err))
            messagebox.showinfo("MedicalREC", "Paciente No Encontrado")

    def CompletarData_NombreyApellido(self):
        try:
            pacientes=Pacientes()
            listadata=pacientes.BuscarporNombreyApellido(self.datacuadroNombre_B.get(),self.datacuadroApellido_B.get())
            datos=listadata[0]
            if datos is not None:
                self.datacuadroNombre.set(datos[1])
                self.datacuadroApellidos.set(datos[2])
                self.datacuadroDni.set(datos[3])
                self.datacuadroTelefono.set(datos[4])
                self.datacuadroDireccion.set(datos[5])
                self.datacuadroEdad.set(datos[6])
                self.id_seleccion_paciente=datos[0]
                self.id_seleccion_sesion=datos[0]
                self.id_seleccion_volante=datos[0]
                UpdateTreeView(self.miFrame_Volantes,self.treeVolantes,self.BuscarporIDVolante(self.id_seleccion_paciente))
                UpdateTreeView(self.miFrame_Volantes,self.treeSesiones,self.BuscarporIDSesion(self.id_seleccion_sesion))
                messagebox.showinfo("MedicalREC", "Paciente Encontrado")
            else:
                messagebox.showinfo("MedicalREC", "Paciente No Encontrado")
        except Exception as err:
            print("Error: {}".format(err))
            messagebox.showinfo("MedicalREC", "Paciente No Encontrado") 
    
    #-----------------FUNCIONES PARA SESIONES-----------------------

    def EliminarDataSession(self):
        data_old=DataSeleccionado(self.miFrame_Volantes,self.treeSesiones)
        id_paciente=int(data_old[0])
        try:
            if id_paciente!=-1:
                opcion=messagebox.askyesno("Eliminar","Desea eliminar la session Selecionado?")
                if opcion:
                    self.EliminarSesion(id_paciente,data_old)
                    self.borrarInputBox()
                    messagebox.showinfo("MedicalREC", "Sesion Eliminado")
        except Exception as err:
            print("Error: {}".format(err))
            messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")
        finally:
            UpdateTreeView(self.miFrame_Volantes,self.treeSesiones,self.BuscarporID(id_paciente))

    def leerInfoInputBox(self):
        print(self.cal_add.get_date())
        print(self.var.get())

        return [self.cal_add.get_date(),self.var.get()]

    def seleccionar(self,value):
        self.var_check.set(value)

    def EditarSesion(self,root,data_old,id_paciente,data_new):
        
        lista=(data_new,self.var_check.get())
        try:
            print("Data New; {}".format(lista))
            # data_old=self.leerInfoInputBox()
            if self.ModificarSesion(id_paciente,data_old,lista):
                messagebox.showinfo("MedicalREC", "Sesion Modificada")
            else:
                messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")
                
        except Exception as err:
                print("Error: {}".format(err))
                messagebox.showinfo("MedicalREC", "Error en los Datos Ingresados")
        finally:
                UpdateTreeView(self.miFrame_Volantes,self.treeSesiones,self.BuscarporIDSesion(self.id_seleccion_sesion))
                CerrarEdicion(root)
    
    def InsertarDataSesiones(self):
        try:
            # data_old=self.DataSeleccionado()
            id_paciente=self.id_seleccion_paciente
            if id_paciente != -1:
                edit = tk.Tk()
                edit.title("MedicalREC - Ingresar Sesiones")
                edit.configure(width="350", height="350")
                edit.withdraw()
                edit.update_idletasks() # Update "requested size" from geometry manager 

                x = (edit.winfo_screenwidth() - edit.winfo_reqwidth())/2 
                y = (edit.winfo_screenheight() - edit.winfo_reqheight())/2 
                edit.geometry("+%d+%d" % (x, y)) 

                # This seems to draw the window frame immediately, so only call deiconify() 
                # after setting correct window position 
                edit.deiconify() 
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

                botonEditar = Button(edit, text="ACEPTAR ", width=12,command=lambda:self.InsertarSesion(edit,id_paciente,calendario.get_date()))
                botonEditar.grid(row=3, column=2, padx=10, pady=10,columnspan=2)
            else:
                messagebox.showinfo("MedicalREC", "No se selecciono ningun Paciente")   
        except Exception as err:
                print("Error: {}".format(err))
                messagebox.showinfo("MedicalREC", "Sesion del Listado No seleccionada")   

    def InsertarSesion(self,root,id_paciente,data_new):
        
        lista=(data_new,self.var_check.get())
        try:
            print("Data New; {}".format(lista))
            # data_old=self.leerInfoInputBox()
            if self.InsertarSesiones(id_paciente,lista):
                messagebox.showinfo("MedicalREC", "Sesion Insertada")
            else:
                messagebox.showinfo("MedicalREC", "No se Puedo Completar la Accion!!")
                
        except Exception as err:
                print("Error: {}".format(err))
                messagebox.showinfo("MedicalREC", "Error en los Datos Ingresados")
        finally:
                UpdateTreeView(self.miFrame_Volantes,self.treeSesiones,self.BuscarporIDSesion(self.id_seleccion_sesion))
                CerrarEdicion(root)
    
    def ModificarDataSesiones(self):
        try:
            # data_old=self.DataSeleccionado()
            data_old=DataSeleccionado(self.miFrame_Volantes,self.treeSesiones)
            id_paciente=int(data_old[0])
            edit = tk.Tk()
            edit.title("MedicalREC - Edit Sesiones")
            edit.configure(width="350", height="350")
            edit.withdraw()
            edit.update_idletasks() # Update "requested size" from geometry manager 

            x = (edit.winfo_screenwidth() - edit.winfo_reqwidth())/2 
            y = (edit.winfo_screenheight() - edit.winfo_reqheight())/2 
            edit.geometry("+%d+%d" % (x, y)) 

            # This seems to draw the window frame immediately, so only call deiconify() 
            # after setting correct window position 
            edit.deiconify() 
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

            botonEditar = Button(edit, text="ACEPTAR ", width=12,command=lambda:self.EditarSesion(edit,data_old,id_paciente,calendario.get_date()))
            botonEditar.grid(row=3, column=2, padx=10, pady=10,columnspan=2)
        
        except Exception as err:
                print("Error: {}".format(err))
                messagebox.showinfo("MedicalREC", "Sesion del Listado No seleccionada")


class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("MedicalREC - Gestion de Base de Datos Pacientes")
        # main_window.configure(background="#00CD63")
        main_window.configure(background="gray")
        # main_window.geometry("1980x800")
        
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
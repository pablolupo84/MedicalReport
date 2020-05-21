#IMPORTAMOS LIBRERÍAS NECESARIAS.
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from conexion import *
from clases_paciente import *
from clases_sesiones import *
from clases_antecedentes import *
from clases_volante import *
from tkcalendar import DateEntry
from datetime import date

#CREAMOS VENTANA PRINCIPAL.

class LoginApp(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Login MedicalREC")
        main_window.configure(background="gray")
        
        self.userPasswords = {
            'admin':'admin',
            'root':'root',
        }
        
        self.pestas_color="DarkGrey"
        self.nombre_usuario = StringVar() 
        self.clave = StringVar() 
        
        self.opcion=Label(main_window,text="Login MedicalREC", bg="LightGreen", font=("Calibri", 13))#ETIQUETA CON TEXTO
        self.opcion.grid(row=0, column=0, padx=10, pady=10,sticky="we",columnspan=2)
        
        self.etiqueta_nombre = Label(main_window,text="Nombre de usuario * ",width=25)
        self.etiqueta_nombre.grid(row=1, column=0, padx=10, pady=10)
        
        self.entrada_nombre = Entry(main_window,textvariable=self.nombre_usuario,width=25) #ESPACIO PARA INTRODUCIR EL NOMBRE.
        self.entrada_nombre.grid(row=1, column=1, padx=10, pady=10)
        
        self.etiqueta_clave = Label(main_window,text="Contraseña * ",width=25)
        self.etiqueta_clave.grid(row=2, column=0, padx=10, pady=10)
        
        self.entrada_clave = Entry(main_window,textvariable=self.clave, show='*',width=25) #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
        self.entrada_clave.grid(row=2, column=1, padx=10, pady=10)
        
        self.button=Button(main_window, text="Acceder", width=10, height=1,command=lambda:self.ValidarAcceso(self.userPasswords,self.entrada_nombre.get(),self.entrada_clave.get()))
        self.button.grid(row=3, column=0, padx=10, pady=10,columnspan=2)
    
    def ValidarAcceso(self,diccionario,user,password):
        resultado=False
        if user in diccionario:
            if diccionario.get(user)==password:
                print("User: {}".format(user))
                print("Password: {}".format(password))
                print("Acceso OK")
                resultado=True
            else:
                print("Pssword Incorrecta")
        else:
            print("Usuario no existente")
        return resultado
            

main_window = tk.Tk()
app = LoginApp(main_window)
app.mainloop()


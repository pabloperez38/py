from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, date, timedelta

import operaciones

ventana = Tk()

fondo = PhotoImage(file = "fondo.png")

ventana.minsize(width=800, height=600)
ventana.maxsize(width=800, height=600)
ventana.title('Sistema de pacientes - Instituto Médico Las Luciérnagas')

background = Label(image = fondo, text = "Imagen de fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

def ventana_pacientes():

    def ventana_agregar_paciente():

        def funcion_agregar_paciente():    
            if txtDNI.get() == "":
                messagebox.showinfo('Error','Ingrese el DNI del paciente', parent=agregarPaciente)
                txtDNI.focus()
            elif not txtDNI.get().isnumeric():
                messagebox.showinfo('Error', 'El DNI debe ser solo números', parent=agregarPaciente)
                txtDNI.delete(0, END)
                txtDNI.focus()            
            elif txtApellido.get() == "":
                messagebox.showinfo('Error', 'Ingrese el apellido del paciente', parent=agregarPaciente)
                txtApellido.focus()
            elif txtNombre.get() == "":
                messagebox.showinfo('Error', 'Ingrese el nombre del paciente', parent=agregarPaciente)
                txtNombre.focus()        
            elif fchFecha.get() == "":
                messagebox.showinfo('Error', 'Ingrese una fecha', parent=agregarPaciente)
                fchFecha.focus()
            elif txtNacionalidad.get() == "":
                messagebox.showinfo('Error', 'Ingrese la nacionalidad del paciente', parent=agregarPaciente)
                txtNacionalidad.focus()
            else:
                operaciones.crear_paciente(txtNombre.get(), txtApellido.get(), txtDNI.get(), fchFecha.get(), txtNacionalidad.get())

                caja_pacientes.delete(*caja_pacientes.get_children())
                lista_pacientes = operaciones.ver_pacientes()

                for p in reversed(lista_pacientes):
                    date_format = '%d/%m/%Y'
                    now = date.today().year
                    birthDay = datetime.strptime(p["fechaNacimiento"], date_format).date()
                    birthYear = int(birthDay.strftime('%Y'))                            
                    edad =  (now - birthYear)-1 

                    caja_pacientes.insert(parent='', index='end', text="", values=(p['id'], p['nombre'],p['apellido'],p['dni'],p["fechaNacimiento"],edad,p["nacionalidad"]))

                ventana_agregar_paciente.destroy()
                messagebox.showinfo('Éxito', 'Paciente agregado correctamente')

        def focus_dni(event):
            if len(txtDNI.get()) > 5:
                if operaciones.existe_paciente(txtDNI.get()) == "ok":
                    messagebox.showinfo("Error", "El paciente "+ txtDNI.get() + " ya existe", parent=agregarPaciente)
                    txtDNI.delete(0, END)
                    txtDNI.focus()
        
        ventana_agregar_paciente = Toplevel(width=500, height=430, bg="#24B8AA")
        ventana_agregar_paciente.minsize(500, 430)
        ventana_agregar_paciente.maxsize(500, 430)
        
        ventana_agregar_paciente.title("Agregar paciente")

        Label(ventana_agregar_paciente, text="Agregar paciente", font="Arial 18 bold", bg="#24B8AA", fg="#ffffff").place(x=20, y=15)

        Label(ventana_agregar_paciente, text="DNI: ", font="Arial 10 bold", bg="#24B8AA", fg="#ffffff").place(x = 20,y = 60)
        dni = StringVar()
        txtDNI = Entry(ventana_agregar_paciente, font="Arial 12", textvariable=dni)    
        txtDNI.place(x = 20,y = 80, width=400,height=30)
        txtDNI.bind("<FocusOut>", focus_dni)

        Label(ventana_agregar_paciente, text="Nombre: ", font="Arial 10 bold", bg="#24B8AA", fg="#ffffff").place(x = 20,y = 120)
        nombre = StringVar()
        txtNombre = Entry(ventana_agregar_paciente, font="Arial 12", textvariable=nombre)
        txtNombre.place(x = 20,y = 140, width=400,height=30)
        
        Label(ventana_agregar_paciente, text="Apellido: ", font="Arial 10 bold", bg="#24B8AA", fg="#ffffff").place(x = 20,y = 180)
        apellido = StringVar()
        txtApellido = Entry(ventana_agregar_paciente, font="Arial 12", textvariable=apellido)
        txtApellido.place(x = 20,y = 200, width = 400,height = 30) 

        Label(ventana_agregar_paciente, text="Fecha de nacimiento: ", font="Arial 10 bold", bg="#24B8AA", fg="#ffffff").place(x = 20,y = 240)
        fecha = StringVar()   
        fchFecha = Entry(ventana_agregar_paciente, font="Arial 12", textvariable=fecha)
        fchFecha.place(x = 20,y = 260, width=400,height=30)

        Label(ventana_agregar_paciente, text="Nacionalidad: ", font="Arial 10 bold", bg="#24B8AA", fg="#ffffff").place(x = 20,y = 300)        
        nacionalidad = StringVar()
        txtNacionalidad = Entry(ventana_agregar_paciente, font="Arial 12", textvariable=nacionalidad)
        txtNacionalidad.place(x = 20,y = 320, width = 400,height = 30)

        #boton agregar paciente
        agregarPaciente = Button(ventana_agregar_paciente, text = "AGREGAR", width=12, height= 2, bg="#296472", fg="white",font="Arial 10 bold", command=funcion_agregar_paciente)
        agregarPaciente.place(x = 200, y=370)

    def ventana_actualizar_paciente():

        try:            
            selected = caja_pacientes.focus()            
            valor = caja_pacientes.item(selected, 'values')
         
            if valor == "":
                 messagebox.showinfo('Error', 'Debe seleccionar un paciente')
            else:
                def funcion_actualizar_paciente():
                    #controlar datos
                    if txtNombre.get() == "":
                        messagebox.showinfo('Error', 'Ingrese el nombre del paciente', parent=editar_paciente)
                        txtNombre.focus()                 
                    elif txtApellido.get() == "":
                        messagebox.showinfo('Error', 'Ingrese el apellido del paciente', parent=editar_paciente)
                        txtApellido.focus()                          
                    elif fchFecha.get() == "":
                        messagebox.showinfo('Error', 'Ingrese una fecha', parent=editar_paciente)
                        fchFecha.focus()
                    elif txtNacionalidad.get() == "":
                        messagebox.showinfo('Error', 'Ingrese la nacionalidad del paciente', parent=editar_paciente)
                        txtNacionalidad.focus()
                    else:
                        operaciones.actualizar_paciente(txtNombre.get(), txtApellido.get(), txtDNI.get(), fchFecha.get(), txtNacionalidad.get(), valor[0])                        

                        caja_pacientes.delete(*caja_pacientes.get_children())
                        lista_pacientes = operaciones.ver_pacientes()

                        for p in reversed(lista_pacientes):                    
                            caja_pacientes.insert(parent='', index='end', text="", values=(p['id'], p['nombre'],p['apellido'],p['dni'],p["fechaNacimiento"],edad,p["nacionalidad"]))

                        editar_paciente.destroy()
                        messagebox.showinfo('Éxito', 'El paciente se actualizó correctamente')

                def focus_dni(event):
                    if len(txtDNI.get()) > 5:
                        if operaciones.existe_paciente(txtDNI.get()) == "ok":
                            messagebox.showinfo("Error", "El paciente "+ txtDNI.get() + " ya existe", parent=editar_paciente)
                            txtDNI.delete(0, END)
                            txtDNI.focus()

                editar_paciente = Toplevel(width=500, height=430, bg="#24B8AA")
                editar_paciente.minsize(500, 430)
                editar_paciente.maxsize(500, 430)
                      
                editar_paciente.title("Actualizar paciente")

                Label(editar_paciente, text="Actualizar paciente", font="Arial 18 bold", bg="#24B8AA", fg="#ffffff").place(x=20, y=15)

                Label(editar_paciente, text="DNI: ", font="Arial 10 bold", bg="#24B8AA", fg="#ffffff").place(x = 20,y = 60)
                dni = StringVar()
                txtDNI = Entry(editar_paciente, font="Arial 12", textvariable=StringVar(editar_paciente,value=valor[3]),state=DISABLED)    
                txtDNI.place(x = 20,y = 80, width=400,height=30)
                txtDNI.bind("<FocusOut>", focus_dni)

                Label(editar_paciente, text="Nombre: ", font="Arial 10 bold", bg="#24B8AA", fg="#ffffff").place(x = 20,y = 120)
                txtNombre = Entry(editar_paciente, textvariable=StringVar(editar_paciente,value=valor[1]), font="Arial 12")
                txtNombre.place(x = 20,y = 140, width=400,height=30)
                
                Label(editar_paciente, text="Apellido: ", font="Arial 10 bold", bg="#24B8AA", fg="#ffffff").place(x = 20,y = 180)

                txtApellido = Entry(editar_paciente, font="Arial 12", textvariable=StringVar(editar_paciente,value=valor[2]))
                txtApellido.place(x = 20,y = 200, width = 400,height = 30) 

                Label(editar_paciente, text="Fecha de nacimiento: ", font="Arial 10 bold", bg="#24B8AA", fg="#ffffff").place(x = 20,y = 240)
                fchFecha = Entry(editar_paciente, font="Arial 12", textvariable=StringVar(editar_paciente,value=valor[4]))
                fchFecha.place(x = 20,y = 260, width=400,height=30)

                Label(editar_paciente, text="Nacionalidad: ", font="Arial 10 bold", bg="#24B8AA", fg="#ffffff").place(x = 20,y = 300)        
                txtNacionalidad = Entry(editar_paciente, textvariable=StringVar(editar_paciente,value=valor[6]), font="Arial 12")
                txtNacionalidad.place(x = 20,y = 320, width = 400,height = 30)

                editarPaciente = Button(editar_paciente, text = "ACTUALIZAR", width=12, height= 2, bg="#296472", fg="white",font="Arial 10 bold", command=funcion_actualizar_paciente)
                editarPaciente.place(x = 200, y=370)    

        except IndexError:
            pass       

    def funcion_eliminar_paciente():
        try:            
            selected = caja_pacientes.focus()            
            valor = caja_pacientes.item(selected, 'values')

            if valor == "":
                messagebox.showinfo('Error', 'Debe seleccionar un paciente')
            else:
                #pregunto si deseo eliminar paciente
                eliminar_paciente = messagebox.askquestion(message="¿Desea eliminar el paciente?", title="Eliminar")
                if eliminar_paciente == "yes":
                    operaciones.eliminar_paciente(valor[0])                    

                    caja_pacientes.delete(*caja_pacientes.get_children())
                    lista_pacientes = operaciones.ver_pacientes()

                    for p in reversed(lista_pacientes):
                        date_format = '%d/%m/%Y'
                        now = date.today().year
                        birthDay = datetime.strptime(p["fechaNacimiento"], date_format).date()
                        birthYear = int(birthDay.strftime('%Y'))                            
                        edad =  (now - birthYear)-1                
                        caja_pacientes.insert(parent='', index='end', text="", values=(p['id'], p['nombre'],p['apellido'],p['dni'],p["fechaNacimiento"],edad,p["nacionalidad"]))
                    messagebox.showinfo('Éxito', 'Paciente eliminado correctamente')
                             
        except IndexError:
                pass        

    ocultarFrame()    
    pacientes.pack(fill="both", expand=1)
    Label(pacientes, text="Listado de pacientes", font="Arial 18 bold", bg="#24B8AA", fg="#ffffff").place(x=20, y=20)

    #treeview pacientes
    caja_pacientes = ttk.Treeview(pacientes, height=15)
    caja_pacientes["columns"] = ("#", "Nombre", "Apellido", "DNI", "Fecha de Nacimiento", "Edad" ,"Nacionalidad")
    caja_pacientes.column("#0", width=0, minwidth=0)
    caja_pacientes.column("#", width=40, minwidth=0)
    caja_pacientes.column("Nombre", width=115, minwidth=0)
    caja_pacientes.column("Apellido",width=115, minwidth=0)
    caja_pacientes.column("DNI", width=100, minwidth=0)
    caja_pacientes.column("Fecha de Nacimiento", width=130, minwidth=0)
    caja_pacientes.column("Edad", width=40, minwidth=0)
    caja_pacientes.column("Nacionalidad", width=200, minwidth=0)

    caja_pacientes.heading("#0", text="")
    caja_pacientes.heading("#", text="#")
    caja_pacientes.heading("Nombre", text="Nombre")
    caja_pacientes.heading("Apellido", text="Apellido")
    caja_pacientes.heading("DNI", text="DNI")
    caja_pacientes.heading("Fecha de Nacimiento", text="Fecha de Nacimiento")
    caja_pacientes.heading("Edad", text="Edad")
    caja_pacientes.heading("Nacionalidad", text="Nacionalidad")

    lista_pacientes = operaciones.ver_pacientes()

    for p in reversed(lista_pacientes):
        date_format = '%d/%m/%Y'
        now = date.today().year
        birthDay = datetime.strptime(p["fechaNacimiento"], date_format).date()
        birthYear = int(birthDay.strftime('%Y'))                            
        edad =  (now - birthYear)-1

        caja_pacientes.insert(parent='', index='end', text="", values=(p['id'], p['nombre'],p['apellido'],p['dni'],p["fechaNacimiento"],edad,p["nacionalidad"]))        

    caja_pacientes.place(x = 20,y = 60)    
    #caja_pacientes.bind("<Double-Button-1>", seleccionar_paciente)
    #-----------------------------------------------------
    scroll = ttk.Scrollbar(pacientes, orient="vertical", command= caja_pacientes.yview)
    caja_pacientes.configure(yscroll= scroll.set)
    scroll.place(x = 750,y = 61, height=325)
    Button(pacientes, text = 'AGREGAR', font="Arial 10 bold", width=12, height= 2, bg="#296472", fg="white", command = ventana_agregar_paciente).place(x = 220,y = 400)
    Button(pacientes, text = 'EDITAR', font="Arial 10 bold", width=12, height= 2, bg="#296472", fg="white", command = ventana_actualizar_paciente).place(x = 340,y = 400)
    Button(pacientes, text = 'ELIMINAR', font="Arial 10 bold", width=12, height= 2, bg="#296472", fg="white", command = funcion_eliminar_paciente).place(x = 460,y = 400)

def ventana_buscar_pacientes():
   
    ocultarFrame()
    buscar_pacientes.pack(fill="both", expand=1)
    def buscar_por_fecha(start, stop):
        #transformar fecha

        dia1 = datetime.strptime(start, '%d/%m/%Y')
        dia2 = datetime.strptime(stop, '%d/%m/%Y')        
        
        global dates
        dates = []
        diff = (dia2-dia1).days
        for i in range(diff+1):
            day = dia1 + timedelta(days=i)
            dates.append(day)
        if dates:

            historias = operaciones.ver_historias()            
            caja_buscar.delete(*caja_buscar.get_children())    
            for h in reversed(historias):
               
                if h["fecha"] >= start and h["fecha"] <= stop:   
                    paciente = operaciones.traer_datos_paciente(h["paciente"])
                    date_format = '%d/%m/%Y'
                    now = date.today().year
                    birthDay = datetime.strptime(paciente["fechaNacimiento"], date_format).date()
                    birthYear = int(birthDay.strftime('%Y'))                    
                    edad =  (now - birthYear)-1
                    
                    caja_buscar.insert(parent='', index='end', text="", values=(paciente["id"],paciente["nombre"],paciente["apellido"],paciente["dni"], paciente["fechaNacimiento"], edad, paciente["nacionalidad"]))         
                
                    buscar_paciente.delete(0, END)
        
        else:
            messagebox.showinfo('Error', 'La segunda fecha debe ser mayor a la primera')    

    def buscar(event, termino):
       
        if termino:
            if radio.get() == 1:

                if termino.isnumeric():
                    messagebox.showinfo('Error', 'No debe ingresar números')
                    buscar_paciente.delete(0, END)
                    buscar_paciente.focus()
                else:
    
                    paciente = operaciones.buscador(radio.get())            
                    caja_buscar.delete(*caja_buscar.get_children())    
                    for h in reversed(paciente):
                          
                        if(h["nombre"].lower().find(termino.lower()) != -1):
                            date_format = '%d/%m/%Y'
                            now = date.today().year
                            birthDay = datetime.strptime(h["fechaNacimiento"], date_format).date()
                            birthYear = int(birthDay.strftime('%Y'))                            
                            edad =  (now - birthYear)-1                            
                            caja_buscar.insert(parent='', index='end', text="", values=(h["id"],h["nombre"],h["apellido"],h["dni"], h["fechaNacimiento"], edad, h["nacionalidad"]))         
                        
                            buscar_paciente.delete(0, END)

            elif radio.get() == 2:

                if termino.isnumeric():
                    messagebox.showinfo('Error', 'No debe ingresar números')
                    buscar_paciente.delete(0, END)
                    buscar_paciente.focus()
                else:
       
                    paciente = operaciones.buscador(radio.get())            
                    caja_buscar.delete(*caja_buscar.get_children())    
                    for h in reversed(paciente):
                          
                        if(h["apellido"].lower().find(termino.lower()) != -1):
                            date_format = '%d/%m/%Y'
                            now = date.today().year
                            birthDay = datetime.strptime(h["fechaNacimiento"], date_format).date()
                            birthYear = int(birthDay.strftime('%Y'))                            
                            edad =  (now - birthYear)-1
                            
                            caja_buscar.insert(parent='', index='end', text="", values=(h["id"],h["nombre"],h["apellido"],h["dni"], h["fechaNacimiento"], edad, h["nacionalidad"]))         
                        
                            buscar_paciente.delete(0, END)

            elif radio.get() == 3:

                if not termino.isnumeric():
                    messagebox.showinfo('Error', 'Debe ingresar números')
                    buscar_paciente.delete(0, END)
                    buscar_paciente.focus()         
                else:                   

                    paciente = operaciones.buscador(radio.get())            
                    caja_buscar.delete(*caja_buscar.get_children())    
                    for h in reversed(paciente):
                          
                        if(h["dni"].find(termino) != -1):
                            date_format = '%d/%m/%Y'
                            now = date.today().year
                            birthDay = datetime.strptime(h["fechaNacimiento"], date_format).date()
                            birthYear = int(birthDay.strftime('%Y'))                            
                            edad =  (now - birthYear)-1                            
                            caja_buscar.insert(parent='', index='end', text="", values=(h["id"],h["nombre"],h["apellido"],h["dni"], h["fechaNacimiento"], edad, h["nacionalidad"]))         
                        
                            buscar_paciente.delete(0, END)

            elif radio.get() == 4:

                buscar_por_fecha(date1, date2)                

            elif radio.get() == 5:

                if termino.isnumeric():
                    messagebox.showinfo('Error', 'No debe ingresar números')
                    buscar_paciente.delete(0, END)
                    buscar_paciente.focus()
                else:                     
                    enfermedad = operaciones.buscador(radio.get())        
                    caja_buscar.delete(*caja_buscar.get_children())    
                    for h in reversed(enfermedad):
                        if(h["enfermedad"].lower().find(termino.lower()) != -1):
                            #dependiendo la enfermedad, traemos pacientes
                            pacientes = operaciones.ver_pacientes()
                            for p in pacientes:
                                if p["id"] == h["paciente"]:

                                    date_format = '%d/%m/%Y'
                                    now = date.today().year
                                    birthDay = datetime.strptime(p["fechaNacimiento"], date_format).date()
                                    birthYear = int(birthDay.strftime('%Y'))                            
                                    edad =  (now - birthYear)-1
                            
                                    caja_buscar.insert(parent='', index='end', text="", values=(p["id"],p["nombre"],p["apellido"],p["dni"], p["fechaNacimiento"], edad, p["nacionalidad"]))         
                        
                            buscar_paciente.delete(0, END)
            else:
                if termino.isnumeric():
                    messagebox.showinfo('Error', 'No debe ingresar números')
                    buscar_paciente.delete(0, END)
                    buscar_paciente.focus()
                else:       
                    medico = operaciones.buscador(radio.get())        
                    caja_buscar.delete(*caja_buscar.get_children())
                    for m in reversed(medico):                    
                        if(m["nombre"].lower().find(termino.lower()) != -1):
                            #dependiendo el medico, traemos las historias asociadas
                            historias = operaciones.ver_historias()
                            for h in historias:                                                           
                                if h["medico"] == m["id"]:
                                    #si hay conicidencia, traigo fatos del paciente atendido
                                    pacientes = operaciones.ver_pacientes()
                                    for p in pacientes:
                                        #if p["id"] == h["id"]:
                                        date_format = '%d/%m/%Y'
                                        now = date.today().year
                                        birthDay = datetime.strptime(p["fechaNacimiento"], date_format).date()
                                        birthYear = int(birthDay.strftime('%Y'))                            
                                        edad =  (now - birthYear)-1
                                        
                                        caja_buscar.insert(parent='', index='end', text="", values=(p["id"],p["nombre"],p["apellido"],p["dni"], p["fechaNacimiento"], edad, p["nacionalidad"]))         
                                
                                        buscar_paciente.delete(0, END)
                
        else:
            messagebox.showinfo('Error', 'Introduce un término a buscar')
            buscar_paciente.focus()   

    Label(buscar_pacientes, text="Buscar pacientes", font="Arial 18 bold", bg="#24B8AA", fg="#ffffff").place(x=20, y=20)
    Label(buscar_pacientes, text="", font="Arial 10",borderwidth=1, relief="solid", padx=11, pady=11, width=90, justify="left").place(x=20, y=60)
    Label(buscar_pacientes, text="Seleccionar opción", font="Arial 10 bold").place(x=22, y=67)
    radio = IntVar()
    #radio.set("1")
    boton1 = Radiobutton(buscar_pacientes, text='Por nombre',variable=radio, value=1, command=lambda:[ buscar_paciente.place(x = 20,y = 105, width=340,height=30),date1.place_forget(), date2.place_forget(),boton_buscar.place_forget()])

    boton1.place(x=180, y=67) 

    boton2 = Radiobutton(buscar_pacientes, text='Por apellido',variable=radio, value=2, command=lambda:[ buscar_paciente.place(x = 20,y = 105, width=340,height=30),date1.place_forget(), date2.place_forget(),boton_buscar.place_forget()])

    boton2.place(x=280, y=67)

    boton3 = Radiobutton(buscar_pacientes, text='Por DNI',variable=radio, value=3, command=lambda:[ buscar_paciente.place(x = 20,y = 105, width=340,height=30),date1.place_forget(), date2.place_forget(),boton_buscar.place_forget()])
    
    boton3.place(x=380, y=67)

    boton4 = Radiobutton(buscar_pacientes, text='Por fecha',variable=radio, value=4, command=lambda:[date1.place(x = 20,y = 110, width = 120,height = 30), date2.place(x = 150,y = 110, width = 120,height = 30),boton_buscar.place(x = 280,y = 112), buscar_paciente.place_forget()])
    boton4.place(x=450, y=67)

    boton5 = Radiobutton(buscar_pacientes, text='Por enfermedad',variable=radio, value=5, command=lambda:[date1.place_forget(), date2.place_forget(), buscar_paciente.place(x = 20,y = 105, width=340,height=30),boton_buscar.place_forget()])
    boton5.place(x=540, y=67)

    boton6 = Radiobutton(buscar_pacientes, text='Por médico',variable=radio, value=6, command=lambda:[date1.place_forget(), date2.place_forget(), buscar_paciente.place(x = 20,y = 105, width=340,height=30),boton_buscar.place_forget()])
    boton6.place(x=670, y=67)

    # #buscar = StringVar()
    buscar_paciente = Entry(buscar_pacientes, font="Arial 12", textvariable=buscar)
    buscar_paciente.bind('<Return>', (lambda event: buscar(event, buscar_paciente.get())))
    
    date1 = Entry(buscar_pacientes, font="Arial 12")  
    date2 = Entry(buscar_pacientes, font="Arial 12")  
   
    boton_buscar = Button(buscar_pacientes,text='BUSCAR',command=lambda: buscar_por_fecha(date1.get(),date2.get()),font="Arial 8 bold", width=8, height= 1, bg="#296472", fg="white")
    
    ############################tree historias#####################################

    caja_buscar = ttk.Treeview(buscar_pacientes, height=10)
    caja_buscar["columns"] = ("#", "Nombre", "Apellido", "DNI", "Fecha de Nac.", "Edad" ,"Nacionalidad")
    caja_buscar.column("#0", width=0, minwidth=0)
    caja_buscar.column("#", width=40, minwidth=0)
    caja_buscar.column("Nombre", width=120, minwidth=0)
    caja_buscar.column("Apellido",width=120, minwidth=0)
    caja_buscar.column("DNI", width=100, minwidth=0)
    caja_buscar.column("Fecha de Nac.", width=130, minwidth=0)
    caja_buscar.column("Edad", width=40, minwidth=0)
    caja_buscar.column("Nacionalidad", width=220, minwidth=0)

    caja_buscar.heading("#0", text="", anchor=CENTER)
    caja_buscar.heading("#", text="#", anchor=CENTER)
    caja_buscar.heading("Nombre", text="Nombre", anchor=CENTER)
    caja_buscar.heading("Apellido", text="Apellido", anchor=CENTER)
    caja_buscar.heading("DNI", text="DNI", anchor=CENTER)
    caja_buscar.heading("Fecha de Nac.", text="Fecha de Nac.", anchor=CENTER)
    caja_buscar.heading("Edad", text="Edad", anchor=CENTER)
    caja_buscar.heading("Nacionalidad", text="Nacionalidad", anchor=CENTER)

    caja_buscar.place(x = 20,y = 180)

def ventana_historias():
    ocultarFrame()   

    def detalle_historias(event):
        selected = cajaHistorias.focus()
        valor = cajaHistorias.item(selected, 'values')
        ver_pacientes = operaciones.ver_pacientes()        
        for p in ver_pacientes: 
                  
            if p["id"] == int(valor[1]):
                for h in p["historias"]:
                    
                    if h["id"] == int(valor[0]):

                        detalle_historia = h["descripcion"]

                #datos del paciente
                paciente = operaciones.traer_datos_paciente(int(valor[1]))
                nombre_paciente = paciente["nombre"]+" "+paciente["apellido"]
                #datos del médico
                nombre_medico = valor[2]                
                ver_historia = Toplevel(width=450, height=380, bg="#24B8AA")
                ver_historia.minsize(450, 380)
                ver_historia.maxsize(450, 380)

                def cerrar_historia():
                    ver_historia.destroy()

                ver_historia.title("Ver detalle historia clínica")
                Label(ver_historia, text="Fecha: "+valor[3], font="Arial 16 bold", bg="#24B8AA", fg="white").place(x=20, y=20)
                Label(ver_historia, text="Paciente: "+nombre_paciente, font="Arial 16 bold", bg="#24B8AA", fg="white").place(x=20, y=70)
                Label(ver_historia, text="Médico: "+nombre_medico, font="Arial 16 bold", bg="#24B8AA", fg="white").place(x=20, y=120)
                Label(ver_historia, text="Enfermedad: "+valor[4], font="Arial 16 bold", bg="#24B8AA", fg="white").place(x=20, y=170)
                Label(ver_historia, text="Observaciones: "+detalle_historia, font="Arial 16 bold", bg="#24B8AA", fg="white", wraplength=450).place(x=20, y=220)
                Button(ver_historia, text = 'CERRAR', font="Arial 10 bold", width=12, height= 2, bg="#296472", fg="white", command = cerrar_historia).place(x = 170,y = 320)

    def seleccionar_historias(event):
        try:
            global valor        
            selected = caja_pacientes.focus()
            valor = caja_pacientes.item(selected, 'values')
            ver_historias = operaciones.ver_historias()            
            cajaHistorias.delete(*cajaHistorias.get_children())

            for h in reversed(ver_historias):           
                if h["id"] == int(valor[0]):
                    for historia in h["historias"]:
                        medico = operaciones.traer_datos_medico(historia["medico"])
                        nombre_medico = medico["nombre"]+" "+medico["apellido"]
                        cajaHistorias.insert(parent='', index='end', text="", values=(historia["id"], valor[0],nombre_medico,historia["fecha"],historia["enfermedad"]))

        except IndexError:
            pass

    def funcion_agregar_historia():       
                    
        try:
            global valor
            
            selected = caja_pacientes.focus()
            valor = caja_pacientes.item(selected, 'values')
            if selected == "":
                messagebox.showinfo('Error', 'Debe seleccionar un paciente') 
            else:
                
                def funcion_guardar_historia():
                    if combo.get() == "":
                        messagebox.showinfo('Error', 'Seleccione el médico', parent=agregar_historia)
                        combo.focus()
                    elif txtEnfermedad.get() == "":
                        messagebox.showinfo('Error', "Ingrese una enfermedad", parent=agregar_historia)
                        txtEnfermedad.focus()
                    
                    else:                        
                        fecha = datetime.today().strftime('%d/%m/%Y')                        
                        operaciones.crear_historia(int(valor[0]), combo.get(),fecha, txtEnfermedad.get(), txtDescripcion.get("1.0","end"))

                        agregar_historia.destroy()                        
                        messagebox.showinfo('Éxito', 'Historia agregada correctamente')

                        ver_historias = operaciones.ver_historias()            
                        cajaHistorias.delete(*cajaHistorias.get_children())

                        for h in reversed(ver_historias):           
                            if h["id"] == int(valor[0]):
                                for historia in h["historias"]:
                                    medico = operaciones.traer_datos_medico(historia["medico"])
                                    nombre_medico = medico["nombre"]+" "+medico["apellido"]
                                    cajaHistorias.insert(parent='', index='end', text="", values=(historia["id"], valor[0],nombre_medico,historia["fecha"],historia["enfermedad"]))              
                
                agregar_historia = Toplevel(width=450, height=380, bg="#24B8AA")
                paciente = valor[1] +" "+ valor[2]
                agregar_historia.minsize(450, 380)
                agregar_historia.maxsize(450, 380)
                agregar_historia.title("Agregar historia")
                Label(agregar_historia, text="Paciente:", font="Arial 16 bold", bg="#24B8AA", fg="white").place(x=20, y=20)
                Label(agregar_historia, text=paciente, font="Arial 16 bold", bg="#24B8AA", fg="white").place(x=130, y=20)
                Label(agregar_historia, text="Médico:", font="Arial 12 bold", bg="#24B8AA", fg="white").place(x=20, y=60)
                txtMedico = StringVar()
                listaMedicos = []
                medicos = operaciones.ver_medicos()
                for p in medicos:
                    medico = p["nombre"], p["apellido"]
                    listaMedicos.append(medico)
                combo = ttk.Combobox(agregar_historia, textvariable=txtMedico, values=listaMedicos, state="readonly")
                combo.bind("<<ComboboxSelected>>")
                combo.place(x = 20,y = 85, width = 410,height = 30)

                Label(agregar_historia, text="Enfermedad:", font="Arial 12 bold", bg="#24B8AA", fg="white").place(x=20, y=125)
                enfermedad = StringVar()
                txtEnfermedad = Entry(agregar_historia, textvariable=enfermedad, font="Arial 12")
                txtEnfermedad.place(x=20, y=150,width = 410,height = 30)
                
                Label(agregar_historia, text="Descripción:", font="Arial 12 bold", bg="#24B8AA", fg="white").place(x=20, y=195)

                txtDescripcion = Text(agregar_historia, width=45, height=5,font =("Arial","12"))
                txtDescripcion.place(x=20, y=220)

                Button(agregar_historia, text = 'GUARDAR', font="Arial 10 bold", width=12, height= 2, bg="#296472", fg="white", command = funcion_guardar_historia).place(x = 170,y = 320)         
            
        except IndexError:
            pass
    
    historias.pack(fill="both", expand=1)
    Label(historias, text="Historias clínicas", font="Arial 18 bold", bg="#24B8AA", fg="#ffffff").place(x=20, y=20)
    caja_pacientes = ttk.Treeview(historias, height=10)
    caja_pacientes["columns"] = ("#", "Nombre", "Apellido", "DNI", "Fecha de Nacimiento" ,"Nacionalidad")
    caja_pacientes["displaycolumns"]= ("#", "Nombre", "Apellido", "DNI", "Fecha de Nacimiento" ,"Nacionalidad")
    caja_pacientes.column("#0", width=0, minwidth=0)
    caja_pacientes.column("#", width=40, minwidth=0)
    caja_pacientes.column("Nombre", width=120, minwidth=0)
    caja_pacientes.column("Apellido",width=120, minwidth=0)
    caja_pacientes.column("DNI", width=100, minwidth=0)
    caja_pacientes.column("Fecha de Nacimiento", width=130, minwidth=0)
    caja_pacientes.column("Nacionalidad", width=220, minwidth=0)

    caja_pacientes.heading("#0", text="")
    caja_pacientes.heading("#", text="#")    
    caja_pacientes.heading("Nombre", text="Nombre")
    caja_pacientes.heading("Apellido", text="Apellido")
    caja_pacientes.heading("DNI", text="DNI")
    caja_pacientes.heading("Fecha de Nacimiento", text="Fecha de Nacimiento")
    caja_pacientes.heading("Nacionalidad", text="Nacionalidad")

    lista_pacientes = operaciones.ver_pacientes()

    for p in reversed(lista_pacientes):        
        caja_pacientes.insert(parent='', index='end', text="", values=(p['id'], p['nombre'],p['apellido'],p['dni'],p["fechaNacimiento"],p["nacionalidad"]))

    caja_pacientes.place(x = 20,y = 60)    
    caja_pacientes.bind("<Double-Button-1>", seleccionar_historias)
    scroll = ttk.Scrollbar(historias, orient="vertical", command= caja_pacientes.yview)
    caja_pacientes.configure(yscroll= scroll.set)
    scroll.place(x = 750,y = 61, height=225)
    Button(historias, text = 'AGREGAR', font="Arial 10 bold", width=12, height= 2, bg="#296472", fg="white", command = funcion_agregar_historia).place(x = 660,y = 350)

    ############################tree historias#####################################
    Label(historias, text="Listado de historias clínicas", font="Arial 16 bold", bg="#24B8AA", fg="#ffffff").place(x=20, y=320)
    cajaHistorias = ttk.Treeview(historias, height=10)
    cajaHistorias["columns"] = ("#", "id", "Médico", "Fecha", "Enfermedad")
    cajaHistorias.column("#0", width=0, minwidth=0)
    cajaHistorias.column("#", width=40, minwidth=0)
    cajaHistorias.column("id", width=0, minwidth=0)
    cajaHistorias.column("Médico",width=150, minwidth=0)
    cajaHistorias.column("Fecha", width=100, minwidth=0)
    cajaHistorias.column("Enfermedad", width=280, minwidth=0)

    cajaHistorias.heading("#0", text="")
    cajaHistorias.heading("#", text="#")
    cajaHistorias.heading("id", text="id")
    cajaHistorias.heading("Médico", text="Médico")
    cajaHistorias.heading("Fecha", text="Fecha")
    cajaHistorias.heading("Enfermedad", text="Enfermedad")

    cajaHistorias.place(x = 20,y = 350)
    cajaHistorias.bind("<Double-Button-1>", detalle_historias)

def ventana_medicos():
   
    def ventana_agregar_medico():

        def funcion_agregar_medico():
            if txtNombre.get() == "":
                messagebox.showinfo('Error', 'Ingrese el nombre del médico', parent=ventana_agregar_medico)
                txtNombre.focus()
            elif txtApellido.get() == "":
                messagebox.showinfo('Error', 'Ingrese el apellido del médico', parent=ventana_agregar_medico)
                txtApellido.focus()
            elif txtEspecialidad.get() == "":
                messagebox.showinfo('Error', 'Ingrese la especialidad del médico', parent=ventana_agregar_medico)
                txtEspecialidad.focus()
            else:
                operaciones.crear_medico(txtNombre.get(), txtApellido.get(), txtEspecialidad.get())
                caja_medicos.delete(*caja_medicos.get_children())               

                lista_medicos = operaciones.ver_medicos()
                for l in reversed(lista_medicos):
                    caja_medicos.insert(parent='', index='end', text="", values=(l['id'], l['nombre'],l['apellido'],l['especialidad']))

                ventana_agregar_medico.destroy()
                messagebox.showinfo('Éxito', 'El médico se guardó correctamente')

        ventana_agregar_medico = Toplevel(width=500, height=250, bg="#24B8AA")
        ventana_agregar_medico.minsize(500, 250)
        ventana_agregar_medico.maxsize(500, 250)
        
        ventana_agregar_medico.title("Editar médico")

        Label(ventana_agregar_medico, text="Nombre: ", font="Arial 10 bold", bg="#24B8AA", fg="#ffffff").place(x = 20,y = 20)
        Label(ventana_agregar_medico, text="Apellido: ", font="Arial 10 bold", bg="#24B8AA", fg="#ffffff").place(x = 20,y = 55)
        Label(ventana_agregar_medico, text="Especialidad: ", font="Arial 10 bold", bg="#24B8AA", fg="#ffffff").place(x = 20,y = 95)
        #entradas       
       
        nombre = StringVar()
        txtNombre = Entry(ventana_agregar_medico, textvariable=nombre ,font="Arial 12")
        txtNombre.place(x=150, y=15, width = 300,height = 30)
       
        apellido = StringVar()
        txtApellido = Entry(ventana_agregar_medico, textvariable=apellido ,font="Arial 12")
        txtApellido.place(x=150, y=55, width = 300,height = 30)        
        
        especialidad = StringVar()
        txtEspecialidad = Entry(ventana_agregar_medico, textvariable=especialidad ,font="Arial 12")
        txtEspecialidad.place(x=150, y=95, width = 300,height = 30)
        
        Button(ventana_agregar_medico, text="Agregar",font="Arial 10 bold", bg="#296472", fg="white",width=12, height= 2, command=funcion_agregar_medico).place(x=200, y=180)             
        
    def ventana_editar_medico():

        try:            
            selected = caja_medicos.focus()            
            valor = caja_medicos.item(selected, 'values')

            if valor == "":
                 messagebox.showinfo('Error', 'Debe seleccionar un médico')
            else:
                def funcion_actualizar_medico():

                    if txtNombre.get() == "":
                        messagebox.showinfo('Error', 'Ingrese el nombre del médico', parent=ventana_agregar_medico)
                        txtNombre.focus()
                    elif txtApellido.get() == "":
                        messagebox.showinfo('Error', 'Ingrese el apellido del médico', parent=ventana_agregar_medico)
                        txtApellido.focus()
                    elif txtEspecialidad.get() == "":
                        messagebox.showinfo('Error', 'Ingrese la especialidad del médico', parent=ventana_agregar_medico)
                        txtEspecialidad.focus()
                    else:
                        operaciones.actualizar_medico(txtNombre.get(), txtApellido.get(), txtEspecialidad.get(), valor[0])
                        caja_medicos.delete(*caja_medicos.get_children())
                        lista_medicos = operaciones.ver_medicos()
                        for l in reversed(lista_medicos):
                            caja_medicos.insert(parent='', index='end', text="", values=(l['id'], l['nombre'],l['apellido'],l['especialidad']))

                    editar_medico.destroy()
                    messagebox.showinfo('Éxito', 'El médico se actualizó correctamente')   

                editar_medico = Toplevel(width=500, height=250, bg="#24B8AA")
                editar_medico.minsize(500, 250)
                editar_medico.maxsize(500, 250)
                editar_medico.title("Editar médico")
                #datos viejos
                Label(editar_medico, text="Nombre:", font="Arial 10 bold", bg="#24B8AA", fg="white").place(x=20, y=20)
                txtNombre = Entry(editar_medico, textvariable=StringVar(editar_medico,value=valor[1]), font="Arial 12")
                txtNombre.place(x=150, y=15, width = 300,height = 30)

                Label(editar_medico, text="Apellido:", font="Arial 10 bold", bg="#24B8AA", fg="white").place(x=20, y=60)
                txtApellido = Entry(editar_medico, textvariable=StringVar(editar_medico,value=valor[2]), font="Arial 12")
                txtApellido.place(x=150, y=55, width = 300,height = 30)
                
                Label(editar_medico, text="Especialidad:", font="Arial 10 bold", bg="#24B8AA", fg="white").place(x=20, y=100)
                txtEspecialidad = Entry(editar_medico, textvariable=StringVar(editar_medico, value=valor[3]), font="Arial 12")
                txtEspecialidad.place(x=150, y=95, width = 300,height = 30)
                
                Button(editar_medico, text="Actualizar",font="Arial 10 bold", bg="#296472", fg="white",width=12, height= 2, command=funcion_actualizar_medico).place(x=200, y=180)
                
        except IndexError:
                pass
    
    ocultarFrame()
    medicos.pack(fill="both", expand=1)

    Label(medicos, text="Médicos", font="Arial 18 bold", bg="#24B8AA", fg="#ffffff").place(x=20, y=20)
    #treeview medicos
    caja_medicos = ttk.Treeview(medicos, height=15)
    caja_medicos["columns"] = ("#", "Nombre", "Apellido", "Especialidad")
    caja_medicos.column("#0", width=0, minwidth=0)
    caja_medicos.column("#", width=40, minwidth=40)
    caja_medicos.column("Nombre", anchor=W, width=230)
    caja_medicos.column("Apellido",anchor=W, width=230)
    caja_medicos.column("Especialidad", anchor=W, width=230)

    caja_medicos.heading("#0", text="")
    caja_medicos.heading("#", text="#")
    caja_medicos.heading("Nombre", text="Nombre")
    caja_medicos.heading("Apellido", text="Apellido")
    caja_medicos.heading("Especialidad", text="Especialidad")

    lista_medicos = operaciones.ver_medicos()
    for l in reversed(lista_medicos):
        caja_medicos.insert(parent='', index='end', text="", values=(l['id'], l['nombre'],l['apellido'],l['especialidad']))
    caja_medicos.place(x = 20,y = 60)    
    #caja_medicos.bind("<Double-Button-1>", funcion_editar_medico)
    #-----------------------------------------------------

    scroll = ttk.Scrollbar(medicos, orient="vertical", command= caja_medicos.yview)
    caja_medicos.configure(yscroll= scroll.set)
    scroll.place(x = 750,y = 61, height=325)
    Button(medicos, text = 'AGREGAR', font="Arial 10 bold", width=12, height= 2, bg="#296472", fg="white", command = ventana_agregar_medico).place(x = 285,y = 400)
    Button(medicos, text = 'EDITAR', font="Arial 10 bold", width=12, height= 2, bg="#296472", fg="white", command = ventana_editar_medico).place(x = 410,y = 400)          

def acerca_de():
    messagebox.showinfo("Aviso", "Programa creado por Pablo Pérez - Año 2022")

def ocultarFrame():
    buscar_pacientes.pack_forget()
    pacientes.pack_forget()
    medicos.pack_forget()
    historias.pack_forget()    
       
menubar = Menu(ventana, tearoff=0)
menubar.add_command(label="Médicos", command=ventana_medicos)
menubar.add_command(label="Pacientes", command=ventana_pacientes)
menubar.add_command(label="Buscar paciente", command=ventana_buscar_pacientes)
menubar.add_command(label="Historias clínicas", command=ventana_historias)
menubar.add_command(label="Acerca de..", command=acerca_de)
menubar.add_command(label="Salir", command=ventana.quit)
ventana.config(menu=menubar, background="#24B8AA")

medicos = Frame(ventana, width=800, height=600, background="#24B8AA")
pacientes = Frame(ventana, width=800, height=600, background="#24B8AA")
historias = Frame(ventana, width=800, height=600, background="#24B8AA")
buscar_pacientes = Frame(ventana, width=800, height=600, background="#24B8AA")

ventana.mainloop()
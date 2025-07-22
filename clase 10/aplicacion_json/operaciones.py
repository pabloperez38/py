import json

##########################médicos############################
def ver_medicos():
    with open('medicos.json', 'r', encoding='utf-8') as f:
        listaMedicos = json.load(f)
        MedicosDict = {}
        MedicosDict = listaMedicos
        return MedicosDict

def guardar_medico(datos):
    with open('medicos.json', 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4)

def crear_medico(nombre, apellido, especialidad):
    json_data_medicos = ver_medicos()
    contador = 1
    for medico in json_data_medicos:
        contador = contador + 1
    persona = {}
    persona["id"] = contador
    persona["nombre"] = nombre
    persona["apellido"] = apellido
    persona["especialidad"] = especialidad
    json_data_medicos.append(persona)
    guardar_medico(json_data_medicos)

def actualizar_medico(nombre, apellido, especialidad, idMedico):
    json_data_medicos = ver_medicos()    
    for medico in json_data_medicos:
        print(type(idMedico))
        print(type(medico["id"]))
        if medico["id"] == int(idMedico):
            medico["nombre"] = nombre 
            medico["apellido"] = apellido
            medico["especialidad"] = especialidad
            guardar_medico(json_data_medicos)

def traer_datos_medico(medico):
    json_data_medicos = ver_medicos()   
    for entrada in json_data_medicos: 
        if entrada["id"] == medico:
            return entrada
#########################pacientes#############################

def ver_pacientes():
    with open('pacientes.json', 'r', encoding='utf-8') as f:
        listaPacientes = json.load(f)
        PacientesDict = {}
        PacientesDict = listaPacientes
        return PacientesDict

def guardar_paciente(datos):
    with open('pacientes.json', 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4)

def crear_paciente(nombre, apellido, dni, fechaNacimiento, nacionalidad):   

    json_data_pacientes = ver_pacientes()

    if len(json_data_pacientes) == 0:
        contador = 1
    else: 
        for paciente in json_data_pacientes:
            contador = int(paciente["id"]) + 1
        
    persona = {}
    
    persona["id"] = int(contador)    
    persona["nombre"] = nombre
    persona["apellido"] = apellido
    persona["dni"] = dni
    persona["fechaNacimiento"] = str(fechaNacimiento)
    persona["nacionalidad"] = nacionalidad
    persona["historias"] = []
    json_data_pacientes.append(persona)
    guardar_paciente(json_data_pacientes)

def eliminar_paciente(paciente):    
    json_data_pacientes = ver_pacientes()   
    data_final = []
    for x in json_data_pacientes:
        if not str(x["id"]) in paciente:
            data_final.append(x)
    guardar_paciente(data_final)

def actualizar_paciente(nombre, apellido, dni, fechaNacimiento, nacionalidad, idPaciente):
    json_data_pacientes = ver_pacientes()
   
    for paciente in json_data_pacientes:
        if str(paciente["id"]) == idPaciente:
            paciente["nombre"] = nombre 
            paciente["apellido"] = apellido
            paciente["dni"] = dni
            paciente["fechaNacimiento"] = fechaNacimiento
            paciente["nacionalidad"] = nacionalidad
            guardar_paciente(json_data_pacientes)

############# comprobar si existe un paciente

json_data_pacientes = ver_pacientes()

def existe_paciente(dni):
    for entrada in json_data_pacientes:        
        if(json.dumps(entrada).lower().find(dni.lower()) != -1):
            
            return "ok"

def buscador(tipo):
    if tipo == 1 or tipo == 2 or tipo == 3:
        json_data_pacientes = ver_pacientes()
        PacientesDict = {}
        PacientesDict = json_data_pacientes
        return PacientesDict
    elif tipo == 5:
        json_data_historias = ver_historias()
        HistoriasDict = {}
        HistoriasDict = json_data_historias
        return HistoriasDict
    elif tipo == 6:
        json_data_medicos = ver_medicos()
        MedicosDict = {}
        MedicosDict = json_data_medicos
        return MedicosDict

def traer_datos_paciente(paciente):    
    for entrada in json_data_pacientes: 
        if entrada["id"] == paciente:
            return entrada

#########################historias#####################################

def ver_historias():
    with open('pacientes.json', 'r', encoding='utf-8') as f:
        listaHistorias = json.load(f)
        HistoriasDict = {}
        HistoriasDict = listaHistorias
        return HistoriasDict

def guardar_historia(datos):
    with open('historias.json', 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4)

def crear_historia(paciente, medico, fecha, enfermedad, descripcion):
    medicos = ver_medicos()
    for p in medicos:               
        if p["nombre"]+ " " + p["apellido"] == medico:       
            medico = p["id"]   
    json_data_pacientes = ver_pacientes()

    for p in json_data_pacientes:
        if paciente == p["id"]:
            historias = p["historias"]
            if len(historias) == 0:
                contador = 1
            else: 
                for h in historias:
                    contador = int(h["id"]) + 1
            nueva_historia = {
                "id": contador,
                "medico" : medico,
                "fecha" : fecha,
                "enfermedad" : enfermedad,
                "descripcion" : descripcion}
            historias.append(nueva_historia)
            guardar_paciente(json_data_pacientes)

def traer_historias():  
    json_data_historias = ver_historias()
    HistoriasDict = {}
    HistoriasDict = json_data_historias
    return HistoriasDict

def eliminar_historias(paciente):
    json_data_historias = ver_historias()   
    data_final = []
    for x in json_data_historias:
        if not str(x["paciente"]) in paciente:
            data_final.append(x)
    guardar_historia(data_final)

       
           
           



        


                    

    

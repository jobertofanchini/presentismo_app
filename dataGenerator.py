import os
import pandas as pd
import random
import datetime as dt

cwd = os.path.dirname(__file__)
os.chdir(cwd)

def generaNombre():
    archivoNombres = open(".\\random_data\\nombres.txt", "r",
                          encoding = "UTF-8")
    listArchivoNombres = archivoNombres.readlines()
    archivoNombres.close()
    global nombreRegistro
    nombreRegistro = random.choice(listArchivoNombres).rstrip().title() 
    return nombreRegistro

def generaApellido():
    archivoApellidos = open(".\\random_data\\apellidos.txt", "r",
                           encoding = "UTF-8")
    listArchivoApellidos = archivoApellidos.readlines()
    archivoApellidos.close()
    global apellidoRegistro
    apellidoRegistro = random.choice(listArchivoApellidos).rstrip().upper()
    return apellidoRegistro
             
def generaCorreoElectronico():
    archivoDominios = open(".\\random_data\\dominios.txt", "r",
                           encoding = "UTF-8")
    listDominios = archivoDominios.readlines()
    archivoDominios.close()
    dominio = random.choice(listDominios).rstrip() 
    correoElectronicoTilde = nombreRegistro[0].lower() + apellidoRegistro.lower() + "@" + dominio
    correoElectronico = ""
    for i in correoElectronicoTilde:
        if i == "á":
            correoElectronico += "a"
        elif i == "é":
            correoElectronico += "e" 
        elif i == "í":
            correoElectronico += "i"
        elif i == "ó":
            correoElectronico += "o"
        elif i == "ú":
            correoElectronico += "u"
        elif i == "ñ":
            correoElectronico += "n"
        else: correoElectronico += i  
    return correoElectronico

def generaDNI():
    return random.randint(6000000, 40000000)

def generaTelefono():
    prefijo, numInicio, numFinal = 11, random.randint(4000,9500), random.randint(1000,9999)
    return int(str(prefijo) + str(numInicio) + str(numFinal))

def generaAsistencia70PorCiento():
     numAzar = random.randint(0, 9)
     if numAzar > 6:
        return False
     else:
        return True     
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>alumnos.xlsx>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     
dfAlumnos = pd.DataFrame()

cantidadAlumnos = 100
while cantidadAlumnos > 0:
    
    dictRegistroAlumno = {"Comisión": "22918",
                        "DNI": generaDNI(),
                        "Apellido": generaApellido(),
                        "Nombre": generaNombre(),
                        "Teléfono": generaTelefono(), 
                        "Correo Electrónico": generaCorreoElectronico(),}
    
    dfAlumnos = pd.concat([dfAlumnos, pd.DataFrame.from_records([dictRegistroAlumno])],
                          ignore_index = True)
    
    cantidadAlumnos -= 1 

dfAlumnos = dfAlumnos.sort_values("Apellido").reset_index(drop = True)

alumnosFile = open(".\\data\\alumnos.xlsx","w")
dfAlumnos.to_excel(".\\data\\alumnos.xlsx")
alumnosFile.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>presentismo.xlsx>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dfAsistencia = pd.DataFrame()

fecha = dt.datetime(2022,8,2)
lapsoEntreClases = 0
switch = True 
cantidadClases = 40
while cantidadClases > 0: 
    
    lapsoConFormato = dt.timedelta(days = lapsoEntreClases)
    fecha = fecha + lapsoConFormato
    fechaConFormato = dt.datetime.strftime(fecha, "%d/%m/%y")

    for i in range(len(dfAlumnos)):
        
        dniAlumno = dfAlumnos.iat[i, 1]
        
        dictAsistencia = {"Fecha": fechaConFormato,
                        "DNI": dniAlumno, 
                        "Asistencia": generaAsistencia70PorCiento(),}
        
        dfAsistencia = pd.concat([dfAsistencia, pd.DataFrame.from_records([dictAsistencia])],
                                 ignore_index = True)
    if switch == True:
        lapsoEntreClases = 2
        switch = False
    else:
        lapsoEntreClases = 5 
        switch = True 
    
    cantidadClases -= 1

presentismoFile = open(".\\data\\presentismo.xlsx","w")
dfAsistencia.to_excel(".\\data\\presentismo.xlsx")   
presentismoFile.close()
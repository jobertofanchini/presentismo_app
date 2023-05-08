import os
import pandas as pd
import random
import datetime  

cwd = os.path.dirname(__file__)
os.chdir(cwd)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>alumnos.xlsx>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
alumnosFile = open (".\\data\\alumnos.xlsx","w")
dfAlumnos = pd.DataFrame()

cantidadRegistros = 100
while cantidadRegistros > 0:
         
    nombre = ""
    apellido = ""
    correoElectronico = ""
    dni = 0
    telefono = 0
    COMISION = "22918" 
      
    archivoNombres = open (".\\random_data\\nombres.txt", "r", 
                           encoding = "UTF-8")
    listArchivoNombres = archivoNombres.readlines()
    x = random.randint (0, len(listArchivoNombres) - 1)
    nombre = listArchivoNombres [x].rstrip().title()  #nombre
    archivoNombres.close()
    
    archivoApellidos = open (".\\random_data\\apellidos.txt", "r",
                            encoding = "UTF-8")
    listArchivoApellidos = archivoApellidos.readlines()
    x = random.randint (0, len(listArchivoApellidos) - 1)
    apellido = listArchivoApellidos[x].rstrip().upper()  #apellido
    archivoApellidos.close()

    archivoDominios = open (".\\random_data\\dominios.txt", "r", 
                            encoding = "UTF-8")
    listDominios = archivoDominios.readlines()
    x = random.randint (0, len(listDominios) - 1)
    dominio = listDominios [x].rstrip() 
    correoElectronicoTilde = nombre[0].lower() + apellido.lower() + "@" + dominio
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
        else: correoElectronico += i  #correo electrónico
    archivoDominios.close()
    
    x = random.randint (6000000, 40000000)
    dni = x  #DNI

    prefijo = 11
    caracteristica = random.randint(4000,9500)
    final = random.randint(1000,9999)
    telefonoString = str(prefijo) + str(caracteristica) + str(final)
    telefono = int(telefonoString)  #teléfono

    dictIngresoAlumno = {"Comisión": COMISION, "DNI": dni, "Apellido": apellido, 
                         "Nombre": nombre, "Teléfono": telefono, 
                         "Correo Electrónico": correoElectronico}
    
    dfAlumnos = pd.concat([dfAlumnos, pd.DataFrame.from_records([dictIngresoAlumno])],
                          ignore_index = True)
    
    dfAlumnos.to_excel(".\\data\\alumnos.xlsx")
    cantidadRegistros -= 1 

dfAlumnos = dfAlumnos.sort_values("Apellido")
dfAlumnos.to_excel(".\\data\\alumnos.xlsx")
alumnosFile.close()
"""
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>presentismo.xlsx>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
alumnosFile = ".\\data\\alumnos.xlsx"
dfAlumnos = pd.read_excel(alumnosFile)

dfAsistenciaOriginal = ".\\data\\presentismo.xlsx"

presentismoFile = open (".\\data\\presentismo.xlsx","w")
dfAsistencia = pd.DataFrame()

fecha = datetime.datetime(2022,8,2)
lapsoEntreClases = 0
fechaFormato = datetime.datetime.strftime(fecha, "%d/%m/%y")
dni_ = 0
asistencia = True

switch = True 
contador = 1
while contador <= 10:  #<<<<<<<<<<<---------- va 37 pero tarda demasiado
    diasSinClases = datetime.timedelta(days = lapsoEntreClases)
    fecha = fecha + diasSinClases
    fechaFormato = datetime.datetime.strftime(fecha, "%d/%m/%y")

    for i in range(len(dfAlumnos)):
        dni_ = dfAlumnos.iloc[i,1]
        x = random.randint(0, 9)
        if x > 6:
            asistencia = False
        else:
            asistencia = True            
    
        dictAsistencia = {"Fecha": fechaFormato, "DNI": dni_, "Asistencia": asistencia,}
        dfAsistencia = pd.concat([dfAsistencia, pd.DataFrame.from_records([dictAsistencia])],
                                 ignore_index = True)
        
        
        
        print ("*" * i)
    
    if switch == True:
        lapsoEntreClases = 2
        switch = False
    else:
        lapsoEntreClases = 5 
        switch = True 
    
    print ("Registros de clase número", contador, "OK")   
    contador += 1

dfAsistenciaFinal= pd.concat([dfAsistenciaOriginal, dfAsistencia], ignore_index = True)
dfAsistencia.to_excel(".\\data\\presentismo.xlsx")

presentismoFile.close()
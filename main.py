import pandas as pd

dfAlumnos = pd.read_excel(".\\data\\alumnos.xlsx")
dfPresentismo = pd.read_excel(".\\data\\presentismo.xlsx")

print (dfAlumnos)
print (dfPresentismo)

dfActa = pd.DataFrame()
camposDF = "Apellido", "Nombre", "¿?"
dfActa = pd.DataFrame(index = (), columns = camposDF)

dfActa["Apellido"] = dfAlumnos["Apellido"]  
dfActa["Nombre"] = dfAlumnos["Nombre"]

rangoFilasPresentismo = dfPresentismo.index
rangoFilasAlumnos = dfAlumnos.index

#************************************************************
fechaBuscada = "09/08/22"  #...... POR EJEMPLO
#************************************************************

contador = 1
for i in rangoFilasPresentismo:
    
    if dfPresentismo.at[i, "Fecha"] == fechaBuscada:
     print ("ENCONTRADA", contador)
     contador += 1
     dniMatch = dfPresentismo.at[i, "DNI"]
     print (dniMatch)
     
    for j in rangoFilasAlumnos:
         
        if dfAlumnos.at[j, "DNI"] == dniMatch:
            print ("El alumno o la alumna es: ", end = "")
            print (dfAlumnos.at[j, "Nombre"], dfAlumnos.at[j, "Apellido"])
            print ("Y ese día ", end = "")
            if dfPresentismo.at[i, "Asistencia"] == True:
                print ("concurrió a clases.")
            else: 
                print ("NO concurrió a clases.")           
         
acta = open (".\\acta.xlsx","w") 
dfActa.to_excel(".\\acta.xlsx")
acta.close()

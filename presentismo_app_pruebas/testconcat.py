import pandas as pd


dictIngresoAlumno = {"Comisión": 1, "DNI": 2, "Apellido": 3, 
                         "Nombre": 5, "Teléfono": 4, 
                         "Correo Electrónico": 6}
    


dfTest = pd.DataFrame()
dfAuxiliar = (pd.DataFrame.from_records([dictIngresoAlumno]))   

#print (dfAuxiliar)

dfTest = (pd.DataFrame.from_records([dictIngresoAlumno]))   

#print (dfTest)

dfResultante = pd.DataFrame()
dfResultante = pd.concat([dfResultante, dfAuxiliar], ignore_index = True)
dfResultante = pd.concat([dfResultante, pd.DataFrame.from_records([dictIngresoAlumno])], ignore_index = True)
print (dfResultante)


"""
dfTest = pd.concat(dfTest,dfAuxiliar)

print (dfTest)
"""

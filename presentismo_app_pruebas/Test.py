import datetime
from datetime import datetime
import random
import pandas as pd


def generar_marcas_temporal(first_date, second_date):
    while True:
        d1, d2 = datetime.strptime(first_date, '%d/%m/%Y'), datetime.strptime(second_date, '%d/%m/%Y')
        random_timestamp = random.randint(d1.timestamp(), d2.timestamp())
        fecha = datetime.fromtimestamp(random_timestamp)
        dia = fecha.isoweekday()
        if dia == 3 or dia == 5:
            break
    return datetime.strftime(fecha, '%d-%m-%Y')



resultadoFuncion = generar_marcas_temporal('1/8/2022', '16/12/2022')
print (resultadoFuncion)


lista = []

print(lista)





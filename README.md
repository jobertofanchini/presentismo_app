Objetivos y descripción de la aplicación:

    Aplicación para elaborar un acta de presentismo teniendo en cuenta 2 fuentes de información en formato Excel.

    1ra fuente: Listado de alumnos cuyos campos son:
    comision	email	name	last_name	dni	    telefono

    2da fuente: Desde un sistema donde los alumnos dan el presente, se genera otro Excel cuyos campos son:
    marca_temporal	comision	apellido	nombre	dni	email

    Nuestra aplicación filtra una fecha en la segunda fuente, y cruza los DNIs de dicho resultado con la primera.
    Genera un nuevo archivo "acta_presentismo" tomando como punto de partida el listado de alumnos (1ra fuente) y agregando una nueva columna cuyo nombre es la fecha filtrada y sus valores son True en caso de coincidir los DNIs de los alumnos.
    Así sabemos en cada columna qué alumno dio el presente en tal fecha.

Modo de uso:
    En primera instancia las variables y constantes que configuran su entorno estarán definidas literalmente en el archivo main.py.

    dbAlumnosFileStr = 'alumnos.xlsx'
    presentismoFileStr = 'presentismo.xlsx'
    actaFileStr = 'acta_presentismo.xlsx'

    Se ejecuta el archivo main.py sin argumentos.

    Para generar un flujo de trabajo y probar la aplicación, ver archivo dataGenerator.py

DataGenerator:
    Este script genera data ficticia en los archivos de alumnos y presentismo, para poder probar la aplicación sin necesidad de trabajar con datos reales.

    Al igual que el script principal main.py, inicialmente sus variables y constantes están definidas en el propio archivo.
    
    comision = '22919'
    fecha_inicial = dt.datetime.strptime("1/8/2022 00:00", '%d/%m/%Y %H:%M') 
    fecha_final = dt.datetime.strptime("16/12/2022 23:59", '%d/%m/%Y %H:%M') # Las fechas aleatorias se generan en este rango.
    diasDeLaSemana = 3,5, # Esta tupla indica que las fechas que se generarán pertenecen a días miercoles y viernes.
    
    # Nombres de los archivos y directorios a utilizar:
    dataDir = path.dirname(__file__) + '\\data'
    randomDataDir = path.dirname(__file__) + '\\random_data'
    presentismoFileStr = f'{dataDir}\\presentismo.xlsx'
    alumnosFileStr = f'{dataDir}\\alumnos.xlsx'
    apellidosFileStr = f'{randomDataDir}\\apellidos.txt'
    nombresFileStr = f'{randomDataDir}\\nombres.txt'
    dominiosFileStr = f'{randomDataDir}\\dominios.txt'

Propuestas de mejora:
    Luego de generada la info aleatoria en ambos archivos .xlsx y ejecutado el main.py con resultados satisfactorios será necesario mejorar algunos aspectos del programa relacionados a su universalización.
    Tener en cuenta que datos tales como:
        - El nro de comisión.
        - El rango de fechas y los días de la semana en los que dicha comisión cursa.
        - La/s fechas a tomar presentismo.
        - Los nombres de los archivos de origen de info y de destino.
    Deben poder ser elegidos por el usuario sin necesidad de modificar los archivos ".py".

    A tal respecto se propone tomar dichos datos como mínimo de la linea de comandos.
    Idealmente los datos de nombres de archivo, rango de fechas y días de la semana en los cuales se cursa podrían ser tomados de un archivo de configuración.
    Hay módulos que parsean (analizan a modo de string) archivos JSON, XML, etc. que son ideales para guardar configuraciones que luego los programas utilizan en su ejecución.
    Esto es conveniente ya que tanto el dataGenerator como el main comparten algunas constantes, como el nombre de los archivos. Sería útil que ambos leyeran tales valores de un solo archivo de configuración.
    De la linea de comandos se suelen tomar datos que son más cambiantes, como pueden ser en este caso el nro de comisión, y la fecha a tomar presentismo.
    Tener en cuenta que nuestra app debería servir para tomar presentismo de 'n' comisiones, en tal caso los archivos podrían como prefijo en sus nombres el nro de comisión, para poder individualizarlos.

Estructura de archivos y directorios de la aplicación con las mejoras resueltas:

└───presentismo_app
    │   dataGenerator.py
    │   generalFunctions.py
    │   main.py
    │
    ├───backup_data
    │       alumnos_ori.xlsx
    │       config.json_example
    │       presentismo_ori.xlsx
    │
    ├───config
    │       config.json
    │
    ├───data
    │       acta_presentismo.xlsx
    │       acta_presentismo_temp.xlsx
    │       alumnos.xlsx
    │       presentismo.xlsx
    │
    ├───help
    │       archivos_ayuda.ipynb
    │       datetime_ayuda.ipynb
    │       pandas_ayuda.ipynb
    │       random_ayuda.ipynb
    │
    ├───random_data
    │       apellidos.txt
    │       dominios.txt
    │       nombres.txt

Estructura mínima para que la aplicación funcione.

└───presentismo_app
    │   dataGenerator.py
    │   generalFunctions.py
    │   main.py
    │
    ├───config
    │       config.json
    │
    ├───data
    │       alumnos.xlsx
    │       presentismo.xlsx
    │
    ├───random_data
    │       apellidos.txt
    │       dominios.txt
    │       nombres.txt

Info sobre la consigna:
    https://docs.google.com/document/d/1oMXZOJYG9377ZwhF2tHV_yteKB54SiqRERx8UWzzBE8/edit?usp=sharing
import csv
import os

URL_BIBLIOTECA = 'biblioteca.csv'
URL_PROGRAMAS = r'C:\Users\Usuario\Documents\programacion\programas'

def buscar_carpeta(nombre_carpeta):
    for root, dirs, files in os.walk(URL_PROGRAMAS):
        if nombre_carpeta in dirs:
            return os.path.join(root, nombre_carpeta)
    return None

def obtenerDatosPrograma(dato_buscar):
    if os.path.exists(URL_BIBLIOTECA):
        if os.path.getsize(URL_BIBLIOTECA) > 0:
            if dato_buscar!=None:
                with open(URL_BIBLIOTECA, 'r', newline='') as biblioteca:
                    lector_csv = csv.reader(biblioteca)
                    for fila in lector_csv:
                        nombre_programa, lenguaje, nombre_carpeta  = fila[0].split(';')
                        if (nombre_programa == dato_buscar) or (nombre_carpeta==dato_buscar):
                            urlCarpeta=None
                            if nombre_carpeta!=None:
                                urlCarpeta=buscar_carpeta(nombre_carpeta)
                            return [nombre_programa,lenguaje,urlCarpeta]
                return None
            else:
                datos_programas = []
                with open(URL_BIBLIOTECA, 'r', newline='') as biblioteca:
                    lector_csv = csv.reader(biblioteca)
                    for fila in lector_csv:
                        nombre_programa, nombre_carpeta, lenguaje, *_ = fila[0].split(';')
                        datos_programas.append((nombre_programa.strip(), nombre_carpeta.strip(), lenguaje.strip()))
                return datos_programas
        else:
            return None
    else:
        print('La Biblioteca no está creada')
        #preguntar si quiere registrar
        op=input('\nQuieres registrar un programa? (si/no): ').lower()
        if op=='si':
            registrarPrograma()

def registrarPrograma(dato=None,op=0):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('***DATOS REGISTRAR PROGRAMA***')
    if dato!=None and op==0:
        print(f'Nombre: {dato}')
        nombre_programa=dato
    else:
        nombre_programa=str(input('Nombre: '))
    lenguaje=str(input('Lenguaje: '))
    if dato!=None and op==1:
        print(f'Nombre de la carpeta donde se ubica:{dato}')
        nombre_carpeta=dato
    else:
        nombre_carpeta=str(input('Nombre de la carpeta donde se ubica: '))
    if os.path.exists(URL_BIBLIOTECA):
        with open(URL_BIBLIOTECA, 'a', newline='') as biblioteca:
            escritor_csv = csv.writer(biblioteca,delimiter=';')
            escritor_csv.writerow([nombre_programa,lenguaje,nombre_carpeta])
        print('\nRegistrado con éxito\n')
    else:
        with open(URL_BIBLIOTECA,'w', newline='') as biblioteca:
            escritor_csv = csv.writer(biblioteca,delimiter=';')
            escritor_csv.writerow([nombre_programa,lenguaje,nombre_carpeta])
        print('\nBiblioteca creada')
        print('Registrado con éxito\n')

def borrarPrograma(nombre_programa=None):
    if os.path.exists(URL_BIBLIOTECA):
        print('***ELIMINAR PROGRAMA***\n')
        if nombre_programa==None:
            nombre_programa=str(input('Introduzca el programa a eliminar: '))
        else:
            print(f"Programa a eliminar '{nombre_programa}'")
        programa_encontrado = False
        datos_programa_borrar=None
        filas_nuevas = []

        with open(URL_BIBLIOTECA, 'r', newline='') as biblioteca:
            lector_csv = csv.reader(biblioteca, delimiter=';')
            for fila in lector_csv:
                if fila[0] == nombre_programa:
                    programa_encontrado = True
                    datos_programa_borrar=fila
                else:
                    filas_nuevas.append(fila)

        if programa_encontrado:
            with open(URL_BIBLIOTECA, 'w', newline='') as biblioteca:
                escritor_csv = csv.writer(biblioteca, delimiter=';')
                for fila in filas_nuevas:
                    escritor_csv.writerow(fila)
            print(f"El programa '{nombre_programa}' ha sido borrado.")
            print('***Datos del programa borrado***\n')
            print(f'Nombre:{datos_programa_borrar[0]}')
            print(f'Lenguaje:{datos_programa_borrar[1]}')
            print(f'Carpeta:{datos_programa_borrar[2]}')
        else:
            print(f"No se encontró el programa '{nombre_programa}'.")
    else:
        print('La Biblioteca no está creada')
        #preguntar si quiere registrar
        op=input('\nQuieres registrar un programa? (si/no): ').lower()
        if op=='si':
            registrarPrograma()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('***MENU CONTROLADOR PROGRAMAS***\n')
    #opciones
    print('0-Salir.')
    print('1-Recibir Programas Guardados.')
    print('2-Buscar Programa Guardado.')
    print('3-Registrar Nuevo Programa.')
    print('4-Borrar Programa Guardado.')
    #pedir opcion
    op=str(input('\nElige una opcion: '))
    #control opciones
    if op=='0':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('*Programa Cerrado*')
        break
    elif op=='1':
        os.system('cls' if os.name == 'nt' else 'clear')
        data=obtenerDatosPrograma()
        print('***DATOS DE LA BASE***')
        if data!=None:
            for i in range(len(data)):
                print(f'\n{i}->[Nombre:{data[i][0]}, Lenguaje:{data[i][1]}, Carpeta:{data[i][2]}]')
        else:
            print('No se han encontrado datos')
    elif op=='2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('***DATOS BUSCAR***\n')
        print('1-Nombre.')
        print('2-Carpeta.')
        op=str(input('\nElige una opcion: '))
        nombre_programa_buscar=str(input('Introduzca el programa a buscar: '))
        if nombre_programa_buscar=='':
            nombre_programa_buscar=None
        data=obtenerDatosPrograma(nombre_programa_buscar)#nombre programa, lenguaje, url carpeta guardada
        if data!=None:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"***Datos encontrados '{nombre_programa_buscar}'***\n")
            print(f'Nombre: {data[0]}')
            print(f'Lenguaje: {data[1]}')
            print(f'Ubicacion: {data[2]}')
            #preguntar si quiere borrarlo
            op=input('\nQuieres eliminarlo? (si/no): ').lower()
            if op=='si':
                borrarPrograma(nombre_programa_buscar)
        else:
            print(f"Sin registrar '{nombre_programa_buscar}'")
            #preguntar si quiere registrar
            op1=input('\nQuieres registrarlo? (si/no): ').lower()
            if op1=='si':
                registrarPrograma(nombre_programa_buscar,op)
    elif op=='3':
        os.system('cls' if os.name == 'nt' else 'clear')
        registrarPrograma()
    elif op=='4':
        os.system('cls' if os.name == 'nt' else 'clear')
        borrarPrograma()
    #salir
    while op!='s':
        op=input('\nQuieres salir? (s): ').lower()
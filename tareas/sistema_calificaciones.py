import time

#Se crea la constante para evitar tenerla codificada en duro dentro del codigo
PROMEDIO_MINIMO_APROBADO = 6.0

#Se crea la constante para agregar un atraso de x segundos 
SLEEP = 1


def cargar_valor_numerico(info_dato_a_cargar):
    '''
        Metodo encargado de encapsular toda la logica y validaciones de datos numericos, 
        en caso de ser una calificacion, se valida ademas que el rango este entre el 0 - 10
    '''
    is_valor_valido = False
    valor = 0
    while not is_valor_valido:
        valor = input(info_dato_a_cargar)

        if len(valor) == 0:
            print("Campo obligatorio\n")

        elif not valor.isnumeric():
            print("Valor no valido\n")

        elif info_dato_a_cargar.casefold().find("calificacion") > -1:
            if  int(valor) < 0 or int(valor) > 10:
                print("La calificacion debe ser numero del 0 al 10\n")
            else:
                is_valor_valido = True
        else:
            is_valor_valido = True

    return int(valor)


def cargar_valor_cadena(info_dato_a_cargar):
    '''
        Metodo encargado de encapsular toda la logica y validaciones de carga de datos no numericos
    '''
    is_valor_valido = False
    valor = 0
    while not is_valor_valido:
        valor = input(info_dato_a_cargar)
        if len(valor) == 0:
            print("Campo obligatorio\n")
        elif valor.isnumeric():
            print("Este campo no es numerico, debe cargar una cadena\n")
        else:
            is_valor_valido = True

    return valor


def obtener_numero_estudiantes():
    # Pide al usuario el número de estudiantes y devuelve el valor
        return cargar_valor_numerico("\nIngrese el numero total de estudiantes del curso: ")

def obtener_nombre_estudiante(nro_estudiante):
    # Pide al usuario el nombre del estudiante y devuelve el valor
    return cargar_valor_cadena("\nNombre completo del estudiante nro {}: ".format(nro_estudiante + 1))

def obtener_numero_asignaturas():
    # Pide al usuario el número de asignaturas y devuelve el valor
    return cargar_valor_numerico("\nNumero de asignaturas: ")

def obtener_calificaciones(num_asignaturas):
    # Pide al usuario las calificaciones para cada asignatura y las devuelve en una lista
    lista_calificaciones = []
    cont = 0
    while (cont < num_asignaturas):
        asignatura = cargar_valor_cadena("\nAsignatura: ")
        calificacion = cargar_valor_numerico("\nCalificacion: ")
        lista_calificaciones.append({"asignatura": asignatura, "calificacion": calificacion})
        cont += 1

    return lista_calificaciones

def calcular_promedio(calificaciones):
    # Calcula y devuelve el promedio de las calificaciones
    sumatoria = 0
    for i in range(len(calificaciones)):
        sumatoria += calificaciones[i].get("calificacion")
    return sumatoria/len(calificaciones)

def determinar_estado(promedio):
    # Determina si el estudiante ha aprobado o reprobado basándose en el promedio
    if promedio >= PROMEDIO_MINIMO_APROBADO:
        return 'Aprobado'
    else:
         return 'Reprobado'

def imprimir_resumen(estudiantes):
    # Imprime un resumen con el nombre de los estudiantes, su promedio y su estado
    print("\n--Generando reporte de estudiantes--:\n")
    time.sleep(SLEEP)
    print("Promedio minimo para aprobar: {}\n".format(PROMEDIO_MINIMO_APROBADO))
    for i in estudiantes:
        print("Nombre/Apellido: {}".format(i.get('nombre')))
        print("Promedio obtenido: {}".format(i.get('promedio')))
        print("Estado academico: {}".format(i.get('estado')))
        print("\n") 
    print("\n-- Fin del reporte -- \n")


def iniciar_ejecucion():
    '''
        Se encapsula en una funcion la ejecucion de todo el programa, con el fin de capturar la excepcion KeyboardInterrupt
        y mostrar un mensaje amigable en caso de terminar la ejecucion 
    '''
    try:
        print("\n-- Ejecucion iniciada --\n")
        num_estudiantes = obtener_numero_estudiantes()
        estudiantes = []

        for i in range(num_estudiantes):
            nombre = obtener_nombre_estudiante(i)
            num_asignaturas = obtener_numero_asignaturas()
            calificaciones = obtener_calificaciones(num_asignaturas)
            promedio = calcular_promedio(calificaciones)
            estado = determinar_estado(promedio)
        
            estudiantes.append({
                'nombre': nombre,
                'promedio': promedio,
                'estado': estado
            })

        imprimir_resumen(estudiantes)
        print("\n-- Ejecucion finalizada --\n")
        quit()
    except KeyboardInterrupt:
        print("\n")
        print("-- Ejecucion terminada por el usuario --\n")
        quit()

iniciar_ejecucion()
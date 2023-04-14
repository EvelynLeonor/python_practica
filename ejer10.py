"""
10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un
programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
notas. Utilizar esta estructura para la resolución de los siguientes items.
B. Calcular el promedio de notas de cada estudiante.
C. Calcular el promedio general del curso.
D. Identificar al estudiante con la nota promedio más alta.
E. Identificar al estudiante con la nota más baja.
Nota:
• Las 3 estructuras están ordenadas de forma que los elementos en la misma posición corresponden
a un mismo alumno.
• Realizar funciones con cada item

-------------------------------------------------------------------------------------

''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
----------------------------------------------------------------------------------------
"""


def almacenar_notas(texto,calif_1,calif_2):
    quitar= "'\n"
    for caracter in quitar:
        texto = texto.replace(caracter,"")
    lista_nombres = texto.split(",")
    print(lista_nombres)
    dicc_calificacion= {i:[j, k] for i, j, k in zip(lista_nombres,calif_1,calif_2)}
    print("*" *100)
    print("el diccio es: " , dicc_calificacion)
    print("*" *100)
    return dicc_calificacion

def promedio_alumno(dicc):
    prom = list(map(lambda alumnos: (alumnos[0], (alumnos[1][0] + alumnos[1][1])// 2 ), dicc.items()))
    print("promedio_alumno es : ",prom)
    print("*" *100)
    return prom

def promedio_general(dicc):
    prom= promedio_alumno(dicc)
    print("el promedio general es: ", sum(i[1] for i in prom ) / len(prom))
    print("*" *100)

def promedio_alto(dicc):
    prom= promedio_alumno(dicc)
    print("estudiante con la nota promedio más alta es:  ",max(prom, key=lambda x:x[1]))
    print("*" *100)


def nota_baja(dicc):
    print("alumnx con la nota mas baja es: ", min(dicc.items(), key=lambda x:x[1])[0]," y su nota es: ",min(dicc.values()))
    print("*" *100)


nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


dicc = almacenar_notas(nombres,notas_1,notas_2) #inciso A
prom = promedio_alumno(dicc)                    #inciso B
promedio_general(dicc)                          #inciso C
promedio_alto(dicc)                             #inciso D
nota_baja(dicc)                                 #inciso E

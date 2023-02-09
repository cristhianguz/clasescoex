'''nEstudiante=int(input('digite la cantidad de estudiantes: '))

nombreEstudiante=[]
cursoEstudiante=[]
generoEstudiante=[]
promedioEstudiantes=[]
sumatoria=0
promedio=0

for i in range(nEstudiante):
    nombreEstudiante.append(input('digite el nombre del estudiante '))
    curso=int(input('digite el curso del estudiante: '))
    while curso<1 or curso >11:
        print('curso invalido')
        curso=int(input('digite el curso del estudiante: '))
    else:
        cursoEstudiante.append(curso)
    genero=input('ingrese el genero del estudiante: ').lower()
    while genero !='m' and genero!='f':
        print('genero invalido')
        genero=input('digite el genero del estudiante: ')
    else:
        generoEstudiante.append(genero)
    
    for nota in range(3):
        notaEstudiante=float(input('ingrese la nota del estudiante: '))
        while notaEstudiante<0 or notaEstudiante >5:
            print('Nota invalida')
            notaEstudiante=float(input('ingrese la nota del estudiante '))
        sumatoria += notaEstudiante
    promedio = sumatoria/3
    promedioEstudiantes.append(promedio)'''

#for alumno in range(nombreEstudiante):
#    print(nombreEstudiante{alumno})
#    print(cursoEstudiante{alumno})
#    print(promedioEstudiantes{alumno})
#    print(generoEstudiante{alumno})

'''alumnos=[]
alumno={}

for i in range(2):
    alumno["nombre"]=input('nombre')
    alumno["curso"]=input('curso')
    alumno["genero"]=input('genero')
    alumnos.append(alumno)
    alumno={}

    
print(alumnos)'''



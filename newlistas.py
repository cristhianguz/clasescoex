'''suma=0
import random
lista=[]
for i in range(10):
    lista.append(random.randint(1,10))
for j in range(10):
    suma+=lista[i]
print(lista)'''

#mostrar el valor mas grande destro de una lista sin usar metodos o funciones
'''lista=[12,35,1,35,34,23,24,15,2,56]
mayor=lista[0]
for i in range(10):
    if lista[i]>mayor:
        mayor=lista[i]
print(mayor)'''

#mostrar el valor menor destro de una lista sin usar metodos o funciones
'''lista=[12,35,1,35,34,23,24,15,2,56]
menor=lista[0]
for i in range(10):
    if lista[i]<menor:
        menor=lista[i]
print(menor)'''

estudiante=[]
nota=[]
menu=0
while menu!=5:
    menu=int(input(''' 1.Ingresa 5 estudiantes 
    2.ingresar nota de cada estudiante
    3.mostrar mayor nota y de que estudiante es
    4.mostrar estudiantes y notas
    5.salir \n '''))
match menu:
    case 1:
        for i in range(5):
            estudiante.append(input('Digita el nombre '))
    case 2:
        for j in range(5):
            nota.append(input('Digita la nota '))
    case 3:
        max=nota[0]
        for k in nota:
            if k>max:
                max=k
            print(f'la nota mayo es{max} y pertenese a {nota==estudiante} ')

            

    


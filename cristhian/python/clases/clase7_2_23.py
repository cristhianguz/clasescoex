#por teclado se ingresa el valor hora de N cantidad de empleados. posteriormente se ingresa el nombre del empleado la antiguedad y la cantidad de horas trabajadas en el mes, se pide calcular el importe a cobrar teniendo en cuenta que al total que resulta de multiplicar el valor hora por la cantidad de horas trabajadas hay que sumarle la cantidad de años trabajados multiplicados por 30 y al total de todas esas operaciones restarle el 13% en concepto de descuentos, imprimir el cecibo correspondiente con el nombre la antiguedad el valor hora el total a cobrar en bruto el total de descuentos y el valor neto a cobrar.



'''empleados=[]
hora=25
horas=1
descuento=0
empleado={
    "nombre":"",
    "antigueda":"",
    "horas":"",
}

for i in range(2):
    empleado["nombre"]=input('nombre: ')
    empleado["antiguedad"]=int(input('antiguedad: '))
    empleado["horas"]=int(input('horas trabajadas: '))
    empleados.append(empleado)
    empleado={}


    if horas>0:
        horas=horas*hora
    print(horas)
    if antiguedad>1:
        antiguedad=antiguedad*30
    print(antiguedad)'''


#punto 10







    





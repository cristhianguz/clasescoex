#cantidad=int(input('ingrese la cantidad de camisas '))
#valor=int(input('ingrese el valor unitario '))
#total=0
#des=0
#d=0
#if cantidad>=1000:
#    total=cantidad*valor 
#    des=total*0.9
#    d=10
#    print(f'su descuento es {d} su total a pagar es {des } ')
#elif cantidad>500 and cantidad<999:
#    total=cantidad*valor
#    des=total*0.92
#    d=8
#    print(f'su decuento es {d} su total a pagar es{des } ')
#elif cantidad>200 and cantidad<499:
#    total=cantidad*valor
#    des=total*0.95
#    d=5
#    print(f'su descuento es {d} su total a pagar es {des } ')
#else:
#    print(f'no tienes descuento por lo tanto su valor a paghar es {total } ')



#inversion=int(input('digite la cantidad invertida '))
#tiempo=int(input('digite la cantidad de meses invertidos '))
#ganancias=0
#porc=0
#if tiempo>=24:
#    ganancias=inversion*1.18
#    porc=18
#    print(f'el porcentaje ganado fue del {porc} y su valor ganado al año es de {ganancias}')
#elif tiempo>19 and tiempo<24:
#    ganancias=inversion*1.15
#    porc=15
#    print(f'el porcentaje ganado fue del {porc} y su valor ganado al año es de {ganancias}')
#elif tiempo>13 and tiempo<18:
#    ganancias=inversion*1.12
#    porc=12
#    print(f'el porcentaje ganado fue del {porc} y su valor ganado al año es de {ganancias}')
#elif tiempo>7 and tiempo<12:
#    ganancias=inversion*1.10
#    porc=10
#    print(f'el porcentaje ganado fue del {porc} y su valor ganado al año es de {ganancias}')
#elif tiempo<7:
#    ganancias=inversion*1.08
#    porc=8
 #   print(f'el porcentaje ganado fue del {porc} y su valor ganado al año es de {ganancias}')


#sueldo=int(input('ingrese el sueldo a pagar '))
#cargo=int(input(f'selecciones su rama de trabajo \n1. vendedor \n2. diseño \n3. administrativo \n '''))
#new=0
#pg=0
#match cargo:
#    case 1:
#        new=sueldo*1.12
#        pg=12
#        print(f'tu incremento fue del {pg} su nuevo sueldo es de{new} ')
#    case 2:
#        new=sueldo*1.10
#        pg=10
#        print(f'tu incremento fue del {pg} su nuevo sueldo es de{new} ')
#    case 3:
#        new=sueldo*1.05
#        pg=5
#        print(f'tu incremento fue del {pg} su nuevo sueldo es de{new} ')


'''salario=int(input('digita el valor de su sueldo '))
tv=int(input('ingresa el valor optenido en ventas '))
comision=0
porsentaje=0
total=0
if tv>=1000000 and tv<=2000000:
    comision=tv*0.3
    porsentaje=3
    total=comision+salario
    print(f'su porsentaje ganado fue del {porsentaje} para una ganancia de {comision} su sueldo final es de {total} ')
elif tv>2000000 and tv<5000000:
    comision=tv*0.5
    porsentaje=5
    total=comision+salario
    print(f'su porsentaje ganado fue del {porsentaje} para una ganancia de {comision} su sueldo final es de {total} ')
elif tv>5000000:
    comision=tv*0.8
    porsentaje=8
    total=comision+salario
    print(f'su porsentaje ganado fue del {porsentaje} para una ganancia de {comision} su sueldo final es de {total} ')
else:
    print(f'no cumpliste con los objetivos requeridos para comision tu sueldo final es {salario} ')'''


'''num1=int(input('primer numero '))
num2=int(input('segundo numero '))
num3=int(input('tercer numero '))
if num1>num2 and num1>num3:
    print(f'el numero mayor es {num1} ')
elif num2>num1 and num2>num3:
    print(f'el numero mayor es {num2} ')
elif num3>num1 and num3>num2:
    print(f'el numero mayor es {num3} ')
elif num1==num2 and num1==num3 and num2==num3:
    print(f'los numeros ingresados son iguales')
else:
    print(f'dos de los numeros ingresados son iguales')'''


'''nota1=int(input('primera nota obtenida '))
nota2=int(input('segunda nota obtenida '))
nota3=int(input('tercera nota obtenida '))
if nota1>=0 and nota1<=5 and nota2>=0 and nota2<=5 and nota3>=0 and nota3<=5:
    final=(nota1+nota2+nota3)/3
    if final>=3:
        print(f'felicidades aprobaste {final}')
    else:
        print(f'estudie vago')
else:
    print(f'tienes un error en tus notas')'''
    
'''parcial1=float(input('digite nota parcial 1 '))
parcial2=float(input('digite nota pacial 2 '))
if parcial1>=0 and parcial1<=5 and parcial2>=0 and parcial2<=5:
    pp=(parcial1+parcial2)/2
    if pp>=2:
        print(f'puede presentar examen final tu nota es {pp}')
        examenf=float(input('digite nota examenf '))
    elif pp<2:
        print(f'perdiste la materia por bajo rendimiento ')
    else:
        print(f'lo siento no puedes presentar examen ')
if examenf<2:
    print(f'su nota final es la optenida en el examen ')
elif examenf>=2:
    notaf=(examenf*0.40+parcial1*0.30+parcial2*0.30)
    if notaf>=3:
        print(f'felicidades aprobaste tu calificacion es {notaf}')
    elif notaf<3:
        print(f'lo lamento no aprobaste la materia, si tu examen final es mayor que 2 puedes habilitar ')'''

'''salario=int(input('digite su salario '))
tiempo=int(input('digite el tiempo en la empresa '))
estado=int(input(f'digite su estado civil \n1. soltero \n2. casado \n '))
bono=0
sueldof=0
match estado:
    case 1:
        if tiempo==5:
            sueldof=salario*0.2
            bono=2
            print(f'el bono ganado fue del {bono} y su sueldo final ganado es de {sueldof+salario}')
        elif tiempo>=6 and tiempo<=10:
            sueldof=salario*0.5
            bono=5
            print(f'el bono ganado fue del {bono} y su sueldo final ganado es de {sueldof+salario}')
        elif tiempo>10:
            sueldof=salario*0.10
            bono=10
            print(f'el bono ganado fue del {bono} y su sueldo final ganado es de {sueldof+salario}')
    case 2:
        if tiempo==5:
            sueldof=salario*0.5
            bono=5
            print(f'el bono ganado fue del {bono} y su sueldo final ganado es de {sueldof+salario}')
        elif tiempo>=6 and tiempo<=10:
            sueldof=salario*0.10
            bono=10
            print(f'el bono ganado fue del {bono} y su sueldo final ganado es de {sueldof+salario}')
        elif tiempo>10:
            sueldof=salario*0.15
            bono=15
            print(f'el bono ganado fue del {bono} y su sueldo final ganado es de {sueldof+salario}')'''



'''estudios=int(input(f'digite el nivel de estudios del aspirante \n1. profesional \n2. especializacion \n '))
edad=int(input('ingrese edad del aspirante '))
cumple=0
match estudios:
    case 1:
        if edad>=25 and edad<35:
            print(f'cumple con los requisitos minimos para el puesto ')
        else:
            print('no cumples con los requisitos' )
    case 2:
        if  edad>25:
            print(f'cumples con los requisitos minimos para el puesto')'''




   





    


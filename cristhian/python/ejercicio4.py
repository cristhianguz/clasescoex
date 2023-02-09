parcial1=float(input('resultados parcial1 '))
parcial2=float(input('resultado parcial2 '))
parcial3=float(input('resultado parcial3 '))
examenf=float(input('resultado examen '))
trabajof=float(input('resultado trabajo '))
prom=(parcial1+parcial2+parcial3)/3*0.55
exam=examenf*0.30
trab=trabajof*0.15
notafinal=prom+trab+exam
print(f'{round(notafinal,1)} final ')
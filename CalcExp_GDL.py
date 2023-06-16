#Calcula numero y profundidad de sondeos en GDL

print('------------ CALCULADORA DE EXPLORACIÓN GEOTÉCNICA ----------------')
print('               Area Metropolitana de Guadalajara                   ')
print('')

#DATOS
print('---------------------------- DATOS --------------------------------')

#Determinar el numero de sondeos
AreaConstruccion = float(input('¿Cual es el Area de construcción en m2? '))

if AreaConstruccion < 100:
    NoSondeos = '1 Sondeo'
elif 100 <= AreaConstruccion < 250:
    NoSondeos ='2 Sondeos'
elif 200 <= AreaConstruccion <=1000:
    NoSondeos ='3 Sondeos'
elif AreaConstruccion > 1000:
    NoSondeos ='>= 4 Sondeos'
else:
    NoSondeos ='error'



#Determinar la profundidad de sondeos
NumeroDeNiveles = float(input('¿Cual es el NÚMERO DE NIVELES del proyecto? '))

if NumeroDeNiveles == 1:
    ProfSondeos = '4 m de profundidad'
elif NumeroDeNiveles == 2:
    ProfSondeos = '5 m de profundidad'
elif NumeroDeNiveles == 3:
    ProfSondeos = '7 m de profundidad'
elif NumeroDeNiveles == 4 or 5:
    ProfSondeos = '9 m de profundidad'
elif NumeroDeNiveles == 6 or 7:
    ProfSondeos = '12 m de profundidad'
elif NumeroDeNiveles == 8 or 9:
    ProfSondeos = '14 m de profundidad'
elif NumeroDeNiveles == 10:
    ProfSondeos = '16 m de profundidad'
elif NumeroDeNiveles > 10:
    ProfSondeos = ' hasta donde el incremento de esfuerzos es < 10% de la superficie'
else:
    ProfSondeos ='error'


#RESULTADOS 
print('')
print('*******************************************************************')
print('------------------------- RESULTADOS ------------------------------')
print('Para un ÁREA de construcción de: ' + str(AreaConstruccion) + ' m2')
print('Se requieren: ' + str(NoSondeos))
print('')

print('Para un proyecto de ' + str(NumeroDeNiveles) + ' niveles')
print('La profundidad mínima de exploración: ' + str(ProfSondeos))
print('*******************************************************************')

# 1 Escriba una función redondear() que permita redondear un número decimal de acuerdo al criterio: Si la parte decimal es mayo 0.5 (por ejemplo 3.5), devolver el entero siguiente (en este caso, 4), si no devolver el entero inmediatamente anterior
def redondear(a):
    ent = int(a)
    dec = a-ent
    if dec>0.5:
        return ent+1
    else:
        return ent
num = float(input("ingrese un numero para redondear: "))
print("su numero redondeado es: ",redondear(num))
# 2 Coloque el módulo del ejercicio anterior dentro de un paquete. En un módulo que esté fuera de ese paquete, cree una función de suma de decimales que redondee el resultado haciendo uso de la función redondear() del paquete recién creado.
import paquete1.modulo1
from paquete1.modulo1 import *
def sumadec(a,b):
    resul = a+b
    return redondear(resul)
num1 = float(input("ingrese un numero: "))
num2 = float(input("ingrese otro numero: "))
print("su resultado es:",sumadec(num1,num2))                
# 3 Usando el módulo datetime, escribe un programa que muestre la fecha y hora actuales del sistema.
import datetime
from datetime import *
print("la fecha y hora es: ",datetime.today())
# 4 Escriba un programa que devuelva un número par al azar entre 2 y 10 (pista: para comprobar si se pueden generar todos los números, pruebe ejecutar el programa dentro de un ciclo infinito). 
import random
fin = ''
print("presiona * para finalizar y para continuar presione enter")
while fin!="*":
    print(random.randint(2,10))
    fin = input()
# 5 Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado para la adivinación o para buscar consejo. Su mecanismo es muy simple:
# ante una pregunta del usuario, la bola responde con una de 8 posibles respuestas: 
import random
pregunta = input("ingrese su pregunta: ")
respuestas=["Es seguro que sí","Las chances son buenas","Puedes contar con ello","Pregúntame de nuevo más tarde","Concéntrate y pregunta de nuevo","No veo con claridad, intenta de nuevo","Mi respuesta es no","Mis fuentes me dicen que no "]
print(respuestas[random.randint(0,7)])  
# 6 Encuentre el tiempo de ejecución de los programas de los ejercicios anteriores (pista: use el módulo time)  
import time
ini = time.process_time()
def redondear(a):
    ent = int(a)
    dec = a-ent
    if dec>0.5:
        return ent+1
    else:
        return ent
num = float(input("ingrese un numero para redondear: "))
print("su numero redondeado es: ",redondear(num))
fin = time.process_time()
print("tiempo de ejecucion de ejercicio 1 es: ",fin-ini,ini,fin)
ini = time.process_time()
import random
fin = ''
print("presiona * para finalizar y para continuar presione enter")
while fin!="*":
    print(random.randint(2,10))
    fin = input()
fin = time.process_time()
print("tiempo de ejecucion de ejercicio 4 es: ",fin-ini,ini,fin)
# 7 Sorteo: Escriba un programa que simule un sorteo donde toman uno o más papeles al azar de un pozo para elegir los ganadores. 
participantes = []
print("ingrese a los participantes del sorteo,para finalizar presione n")
fin = ''
while fin!="n":
    nombre = input("nombre del participante: ")
    participantes.append(nombre)
    fin = input()
import random    
print("el ganador es: ",participantes[random.randint(0,len(participantes)-1)])
# 8 Escriba una función que pida al usuario ingresar su fecha de nacimiento y sea capaz de devolver la cantidad de días desde su nacimiento hasta hoy. 
 

from datetime import datetime
year = int(input('Igrese su año de nacimiento :'))
month = int(input('Ingrese su mes de nacimiento :'))
day = int(input('Ingrese su dia de nacimiento :'))

fechaing = datetime(year, month, day, 0, 0, 0)
now = datetime.now()
diferencia= now-fechaing
print("Cantidad de dias desde su nacimiento : ", diferencia)

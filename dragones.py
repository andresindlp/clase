import random
import time

def muestraintro():
    print("Estas en un planeta lleno de dragones. En frente tuyo\nhay dos cuevas. En ellas, el dragón es bueno y\ncompartira su tesoro contigo. El otro dragon\nesta hambriento y te deborara en cuanto te vea.")

def eligeCueva():
    cueva = "0"
    while cueva != "1" and cueva != "2" and cueva != "3" :
        cueva = input("¿A qué cueva quieres ir? (1 or 2 or 3): ")
    return cueva

class colors:
    RED = '\033[31m'
    EDNC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'


def mirarCueva(queCueva):
    print ("Te aproximas a la cueva...")
    time.sleep(2)
    print ("Está oscuro y misterioso...")
    time.sleep(2)
    print ("¡Un gran dragón aparece deante tuyo! Abre sus fauces y...")
    time.sleep(2)
    cuevasalvadora = random.randint(1,3)
    cuevaPerdedora = random.randint(1,3)
    if queCueva == str(cuevasalvadora):
        print(colors.GREEN + "...¡Te da su tesoro!" + colors.EDNC)
    elif queCueva == str(cuevaPerdedora):
        print(colors.YELLOW + "No hay dragón, solo un perrito :)" + colors.EDNC)
    else:
        print(colors.RED + "¡Te debora de un solo bocado!" +  colors.EDNC)
    
    

jugar="s"

while jugar=="s" or jugar == "S":
    muestraintro()
    numeroCueva = eligeCueva()
    mirarCueva(numeroCueva)
    jugarotravez = input("¿Quieres jugar otra vez? (s or n)")
    if jugarotravez == "n" or jugarotravez =="N":
        break

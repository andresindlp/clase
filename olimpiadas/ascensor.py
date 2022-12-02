global panta, pisos_validos, personas, avisos, entrada, ultimo_piso
planta = 0
pisos_validos, pisos_invalidos, avisos, personas, entrada = [], [], ["\nAVISOS"], 1, input("Abriendo puertas. Pueden pasar ... ").split(" ")

# pisos = 20
# max personas = 6

for i in entrada:
    if int(i) != -1:
        if 0 < int(i) < 21:
            if len(pisos_validos) <= 5:
                pisos_validos.append(i)

            else:
                avisos.append("- El usuario que quiere ir al piso " + i + " ya no cabe\n")
        else:
            avisos.append("- El piso " + i + " no existe\n")

print("\n".join(avisos))

print("Cerrando puertas. Estamos en el piso 0")

for piso in pisos_validos:
    if int(piso) > int(planta):
        print("Subiendo a una persona la planta", str(piso))
        planta = piso
    elif int(piso) == int(planta):
        print("\tLa siguiente persona puede bajar")
        planta = piso
    else:
        print("Bajando a una persona la planta", str(piso))
        planta = piso



        
    


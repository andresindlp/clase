global panta, pisos_validos, personas, avisos, entrada, ultimo_piso
planta = 0
pisos_validos = []
personas = 0
avisos = ["AVISOS"]
entrada = input("Abriendo puertas. Pueden pasar ... ").split(" ")
pisos_invalidos = []



# pisos = 20
# max personas = 6

while personas <= 6:
    for i in entrada:
        if int(i) != -1:
            if 0 < int(i) < 20:
                pisos_validos.append(i)
                personas += 1
                ultimo_piso = i
            else:
                avisos += ("El usuario que quiere ir al piso " + i + " no puede subir al ascensor\n")
                ultimo_piso = i
        else:
            break
else:
    avisos.append("El usuario que quiere ir al piso " + ultimo_piso + " ya no cabe")

print("\n".join(avisos))
        
    


    
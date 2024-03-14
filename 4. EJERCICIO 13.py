#Capitulo 4. Ejercicio resuelto 13

VALCOMP = float(input("Ingrese el valor de la compra: "))
COLOR = input("Ingrese el color de la bolita: ")

if COLOR == "BLANCO":
    VALPAG = VALCOMP

elif COLOR == "VERDE":
    VALPAG = VALCOMP * (1 - 0.1)

elif COLOR == "AMARILLA":
    VALPAG = VALCOMP * (1 - 0.25)

elif COLOR == "AZUL":
    VALPAG = VALCOMP * (1 - 0.5)

else:
    VALPAG = 0

print(f"El cliente debe pagar: ${VALPAG}")

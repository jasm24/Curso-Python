temperatura = float(input("Ingrese temperatura: "))
escala = input("Es Fahrenheit(F) o es Celsius(C)?:").lower()
if escala == "f":
    celsius = (temperatura - 32) * 5/9
    print(celsius)
elif escala == "c":
    fahrenheit = temperatura * 1.8 +32
    print(fahrenheit)
else:
    print("Escala incorrecta")

#grados = input("Ingrese temperatura a convertir")
#escala = input("Ingrese escala de grados (C/F)")
#grado = float(grados)
#escal = escala.upper()
#if escal == "C":
#    faren = (grado*9/5)+32
#    print(faren)
#elif escal == "F":
#    celsi = ((grado-32)*5/9)
#    print(celsi)
#else:
#    print("La Escala es incorrecta")




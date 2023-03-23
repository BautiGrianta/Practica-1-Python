from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
correcto = 0
incorrecto = 0
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Chequeo que se pueda realizar la operacion. En caso contrario vuelvo a elegir un numero y un operador.
    while (number_2 == 0 and operator == "/"):
        number_2 = randrange(10)
        operator = choice(operators)

    # Chequeo cual es el operador y realizo la cuenta.
    match operator:
        case "+": 
            cuenta = number_1 + number_2
        case "-":
            cuenta = number_1 - number_2
        case "*":
            cuenta = number_1 * number_2
        case "/":
            cuenta = number_1 / number_2
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")         
    # Le pedimos al usuario el resultado
    result = float(input("resultado: "))
    # Chequeo si el resultado es correcto.
    if (cuenta == result):
        print("Correcto!")
        correcto += 1
    else:
        print("Incorrecto!")
        incorrecto += 1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos. Tuviste {correcto} aciertos y {incorrecto} errores.")
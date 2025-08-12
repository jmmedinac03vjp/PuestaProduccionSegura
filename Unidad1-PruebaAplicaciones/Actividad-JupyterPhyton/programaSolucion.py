import random

# Tablero: lista de listas con los números de casilla
tablero = [
    [12, 11, 10, 9, 8],
    [13, 22, 21, 20, 7],
    [14, 23, 24, 19, 6],
    [15, 16, 17, 18, 5],
    [0, 1, 2, 3, 4]
]

def mostrar_tablero(pos_jugadores, iniciales):
    for fila in tablero:
        fila_str = ""
        for casilla in fila:
            casilla_str = str(casilla)
            # Mostrar inicial si hay jugador en la casilla
            jugadores_en_casilla = [iniciales[i] for i in range(2) if pos_jugadores[i] == casilla]
            if jugadores_en_casilla:
                casilla_str += "(" + ",".join(jugadores_en_casilla) + ")"
            elif casilla == 0:
                casilla_str = "Inicio"
            elif casilla == 24:
                casilla_str = "Meta"
            fila_str += casilla_str.ljust(10)
        print(fila_str)
    print("-" * 50)

def pedir_inicial(jugador):
    while True:
        inicial = raw_input("Introduce la inicial del jugador %d (mayúscula): " % jugador)
        if len(inicial) == 1 and inicial.isupper():
            return inicial
        print("Debe ser una sola letra mayúscula.")

# Iniciales de los jugadores
inicial1 = pedir_inicial(1)
while True:
    inicial2 = pedir_inicial(2)
    if inicial2 != inicial1:
        break
    print("La inicial debe ser diferente a la del jugador 1.")

iniciales = [inicial1, inicial2]
pos_jugadores = [0, 0]  # Ambos empiezan en la casilla de inicio

# Sorteo de turno
turno = random.randint(0, 1)
print("Empieza el jugador %s" % iniciales[turno])

# Bucle principal del juego
while True:
    mostrar_tablero(pos_jugadores, iniciales)
    raw_input("Turno de %s. Pulsa Enter para tirar el dado..." % iniciales[turno])
    tirada = random.randint(1, 6)
    print("Ha salido un %d" % tirada)
    nueva_pos = pos_jugadores[turno] + tirada
    if nueva_pos >= 24:
        pos_jugadores[turno] = 24
        mostrar_tablero(pos_jugadores, iniciales)
        print("¡El jugador %s ha llegado a la meta y gana!" % iniciales[turno])
        break
    pos_jugadores[turno] = nueva_pos
    # Comprobar si "come" al otro jugador
    otro = 1 - turno
    if pos_jugadores[turno] == pos_jugadores[otro] and pos_jugadores[turno] != 0:
        print("El jugador %s ha comido a %s!" % (iniciales[turno], iniciales[otro]))
        pos_jugadores[otro] = 0
    # Cambiar turno
    turno = otro
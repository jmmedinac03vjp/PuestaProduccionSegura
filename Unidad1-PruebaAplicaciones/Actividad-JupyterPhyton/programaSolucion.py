import random
import time

# Inicialización de jugadores
jugadores = []
while len(jugadores) < 5:
    inicial = input(f"Introduce la inicial del jugador {len(jugadores)+1} (mayúscula): ").upper()
    if inicial.isalpha() and len(inicial) == 1 and inicial not in jugadores:
        jugadores.append(inicial)
    else:
        print("Inicial no válida o repetida. Intenta de nuevo.")

# Posiciones iniciales
posiciones = [0] * 5

# Sorteo para decidir quién empieza
turno = random.randint(0, 4)
print(f"\nSorteo realizado. Empieza el jugador {jugadores[turno]}.")
time.sleep(1)

def mostrar_tablero(posiciones, jugadores):
    tablero = []
    for i in range(25):
        casilla = "Inicio" if i == 0 else "Meta" if i == 24 else str(i)
        jugadores_en_casilla = [jugadores[j] for j, pos in enumerate(posiciones) if pos == i]
        if jugadores_en_casilla:
            casilla += " (" + ",".join(jugadores_en_casilla) + ")"
        tablero.append(casilla)
    print(" | ".join(tablero))

# Juego principal
fin = False
while not fin:
    jugador_actual = turno
    input(f"\nTurno de {jugadores[jugador_actual]}. Pulsa Enter para tirar el dado...")
    tirada = random.randint(1, 6)
    print(f"{jugadores[jugador_actual]} ha sacado un {tirada}.")
    posiciones[jugador_actual] += tirada
    if posiciones[jugador_actual] >= 24:
        posiciones[jugador_actual] = 24
        mostrar_tablero(posiciones, jugadores)
        print(f"\n¡{jugadores[jugador_actual]} ha llegado a la Meta y gana el juego!")
        fin = True
        break
    # Comprobar si ha "comido" a otro jugador
    for otro in range(len(jugadores)):
        if otro != jugador_actual and posiciones[jugador_actual] == posiciones[otro] and posiciones[jugador_actual] != 0:
            print(f"{jugadores[jugador_actual]} ha caído en la casilla de {jugadores[otro]} y lo envía a Inicio.")
            posiciones[otro] = 0
    mostrar_tablero(posiciones, jugadores)
    time.sleep(1)
    turno = (turno + 1) % len(jugadores)
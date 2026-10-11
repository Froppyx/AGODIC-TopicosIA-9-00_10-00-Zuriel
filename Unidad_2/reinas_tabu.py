"""
Problema de las 8 reinas con Búsqueda Tabú.

Estado: lista de 8 números, estado[columna] = fila de la reina.
h(estado): número de pares de reinas que se atacan. Meta: h = 0.
Vecino: mover una reina a otra fila de su misma columna (56 vecinos).
Lista tabú: (columna, fila) que una reina acaba de dejar.
"""

import random
import time

N = 8
TENENCIA = 10      # tamaño de la lista tabú
MAX_MOV = 1000     # máximo de movimientos


def ataques(estado):
    h = 0
    for i in range(N):
        for j in range(i + 1, N):
            if estado[i] == estado[j] or abs(estado[i] - estado[j]) == j - i:
                h += 1
    return h


def busqueda_tabu(estado):
    inicio = time.perf_counter()
    mejor = estado[:]
    tabu = []
    movimientos = 0

    while ataques(mejor) > 0 and movimientos < MAX_MOV:
        # Buscar el mejor vecino permitido
        mejor_vecino, mejor_h, mov = None, None, None
        for col in range(N):
            for fila in range(N):
                if fila == estado[col]:
                    continue
                vecino = estado[:]
                vecino[col] = fila
                h = ataques(vecino)
                # Un movimiento tabú solo se permite si mejora al mejor (aspiración)
                if (col, fila) in tabu and h >= ataques(mejor):
                    continue
                if mejor_h is None or h < mejor_h or (h == mejor_h and random.random() < 0.5):
                    mejor_vecino, mejor_h, mov = vecino, h, (col, estado[col])

        # Moverse al vecino y prohibir regresar
        estado = mejor_vecino
        movimientos += 1
        tabu.append(mov)
        if len(tabu) > TENENCIA:
            tabu.pop(0)

        if mejor_h < ataques(mejor):
            mejor = estado[:]

    tiempo = time.perf_counter() - inicio
    return mejor, movimientos, tiempo


def imprimir(estado):
    for fila in range(N):
        print(" ".join("Q" if estado[col] == fila else "." for col in range(N)))


def rendimiento(pruebas=100):
    exitos, total_mov, total_t = 0, 0, 0
    for _ in range(pruebas):
        sol, mov, t = busqueda_tabu([random.randrange(N) for _ in range(N)])
        exitos += ataques(sol) == 0
        total_mov += mov
        total_t += t
    print(f"\nRendimiento con {pruebas} estados aleatorios")
    print(f"Éxitos: {exitos}/{pruebas}")
    print(f"Movimientos promedio: {total_mov / pruebas:.2f}")
    print(f"Tiempo promedio: {total_t / pruebas * 1000:.3f} ms")


if __name__ == "__main__":
    inicial = [random.randrange(N) for _ in range(N)]
    print("Estado inicial:", inicial, "h =", ataques(inicial))
    imprimir(inicial)

    solucion, movimientos, tiempo = busqueda_tabu(inicial)

    print("\nSolución:", solucion, "h =", ataques(solucion))
    imprimir(solucion)
    print(f"\nMovimientos: {movimientos}")
    print(f"Tiempo: {tiempo * 1000:.3f} ms")

    rendimiento(100)

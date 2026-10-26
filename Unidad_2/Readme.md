<img width="778" height="331" alt="image" src="https://github.com/user-attachments/assets/20ffa31b-a3b8-4536-9c42-fd2457263d5c" />

# Unidad 2 — Optimización Combinatoria, Heurísticas y Metaheurísticas

Carpeta de prácticas, investigaciones y proyectos de la **Unidad 2** para la materia **Tópicos de IA** en el **Instituto Tecnológico de Culiacán**.

* **Docente:** M.C. Zuriel Datan Mora
* **Integrantes:**
  * Mariana Manjarrez Olivas
  * Carlos Iván Cervantes Araujo

---

## 📂 Contenido de la Unidad

1. [Tarea Bonus II: Modelación y Representación Formal](#1-tarea-bonus-ii-modelación-y-representación-formal)
2. [Problema de las N-Reinas con Búsqueda Tabú](#2-problema-de-las-n-reinas-con-búsqueda-tabú)
3. [Proyecto 2: Optimización de Rutas mediante Recocido Simulado](#3-proyecto-2-optimización-de-rutas-mediante-recocido-simulado)

---

## 1. Tarea Bonus II: Modelación y Representación Formal
> **Estudio analítico sobre espacios de búsqueda, restricciones canónicas y codificación computacional.**

Investigación teórica centrada en demostrar cómo una adecuada representación matemática restringe los espacios de búsqueda hacia regiones factibles y reduce la complejidad algorítmica en cuatro problemas clásicos:

| Problema | Clase / Complejidad | Espacio de Búsqueda | Representación Canónica | Restricción Crítica |
| :--- | :--- | :--- | :--- | :--- |
| **JSSP** *(Job Shop Scheduling)* | NP-Hard | Permutaciones disyuntivas | Vector con repetición / Grafo disyuntivo | Precedencia tecnológica y no solapamiento |
| **N-Reinas** *(N-Queens)* | CSP (NP-C) | $N!$ (con restricción fila/columna) | Permutación posicional ($Q \in S_N$) | No colisión en diagonales absolutas |
| **MST** *(Minimum Spanning Tree)* | P (Polinomial) | $n^{n-2}$ árboles en $K_n$ | Vector booleano de aristas / Código Prüfer | Conectividad global y aciclicidad ($n-1$ aristas) |
| **TSP** *(Traveling Salesperson)* | NP-Hard | $\frac{(n-1)!}{2}$ (simétrico) | Permutación directa ($\pi$) / Matriz binaria MILP | Visita unívoca y supresión de subciclos (MTZ) |

📄 **Entregable:** `Topicos de IA - Tarea Bonus II.pdf`

---

## 2. Problema de las N-Reinas con Búsqueda Tabú
> **Implementación y análisis empírico de la metaheurística de Búsqueda Tabú (Fred Glover) aplicada a $N=8$.**

Resolución del clásico problema de ubicar 8 reinas en un tablero de $8 \times 8$ sin ataques mutuos ($h = 0$).

### ⚙️ Modelado y Configuración
* **Representación del Estado ($P$):** Vector unidimensional de tamaño 8 donde `estado[columna] = fila`. Elimina por diseño colisiones por columna.
* **Función Objetivo ($h$):** Número de pares de reinas que comparten fila o diagonal.
* **Vecindario:** Movimiento de una reina a otra fila dentro de su columna ($8 \times 7 = 56$ vecinos evaluados por paso).
* **Memoria de Corto Plazo (Lista Tabú):** Pares `(columna, fila)` abandonados recientemente, con **Tenencia = 10**.
* **Criterio de Aspiración:** Permite ejecutar un movimiento tabú si su valor $h$ mejora al mejor mínimo histórico global.
* **Límite de Parada:** $h = 0$ o máximo 1000 iteraciones.

### 📊 Métricas de Desempeño Promedio (100 ejecuciones aleatorias)
* **Tasa de éxito:** 100 / 100 (100% de convergencia a soluciones óptimas con $h = 0$).
* **Movimientos promedio:** ~13.22 movimientos.
* **Tiempo promedio de ejecución:** ~3.612 ms (medido con `time.perf_counter()`).

📄 **Entregables:** 
* `Problema de las N-Reinas con Búsqueda Tabú.pdf` — Reporte técnico y formulación.
* `reinas_tabu.py` — Código fuente documentado con benchmarks.

---

## 3. Proyecto 2: Optimización de Rutas mediante Recocido Simulado
> **Ruteo logístico multi-depósito (10 centros y 90 sucursales en Culiacán, Sin.) resuelto mediante Simulated Annealing.**

* **Reducción de Distancia:** De **421.78 km** a **205.35 km** (**51.31% de ahorro global**).
* **Acceso Completo y Código:** Toda la documentación, el notebook ejecutable y el video explicativo se encuentran dentro del directorio dedicado:
  * 📁 [**Ver carpeta Proyecto_2**](./Proyecto_2/)

---
* **Tiempo promedio de ejecución:** ~3.612 ms (medido con `time.perf_counter()`).

### 💻 Ejecución
```bash
python reinas_tabu.py

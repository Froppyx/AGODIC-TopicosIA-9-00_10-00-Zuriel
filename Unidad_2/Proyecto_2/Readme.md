<img width="778" height="331" alt="image" src="https://github.com/user-attachments/assets/20ffa31b-a3b8-4536-9c42-fd2457263d5c" />

# Proyecto 2: Optimización de Rutas de Distribución Multi-Depósito mediante Recocido Simulado (Simulated Annealing)

> **Optimización logística urbana para una cadena de restaurantes en Culiacán, Sinaloa.**

---

## 🚀 Enlaces Principales del Proyecto

# [**Jupiter Notebook con el Proyecto listo para ejecutar**](https://colab.research.google.com/drive/19Hu5_5_s1fn_vJy3M6Mbvni4Bx6yx-pT)

# [**Video Explicación del Proyecto**](https://drive.google.com/file/d/1ck63KpcF5epWnzNh6tgrOJelvqFI4NKz/view?usp=drive_link)

---

## 📌 Datos Generales

* **Institución:** Tecnológico Nacional de México – Instituto Tecnológico de Culiacán
* **Materia:** Tópicos de Inteligencia Artificial
* **Docente:** M.C. Zuriel Datan Mora
* **Integrantes:**
  * Carlos Iván Cervantes Araujo
  * Mariana Manjarrez Olivas
* **Fecha:** 22 de octubre de 2026

---

## 📝 Descripción del Problema

El proyecto aborda la planeación logística de reparto de abarrotes de una cadena de restaurantes en Culiacán con una red compuesta por **10 centros de distribución (CD)** y **90 sucursales** (100 puntos en total).

El problema se modeló en dos fases:
1. **Asignación voraz inicial:** Cada sucursal se asigna a su centro de distribución más cercano según la matriz de distancias.
2. **Optimización por clúster (TSP):** Para cada centro de distribución se resuelve un Problema del Viajante (*Traveling Salesperson Problem*) cerrado que parte del CD, visita sus tiendas asignadas y regresa al mismo CD, minimizando la distancia recorrida.

---

## 🧠 Metaheurística: Recocido Simulado (*Simulated Annealing*)

Programado desde cero en Python sobre Google Colab, el algoritmo emula el proceso físico de enfriamiento térmico de metales:
* **Criterio de Metrópolis:** Si una ruta vecina es más corta, se acepta de inmediato; si empeora la distancia ($\Delta E > 0$), se acepta con una probabilidad $P = e^{-\Delta E / T}$, permitiendo al sistema escapar de óptimos locales durante las temperaturas iniciales.
* **Operador de Vecindad:** Intercambio aleatorio de dos posiciones intermedias dentro de la ruta (`swap`), conservando intacto el punto de origen y regreso (el CD).
* **Parámetros de Enfriamiento:**
  * Temperatura inicial ($T_0$): `1000`
  * Temperatura mínima ($T_{min}$): `0.1`
  * Factor de enfriamiento geométrico ($\alpha$): `0.995`
  * Intentos por temperatura: `100` (~183,800 evaluaciones por centro)

---

## 📊 Resultados y Desempeño

Comparativa entre la **ruta inicial de referencia** (orden secuencial de la tabla) y la **ruta optimizada mediante Recocido Simulado** (evaluada con semilla 42):

| Métrica | Ruta Inicial de Referencia | Ruta con Recocido Simulado | Reducción / Ahorro |
| :--- | :--- | :--- | :--- |
| **Distancia total (km)** | 421.78 km | 205.35 km | **-51.31%** (216.43 km menos) |
| **Tiempo estimado (a 30 km/h)** | 843.57 min (~14.0 hrs) | 410.70 min (~6.8 hrs) | **-51.31%** |
| **Costo de combustible (0.15 MXN/km)** | $63.27 MXN | $30.80 MXN | **-51.31%** |

*Pruebas adicionales con 5 semillas aleatorias (`2024`, `42`, `100`, `1`, `7`) demostraron mejoras consistentes entre **49.82% y 51.76%**, confirmando la solidez y estabilidad del algoritmo.*

---

## 📂 Archivos en este Directorio

* `Topicos de IA - Proyecto 2 con Recocido Simulado.pdf` — Reporte técnico formal y formulación matemática.
* `README.md` — Documentación explicativa y accesos directos al proyecto.

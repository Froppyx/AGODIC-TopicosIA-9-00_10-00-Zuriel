<div align="center">
  <img width="778" height="331" alt="LogoTec" src="https://github.com/user-attachments/assets/2f896865-0184-442d-b4bb-cb113e745c3b" />
</div>

# Unidad 3 — Optimización de Riego con Enjambre de Partículas (PSO)

**Institución:** Instituto Tecnológico de Culiacán  
**Carrera:** Ingeniería en Sistemas Computacionales  
**Materia:** Tópicos de Inteligencia Artificial  
**Docente:** M.C. Zuriel Dathan Mora Félix  
**Integrantes:**  
* Manjarrez Olivas Mariana  
* Cervantes Araujo Carlos Iván  

---

## 🔗 Enlaces Directos y Entregables

[![Proyecto 3 - Notebook]([https://img.shields.io/badge/Proyecto_3-Abrir_en_Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/11qhTN67yXb8EWfSNhAoPAK7AIPEEXtl?usp=sharing](https://colab.research.google.com/drive/11qhTN67yXb8EWfSNhAo_PAK7AIPeEXtI?usp=sharing))

### 📁 Estructura de Archivos en esta Carpeta
* `Topicos_IA_Cervantes___Manjarrez_Proyecto_3_PSO.ipynb` — Notebook ejecutable con el código fuente en Python, pruebas de corrida y gráficas de convergencia.
* `Topicos de IA - Cervantes_Manjarrez - Proyecto 3.pdf` — Documentación técnica y reporte completo del proyecto.

---

## 📋 Descripción del Proyecto

Este proyecto aplica la metaheurística bioinspirada **Optimización por Enjambre de Partículas (PSO)** para resolver el problema de ubicación estratégica de sensores de humedad en terrenos agrícolas de **Guasave, Sinaloa**.

A partir de un conjunto de **100 parcelas muestreadas**, el algoritmo busca las coordenadas continuas `(Latitud, Longitud)` óptimas para instalar $K$ sensores dentro de un espacio multidimensional ($D = 2 \times K$), minimizando la distancia ponderada hacia cada cultivo según su **criticidad hídrica**.

### Variables Agroclimáticas Consideradas
* **Humedad del suelo (`HSuelo`):** Rango aproximado de $5.1\%$ a $45\%$.
* **Tipo de cultivo (`TipCul`):** Tomate rojo (factor $1.35$), Chile verde (factor $1.20$) y Maíz grano (factor $1.00$).
* **Elevación del terreno (`ElevacionT`):** Altitud entre $10\text{ m}$ y $50\text{ m}$ sobre el nivel del mar.
* **Salinidad del suelo (`SSuelo`):** Valores de $0.54$ a $3.95\text{ dS/m}$.
* **Coordenadas geoespaciales (`LatGps`, `LonGps`):** Ubicación en formato WGS 84.

---

## ⚙️ Arquitectura del Algoritmo

El modelo implementado en Python se divide en tres módulos principales:

1. **Índice de Prioridad de Riego (`CalPesoCrit`):** Calcula la criticidad `PesCri` de cada parcela normalizando el déficit de humedad ($50\%$), el nivel de salinidad ($30\%$) y la elevación relativa ($20\%$), ponderado por la sensibilidad del cultivo.
2. **Función Objetivo (`FunObjPso`):** Evalúa cada partícula calculando la distancia euclidiana en kilómetros ($1^\circ \approx 111\text{ km}$) desde cada parcela hasta su sensor más cercano, ponderada por `PesCri`, e incorpora una penalización cuando dos sensores quedan a menos de $0.85\text{ km}$ entre sí para evitar redundancia.
3. **Ciclo Principal del Enjambre (`EjeOptPso`):** Ejecuta la actualización iterativa de velocidades y posiciones respetando los límites geográficos del terreno mediante `np.clip`, utilizando semilla fija (`np.random.seed(67)`) para reproducibilidad.

### Hiperparámetros Utilizados
| Parámetro | Valor | Descripción |
| :--- | :---: | :--- |
| **Partículas (`TEnjambre`)** | `35` | Tamaño de la población en el enjambre |
| **Iteraciones (`MaxIte`)** | `90` | Ciclos de búsqueda por ejecución |
| **Peso de inercia** | `0.72` | Control de velocidad previa de la partícula |
| **Coeficiente cognitivo ($c_1$)** | `1.45` | Atracción hacia el mejor personal ($pBest$) |
| **Coeficiente social ($c_2$)** | `1.45` | Atracción hacia el mejor global ($gBest$) |

---

## 📊 Resultados de las Muestras de Corrida

Se realizaron tres pruebas experimentales sobre distintos subconjuntos de parcelas:

| Muestra | Selección de Parcelas | Parcelas | Sensores | Costo Inicial | Costo Final | Mejora (%) | Dist. Media (km) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Muestra 1** | Primeras 30 filas del dataset | 30 | 4 | 99.7324 | 69.3871 | **30.43%** | 1.954 |
| **Muestra 2** | Parcelas con salinidad $\ge 2.2\text{ dS/m}$ | 40 | 5 | 131.4485 | 81.8091 | **37.76%** | 1.654 |
| **Muestra 3** | Campo completo de Guasave | 100 | 8 | 205.3540 | 108.0352 | **47.39%** | 1.300 |

---

## 🛠️ Tecnologías y Dependencias

* **Lenguaje:** Python 3.x
* **Entorno:** Google Colab / Jupyter Notebook
* **Librerías:** `NumPy`, `pandas`, `SciPy` (`cdist`), `Matplotlib`

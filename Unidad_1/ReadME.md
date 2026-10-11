<img width="778" height="331" alt="image" src="https://github.com/user-attachments/assets/c0516cf9-cb75-4e19-8f7c-0c2bf40baf34" />

# Unidad 1 — Inteligencia Artificial e Impacto Ambiental

Carpeta correspondiente a los entregables, investigación y materiales de la **Unidad 1** para la materia **Tópicos de IA** (Instituto Tecnológico de Culiacán).

---

## 📌 Proyecto: Acuicontrol
> **Aplicación Inteligente para la Optimización de la Alimentación de Camarón y Mitigación del Impacto Ambiental en Cuerpos de Agua**

* **Sector / Región:** Granjas acuícolas semi-intensivas e intensivas en Sinaloa, México.
* **Docente:** Dr. Zuriel Datan Mora Félix
* **Integrantes:**
  * Mariana Manjarrez Olvias
  * Carlos Iván Cervantes Araujo

---

## 🎯 Resumen y Problemática

El alimento balanceado representa entre el **50% y el 70% de los costos directos** en las granjas camaronícolas de Sinaloa. Un manejo inadecuado genera acumulación de pellets no consumidos y materia fecal, lo que dispara la **Demanda Bioquímica de Oxígeno (DBO)**, genera toxicidad por amonio/nitritos y provoca eutrofización en esteros y bahías costeras.

**Acuicontrol** propone una solución de bajo costo basada en software que democratiza la acuicultura de precisión para PyMEs sin requerir sensores IoT costosos de inicio, optimizando la dosis diaria mediante análisis de datos de campo.

---

## 🧠 Arquitectura de Inteligencia Artificial

El sistema implementa un enfoque analítico progresivo en dos niveles:

1. **Nivel 1 — Motor Heurístico (Sistema Experto):**
   * Respuestas inmediatas y explicables desde el día uno mediante reglas operativas de campo.
   * *Ejemplo:* Si el sobrante en charola supera el 15%, aplica una reducción preventiva de ración (-8%) para prevenir anoxia; si el oxígeno cae por debajo de 4.0 mg/L, suspende o congela la dosis.

2. **Nivel 2 — Machine Learning Supervisado:**
   * Modelos entrenados sobre series temporales para estimar raciones continuas y clasificar riesgo de sobrealimentación.
   * Modelos evaluados: *Regresión Lineal Múltiple*, *Árboles de Decisión (CART)*, *Random Forest* y *Gradient Boosting (XGBoost)*.

---

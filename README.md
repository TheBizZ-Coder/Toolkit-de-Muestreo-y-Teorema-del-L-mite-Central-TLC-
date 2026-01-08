# Toolkit de Muestreo y Teorema del Límite Central (TLC)

Este proyecto es una herramienta interactiva desarrollada en Python para visualizar y comprobar el **Teorema del Límite Central (TLC)** mediante simulaciones de Monte Carlo.

El programa permite al usuario seleccionar diferentes distribuciones de probabilidad base, definir el tamaño de la muestra y el número de repeticiones, para posteriormente graficar la distribución de las medias muestrales y compararla con la curva Normal teórica.

## 📋 Características

* **Selección de Distribución Base:**
    * Uniforme $(0, 1)$
    * Exponencial $(\lambda=1)$
    * Binomial/Bernoulli $(p=0.5)$
* **Simulación Monte Carlo:** Generación de miles de muestras aleatorias para calcular promedios.
* **Cálculo de Parámetros:** Comparación automática entre los valores teóricos ($\mu$, $\sigma$) y los simulados.
* **Visualización Gráfica:**
    * Histograma de las medias muestrales.
    * Superposición de la Función de Densidad de Probabilidad (PDF) Normal teórica.
* **Interfaz de Consola:** Menú interactivo fácil de usar.

## 🛠️ Requisitos del Sistema

Para ejecutar este proyecto necesitas tener instalado **Python 3.x** y las siguientes librerías científicas:

* `numpy`
* `matplotlib`
* `scipy`

Puedes instalar las dependencias ejecutando:

```bash
pip install numpy matplotlib scipy

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# ============================================
# Proyecto Final - Probabilidad y Estadística
# Opción 2: Toolkit de Muestreo y TLC
# ============================================

# -----------------------------
# 1. Seleccion de distribucion
# -----------------------------
def generar_muestra(distribucion, n):
    if distribucion == "uniforme":
        return np.random.uniform(0, 1, n)
    elif distribucion == "exponencial":
        return np.random.exponential(scale=1, size=n)
    elif distribucion == "binomial":
        return np.random.binomial(n=1, p=0.5, size=n)
    else:
        raise ValueError("Distribución no válida")

# -------------------------------------
# 2. Simulacion Monte Carlo
# -------------------------------------
def simular_tlc(distribucion, n, N):
    medias = []
    for _ in range(N):
        muestra = generar_muestra(distribucion, n)
        medias.append(np.mean(muestra))
    return np.array(medias)

# -------------------------------------
# 3. Parametros teoricos
# -------------------------------------
def parametros_teoricos(distribucion, n):
    if distribucion == "uniforme":
        mu = 0.5
        sigma2_base = 1/12
    elif distribucion == "exponencial":
        mu = 1.0
        sigma2_base = 1.0
    elif distribucion == "binomial":
        mu = 0.5
        sigma2_base = 0.25
    else:
        return 0, 0, 0

    var_teorica_xbarra = sigma2_base / n
    error_estandar = np.sqrt(var_teorica_xbarra)
    
    return mu, var_teorica_xbarra, error_estandar

# -------------------------------------
# 4. Grafica del TLC 
# -------------------------------------
def graficar_resultados(medias, mu, var, n, distribucion):
    # Si hay graficas anteriores abiertas, las cerramos para evitar conflictos
    plt.close('all') 
    
    plt.figure(figsize=(10, 6))
    
    # Histograma
    plt.hist(medias, bins=40, density=True, alpha=0.6, color='#4CAF50', edgecolor='black', label='Simulación (Histograma)')
    
    # Curva Normal Teórica
    sigma = np.sqrt(var)
    x_min, x_max = min(medias), max(medias)
    x = np.linspace(x_min, x_max, 200)
    y = norm.pdf(x, mu, sigma)
    
    # Etiqueta con formula matematica
    label_teo = r'Teórica $\bar{X} \approx N(\mu=%.2f, \sigma^2/n=%.4f)$' % (mu, var)
    plt.plot(x, y, 'r-', linewidth=2.5, label=label_teo)

    plt.title(f"Teorema del Límite Central\nDist. Base: {distribucion.capitalize()} | n={n}")
    
   
    plt.xlabel(r"Valor de la Media Muestral ($\bar{X}$)") 
    
    plt.ylabel("Densidad")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# -------------------------------------
# 5. Programa principal
# -------------------------------------
def main():
    while True:
        print("\n" + "="*60)
        print("   TOOLKIT DE MUESTREO Y TEOREMA DEL LÍMITE CENTRAL")
        print("="*60)
        print("Seleccione la distribución base:")
        print("1. Uniforme (0,1)")
        print("2. Exponencial (lambda=1)")
        print("3. Binomial/Bernoulli (p=0.5)")
        print("4. Salir")
        
        opcion = input("\nIngrese opción (1-4): ")
        
        if opcion == '4':
            print("Saliendo del programa...")
            plt.close('all')
            break
            
        mapa_dist = {'1': 'uniforme', '2': 'exponencial', '3': 'binomial'}
        
        if opcion not in mapa_dist:
            print("Opción no válida, intente de nuevo.")
            continue
            
        distribucion = mapa_dist[opcion]
        
        try:
            val_n = input("Tamaño de muestra n (ej. 30): ")
            val_N = input("Número de repeticiones N (ej. 5000): ")
            n = int(val_n)
            N = int(val_N)
        except ValueError:
            print("Error: Por favor ingrese números enteros válidos.")
            continue

        print(f"\nSimulando {N} muestras de tamaño {n} con distribución {distribucion}...")
        
        medias = simular_tlc(distribucion, n, N)
        mu_teo, var_teo, err_std = parametros_teoricos(distribucion, n)

        print("\n" + "-"*40)
        print(" RESUMEN NUMÉRICO")
        print("-"*(40))
        print(f"{'Parámetro':<20} | {'Teórico':<10} | {'Simulado':<10}")
        print("-"*(40))
        print(f"{'Media (mu)':<20} | {mu_teo:<10.4f} | {np.mean(medias):<10.4f}")
        print(f"{'Varianza (sigma^2/n)':<20} | {var_teo:<10.4f} | {np.var(medias):<10.4f}")
        print(f"{'Error Estándar':<20} | {err_std:<10.4f} | {np.std(medias):<10.4f}")
        print("-"*(40))
        print("Generando gráfica...")

        graficar_resultados(medias, mu_teo, var_teo, n, distribucion)

if __name__ == "__main__":
    main()
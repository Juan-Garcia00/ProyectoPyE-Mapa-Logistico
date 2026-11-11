"""Parte 1 — Dinámica del mapa logístico (1. Estudio propedéutico)."""

import matplotlib.pyplot as plt
import numpy as np
 
from comun import guardar_figura, titulo, trayectoria
 
X0 = 0.23432
 
# Un valor de r por cada régimen, con su nombre
REGIMENES = [
    (0.8, "extinción"),
    (2.8, "punto fijo"),
    (3.2, "período 2"),
    (3.5, "período 4"),
    (3.83, "ventana de período 3"),
    (3.9, "caos"),
    (4.0, "caos"),
]
 
 
def figura_trayectorias(n=60):
    """Dibuja las trayectorias del mapa logístico para diferentes valores de r."""
    fig, ejes = plt.subplots(len(REGIMENES), 1, figsize=(8, 14), sharex=True)
    for eje, (r, nombre) in zip(ejes, REGIMENES):
        xs = trayectoria(X0, r, n)
        eje.plot(xs, "o-", markersize=3)
        eje.set_title(f"r = {r}: {nombre}")
        eje.set_ylabel("$x_n$")
        eje.set_ylim(0, 1)
    ejes[-1].set_xlabel("Iteración n")
    guardar_figura("parte1_trayectorias.png")
 
 
def figura_solucion_explicita(n=60):
    """Compara iterar la fórmula con la solución explícita para r = 4."""
    iterada = trayectoria(X0, 4.0, n)
    k = np.arange(n + 1)
    explicita = np.sin(2.0**k * np.arcsin(np.sqrt(X0))) ** 2
 
    plt.plot(k, iterada, "o-", markersize=4, label="Iterando $x_{n+1} = 4x_n(1-x_n)$")
    plt.plot(k, explicita, "x--", markersize=5, label=r"Solución explícita $x_n = \sin^2(2^n \arcsin\sqrt{x_0})$")
    plt.title("r = 4: iteración vs. solución explícita")
    plt.xlabel("Iteración n")
    plt.ylabel("$x_n$")
    plt.ylim(0, 1.3)
    plt.legend(loc="upper left")
    guardar_figura("parte1_explicita.png")
 
    separadas = np.where(np.abs(iterada - explicita) > 0.1)[0]
    print(f"Iteración y solución explícita coinciden hasta n = {separadas[0] - 1}; "
          f"en n = {separadas[0]} ya difieren en más de 0.1")
 
 
def diagrama_bifurcacion(r_min=2.5, r_max=4.0, cant_r=1000, transitorio=500, graficar=100):
    rs = np.linspace(r_min, r_max, cant_r)
    x = np.full(cant_r, X0)  # una trayectoria por cada r, en paralelo
    for _ in range(transitorio):  # descartamos las primeras iteraciones
        x = rs * x * (1 - x)
 
    plt.figure(figsize=(10, 6))
    for _ in range(graficar):  # graficamos las 100 siguientes
        x = rs * x * (1 - x)
        plt.plot(rs, x, ",k", alpha=0.3)
 
    # Marcas para ubicar los regímenes
    plt.axvline(3.0, color="red", linestyle="--")
    plt.text(3.01, 0.05, "r = 3: empieza\nel período 2", color="red")
    plt.axvline(3.57, color="red", linestyle="--")
    plt.text(3.58, 0.05, "r ≈ 3,57:\nempieza el caos", color="red")
    plt.axvspan(3.8284, 3.857, color="orange", alpha=0.3)
    plt.annotate("ventana de\nperíodo 3", xy=(3.84, 0.98), xytext=(3.6, 1.08),
                 color="darkorange", arrowprops={"arrowstyle": "->", "color": "darkorange"})
 
    plt.title("Diagrama de bifurcación: valores a los que tiende $x_n$ según r")
    plt.xlabel("r")
    plt.ylabel("$x_n$ (después de 500 iteraciones)")
    plt.ylim(0, 1.2)
    guardar_figura("parte1_bifurcacion.png")
 
 
def describir(x0, r):
    """Describe en palabras a qué tiende la sucesión."""
    finales = trayectoria(x0, r, 5000)[-200:]  # las últimas 200 de 5000 iteraciones
    valores = np.unique(np.round(finales, 4))
    if len(valores) == 1:
        return f"se queda fija en {valores[0]}"
    if len(valores) <= 8:
        return f"se repite cada {len(valores)} valores: {', '.join(str(v) for v in valores)}"
    return "no se repite nunca (caos)"
 
 
def analisis_semillas():
    semillas = [0.1, 0.23432, 0.37, 0.55, 0.8]
    print(f"\n¿A qué tiende la sucesión? (semillas: {semillas})")
    for r, nombre in REGIMENES:
        descripciones = [describir(s, r) for s in semillas]
        print(f"\nr = {r} ({nombre})")
        if len(set(descripciones)) == 1:
            print(f"  Las 5 semillas: {descripciones[0]}")
        else:
            for s, d in zip(semillas, descripciones):
                print(f"  Semilla {s}: {d}")
        if "caos" in descripciones[0]:
            ultimos = [round(float(trayectoria(s, r, 5000)[-1]), 4) for s in semillas]
            print(f"  Pero cada semilla termina en un lugar distinto: x_5000 = {ultimos}")
 
 
def ejecutar():
    titulo("PARTE 1 — Dinámica del mapa logístico")
    figura_trayectorias()
    figura_solucion_explicita()
    diagrama_bifurcacion()
    analisis_semillas()
 
 
if __name__ == "__main__":
    ejecutar()
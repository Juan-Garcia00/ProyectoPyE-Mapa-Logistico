"""Parte 1 — Dinámica del mapa logístico"""

import matplotlib.pyplot as plt
import numpy as np

from comun import guardar_figura, titulo, trayectoria

X0 = 0.23432
VALORES_R = [0.8, 2.8, 3.2, 3.5, 3.83, 3.9, 4.0]


def figura_trayectorias(n=60):
    """Dibuja las trayectorias del mapa logístico para diferentes valores de r."""
    fig, ejes = plt.subplots(len(VALORES_R), 1, figsize=(8, 14), sharex=True)
    for eje, r in zip(ejes, VALORES_R):
        xs = trayectoria(X0, r, n)
        eje.plot(xs, "o-", markersize=3)
        eje.set_ylabel("$x_n$")
        eje.set_title(f"r = {r}")
        eje.set_ylim(0, 1)
    ejes[-1].set_xlabel("Iteración n")
    guardar_figura("parte1_trayectorias.png")


def figura_solucion_explicita(n=60):
    """Compara la iteración numérica con x_n = sin^2(2^n arcsin(sqrt(x0)))."""
    numerica = trayectoria(X0, 4.0, n)
    k = np.arange(n + 1)
    theta = np.arcsin(np.sqrt(X0))
    explicita = np.sin(2.0**k * theta) ** 2

    plt.semilogy(k, np.abs(numerica - explicita) + 1e-18)
    plt.xlabel("Iteración n")
    plt.ylabel("|numérica − explícita|")
    guardar_figura("parte1_explicita.png")


def diagrama_bifurcacion(r_min=2.5, r_max=4.0, cant_r=1000,
                         transitorio=500, graficar=100,
                         nombre="parte1_bifurcacion.png"):
    rs = np.linspace(r_min, r_max, cant_r)
    x = np.full(cant_r, X0)  # una trayectoria por cada r, en paralelo
    for _ in range(transitorio):
        x = rs * x * (1 - x)

    plt.figure(figsize=(10, 6))
    for _ in range(graficar):
        x = rs * x * (1 - x)
        plt.plot(rs, x, ",k", alpha=0.3)
    plt.xlabel("r")
    plt.ylabel("$x_n$ (después del transitorio)")
    guardar_figura(nombre)


def periodo_aproximado(xs_finales, tol=1e-6):
    """Cuenta cuántos valores distintos visita al final (≈ período)."""
    distintos = np.unique(np.round(xs_finales / tol).astype(np.int64))
    return len(distintos)


def analisis_semillas():
    semillas = [0.1, 0.23432, 0.4, 0.6, 0.9]
    print(f"\nValores distintos en las últimas 200 iteraciones (semillas {semillas})")
    for r in VALORES_R:
        fila = []
        for s in semillas:
            xs = trayectoria(s, r, 5000)
            fila.append(periodo_aproximado(xs[-200:]))
        print(f"  r = {r:<5}: {fila}")


def ejecutar():
    titulo("PARTE 1 — Dinámica del mapa logístico")
    figura_trayectorias()
    figura_solucion_explicita()
    diagrama_bifurcacion()
    diagrama_bifurcacion(3.82, 3.86, 1000, nombre="parte1_ventana_p3.png")
    analisis_semillas()


if __name__ == "__main__":
    ejecutar()
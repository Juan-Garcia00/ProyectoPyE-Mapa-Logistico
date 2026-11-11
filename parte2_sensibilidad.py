"""Parte 2 — Sensibilidad a la condición inicial (2. Experimento de sensibilidad)."""

import matplotlib.pyplot as plt
import numpy as np

from comun import guardar_figura, titulo, trayectoria

R = 4.0
X0 = 0.314159265
N = 100
UMBRAL = 0.1

# Escritas como texto para que se vea que difieren en una sola cifra
SEMILLAS = ["0.314159266", "0.3141592651", "0.31415926501",
            "0.314159265001", "0.3141592650001", "0.31415926500001",
            "0.314159265000001"]


def primera_separacion(dist, umbral=UMBRAL):
    indices = np.where(dist > umbral)[0]
    return int(indices[0]) if len(indices) > 0 else None


def ejecutar():
    titulo("PARTE 2 — Sensibilidad a la condición inicial")
    base = trayectoria(X0, R, N)

    plt.figure(figsize=(10, 6))
    print(f"{'Semilla':>20} {'delta0':>10} {'n sep':>6} {'teórico':>8}")
    for s in SEMILLAS:
        y0 = float(s)
        otra = trayectoria(y0, R, N)
        dist = np.abs(base - otra)
        n_sep = primera_separacion(dist)
        delta0 = abs(y0 - X0)
        teorico = np.log2(UMBRAL / delta0)  # la distancia se duplica por paso
        print(f"{s:>20} {delta0:>10.1e} {str(n_sep):>6} {teorico:>8.1f}")

        # Graficar solo mientras la diferencia es significativa
        hasta = min(n_sep + 10, N + 1) if n_sep is not None else N + 1
        plt.semilogy(range(hasta), dist[:hasta] + 1e-17, label=f"δ₀ = {delta0:.0e}")

    plt.axhline(UMBRAL, color="gray", linestyle="--", label="umbral 0,1")
    plt.xlabel("Iteración n")
    plt.ylabel("$|x_n - y_n|$")
    plt.legend()
    guardar_figura("parte2_distancias.png")

    # Paneles con trayectorias: una por semilla (la consigna pide "cada semilla")
    fig, ejes = plt.subplots(len(SEMILLAS), 1, figsize=(10, 15),
                             sharex=True, sharey=True)
    for k, (eje, s) in enumerate(zip(ejes, SEMILLAS)):
        otra = trayectoria(float(s), R, N)
        n_sep = primera_separacion(np.abs(base - otra))
        eje.plot(base, lw=1.2, label="$x_n$ (base)")
        eje.plot(otra, "--", lw=1.2, label="$y_n$ (vecina)")
        eje.axvline(n_sep, color="gray", ls=":", lw=1.5)
        eje.set_title(f"$y_0$ = {s.replace('.', ',')}   "
                      f"($\\delta_0 = 10^{{-{9 + k}}}$, separación en n = {n_sep})",
                      fontsize=10)
        eje.set_ylabel("$x_n$, $y_n$")
    ejes[0].legend(loc="upper left", bbox_to_anchor=(1.01, 1), fontsize=9)
    ejes[-1].set_xlabel("Iteración n")
    guardar_figura("parte2_trayectorias.png")


if __name__ == "__main__":
    ejecutar()
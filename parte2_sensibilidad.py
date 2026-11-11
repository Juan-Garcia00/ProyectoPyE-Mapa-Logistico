import matplotlib.pyplot as plt
import numpy as np

from comun import guardar_figura, titulo, trayectoria

R = 4.0
X0 = 0.314159265
N = 100
UMBRAL = 0.1

# Cada semilla difiere de la base en una sola cifra, cada vez más a la derecha
SEMILLAS = ["0.314159266", "0.3141592651", "0.31415926501",
            "0.314159265001", "0.3141592650001", "0.31415926500001",
            "0.314159265000001"]


def primera_separacion(dist):
    """Primera iteración en la que la distancia supera el umbral."""
    indices = np.where(dist > UMBRAL)[0]
    return int(indices[0]) if len(indices) > 0 else None


def ejecutar():
    titulo("PARTE 2 — Sensibilidad a la condición inicial")
    base = trayectoria(X0, R, N)

    print(f"Semilla base: {X0}\n")
    print(f"{'Semilla vecina':>20} {'Difiere en el decimal':>23} {'Se separan en la iteración':>28}")

    fig_dist = plt.figure(figsize=(10, 6))
    fig_tray, ejes = plt.subplots(len(SEMILLAS), 1, figsize=(10, 16), sharex=True)

    for eje, s in zip(ejes, SEMILLAS):
        otra = trayectoria(float(s), R, N)
        dist = np.abs(base - otra)
        n_sep = primera_separacion(dist)
        decimal = len(s) - 2  # posición de la cifra que cambia
        print(f"{s:>20} {decimal:>23} {n_sep:>28}")

        # Distancia en escala logarítmica, hasta un poco después de separarse
        plt.figure(fig_dist.number)
        hasta = min(n_sep + 10, N + 1)
        plt.semilogy(range(hasta), dist[:hasta], label=f"difieren en el decimal {decimal}")

        # Trayectoria base vs. vecina, con una línea donde se separan
        eje.plot(base, label="base")
        eje.plot(otra, "--", label="vecina")
        eje.axvline(n_sep, color="red", linestyle=":")
        eje.set_title(f"Vecina {s} (difiere en el decimal {decimal}): se separan en n = {n_sep}")
        eje.set_ylabel("valor")
        eje.legend(loc="upper right", fontsize=8)

    plt.figure(fig_dist.number)
    plt.axhline(UMBRAL, color="gray", linestyle="--", label="umbral 0,1")
    plt.title("Distancia entre la trayectoria base y cada vecina (escala logarítmica)")
    plt.xlabel("Iteración n")
    plt.ylabel("$|x_n - y_n|$")
    plt.legend()
    guardar_figura("parte2_distancias.png")

    plt.figure(fig_tray.number)
    ejes[-1].set_xlabel("Iteración n")
    guardar_figura("parte2_trayectorias.png")


if __name__ == "__main__":
    ejecutar()
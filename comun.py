"""Funciones y constantes compartidas por todas las partes del proyecto."""

import os

import matplotlib

matplotlib.use("Agg")  # guarda las figuras sin abrir ventanas
import matplotlib.pyplot as plt
import numpy as np

CARPETA_FIGURAS = "figuras"
os.makedirs(CARPETA_FIGURAS, exist_ok=True)

plt.rcParams.update({"figure.figsize": (8, 5), "font.size": 11})


def logistica(x, r):
    """Un paso del mapa logístico: x_{n+1} = r x_n (1 - x_n)."""
    return r * x * (1 - x)


def trayectoria(x0, r, n):
    """Devuelve un array con x_0, x_1, ..., x_n."""
    xs = np.empty(n + 1)
    xs[0] = x0
    for i in range(n):
        xs[i + 1] = logistica(xs[i], r)
    return xs


def guardar_figura(nombre):
    ruta = os.path.join(CARPETA_FIGURAS, nombre)
    plt.tight_layout()
    plt.savefig(ruta, dpi=200)
    plt.close()
    print(f"Figura guardada: {ruta}")


def titulo(texto):
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)
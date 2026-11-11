"""Parte 5 — Uniformización (4. Uniformización)."""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from comun import guardar_figura, titulo

CUANTILES = [0.10, 0.25, 0.50, 0.75, 0.90]


def decision(p):
    texto_p = "p < 0.001" if p < 0.001 else f"p = {p:.3f}"
    if p < 0.05:
        return f"{texto_p} -> se rechaza H0"
    return f"{texto_p} -> no se rechaza H0"


def ejecutar(muestra):
    titulo("PARTE 4 — Uniformización")
    u = (2 / np.pi) * np.arcsin(np.sqrt(muestra))

    plt.hist(u, bins=40, density=True, alpha=0.6, label="Datos transformados u")
    plt.axhline(1, color="C1", label="Densidad Uniforme(0,1)")
    plt.title("Histograma de los datos transformados")
    plt.xlabel("u")
    plt.ylabel("Densidad")
    plt.ylim(0, 1.5)
    plt.legend(loc="upper center")
    guardar_figura("parte4_histograma_u.png")

    print(f"{'':>14} {'Transformados':>14} {'Uniforme':>10}")
    print(f"{'Media':>14} {u.mean():>14.4f} {0.5:>10.4f}")
    print(f"{'Varianza':>14} {u.var(ddof=1):>14.4f} {1/12:>10.4f}")
    for p in CUANTILES:
        print(f"{'Cuantil ' + str(p):>14} {np.quantile(u, p):>14.4f} {p:>10.4f}")

    ks = stats.kstest(u, "uniform")
    print("\nTest de Kolmogórov–Smirnov (H0: los datos vienen de una Uniforme(0,1))")
    print(f"  D = {ks.statistic:.4f}, {decision(ks.pvalue)}")


if __name__ == "__main__":
    from parte3_distribucion import generar_muestra
    ejecutar(generar_muestra())
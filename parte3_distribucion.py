"""Parte 3 — Distribución de x_1000 (3.1 y 3.2)."""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from comun import guardar_figura, titulo

R = 4.0
N = 10_000
ITERACIONES = 1000
CUANTILES = [0.10, 0.25, 0.50, 0.75, 0.90]


def generar_muestra(n=N, iteraciones=ITERACIONES):
    """Semillas deterministas k/(n+1), k = 1..n; devuelve x_1000 de cada una."""
    x = np.arange(1, n + 1) / (n + 1)
    for _ in range(iteraciones):  # las n trayectorias en paralelo
        x = R * x * (1 - x)
    return x


def tabla_estadisticos(x):
    cuant_beta = [np.sin(np.pi * p / 2) ** 2 for p in CUANTILES]
    print(f"\n{'':>10} {'Muestra':>10} {'Uniforme':>10} {'Beta':>10}")
    print(f"{'Media':>10} {x.mean():>10.4f} {0.5:>10.4f} {0.5:>10.4f}")
    print(f"{'Varianza':>10} {x.var(ddof=1):>10.4f} {1/12:>10.4f} {1/8:>10.4f}")
    for p, qb in zip(CUANTILES, cuant_beta):
        print(f"{'Q' + str(p):>10} {np.quantile(x, p):>10.4f} {p:>10.4f} {qb:>10.4f}")


def ejecutar():
    titulo("PARTE 3 — Distribución de x_1000")
    x = generar_muestra()

    grilla = np.linspace(0.001, 0.999, 500)
    plt.hist(x, bins=40, density=True, alpha=0.6, label="Muestra")
    plt.plot(grilla, np.ones_like(grilla), label="Uniforme(0,1)")
    plt.plot(grilla, stats.beta.pdf(grilla, 0.5, 0.5), label="Beta(1/2, 1/2)")
    plt.xlabel("$x_{1000}$")
    plt.ylabel("Densidad")
    plt.ylim(0, 5)
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.12), ncol=3)
    guardar_figura("parte3_histograma.png")

    ordenados = np.sort(x)
    fde = np.arange(1, N + 1) / N
    plt.step(ordenados, fde, where="post", label="FDA empírica")
    plt.plot(grilla, grilla, "--", label="FDA Uniforme(0,1)")
    plt.plot(grilla, stats.beta.cdf(grilla, 0.5, 0.5), ":", label="FDA Beta(1/2, 1/2)")
    plt.xlabel("x")
    plt.ylabel("F(x)")
    plt.legend(loc="lower right")
    guardar_figura("parte3_fda.png")

    tabla_estadisticos(x)

    ks_u = stats.kstest(x, "uniform")
    ks_b = stats.kstest(x, "beta", args=(0.5, 0.5))
    print(f"\nKS vs Uniforme: D = {ks_u.statistic:.4f}, p = {ks_u.pvalue:.3g}")
    print(f"KS vs Beta:     D = {ks_b.statistic:.4f}, p = {ks_b.pvalue:.3g}")
    return x


if __name__ == "__main__":
    ejecutar()

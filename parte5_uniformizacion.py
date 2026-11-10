"""Parte 5 — Uniformización (4. Uniformización)."""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from comun import guardar_figura, titulo

CUANTILES = [0.10, 0.25, 0.50, 0.75, 0.90]


def ejecutar(muestra):
    titulo("PARTE 4 — Uniformización")
    u = (2 / np.pi) * np.arcsin(np.sqrt(muestra))

    plt.hist(u, bins=40, density=True, alpha=0.6, label="u transformada")
    plt.axhline(1, color="C1", label="Uniforme(0,1)")
    plt.xlabel("u")
    plt.ylabel("Densidad")
    plt.legend()
    guardar_figura("parte4_histograma_u.png")

    print(f"Media:    {u.mean():.4f}  (teórica 0.5)")
    print(f"Varianza: {u.var(ddof=1):.4f}  (teórica {1/12:.4f})")
    for p in CUANTILES:
        print(f"Q{p}: {np.quantile(u, p):.4f}  (teórico {p})")

    ks = stats.kstest(u, "uniform")
    print(f"KS vs Uniforme: D = {ks.statistic:.4f}, p = {ks.pvalue:.3g}")


if __name__ == "__main__":
    from parte3_distribucion import generar_muestra
    ejecutar(generar_muestra())
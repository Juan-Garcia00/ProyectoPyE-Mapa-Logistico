"""Parte 4 — 3.3 Dependencia."""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from comun import guardar_figura, titulo, trayectoria


def decision(p):
    texto_p = "p < 0.001" if p < 0.001 else f"p = {p:.3f}"
    if p < 0.05:
        return f"{texto_p} -> se rechaza H0"
    return f"{texto_p} -> no se rechaza H0"


def chi2_pares(x, bins=10):
    """Test chi-cuadrado de independencia sobre pares (x_i, x_{i+1}).

    Divide el cuadrado [0,1]x[0,1] en 10x10 casillas con la misma probabilidad
    y cuenta cuántos pares caen en cada una. Si los datos son independientes,
    los pares se reparten parejo entre las 100 casillas.
    """
    bordes = np.quantile(x, np.linspace(0, 1, bins + 1))
    tabla, _, _ = np.histogram2d(x[:-1], x[1:], bins=[bordes, bordes])
    chi2, p, gl, _ = stats.chi2_contingency(tabla)
    return chi2, p, gl


def analizar(x, nombre):
    correlacion = np.corrcoef(x[:-1], x[1:])[0, 1]
    chi2, p, gl = chi2_pares(x)
    print(f"\n{nombre}")
    print(f"  Correlación entre cada valor y el siguiente: {correlacion:.4f}")
    print(f"  Chi-cuadrado de independencia: chi2 = {chi2:.1f}, gl = {gl}, {decision(p)}")


def ejecutar(muestra):
    titulo("PARTE 3.3 — Dependencia")
    print("H0 del chi-cuadrado: cada valor es independiente del siguiente")
    consecutiva = trayectoria(0.314159265, 4.0, 10_000)[1:]
    analizar(muestra, "(a) Muestra: x_1000 de cada semilla, una al lado de la otra")
    analizar(consecutiva, "(b) Una sola trayectoria: x_1, x_2, ..., x_10000")

    fig, (izq, der) = plt.subplots(1, 2, figsize=(12, 6))
    izq.plot(muestra[:-1], muestra[1:], ".", markersize=1)
    izq.set_title("(a) Muestra: cada $x_{1000}$ vs. el siguiente")
    der.plot(consecutiva[:-1], consecutiva[1:], ".", markersize=1)
    der.set_title("(b) Una trayectoria: cada $x_n$ vs. $x_{n+1}$")
    for eje in (izq, der):
        eje.set_xlabel("valor")
        eje.set_ylabel("valor siguiente")
    guardar_figura("parte3_dispersion.png")


if __name__ == "__main__":
    from parte3_distribucion import generar_muestra
    ejecutar(generar_muestra())

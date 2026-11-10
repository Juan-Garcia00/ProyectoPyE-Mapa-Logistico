"""Parte 4 — 3.3 Dependencia."""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from statsmodels.sandbox.stats.runs import runstest_1samp
from statsmodels.stats.diagnostic import acorr_ljungbox

from comun import guardar_figura, titulo, trayectoria


def chi2_pares(x, bins=10):
    """Chi-cuadrado de independencia sobre pares consecutivos (x_i, x_{i+1})."""
    bordes = np.quantile(x, np.linspace(0, 1, bins + 1))  # bins equiprobables
    tabla, _, _ = np.histogram2d(x[:-1], x[1:], bins=[bordes, bordes])
    tabla = tabla[tabla.sum(axis=1) > 0][:, tabla.sum(axis=0) > 0]
    chi2, p, gl, _ = stats.chi2_contingency(tabla)
    return chi2, p, gl


def tests(x, nombre):
    z, p_rachas = runstest_1samp(x, cutoff="median")
    lb = acorr_ljungbox(x, lags=[10], return_df=True)
    chi2, p_chi, gl = chi2_pares(x)
    print(f"\n{nombre}")
    print(f"  Rachas:        z = {z:.3f}, p = {p_rachas:.3g}")
    print(f"  Ljung-Box(10): Q = {lb['lb_stat'].iloc[0]:.3f}, p = {lb['lb_pvalue'].iloc[0]:.3g}")
    print(f"  Chi2 pares:    chi2 = {chi2:.1f}, gl = {gl}, p = {p_chi:.3g}")
    print(f"  Autocorrelación lag 1: {np.corrcoef(x[:-1], x[1:])[0, 1]:.4f}")


def dispersion(x, nombre_archivo, etiqueta):
    plt.figure(figsize=(6, 6))
    plt.plot(x[:-1], x[1:], ".", markersize=1)
    plt.xlabel(f"{etiqueta}$_i$")
    plt.ylabel(f"{etiqueta}$_{{i+1}}$")
    guardar_figura(nombre_archivo)


def ejecutar(muestra):
    titulo("PARTE 3.3 — Dependencia")
    consecutiva = trayectoria(0.314159265, 4.0, 10_000)[1:]
    tests(muestra, "Muestra de x_1000 (semillas k/10001, en orden)")
    tests(consecutiva, "Trayectoria consecutiva x_1 ... x_10000")
    dispersion(muestra, "parte3_dispersion_muestra.png", "x")
    dispersion(consecutiva, "parte3_dispersion_trayectoria.png", "x")


if __name__ == "__main__":
    from parte3_distribucion import generar_muestra
    ejecutar(generar_muestra())
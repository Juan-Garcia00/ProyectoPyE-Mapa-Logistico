import numpy as np

from comun import titulo

R = 4.0
N = 10_000
ITERACIONES = 1000


def generar_muestra(n=N, iteraciones=ITERACIONES):
    """Semillas deterministas k/(n+1), k = 1..n; devuelve x_1000 de cada una."""
    x = np.arange(1, n + 1) / (n + 1)
    for _ in range(iteraciones):  # las n trayectorias en paralelo
        x = R * x * (1 - x)
    return x


def ejecutar():
    titulo("PARTE 3 — Distribución de x_1000")
    x = generar_muestra()
    print(f"Muestra generada: {len(x)} valores, media = {x.mean():.4f}")
    return x


if __name__ == "__main__":
    ejecutar()
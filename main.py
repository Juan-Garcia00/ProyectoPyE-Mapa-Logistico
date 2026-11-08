"""Programa principal: reproduce todas las figuras y tablas del informe.

Uso:
    python main.py
"""

import parte1_dinamica
import parte2_sensibilidad
import parte3_distribucion
import parte4_dependencia
import parte5_uniformizacion

if __name__ == "__main__":
    parte1_dinamica.ejecutar()
    parte2_sensibilidad.ejecutar()
    muestra = parte3_distribucion.ejecutar()  # devuelve los 10 000 valores x_1000
    parte4_dependencia.ejecutar(muestra)
    parte5_uniformizacion.ejecutar(muestra)
    print("\nListo. Las figuras están en la carpeta figuras/")
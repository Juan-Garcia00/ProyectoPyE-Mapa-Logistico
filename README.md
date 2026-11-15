# Caos determinista y pseudoaleatoriedad con el mapa logístico

Proyecto de investigación de **Probabilidad y Estadística Aplicada**
Facultad de Ingeniería y Tecnologías, Universidad Católica del Uruguay (2026).

**Autores:** Joaquín Aires, Joaquín Bauza, Juan Diego García, Tiago Garrido.

El código estudia el mapa logístico x<sub>n+1</sub> = r·x<sub>n</sub>(1 − x<sub>n</sub>): su dinámica según el parámetro r, la sensibilidad a las condiciones iniciales, la distribución de los valores que genera con r = 4, la dependencia entre observaciones y una transformación que los vuelve uniformes. Al ejecutarlo se reproducen todas las figuras y tablas del informe.

## Requisitos

- Python 3.10 o superior
- Las bibliotecas de `requirements.txt`: NumPy, SciPy y Matplotlib

## Instalación

```bash
git clone https://github.com/Juan-Garcia00/ProyectoPyE-Mapa-Logistico.git
cd ProyectoPyE-Mapa-Logistico

python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

Esto ejecuta todas las partes en orden:

- Las **tablas** y los resultados numéricos se imprimen en la consola, junto con la decisión de cada test (se rechaza o no H0 con α = 0,05).
- Las **figuras** se guardan como PNG en la carpeta `figuras/`, que se crea automáticamente.

No hace falta ingresar ningún dato: el programa corre de principio a fin sin interacción.

Cada parte también puede ejecutarse sola, por ejemplo:

```bash
python parte2_sensibilidad.py
```

Las partes 4 y 5 necesitan la muestra que genera la parte 3, así que se ejecutan desde `main.py`.

## Estructura del proyecto

| Archivo | Contenido | Sección de la consigna |
| --- | --- | --- |
| `main.py` | Programa principal: ejecuta todas las partes en orden | — |
| `comun.py` | Funciones compartidas: mapa logístico, trayectorias, guardado de figuras | — |
| `parte1_dinamica.py` | Trayectorias por régimen, solución explícita para r = 4, diagrama de bifurcación con la ventana de período 3 marcada, comportamiento con varias semillas | 1. Estudio propedéutico |
| `parte2_sensibilidad.py` | Separación de trayectorias con semillas cercanas | 2. Experimento de sensibilidad |
| `parte3_distribucion.py` | Muestra de 10 000 valores x<sub>1000</sub>, histograma, FDA, estadísticos y tests de Kolmogórov–Smirnov | 3.1 y 3.2 |
| `parte4_dependencia.py` | Correlación entre valores consecutivos y test chi-cuadrado de independencia | 3.3 Dependencia |
| `parte5_uniformizacion.py` | Transformación u = (2/π)·arcsin(√x) y verificación de uniformidad | 4. Uniformización |
| `figuras/` | Figuras generadas por el programa | — |
| `requirements.txt` | Dependencias de Python | — |

## Reproducibilidad

Los resultados son idénticos en cada ejecución porque el programa no usa números aleatorios:

- Las 10 000 semillas de la parte 3 se construyen de forma determinista como x<sub>0,k</sub> = k / 10001, con k = 1, …, 10 000.
- Las demás semillas son valores fijos escritos en el código (por ejemplo, x<sub>0</sub> = 0,23432 y x<sub>0</sub> = 0,314159265).

Los cálculos usan aritmética de punto flotante de doble precisión (`float64`). Como el sistema es caótico, versiones muy distintas de NumPy o del procesador podrían producir diferencias en los últimos decimales de las trayectorias largas; las conclusiones estadísticas no cambian.
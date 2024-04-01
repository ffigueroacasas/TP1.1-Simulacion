import random
import sys
import matplotlib.pyplot as plt
import numpy as np


if len(sys.argv) != 5 or sys.argv[1] != "-n":
    print("Uso: python programa.py -n <num_valores>")
    sys.exit(1)

tiradas = int(sys.argv[2])

corridas = int(sys.argv[3])

nro_elegido = int(sys.argv[4])


def tirada():
    """emite un valor aleatorio entre 0 y 36"""
    return random.randint(0, 36)


def graficar_frecuencia_relativa(frecuencias_relativas, tiradas):
    plt.figure(figsize=(10, 6))
    plt.plot(
        frecuencias_relativas,
        label="Frecuencia Relativa del nro X respecto del nro de tiradas n",
        color="blue",
    )
    plt.plot(
        [1 / 37] * tiradas,
        label="Frecuencia Relativa Esperada",
        linestyle="--",
        color="red",
    )
    plt.xlabel("Número de tirada")
    plt.ylabel("Frecuencia Relativa")
    plt.title("Gráfico de Frecuencias Relativas en la Ruleta")
    plt.legend()
    plt.grid(True)
    plt.show()


def graficar_promedios(promedios, tiradas):
    plt.figure(figsize=(10, 6))
    plt.plot(
        promedios,
        label="Valor Promedio obtenido respecto del nro de tiradas n",
        color="blue",
    )
    plt.plot(
        [18] * tiradas,
        label="Valor Promedio Esperado",
        linestyle="--",
        color="red",
    )
    plt.xlabel("Número de tirada")
    plt.ylabel("Valor Promedio")
    plt.title("Gráfico de Promedios en la Ruleta")
    plt.legend()
    plt.grid(True)
    plt.show()


def graficar_desvios_estandar(desvios, tiradas):
    plt.figure(figsize=(10, 6))
    plt.plot(
        desvios,
        label="Desvio Estándar obtenido respecto del nro de tiradas n",
        color="blue",
    )
    plt.plot(
        [np.std(range(0, 37))] * tiradas,
        label="Desvio Estándar Esperado",
        linestyle="--",
        color="red",
    )
    plt.xlabel("Número de tirada")
    plt.ylabel("Desvío Estándar")
    plt.title("Gráfico de Desvíos Estándares en la Ruleta")
    plt.legend()
    plt.grid(True)
    plt.show()


def graficar_varianzas(varianzas, tiradas):
    plt.figure(figsize=(10, 6))
    plt.plot(
        varianzas,
        label="Varianza obtenida respecto del nro de tiradas n",
        color="blue",
    )
    plt.plot(
        [np.std(range(0, 37)) ** 2] * tiradas,
        label="Varianza Esperada",
        linestyle="--",
        color="red",
    )
    plt.xlabel("Número de tirada")
    plt.ylabel("Varianza")
    plt.title("Gráfico de Varianzas en la Ruleta")
    plt.legend()
    plt.grid(True)
    plt.show()


for j in range(corridas):
    resultados = []
    frecuencia_absoluta = 0
    frecuencias_relativas = []
    promedios = []
    desvios = []
    varianzas = []
    for i in range(tiradas):
        resultados.append(tirada())
        if resultados[-1] == nro_elegido:
            frecuencia_absoluta = frecuencia_absoluta + 1
        # calculo la frecuencia relativa actual y la guardo
        frecuencia_relativa = frecuencia_absoluta / (i + 1)
        frecuencias_relativas.append(frecuencia_relativa)
        # calculo el promedio actual y lo guardo
        promedio = sum(resultados) / len(resultados)
        promedios.append(promedio)
        # calculo el desvio estandar actual y lo guardo
        desvio = np.std(resultados)
        desvios.append(desvio)
        # calculo la varianza actual y la guardo
        varianza = desvio**2
        varianzas.append(varianza)
    graficar_frecuencia_relativa(
        frecuencias_relativas=frecuencias_relativas, tiradas=tiradas
    )
    graficar_promedios(promedios=promedios, tiradas=tiradas)
    graficar_desvios_estandar(desvios=desvios, tiradas=tiradas)
    graficar_varianzas(varianzas=varianzas, tiradas=tiradas)

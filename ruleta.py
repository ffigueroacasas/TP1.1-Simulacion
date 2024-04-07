import random
import sys
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode

if len(sys.argv) != 5 or sys.argv[1] != "-n":
    print(
        "Uso: python programa.py -n <num_valores> (nro_tiradas, nro_corridas, nro_elegido)"
    )
    sys.exit(1)

tiradas = int(sys.argv[2])

corridas = int(sys.argv[3])

nro_elegido = int(sys.argv[4])


def tirada():
    """emite un valor aleatorio entre 0 y 36"""
    return random.randint(0, 36)


def graficar_varios_promedios(promedios):
    plt.figure(figsize=(10, 6))
    for i in range(len(promedios)):
        plt.plot(
            promedios[i],
            label=f"Valor Promedio obtenido respecto del nro de tiradas, corrida {i + 1}",
        )
    plt.plot(
        [18] * tiradas,
        label="Valor Promedio Esperado",
        linestyle="--",
        color="red",
    )
    plt.title("Gráfico de Promedios en la Ruleta")
    plt.legend()
    plt.grid(True)
    plt.xlabel("Número de tirada")
    plt.ylabel("Valor Promedio")
    plt.show()


def graficar_varias_frecuencias_relativas(frecuencias):
    plt.figure(figsize=(10, 6))
    for i in range(len(frecuencias)):
        plt.plot(
            frecuencias[i],
            label=f"Frecuencia Relativa del nro X respecto del nro de tiradas, corrida {i + 1}",
        )
    plt.plot(
        [1 / 37] * tiradas,
        label="Valor Promedio Esperado",
        linestyle="--",
        color="red",
    )
    plt.title("Gráfico de Frecuencias Relativas en la Ruleta")
    plt.legend()
    plt.grid(True)
    plt.xlabel("Número de tirada")
    plt.ylabel("Frecuencia Relativa")
    plt.show()


def graficar_varios_desvios(desvios):
    plt.figure(figsize=(10, 6))
    for i in range(len(desvios)):
        plt.plot(
            desvios[i],
            label=f"Desvio Estandar obtenido respecto del nro de tiradas, corrida {i + 1}",
        )
    plt.plot(
        [np.std(range(0, 37))] * tiradas,
        label="Desvio Estandar Esperado",
        linestyle="--",
        color="red",
    )
    plt.title("Gráfico de Desvios Estandar en la Ruleta")
    plt.legend()
    plt.grid(True)
    plt.xlabel("Número de tirada")
    plt.ylabel("Desvio Estandar")
    plt.show()


def graficar_varias_varianzas(varianzas):
    plt.figure(figsize=(10, 6))
    for i in range(len(varianzas)):
        plt.plot(
            varianzas[i],
            label=f"Varianza obtenida respecto del nro de tiradas, corrida {i + 1}",
        )
    plt.plot(
        [np.std(range(0, 37)) ** 2] * tiradas,
        label="Varianza Esperada",
        linestyle="--",
        color="red",
    )
    plt.title("Gráfico de Varianzas en la Ruleta")
    plt.legend()
    plt.grid(True)
    plt.xlabel("Número de tirada")
    plt.ylabel("Varianza")
    plt.show()


def graficar_varias_medianas(medianas):
    plt.figure(figsize=(10, 6))
    for i in range(len(medianas)):
        plt.plot(
            medianas[i],
            label=f"Mediana obtenida respecto del nro de tiradas, corrida {i + 1}",
        )
    plt.plot(
        [18] * tiradas,
        label="Mediana Esperada",
        linestyle="--",
        color="red",
    )
    plt.title("Gráfico de Medianas en la Ruleta")
    plt.legend()
    plt.grid(True)
    plt.xlabel("Número de tirada")
    plt.ylabel("Mediana")
    plt.show()


def graficar_varias_modas(modas):
    plt.figure(figsize=(10, 6))
    for i in range(len(modas)):
        plt.plot(
            modas[i],
            label=f"Moda obtenida respecto del nro de tiradas, corrida {i + 1}",
        )
    # plt.plot(
    #     [mode(range(0, 37))] * tiradas,
    #     label="Moda Esperada (Teóricamente no existe)",
    #     linestyle="--",
    #     color="red",
    # )
    plt.title("Gráfico de Moda en la Ruleta")
    plt.legend()
    plt.grid(True)
    plt.xlabel("Número de tirada")
    plt.ylabel("Moda")
    plt.show()


def graficar_varios_rangos(rangos):
    plt.figure(figsize=(10, 6))
    for i in range(len(rangos)):
        plt.plot(
            rangos[i],
            label=f"Rango respecto del nro de tiradas, corrida {i + 1}",
        )
    plt.plot(
        [36] * tiradas,
        label="Rango Esperado (Con suficientes tiradas siempre debería tender a 36)",
        linestyle="--",
        color="red",
    )
    plt.title("Gráfico de Rango en la Ruleta")
    plt.legend()
    plt.grid(True)
    plt.xlabel("Número de tirada")
    plt.ylabel("Rango")
    plt.show()


def graficar_terceros_cuartiles(q3s):
    plt.figure(figsize=(10, 6))
    for i in range(len(q3s)):
        plt.plot(
            q3s[i],
            label=f"Tercer cuartil respecto del nro de tiradas, corrida {i + 1}",
        )
    plt.plot(
        [27] * tiradas,
        label="Tercer cuartil Esperado",
        linestyle="--",
        color="red",
    )
    plt.title("Gráfico del tercer cuartil en la Ruleta")
    plt.legend()
    plt.grid(True)
    plt.xlabel("Número de tirada")
    plt.ylabel("Tercer Cuartil")
    plt.show()


resultados = []
promedios = []
frecuencias_absolutas = []
frecuencias_relativas = []
desvios_estandar = []
varianzas = []
medianas = []
modas = []
rangos = []
terceros_cuartiles = []
for j in range(corridas):
    resultados_corrida_n = []
    promedios_corrida_n = []
    frecuencia_absoluta_corrida_n = 0
    frecuencias_relativas_corrida_n = []
    desvios_estandar_corrida_n = []
    varianzas_corrida_n = []
    medianas_corrida_n = []
    modas_corrida_n = []
    rangos_corrida_n = []
    terceros_cuartiles_corrida_n = []
    for i in range(tiradas):
        resultados_corrida_n.append(tirada())
        if resultados_corrida_n[-1] == nro_elegido:
            frecuencia_absoluta_corrida_n += 1
        # calculo la frecuencia relativa
        frecuencias_relativas_corrida_n.append(frecuencia_absoluta_corrida_n / (i + 1))
        # calculo el promedio
        promedio = sum(resultados_corrida_n) / len(resultados_corrida_n)
        promedios_corrida_n.append(promedio)
        # calculo el desvio
        desvio = np.std(resultados_corrida_n)
        desvios_estandar_corrida_n.append(desvio)
        # calculo la varianza
        varianza = desvio**2
        varianzas_corrida_n.append(varianza)
        # calculo la mediana
        mediana = np.median(resultados_corrida_n)
        medianas_corrida_n.append(mediana)
        # calculo la moda
        moda = mode(resultados_corrida_n)
        modas_corrida_n.append(moda)
        # calculo el rango
        rango = max(resultados_corrida_n) - min(resultados_corrida_n)
        rangos_corrida_n.append(rango)
        # calculo el tercer cuartil
        q3 = np.percentile(resultados_corrida_n, 75)
        terceros_cuartiles_corrida_n.append(q3)
    resultados.append(resultados_corrida_n)
    promedios.append(promedios_corrida_n)
    frecuencias_relativas.append(frecuencias_relativas_corrida_n)
    desvios_estandar.append(desvios_estandar_corrida_n)
    varianzas.append(varianzas_corrida_n)
    medianas.append(medianas_corrida_n)
    modas.append(modas_corrida_n)
    rangos.append(rangos_corrida_n)
    terceros_cuartiles.append(terceros_cuartiles_corrida_n)
graficar_varios_promedios(promedios)
graficar_varias_frecuencias_relativas(frecuencias_relativas)
graficar_varios_desvios(desvios_estandar)
graficar_varias_varianzas(varianzas)
graficar_varias_medianas(medianas)
graficar_varias_modas(modas)
graficar_varios_rangos(rangos)
graficar_terceros_cuartiles(terceros_cuartiles)

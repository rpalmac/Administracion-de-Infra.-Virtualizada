{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled15.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPtjc/Lot5zPtj/LigmSlpz",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Ejercicio5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_1txvycw9U_S"
      },
      "source": [
        "from math import sin, cos, tan, exp, log\n",
        "\n",
        "def apply_function(f, n):\n",
        "    '''\n",
        "    Función que aplica una función a los enteros desde 1 hasta n.\n",
        "    Parámetros:\n",
        "        f: Es una función que recibe un número real y devuelve otro.\n",
        "        n: Es un número entero positivo.\n",
        "    Devuelve:\n",
        "        Un diccionario con los pares i:f(i) para cada valor entero i de 1 a n.\n",
        "    '''\n",
        "    functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}\n",
        "    result = {}\n",
        "    for i in range(1, n+1):\n",
        "        result[i] = functions[f](i)\n",
        "    return result\n",
        "\n",
        "def calculator():\n",
        "    '''\n",
        "    Función que aplica una función seleccionada por el usuario (seno, coseno, tangente, exponencial o logarítmo) a la lista de enteros desde 1 hasta n. \n",
        "    Imprime por pantalla una tabla con la secuencia de enteros y el resultado de aplicarles la función introducida.\n",
        "    Parámetros:\n",
        "        f: Es una cadena con la función a aplicar (sin, cos, tan, exp o log).\n",
        "        n: Es un entero positivo.\n",
        "    '''\n",
        "    f = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')\n",
        "    n = int(input('Introduce un entero positivo: '))\n",
        "    for i, j in apply_function(f, n).items():\n",
        "        print (i, '\\t', j)\n",
        "    return\n",
        "\n",
        "calculator()"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
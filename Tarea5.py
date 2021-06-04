{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled4.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPn+hbLNRB7f9Hb3hiUtQYf",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Tarea5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q6qPrTLdEJzc",
        "outputId": "b230db28-5f87-469b-aa42-498f8b364d23"
      },
      "source": [
        "def square(sample):\n",
        "    \"\"\"Función que calcula los cuadrados de una lista de números.\n",
        "    Parámetros\n",
        "    sample: Es una lista de números\n",
        "    Devuelve una lista con los cuadrados de los números de la lista sample.\n",
        "    \"\"\"\n",
        "    list = []\n",
        "    for i in sample:\n",
        "        list.append(i**2)\n",
        "    return list\n",
        "\n",
        "def statistics(sample):\n",
        "    \"\"\"Función que calcula la media, varianza y desviación típica de una muestra de números.\n",
        "    Parámetros\n",
        "    sample: Es una lista de números\n",
        "    Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.\n",
        "    \"\"\"\n",
        "    stat = {}\n",
        "    stat['media'] = sum(sample)/len(sample)\n",
        "    stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2\n",
        "    stat['desviacion tipica'] = stat['varianza']**0.5\n",
        "    return stat\n",
        "\n",
        "print(statistics([1, 2, 3, 4, 5]))\n",
        "print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'media': 3.0, 'varianza': 2.0, 'desviacion tipica': 1.4142135623730951}\n",
            "{'media': 8.700000000000001, 'varianza': 18.95666666666665, 'desviacion tipica': 4.353925431913901}\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
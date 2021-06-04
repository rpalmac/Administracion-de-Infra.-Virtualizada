{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled9.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPoDRnVjj315VlR2xRDXBfa",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Tarea4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jmizPr-RHywj",
        "outputId": "20e2c826-2e15-4522-a574-37fa45f4e8ad"
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
        "print(square([1, 2, 3, 4, 5]))\n",
        "print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1, 4, 9, 16, 25]\n",
            "[5.289999999999999, 32.49, 46.239999999999995, 94.08999999999999, 146.41, 243.35999999999999]\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
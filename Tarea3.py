{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled4.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPBFArFliaoLmq8ct7VsIRc",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Tarea3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q6qPrTLdEJzc",
        "outputId": "4ebb1ca9-d32a-4e56-fe6a-29b9630d8e5d"
      },
      "source": [
        "def mean(sample):\n",
        "    \"\"\"Función que calcula la media de una muestra de números.\n",
        "    Parámetros\n",
        "    sample: Es una lista de números\n",
        "    Devuelve la media de los números en sample. \n",
        "    \"\"\"\n",
        "    return sum(sample)/len(sample)\n",
        "\n",
        "print(mean([1, 2, 3, 4, 5]))\n",
        "print(mean([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3.0\n",
            "8.700000000000001\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
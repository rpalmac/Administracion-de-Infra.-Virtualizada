{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled6.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOgWWa/tX6XjCbeNIg7MCyL",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Tarea7.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q3s0r1TxGpuQ",
        "outputId": "a748181f-8322-4558-915b-aa727aaa7de7"
      },
      "source": [
        "def to_decimal(n):\n",
        "    \"\"\"Función que convierte un número binario en decimal.\n",
        "    Parámetros:\n",
        "        - n: Es una cadena de ceros y unos.\n",
        "    Devuelve:\n",
        "        El número decimal correspondiente a n.\n",
        "    \"\"\"\n",
        "    n = list(n)\n",
        "    n.reverse()\n",
        "    decimal = 0\n",
        "    for i in range(len(n)):\n",
        "        decimal += int(n[i]) * 2 ** i\n",
        "    return decimal\n",
        "\n",
        "def to_binary(n):\n",
        "    \"\"\"Función que convierte un número decimal en binario.\n",
        "    Parámetros:\n",
        "        - n: Es un número entero.\n",
        "    Devuelve:\n",
        "        El número binario correspondiente a n.\n",
        "    \"\"\"\n",
        "    binary = []\n",
        "    while n > 0:\n",
        "        binary.append(str(n % 2))\n",
        "        n //= 2\n",
        "    binary.reverse()\n",
        "    return ''.join(binary)\n",
        "\n",
        "print(to_decimal('10110'))\n",
        "print(to_binary(22))\n",
        "print(to_decimal(to_binary(22)))\n",
        "print(to_binary(to_decimal('10110')))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "22\n",
            "10110\n",
            "22\n",
            "10110\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
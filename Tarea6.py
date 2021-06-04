{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled5.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPZHUTwWSoyUIsnTEipRVwZ",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Tarea6.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wI1L5AfiGgVG",
        "outputId": "9640c60d-dc3f-49f5-8233-87a7262161b1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "def mcd(n, m):\n",
        "    \"\"\"Función que calcula el máximo común divisor de dos números.\n",
        "    Parámetros:\n",
        "        - n: Es un número entero.\n",
        "        - m: Es un número entero.\n",
        "    Devuelve:\n",
        "        El máximo común divisor de n y m.\n",
        "    \"\"\"\n",
        "    rest = 0\n",
        "    while(m > 0):\n",
        "        rest = m\n",
        "        m = n % m\n",
        "        n = rest\n",
        "    return n\n",
        "\n",
        "def mcm(n, m):\n",
        "    \"\"\"Función que calcula el mínimo común múltiplo de dos números.\n",
        "    Parámetros:\n",
        "        - n: Es un número entero.\n",
        "        - m: Es un número entero.\n",
        "    Devuelve:\n",
        "        El mínimo común múltiplo de n y m.\n",
        "    \"\"\"\n",
        "    if n > m:\n",
        "        greater = n\n",
        "    else:\n",
        "        greater = m\n",
        "    while (greater % n != 0) or (greater % m != 0):\n",
        "        greater += 1\n",
        "    return greater\n",
        "\n",
        "print(mcd(24,36))\n",
        "print(mcm(24,36))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "12\n",
            "72\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
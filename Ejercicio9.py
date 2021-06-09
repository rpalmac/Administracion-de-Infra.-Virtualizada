{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled20.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMzgbmqJN7A91tcYtkAA51Y",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Ejercicio9.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PPDv0dbn-srl",
        "outputId": "dfb9f8ce-3d5b-4aac-c867-8ae8e0b91137"
      },
      "source": [
        "a = ((1, 2, 3),\n",
        "     (3, 2, 1))\n",
        "b = ((1, 2),\n",
        "     (3, 4),\n",
        "     (5, 6))\n",
        "\n",
        "def producto(a, b):\n",
        "    producto = []\n",
        "    for i in range(len(a)):\n",
        "        fila = [] \n",
        "        for j in range(len(b[0])):\n",
        "            suma = 0\n",
        "            for k in range(len(a[0])):\n",
        "                suma += a[i][k] * b[k][j]\n",
        "            fila.append(suma)\n",
        "        producto.append(tuple(fila))\n",
        "    return tuple(producto)\n",
        "\n",
        "print(producto(a, b))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "((22, 28), (14, 20))\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
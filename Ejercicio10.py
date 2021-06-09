{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled21.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPUqGZvc3sbO19DQVWAAPMh",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Ejercicio10.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bJd1dVh7_DyS",
        "outputId": "9f00edaf-4980-4702-9adf-a007f64e8b95"
      },
      "source": [
        "u = [1, 2, 3]\n",
        "v = [4, 5, 6]\n",
        "\n",
        "def producto_escalar(u, v):\n",
        "    for i in range(len(u)):\n",
        "        u[i] *= v[i]\n",
        "    return sum(u)\n",
        "\n",
        "print(producto_escalar(u, v))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "32\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
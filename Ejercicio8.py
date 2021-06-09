{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled19.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOU/2VklnPagfT4FR0MhiLV",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Ejercicio8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EGBKtptH-c-n"
      },
      "source": [
        "base = float(input('Introduce la base imponible de la factura: '))\n",
        "\n",
        "def aplica_iva(base, iva = 16):\n",
        "    base += base * iva / 100  \n",
        "    return base \n",
        "\n",
        "print(aplica_iva(base))"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
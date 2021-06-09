{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled18.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOtdkc7aR4Rn3aBl68J9rTI",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Ejercicio7.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iYvsInS--NRQ",
        "outputId": "faabfb96-2a2b-48c1-8cc2-cb8efa15f8e0"
      },
      "source": [
        "contraseña = input('Introduce la contraseña: ')\n",
        "if contraseña in ['sesamo']:\n",
        "    print('Pasa')\n",
        "else:\n",
        "    print('No pasa')"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Introduce la contraseña: sesamo\n",
            "Pasa\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
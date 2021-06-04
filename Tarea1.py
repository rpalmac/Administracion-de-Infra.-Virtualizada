{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled4.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOe86xcMzux8Kt/kw4YEoxm",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Tarea1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q6qPrTLdEJzc",
        "outputId": "2db376b6-9f3c-4262-fe26-e3f93f828012"
      },
      "source": [
        "def invoice(amount, vat=21):\n",
        "    \"\"\"Función de aplica el IVA a una factura.\n",
        "    Parametros\n",
        "    amount: Es la cantidad sin IVA\n",
        "    vat: Es el porcentaje de IVA\n",
        "    Devuelve el total de la factura una vez aplicado el IVA. \n",
        "    \"\"\"\n",
        "    return amount + amount*vat/100\n",
        "\n",
        "print(invoice(1000,10))\n",
        "print(invoice(1000))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1100.0\n",
            "1210.0\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
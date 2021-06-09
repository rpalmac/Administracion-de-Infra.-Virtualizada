{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled14.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMUIftjDksEsb6Ike8rJMG8",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Ejercicio4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N-5ZggdS9IAq",
        "outputId": "c3a88ec2-6e35-4c74-c55a-272d2d675223"
      },
      "source": [
        "def apply_discount(price, discount):\n",
        "    '''\n",
        "    Función que aplica un descuento a una cantidad.\n",
        "    Parámetros:\n",
        "        price: Es un valor real con el precio al que aplicar el descuento.\n",
        "        discount: Es el porcentaje a descontar.\n",
        "    Devuelve:\n",
        "        El precio final tras aplicar el descuento.\n",
        "    '''\n",
        "    return price - price * discount / 100\n",
        "    \n",
        "def apply_IVA(price, percentage):\n",
        "    '''\n",
        "    Función que aplica un IVA a una cantidad.\n",
        "    Parámetros:\n",
        "        price: Es un valor real con el precio al que aplicar el IVA.\n",
        "        percentage: Es el porcentaje del IVA a aplicar.\n",
        "    Devuelve:\n",
        "        El precio final tras aplicar el IVA.\n",
        "    '''\n",
        "    return price + price * percentage / 100\n",
        "\n",
        "def price_basket(basket, function):\n",
        "    '''\n",
        "    Función que calcula el precio de una cesta de la compra una vez aplicada una función a los precios iniciales.\n",
        "    Parámetros:\n",
        "        basket: Es un diccionario formado por pares precio:descuento.\n",
        "        function: Es una función que toma dos valores reales y devuelve otro. Normalmente para aplicar descuentos o IVA.\n",
        "    Devuelve:\n",
        "        El precio final de la cesta de la compra una vez aplicada la función sobre los precios iniciales.\n",
        "    '''\n",
        "    total = 0\n",
        "    for price, discount in basket.items():\n",
        "        total += function(price, discount)\n",
        "    return total\n",
        "\n",
        "print('El precio de la compra tras aplicar los descuentos es: ', price_basket({1000:20, 500:10, 100:1}, apply_discount))\n",
        "print('El precio de la compra tras aplicar el IVA es: ', price_basket({1000:20, 500:10, 100:1}, apply_IVA))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "El precio de la compra tras aplicar los descuentos es:  1349.0\n",
            "El precio de la compra tras aplicar el IVA es:  1851.0\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
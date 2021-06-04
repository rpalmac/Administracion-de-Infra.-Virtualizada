{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled8.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNXTZ9xZcRHEvkDtnQYlMQw",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Tarea2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tn_E2TbsHOON",
        "outputId": "fd7f8c1c-136c-49fb-eb6f-fd7394527edb",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "def circle_area(radius):\n",
        "    \"\"\"Función que calcula el area de un círculo.\n",
        "    Parámetros\n",
        "    radius: Es el radio del círculo.\n",
        "    Devuelve el área del círculo de radio radius. \n",
        "    \"\"\"\n",
        "    pi = 3.1415\n",
        "    return pi*radius**2\n",
        "\n",
        "def cilinder_volume(radius, high):\n",
        "    \"\"\"Función que calcula el volumen de un cilindro.\n",
        "    Parámetros\n",
        "    radius: Es el radio de la base del cilindro.\n",
        "    high: Es la altura del cilindro.\n",
        "    Devuelve el volumen del clindro de radio radius y altura high.\n",
        "    \"\"\"\n",
        "    return circle_area(radius)*high\n",
        "\n",
        "print(cilinder_volume(3,5))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "141.3675\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
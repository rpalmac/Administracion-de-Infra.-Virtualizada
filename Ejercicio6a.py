{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled17.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMej7IcUugMIWfRLfwv7tFs",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Ejercicio6a.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IbYJUYSY9zaI",
        "outputId": "98e68987-7f16-4a17-8aa8-0d6afb3393f8"
      },
      "source": [
        "def grade(score):\n",
        "    '''\n",
        "    Función que devuelve la calificación correspondiente a una nota.\n",
        "    Parámetros:\n",
        "        score: Es un valor real entre 0 y 10.\n",
        "    Devuelve:\n",
        "        La calificación correspondiente a la nota score.\n",
        "    '''\n",
        "    if score < 5:\n",
        "        return 'SS'\n",
        "    elif score < 7:\n",
        "        return 'AP'\n",
        "    elif score < 9:\n",
        "        return 'NT'\n",
        "    elif score < 10:\n",
        "        return 'SB'\n",
        "    else:\n",
        "        return 'MH'\n",
        "\n",
        "def apply_grade(scores):\n",
        "    '''\n",
        "    Función que devuelve la calificación correspondiente a las notas de una lista dada.\n",
        "    Parámetros:\n",
        "        scores: Es una lista de valores reales entre 0 y 10.\n",
        "    Devuelve\n",
        "        La lista de calificaciones correspondiente a las notas de scores.\n",
        "    '''\n",
        "    return [grade(x) for x in scores]\n",
        "\n",
        "print(apply_grade([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "['AP', 'AP', 'SS', 'NT', 'SS', 'SB', 'MH']\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
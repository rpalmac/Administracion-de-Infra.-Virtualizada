{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled7.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyN7a4XyOQ9Ix2HZmRHYq4Z1",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Tarea8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1MFDCZMtG4DI",
        "outputId": "fb5f346c-d65b-4615-d8f2-2e5ba1034558"
      },
      "source": [
        "def count_words(text):\n",
        "    \"\"\"Función que cuenta el número de veces que aparece cada palabra en un texto.\n",
        "    Parámetros:\n",
        "        - text: Es una cadena de caracteres.\n",
        "    Devuelve: \n",
        "        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.\n",
        "    \"\"\"\n",
        "    text = text.split()\n",
        "    words = {}\n",
        "    for i in text:\n",
        "        if i in words:\n",
        "            words[i] += 1\n",
        "        else:\n",
        "            words[i] = 1\n",
        "    return words\n",
        "\n",
        "def most_repeated(words):\n",
        "    max_word = ''\n",
        "    max_freq = 0\n",
        "    for word, freq in words.items():\n",
        "        if freq > max_freq:\n",
        "            max_word = word\n",
        "            max_freq = freq\n",
        "    return max_word, max_freq\n",
        "\n",
        "text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'\n",
        "print(count_words(text))\n",
        "print(most_repeated(count_words(text)))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'Como': 1, 'quieres': 1, 'que': 4, 'te': 1, 'quiera': 3, 'si': 1, 'el': 1, 'quiero': 2, 'me': 3, 'no': 1, 'quiere': 1, 'como': 1}\n",
            "('que', 4)\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled11.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPaqEHqyoDx35SwUMB6emxt",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Ejercicio1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "B79PuLLwITpt",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "bbe8b1f7-0d45-4654-e7ca-ee08ce4bcfe5"
      },
      "source": [
        "def words_file(url):\n",
        "    '''\n",
        "    Función que recibe recibe la url de un fichero de texto y devuelve el número de palabras que contiene.\n",
        "    Parámetros:\n",
        "        url: Es una cadena con la url del fichero de texto.\n",
        "    Devuelve:\n",
        "        El número de palabras que contiene el fichero de texto daro por la url.\n",
        "    '''\n",
        "    from urllib import request\n",
        "    from urllib.error import URLError\n",
        "    try:\n",
        "        file = request.urlopen(url)\n",
        "    except URLError:\n",
        "        return('¡La url ' + url + ' no existe!')\n",
        "    else:\n",
        "        content = file.read()\n",
        "        return len(content.split())\n",
        "\n",
        "print(words_file('https://www.gutenberg.org/files/2000/2000-0.txt'))\n",
        "print(words_file('https://no-existe.txt'))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "389719\n",
            "¡La url https://no-existe.txt no existe!\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
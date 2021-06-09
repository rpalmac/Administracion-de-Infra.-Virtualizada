{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled12.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNI79JyNgs7SIA2P4LI8jtu",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Ejercicio2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bEkwMjNG8jIS",
        "outputId": "41daa479-85c3-48e0-a08e-d1a8720ed90d"
      },
      "source": [
        "def get_pib(url, country='ES'):\n",
        "    '''\n",
        "    Función que muestra por pantalla el pib per cápita un país dado de los años disponibles en un fichero dado.\n",
        "    Parámetros:\n",
        "        url: Es una cadena con la url del fichero de texto que contiene el pib per cápita.\n",
        "        country: Es una cadena con el código del país. \n",
        "    Devuelve:\n",
        "        Un diccionario con pares año:pib del país country que hay en el fichero con la url dada.\n",
        "    '''\n",
        "    from urllib import request\n",
        "    from urllib.error import URLError\n",
        "    try:\n",
        "        f = request.urlopen(url)\n",
        "    except URLError:\n",
        "        return('¡La url ' + url + ' no existe!')\n",
        "    else:\n",
        "        data = f.read().decode('utf-8').split('\\n') # Leer los datos y guardar cada línea en una lista\n",
        "        data = [i.split('\\t') for i in data] # Dividir cada línea por el tabulador\n",
        "        data = [list(map(str.strip, i)) for i in data] # Eliminar espacios en blanco\n",
        "        for i in data:\n",
        "            i[0] = i[0].split(',')[-1] # Obtener el código del país del primer elemento de la lista\n",
        "        data[0][0] = 'years'\n",
        "        data = {i[0]:i[1:] for i in data}\n",
        "        result = {data['years'][i]:data[country][i] for i in range(len(data['years']))}\n",
        "        return result\n",
        "\n",
        "country = input('Introduce el código de un país: ')\n",
        "print('Producto Interior Bruto per cápita de', country)\n",
        "print('Año', '\\t', 'PIB')\n",
        "for year, pib in get_pib('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true').items():\n",
        "    print(year, '\\t', pib)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Introduce el código de un país: mex\n",
            "Producto Interior Bruto per cápita de mex\n",
            "Año \t PIB\n",
            "2000 \t 21460\n",
            "2001 \t 22190\n",
            "2002 \t 22430\n",
            "2003 \t 22680\n",
            "2004 \t 23020\n",
            "2005 \t 23420\n",
            "2006 \t 24000\n",
            "2007 \t 24380\n",
            "2008 \t 24200\n",
            "2009 \t 23100\n",
            "2010 \t 23040\n",
            "2011 \t 22770\n",
            "2012 \t 22080\n",
            "2013 \t 21840\n",
            "2014 \t 22210\n",
            "2015 \t 23080\n",
            "2016 \t 23760\n",
            "2017 \t 24430\n",
            "2018 \t 24910 p\n",
            "2019 \t 25200 p\n",
            "2020 \t 22350 p\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
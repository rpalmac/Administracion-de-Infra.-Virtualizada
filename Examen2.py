{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled11.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOQJDKGJxCkdCFqXau9DDXQ",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Automatizacion-de-Infraestructura-Digital/blob/main/Examen2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "B79PuLLwITpt",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "4e7a5a80-d425-46fd-dd4a-7e42626edbd1"
      },
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "print(\"Construir un programa con la libreria Pandas:\")\n",
        "print(\"\")\n",
        "\n",
        "\n",
        "datos = {\n",
        "  'Nombre': ['Juan', 'Marta', 'Pedro', 'Jorge', 'Blas', 'Lisa', 'Antonio'],\n",
        "  'Edad': [23, 78, 22, 19, 45, 33, 20],\n",
        "  'Género': ['M', 'F', 'M', 'M', 'M', 'F', 'M'],\n",
        "  'Provincia': ['Burgos', 'Madrid', 'Toledo', 'Burgos', 'Madrid', 'Toledo', 'Madrid'],\n",
        "  'Hijos': [2, 0, 0, 3, 2, 1, 4],\n",
        "  'Mascotas': [5, 1, 0, 5, 2, 2, 3]\n",
        "}\n",
        "\n",
        "df = pd.DataFrame(datos)\n",
        "\n",
        "\n",
        "#Paso 1\n",
        "print(\"Crea un DataFrame:\")\n",
        "print(\"\")\n",
        "print(df)\n",
        "\n",
        "\n",
        "#Paso 2\n",
        "print(\"Muestra la información:\")\n",
        "print(\"\")\n",
        "\n",
        "print(df.info())\n",
        "\n",
        "#Paso 3\n",
        "print(\"Muestra las columnas numéricas\")\n",
        "print(\"\")\n",
        "print(df.describe())\n",
        "\n",
        "\n",
        "#Paso 4\n",
        "print(\"Sacar porcentajes de hombres y mujeres en provincias\")\n",
        "print(\"\")\n",
        "print(df.groupby('Provincia').Género.value_counts(normalize = True) * 100)\n",
        "\n",
        "\n",
        "#Paso 5\n",
        "print(\"Mediante un diagrama de dispersión, Muestra número de hijos por el número de mascotas de Madrid\")\n",
        "print(\"\")\n",
        "fig, ax = plt.subplots()\n",
        "df[df.Provincia == 'Madrid'].plot(kind = 'scatter', x = 'Hijos', y = 'Mascotas', ax = ax)\n",
        "plt.show()\n",
        "\n",
        "\n",
        "#Paso 6\n",
        "print(\"Graficar\")\n",
        "print(\"\")\n",
        "\n",
        "\n",
        "fig, ax = plt.subplots()\n",
        "df.groupby('Provincia').size().plot(kind = 'bar')\n",
        "plt.title('Distribución por provincia')\n",
        "plt.show()\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Construir un programa con la libreria Pandas:\n",
            "\n",
            "Crea un DataFrame:\n",
            "\n",
            "    Nombre  Edad Género Provincia  Hijos  Mascotas\n",
            "0     Juan    23      M    Burgos      2         5\n",
            "1    Marta    78      F    Madrid      0         1\n",
            "2    Pedro    22      M    Toledo      0         0\n",
            "3    Jorge    19      M    Burgos      3         5\n",
            "4     Blas    45      M    Madrid      2         2\n",
            "5     Lisa    33      F    Toledo      1         2\n",
            "6  Antonio    20      M    Madrid      4         3\n",
            "Muestra la información:\n",
            "\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 7 entries, 0 to 6\n",
            "Data columns (total 6 columns):\n",
            " #   Column     Non-Null Count  Dtype \n",
            "---  ------     --------------  ----- \n",
            " 0   Nombre     7 non-null      object\n",
            " 1   Edad       7 non-null      int64 \n",
            " 2   Género     7 non-null      object\n",
            " 3   Provincia  7 non-null      object\n",
            " 4   Hijos      7 non-null      int64 \n",
            " 5   Mascotas   7 non-null      int64 \n",
            "dtypes: int64(3), object(3)\n",
            "memory usage: 464.0+ bytes\n",
            "None\n",
            "Muestra las columnas numéricas\n",
            "\n",
            "            Edad     Hijos  Mascotas\n",
            "count   7.000000  7.000000  7.000000\n",
            "mean   34.285714  1.714286  2.571429\n",
            "std    21.383126  1.496026  1.902379\n",
            "min    19.000000  0.000000  0.000000\n",
            "25%    21.000000  0.500000  1.500000\n",
            "50%    23.000000  2.000000  2.000000\n",
            "75%    39.000000  2.500000  4.000000\n",
            "max    78.000000  4.000000  5.000000\n",
            "Sacar porcentajes de hombres y mujeres en provincias\n",
            "\n",
            "Provincia  Género\n",
            "Burgos     M         100.000000\n",
            "Madrid     M          66.666667\n",
            "           F          33.333333\n",
            "Toledo     F          50.000000\n",
            "           M          50.000000\n",
            "Name: Género, dtype: float64\n",
            "Mediante un diagrama de dispersión, Muestra número de hijos por el número de mascotas de Madrid\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        },
        {
          "output_type": "stream",
          "text": [
            "Graficar\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}
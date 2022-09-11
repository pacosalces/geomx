#! /usr/bin/python
# __author__ = [pacosalces,]
#
# Carga archivos geojson con datos de la republica mexicana y calcula el centro

import os
import geopandas
import matplotlib.pyplot as plt

try:
    plt.style.use("pacostyle")
except:
    plt.style.use("default")

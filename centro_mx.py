#! /usr/bin/python
# __author__ = [pacosalces,]
#
# Carga archivos geojson con datos de la republica mexicana
# usando el tutorial de;
# https://geopandas.org/en/stable/getting_started/introduction.html
#
# Aqui en particular calculamos el centroide del pais.

from os.path import exists
from urllib.request import urlopen
from rich.progress import track
import geopandas as geopd
import matplotlib.pyplot as plt

try:
    plt.style.use("pacostyle")
except:
    plt.style.use("default")

# Si no existe ya, se descarga el archivo "shapefile"
# con los datos de division territorial desde la CONABIO
guardar_como = r"./mx_divterr.zip"
if not exists(guardar_como):
    url = r"http://www.conabio.gob.mx/informacion/gis/maps/geo/desta4mgw.zip"
    with urlopen(url) as enlace:
        contenido = enlace.read()
    with open(guardar_como, "wb") as descarga:
        descarga.write(contenido)

mx_geodf = geopd.read_file(guardar_como)
mx_geodf.set_index("ESTADO")
mx_geodf["centroide"] = mx_geodf.centroid
# print(mx_geodf["centroide"])
ax = mx_geodf["geometry"].plot()
# mx_geodf["centroide"].plot(ax=ax, color="k")
ax.grid(False)
plt.show()

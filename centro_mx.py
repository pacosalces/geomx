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
# Union de estados (incluye territorio insular)
mx_geodf = mx_geodf[["ESTADO", "geometry"]]
mx_junto = mx_geodf.dissolve()
# Calculo del centroide
mx_junto["centroide"] = mx_junto.centroid

# Mostrar mapa y centroide
ax = mx_geodf["geometry"].plot(ec="k", alpha=0.7)
mx_junto["centroide"].plot(ax=ax, marker="*", c="tomato", lw=1)
ax.grid(False)
plt.savefig("./centroide_mx.png")

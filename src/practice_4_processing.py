from qgis.core import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.analysis import *
from qgis.gui import *
from qgis.utils import *
import sys
import os

# Add dir to the path to find processing tools
sys.path.append('/Applications/QGIS.app/Contents/Resources/python/plugins')
sys.path.append('/Applications/QGIS.app/Contents/Resources/python/qgis')


# Start interface
app = QgsApplication([], GUIenabled=False)
app.initQgis()

# Import processing module, initiate it and import algorithms
import processing
from processing.core.Processing import Processing

Processing.initialize()
registry = QgsApplication.processingRegistry()


input_layer = '../data/raw/Municipios/Municipios.shp'
output_layer = '../data/outputs.gpkg'
distance = 300
target_crs = "EPSG:3857"

reprojected = processing.run(
    "qgis:reprojectlayer",
    {
        'INPUT': input_layer,
        'TARGET_CRS': target_crs,
        'OUTPUT': 'memory:'
    }
)['OUTPUT']

processing.run(
    "qgis:buffer",
    {
        'INPUT': reprojected,
        'DISTANCE': distance,
        'SEGMENTS': 5,
        'END_CAP_STYLE': 0,
        'JOIN_STYLE': 0,
        'MITER_LIMIT': 2,
        'DISSOLVE': True,
        'OUTPUT': output_layer
    }
)



app.exitQgis()
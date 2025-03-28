from qgis.core import *
import processing


input_layer = iface.activeLayer()
output_layer = "memory:"
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

result = processing.run(
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

buffered_layer = result['OUTPUT']
QgsProject.instance().addMapLayer(buffered_layer)
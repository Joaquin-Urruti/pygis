import random

def createLayer(n):
    # Define the memory layer with a Point geometry and WGS 84 CRS
    URI = "Point?crs=EPSG:4326"
    layer = QgsVectorLayer(URI, 'Capa', "memory")
    layer.dataProvider().addAttributes([QgsField("id", QVariant.String)])
    layer.updateFields()
    
    features = []
    
    for i in range(n):
        feature = QgsFeature()
        feature.setFields(layer.fields())
        
        # Generate random coordinates
        x = random.uniform(-180, 180)
        y = random.uniform(-90, 90)
        point = QgsPointXY(x, y)
        
        # Set geometry and attribute
        geom = QgsGeometry.fromPointXY(point)
        feature.setGeometry(geom)
        feature.setAttribute("id", i)
        features.append(feature)
    layer.dataProvider().addFeatures(features)
    
    return layer

# Create the layer and add it to the project
layer = createLayer(50)
QgsProject.instance().addMapLayer(layer)
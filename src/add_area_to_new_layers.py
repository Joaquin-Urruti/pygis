from qgis.core import QgsExpression, QgsField, QgsProject, QgsMapLayer, QgsExpressionContext, QgsExpressionContextUtils
from qgis.PyQt.QtCore import QVariant

def add_has_column(layer):
    # Check if the layer is vector and of polygon type
    if layer and layer.type() == QgsMapLayer.VectorLayer and layer.geometryType() == 2:  # 2 = Polygon
        # Check if the 'has_' column already exists
        if "has_" not in [field.name() for field in layer.fields()]:
            layer.startEditing()
            # Add the 'has_' field
            layer.dataProvider().addAttributes([QgsField("has_", QVariant.Double)])
            layer.updateFields()
            # Calculate the area in hectares
            expression = QgsExpression("$area/10000")
            context = QgsExpressionContext()
            context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))
            for feature in layer.getFeatures():
                context.setFeature(feature)
                value = expression.evaluate(context)
                layer.changeAttributeValue(feature.id(), layer.fields().indexOf("has_"), value)
            layer.commitChanges()
            print(f"Column 'has_' added to the layer: {layer.name()}")

def on_layer_added(layer):
    add_has_column(layer)

# Connect the event for when a layer is added
QgsProject.instance().layerWasAdded.connect(on_layer_added)
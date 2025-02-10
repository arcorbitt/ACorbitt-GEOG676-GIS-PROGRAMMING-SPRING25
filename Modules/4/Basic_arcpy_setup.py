import arcpy

print(arcpy.ListEnvironments())
# Prints...
['autoCommit', 'XYResolution', 'processingServerUser', 'XYDomain', 'processingServerPassword', 'scratchWorkspace', 'cartographicPartitions', 'terrainMemoryUsage', 'MTolerance', 'compression', 'coincidentPoints', 'randomGenerator', 'outputCoordinateSystem', 'rasterStatistics', 'ZDomain', 'transferDomains', 'S100FeatureCatalogueFile', 'maintainAttachments', 'resamplingMethod', 'snapRaster', 'cartographicCoordinateSystem', 'configKeyword',
'outputZFlag', 'qualifiedFieldNames', 'tileSize', 'parallelProcessingFactor', 'pyramid', 'referenceScale', 'processingServer', 'extent', 'XYTolerance', 'tinSaveVersion', 'nodata', 'MDomain', 'cellSize', 'outputZValue', 'outputMFlag', 'geographicTransformations', 'ZResolution', 'mask', 'maintainSpatialIndex', 'preserveGlobalIds', 'workspace', 'MResolution', 'baDataSource', 'ZTolerance', 'scratchGDB', 'scratchFolder', 'packageWorkspace', 'scriptWorkspace', 'addOutputsToMap']
# This code snippet will print out a list of all the environments that can be set in arcpy.
# This list is useful for understanding what environments can be set in arcpy.

arcpy.env.workspace = "C:/tmp/ArcGISPython"
arcpy.env.scratchWorkspace = "C:/tmp/ArcGISPython/scratch"
arcpy.env.overwriteOutput = True
arcpy.env.parallelProcessingFactor = "100%"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
arcpy.env.outputZFlag = "Enabled"
arcpy.env.outputMFlag = "Enabled"
arcpy.env.cellSize = 10
arcpy.env.extent = "-180 -90 180 90"
arcpy.env.snapRaster = "C:/tmp/ArcGISPython/snap.tif"
arcpy.env.mask = "C:/tmp/ArcGISPython/mask.shp"
arcpy.env.compression = "LZ77"
arcpy.env.outputZValue = 0
arcpy.env.outputMValue = 0
arcpy.env.outputZValue = 0
arcpy.env.outputMValue = 0
arcpy.env.MDomain = "0 100"
arcpy.env.ZDomain = "0 100"
arcpy.env.XYDomain = "0 100"
arcpy.env.MResolution = 1
arcpy.env.ZResolution = 1
arcpy.env.XYResolution = 1
arcpy.env.MTolerance = 1
arcpy.env.ZTolerance = 1
arcpy.env.XYTolerance = 1
arcpy.env.cartographicCoordinateSystem = arcpy.SpatialReference(4326)
arcpy.env.cartographicPartitions = "100 100"
arcpy.env.terrainMemoryUsage = "High"
arcpy.env.randomGenerator = "0 ACM599"
arcpy.env.autoCommit = "1000"
arcpy.env.coincidentPoints = "MEAN"
arcpy.env.geographicTransformations = "WGS_1984_(ITRF00)_To_NAD_1983"
arcpy.env.referenceScale = 1000
arcpy.env.pyramid = "PYRAMIDS -1 NEAREST DEFAULT"
arcpy.env.tileSize = "128 128"
arcpy.env.configKeyword = "GEOMETRY"
arcpy.env.addOutputsToMap = True
arcpy.env.maintainAttachments = True
arcpy.env.preserveGlobalIds = True
arcpy.env.transferDomains = True
arcpy.env.resamplingMethod = "NEAREST"
arcpy.env.rasterStatistics = "STATISTICS 1 1"
arcpy.env.baDataSource = "C:/tmp/ArcGISPython/ba.gdb"
arcpy.env.scratchGDB = "C:/tmp/ArcGISPython/scratch.gdb"
arcpy.env.scratchFolder = "C:/tmp/ArcGISPython/scratch"
arcpy.env.packageWorkspace = "C:/tmp/ArcGISPython/package"
arcpy.env.scriptWorkspace = "C:/tmp/ArcGISPython/script"
arcpy.env.processingServer = "https://myserver.com/arcgis/rest/services"
arcpy.env.process
# This code snippet will set a number of environments in arcpy.
# These environments will be set for the entire arcpy session.
# The environments that are set in this code snippet are:
# - workspace
# - scratchWorkspace
# - overwriteOutput
# - parallelProcessingFactor
# - outputCoordinateSystem
# - outputZFlag
# - outputMFlag
# - cellSize
# - extent
# - snapRaster
# - mask
# - compression
# - outputZValue
# - outputMValue

# The arcpy.env.workspace environment is used to set the workspace for the arcpy session.
# The workspace is the location where the output data will be saved.
# The arcpy.env.scratchWorkspace environment is used to set the scratch workspace for the arcpy session.
# The scratch workspace is the location where temporary data will be saved.
# The arcpy.env.overwriteOutput environment is used to set whether existing output data will be overwritten.
# The arcpy.env.parallelProcessingFactor environment is used to set the parallel processing factor for the arcpy session.


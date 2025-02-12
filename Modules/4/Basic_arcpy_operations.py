import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"
arcpy.CreateFileGDB_management(arcpy.env.workspace, "DC.gdb")
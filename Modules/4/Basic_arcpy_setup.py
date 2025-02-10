import arcpy
print(arcpy.GetInstallInfo()) # Prints the install information of ArcGIS Pro
print(arcpy.GetInstallInfo()['ProductName']) # Prints the product name of ArcGIS Pro

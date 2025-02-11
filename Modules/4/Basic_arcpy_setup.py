import arcpy
print(arcpy.GetInstallInfo()) # Prints the install information of ArcGIS Pro
print(arcpy.GetInstallInfo()['ProductName']) # Prints the product name of ArcGIS Pro
print(arcpy.ListEnvironments()) # Lists all the datasets in the current workspace

arcpy.env.workspace = "C:/tmp/ArcGISPython" # Sets the workspace to the folder where the data is stored
arcpy.env.scratchWorkspace = 'C:/tmp/ArcGISPython/scratch' # Sets the scratch workspace to the folder where the data is stored
arcpy.env.overwriteOutput = True # Overwrites the output if it already exists
folder_path = "C:/tmp/ArcGISPython" # Sets the folder path to the folder where the data is stored
arcpy.CreateFileGDB_management(folder_path, "Test.gdb") # Creates a file geodatabase in the folder path


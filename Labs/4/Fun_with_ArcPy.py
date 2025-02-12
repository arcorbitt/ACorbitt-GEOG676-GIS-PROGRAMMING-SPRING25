#------------------------------------------------------------------------------------Fun with ArcPy------------------------------------------------------------------------------------#

#OBJECTIVES
# 1. Learn how to build an iterator
# 2. Learn several of the general purpose container data types
# 3. Learn how to use Arcpy to:
#    a. Setup a Workspace
#    b. Create a Geodatabase
#    c. Find example Arcpy code
# 4. Learn how to manipulate feature layers and perform some basic spatial analysis (e.g. buffering, intersection) using Arcpy

# TASKS
# 1. Read in garage location X/Y coordinates from a CSV file
# 2. Create a geodatabase and add in the input layers
# 3. Buffer the garage points
# 4. Intersect the buildings layer with the buffered garage points
# 5. Output the resulting table into a CSV file

#------------------------------------------------------------------------------------Fun with ArcPy------------------------------------------------------------------------------------#

#create a geodatabase and garage feature class
import arcpy
import os
import csv

arcpy.env.workspace = r"C:\Users\ms_ra\GitHub\GEOG676-GIS-PROGRAMMING-SPRING25\Labs\4\Workspace"
arcpy.env.overwriteOutput = True
folder_path = r"C:\Users\ms_ra\GitHub\GEOG676-GIS-PROGRAMMING-SPRING25\Labs\4"
gdb_name = 'TestLab4.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r"C:\Users\ms_ra\GitHub\GEOG676-GIS-PROGRAMMING-SPRING25\Labs\4\garages.csv"
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

#open campus gdb, copy building feature to our gdb
campus = r"C:\Users\ms_ra\GitHub\GEOG676-GIS-PROGRAMMING-SPRING25\Labs\4\Campus.gdb"
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

#Re-Projection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

#buffer the garage points
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

#intersect the buildings with the garage points
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersection', 'ALL')

arcpy.TableToTable_conversion(gdb_path + '\\Garage_Building_Intersection.dbf', r"C:\Users\ms_ra\GitHub\GEOG676-GIS-PROGRAMMING-SPRING25\Labs\4", 'nearbyBuildings.csv')

print('Process completed successfully! CSV file created at:', r"C:\Users\ms_ra\GitHub\GEOG676-GIS-PROGRAMMING-SPRING25\Labs\4\nearbyBuildings.csv")

#------------------------------------------------------------------------------------Fun with ArcPy------------------------------------------------------------------------------------#
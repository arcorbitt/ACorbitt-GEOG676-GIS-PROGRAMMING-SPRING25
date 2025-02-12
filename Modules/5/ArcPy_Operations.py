#--------------------------------------------Learning Objectives----------------------------------------

# 1. Clip Layers
# 2. Dissolve
# 3. Union Layers
# 4. Extract data using Select

#-------------------------------------------------Clip---------------------------------------------------
#The clip tool is used to "cut" a feature class with the geometry of another feature class, known as the clip feature.
#Though it sounds like the intersect tool, the clip tool only retains attributes from the input
#This means that the resulting layer only contains attributes from the layer that is cut whereas the intersect tool combines attributes from both the input and the clip feature.

# In the following example we are going to clip campus structures in the feature class with the geographic area  of the garage buffer feature class.
# The result will be a series of structures that fall within the garage 

import arcpy

# Define the path to your geodatabase
campus = r"C:\Program Files\DevSource\arcorbitt-GEOG-676\Module\05\Campus.gdb"

# Set workspace
arcpy.env.workspace = campus

# List feature classes to confirm access
feature_classes = arcpy.ListFeatureClasses()

# Output results
if feature_classes:
    print("Feature Classes in the Geodatabase:")
    for fc in feature_classes:
        print(fc)
else:
    print("No feature classes found or unable to access the geodatabase.")

arcpy.env.overwriteOutput = True

# Check if the required feature classes exist
if "Structures" in feature_classes and "GaragePoints_buffered" in feature_classes:
    arcpy.Clip_analysis(campus + "/Structures", campus + "/GaragePoints_buffered", campus + "/Clipped_Structures")
    print("Clip analysis completed successfully.")
else:
    print("Required feature classes not found in the geodatabase.")

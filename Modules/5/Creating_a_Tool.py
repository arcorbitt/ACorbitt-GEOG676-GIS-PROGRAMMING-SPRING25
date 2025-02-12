#----------------------------------------------------------------------------CREATING A TOOL----------------------------------------------------------------------------

#Appears inside the Geoprocessing pane in ArcGIS Pro
#The tool is created using the Python toolbox

# The following example is of how to create a tool not creating a toolbox
# Handling user inputs

import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"

# Define our geodatabase
campus = r"C:\Program Files\DevSource\arcorbitt-GEOG-676\Module\05\Campus.gdb"

# Setup our user input variables
buildingNumber_input = input("Please enter a building number: ")
bufferSize_input = int(input("Please enter a buffer size: "))

# Generate our where_clause
where_clause = "Bldg = '%s'" % buildingNumber_input

# Check if building exists
structures = campus + "/Structures"
cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
shouldProceed = False

for row in cursor:
    if row.getValue("Bldg") == buildingNumber_input:
        shouldProceed = True

# If we shouldProceed do so
if shouldProceed:
    # Generate the name for our generated buffer layer
    buildingBuff = "/building_%s_buffed_%s" % (buildingNumber_input, bufferSize_input)
    # Get reference to building
    buildingFeature = arcpy.Select_analysis(structures, campus + "/building_%s" % (buildingNumber_input), where_clause)
    # Buffer the selected building
    arcpy.Buffer_analysis(buildingFeature, campus + buildingBuff, bufferSize_input)
    # Clip the structures to our buffered feature
    arcpy.Clip_analysis(structures, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
    # Remove the feature class we just created
    arcpy.Delete_management(campus + "/building_%s" % (buildingNumber_input))
    
else:
    print("Seems we couldn't find the building you entered")
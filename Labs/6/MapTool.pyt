# -*- coding: utf-8 -*-

import arcpy


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [GraduatedColorsRenderer]

class GraduatedColorsRenderer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "graduatedcolor"
        self.description = "create a graduated colored map based on a specific attribute of a layer"
        self.canRunInBackground = False
        self.category = "MapTools"

    def getParameterInfo(self):
        """Define the tool parameters."""
        #Project Name
        param0 = arcpy.Parameter(
            displayName="Input ArcGIS Pro Project Name", #name displayed in the tool for the parameter
            name="aprxInputName", #name of the parameter not displayed in the tool
            datatype="DEFile", #data type of the parameter (DEFile is a file on a disk)
            parameterType="Required",
            direction="Input"
        )
        #Layer to Classify to create the graduated color map
        Param1 = arcpy.Parameter(
            displayName="Layer to Classify",
            name="LayertoClassify",
            datatype="GPLayer", #data type of the parameter (GPLayer is a layer in the map
            parameterType="Required",
            direction="Input"
        )
        #Output Location of the new project
        Param2 = arcpy.Parameter(
            displayName="Output Location",
            name="OutputLocation",
            datatype="DEFolder", #data type of the parameter (DEFolder is a folder on a disk)
            direction="Input"
        )
        #Output Project Name
        Param3 = arcpy.Parameter(
            displayName="Output Project Name",
            name="OutputProjectName",
            datatype="GPString", #data type of the parameter (GPString is a string)
            parameterType="Required",
            direction="Input"
        )
        params = [param0, Param1, Param2, Param3]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        # Define Progressor Variables
        readTime = 2.5  #the time for users to read the progress
        start = 0     #the start of the progress
        max = 100     #the maximum value of the progress, end position
        step = 33     #the step of the progress, the progress interval to move the progressor along

        # Setup Progressor
        arcpy.SetProgressor("step", "Validating Project File...", start, max, step)
        time.sleep(readTime) #pause the excution for 2.5 seconds

        # Add Message to the Results Pane
        arcpy.AddMessage("Validating Project File...")

        # Project File
        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText) #param0 is the imput project file, helps us access the project's maps, layers, and symbology

        # Grabs the First Instance of a Map from the .aprx
        campus = project.listMaps('Map')[0] #get the first map in the project 

        # Increment Progressor
        arcpy.SetProgressorPosition(start + step) #now is 33% complete because the "step" is 33
        arcpy.SetProgressorLabel("Finding your map layer...")
        time.sleep(readTime) #pause the excution for 2.5 seconds
        arcpy.AddMessage("Finding your map layer...")

        # Loop Throguh the Layers in the Map
        for layer in campus.listLayers():
            #Check if the layer is a feature layer
            if layer.isFeatureLayer:
                #copy the layer's symbology
                sym = layer.symbology
                #make sure the symbology has a renderer attribute
                if hasattr(sym, 'renderer'):
                    #check layer name
                    if layer.name == parameters[1].valueAsText: # check if the layer name matches the input layer name
                        
                        # Increment Progressor
                        arcpy.SetProgressorPosition(start + step * 2) #now is 66% complete because the "step" is 33
                        arcpy.SetProgressorLabel("Calculating and classifying...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Calculating and classifying...") #message added to the results pane

                        # Update the Copy's Renderer to "Graduated Colors Renderer"
                        sym.updateRenderer('GraduatedColorsRenderer')

                        # Tell arcpy which field we want to base our chloropleth off of
                        sym.renderer.classificationField = "Shape_Area"

                        # Set how many classes we want for the map
                        sym.renderer.breakCount = 5

                        # Set the color ramp
                        sym.renderer.colorRamp = project.listColorRamps("Oranges (5 Classes)")[0]

                        # Set the Layer's actual symbology equal to the copy's symbology
                        layer.symbology = sym

                        arcpy.AddMessage("Finished Generating Layer...")
                    else
                        print('NO layers found')

        # Increment Progressor
        arcpy.SetProgressorPosition(start + step * 3) #now is 99% complete because the "step" is 33
        arcpy.SetProgressorLabel("Saving Project...")
        time.sleep(readTime)
        arcpy.AddMessage("Saving Project...")

        # Save the Project
        project.saveACopy(parameters[2].valueAsText + "\\" + parameters[3].valueAsText + ".aprx")
        # Param 2 is the folder location, Param 3 is the name of the new project
                                                      
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return

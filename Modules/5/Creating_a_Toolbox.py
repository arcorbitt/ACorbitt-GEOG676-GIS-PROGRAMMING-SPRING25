# A Python toolbox is a single text file that acts as glue to group together multiple Python scripts, functions, and classes. The toolbox is a container for the tools that you create. The toolbox provides a way to organize your tools and scripts into a single, easy-to-use interface. The toolbox is created using the Python toolbox. The Python toolbox is a Python script that creates a toolbox (.tbx) file. The toolbox is a container for the tools that you create. The toolbox provides a way to organize your tools and scripts into a single, easy-to-use interface. The toolbox is created using the Python toolbox. The Python toolbox is a Python script that creates a toolbox (.tbx) file. The toolbox is a container for the tools that you create. The toolbox provides a way to organize your tools and scripts into a single, easy-to-use interface. The toolbox is created using the Python toolbox. The Python toolbox is a Python script that creates a toolbox (.tbx) file. The toolbox is a container for the tools that you create. The toolbox provides a way to organize your tools and scripts into a single, easy-to-use interface. The toolbox is created using the Python toolbox. The Python toolbox is a Python script that creates a toolbox (.tbx) file. The toolbox is a container for the tools that you create. The toolbox provides a way to organize your tools and scripts into a single, easy-to-use interface. The toolbox is created using the Python toolbox. The Python toolbox is a Python script that creates a toolbox (.tbx) file. The toolbox is a container for the tools that you create. The toolbox provides a way to organize your tools and scripts into a single, easy-to-use interface. The toolbox is created using the Python toolbox. The Python toolbox is a Python script that creates a toolbox (.tbx) file. The toolbox is a container for the tools that you create. The toolbox provides a way to organize your tools and scripts into a single, easy-to-use interface. The toolbox is created using the Python toolbox. The Python toolbox is a Python script that creates a toolbox (.tbx) file. The toolbox is a container for the tools that you create. The toolbox provides a way to organize your tools and scripts into a single, easy-to-use interface. The toolbox is created using the Python toolbox. The Python toolbox is a Python script that creates a toolbox (.tbx) file. The toolbox is a container for the tools that you create. The toolbox provides a way to organize your tools and scripts into a
# To create a new toolbox in ArcGIS Pro, right-click on the folder where you want to create the toolbox and select New > Toolbox. Name the toolbox and click OK. The toolbox is created and appears in the Catalog pane. To add a new script to the toolbox, right-click on the toolbox and select New > Script. Name the script and click OK. The script is created and appears in the toolbox. To edit the script, right-click on the script and select Edit. The script opens in the script editor. You can now write your Python code in the script editor. To run the script, click the Run button in the script editor. The script runs and the results appear in the Geoprocessing pane. To create a new toolbox in ArcGIS Pro, right-click on the folder where you want to create the toolbox and select New > Toolbox. Name the toolbox and click OK. The toolbox is created and appears in the Catalog pane. To add a new script to the toolbox, right-click on the toolbox and select New > Script. Name the script and click OK. The script is created and appears in the toolbox. To edit the script, right-click on the script and select Edit. The script opens in the script editor. You can now write your Python code in the script editor. To run the script, click the Run button in the script editor. The script runs and the results appear in the Geoprocessing pane. To create a new toolbox in ArcGIS Pro, right-click on the folder where you want to create the toolbox and select New > Toolbox. Name the toolbox and click OK. The toolbox is created and appears in the Catalog pane. To add a new script to the toolbox, right-click on the toolbox and select New > Script. Name the script and click OK. The script is created and appears in the toolbox. To edit the script, right-click on the script and select Edit. The script opens in the script editor. You can now write your Python code in the script editor. To run the script, click the Run button in the script editor. The script runs and the results appear in the Geoprocessing pane. To create a new toolbox in ArcGIS Pro, right-click on the folder where you want to create the toolbox and select New > Toolbox. Name the toolbox and click OK. The toolbox is created and appears in the Catalog pane. To add a new script to the toolbox, right-click on the toolbox and select New > Script. Name the script and


#----------------------------------------------------------------------------CREATING A TOOLBOX----------------------------------------------------------------------------

# Below is a plain toolbox .pyt file that can be used to create a toolbox in ArcGIS Pro

import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return
    


    # There are two classes; one to define the toolbox and one to define the tool.
    # You cannot change the toolbox class name but you can change the tool class name.
    # The toolbox class has three instance attributes: label, alias, and tools.
    # The label is the name of the toolbox that appears in the Catalog pane.
    # The alias is a short description of the toolbox.
    # The tools attribute is a list of tool classes associated with the toolbox.
    # The tool class has four instance attributes: label, description, canRunInBackground, and tools.
    # The label is the name of the tool that appears in the Catalog pane.
    # The description is a short description of the tool.
    # The canRunInBackground attribute specifies whether the tool can run in the background.
    # The getParameterInfo method defines the parameters for the tool.
    # The isLicensed method specifies whether the tool is licensed to execute.
    # The updateParameters method modifies the values and properties of parameters before internal validation is performed.
    # The updateMessages method modifies the messages created by internal validation for each tool parameter.

    # Changing the value of that list attribute to include BuildingProximity instead and changing the name of the class to BuiildingProximity will create a new tool in the toolbox.

    # self.tools = [Tool] OLD CLASS
self.tools = [BuildingProximity]

class BuildingProximity(object):
    ...

#----------------------------------------------------------------------BuildingProximity----------------------------------------------------------------------

#---------------Methods used in a tool class---------------
# 1. __int__   (required)
# 2. getParameterInfo   (optional)
# 3. isLicensed   (optional)
# 4. updateParameters   (optional)
# 5. updateMessages   (optional)
# 6. execute   (required)

#---------------__int__---------------

# The __int__ method is required and used to define the tool.
# The method has four instance attributes: label, description, canRunInBackground, and category(tools).
# The label is the name of the tool that appears in the Catalog pane.
# The description is a short description of the tool.
# The canRunInBackground attribute specifies whether the tool can run in the background.
# The category attribute specifies the category of the tool.
# The tools attribute is a list of tool classes associated with the tool.

def __init__(self):
    """Define the tool (tool name is the name of the class)."""
    self.label = "Building Proximity"
    self.description = "Determines which buildings on TAMU's campus are near a targeted building"
    self.canRunInBackground = False # Only used in ArcMap
    self.category = "Building Tools"

#---------------getParameterInfo---------------

# The getParameterInfo method is optional and used to define the parameters for the tool.
# Only optional if you do not need to to use any user provided inputs.
# The method returns a list of parameter definitions.
# The parameter definitions are defined using the arcpy.Parameter class.

def getParameterInfo(self):
    """Define parameter definitions"""
    param0 = arcpy.Parameter(
        displayName="Building Number",
        name="buildingNumber",
        datatype="GPString",
        parameterType="Required",
        direction="Input"
    )
    param1 = arcpy.Parameter(
        displayName="Buffer radius",
        name="bufferRadius",
        datatype="GPDouble",
        parameterType="Required",
        direction="Input"
    )
    params = [param0, param1]
    return params

#It is important when setting up your parameter objects to set the correct datatype attribute value.

#---------------isLicensed---------------

# The isLicensed method is optional and used to specify whether the tool is licensed to execute.
# The method returns a Boolean value.
# If your tool relied upon tools requiring a license to use such as any tools under 3D Analyst, you would need to make sure you had the correct license to use the tool.

# Code is ESRI's own example found here: http://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/controlling-license-behavior-in-a-python-toolbox.htm
def isLicensed(self):
    """Allow the tool to execute, only if the ArcGIS 3D Analyst extension 
    is available."""
    try:
        if arcpy.CheckExtension("3D") != "Available":
            raise Exception
    except Exception:
        return False  # tool cannot be executed

    return True  # tool can be executed

#---------------updateParameters---------------

# The updateParameters method is optional and used to modify the values and properties of parameters before internal validation is performed.
# The method has two parameters: parameters and messages.
# The parameters parameter is a list of parameter objects.
# The messages parameter is a list of messages.
# The method is called whenever a parameter has been changed.
# Useful if you need to process the user's input in some way before the tool is executed.

# Code is ESRI's own example found here: http://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/customizing-tool-behavior-in-a-python-toolbox.htm
def updateParameters(self, parameters):
    # Set the default distance threshold to 1/100 of the larger of the width
    #  or height of the extent of the input features.  Do not set if there is no 
    #  input dataset yet, or the user has set a specific distance (Altered is true).
    #
    if parameters[0].valueAsText:
        if not parameters[6].altered:
            extent = arcpy.Describe(parameters[0]).extent
        if extent.width > extent.height:
            parameters[6].value = extent.width / 100
        else:
            parameters[6].value = extent.height / 100

    return

#---------------updateMessages---------------

# The updateMessages method is optional and used to modify the messages created by internal validation for each tool parameter.
# The method has two parameters: parameters and messages.
# The parameters parameter is a list of parameter objects.
# The messages parameter is a list of messages.
# The method is called after internal validation.
# Useful if you need to provide feedback to the user about their input.

# Code is ESRI's own example found here: http://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/customizing-tool-behavior-in-a-python-toolbox.htm
def updateMessages(self, parameters):
    # Check if the input dataset is a feature class
    #
    if parameters[0].altered:
        desc = arcpy.Describe(parameters[0].value)
        if desc.dataType != "FeatureClass":
            parameters[0].setErrorMessage("{0} is not a feature class".format(parameters[0].valueAsText))

    return

#---------------execute---------------

# After __int__ and getParameterInfo, the execute method is required.
# The most inportant method in the tool class.
# Within this method goes all the code and logic behind out building proximity tool.
# We must be careful to change where the user input comes from when copying the code from the original script.
# This method has a parameters argument that contains all the parameters we set up within the getParameterInfo() method.
# We need to update code to make sure that all of the arguments our code needs are passed in from the parameters argument and not from input() calls.
# Since parameters is a list we access the values within square brackets.
# Within getParameterInfo() we created two parameter objects and put them in a list variable. 
# Our building number in contained within param0 and our buffer radius is contained within param1.
# To access our building number, we would access the first location within the parameters argument; wile we would use the second location to access our buffer radius.

 def execute(self, parameters, messages):
        """The source code of the tool."""
        campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb"

        # Setup our user input variables
        buildingNumber_input = parameters[0].valueAsText
        bufferSize_input = int(parameters[1].value)

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
        return None

#----------------------------------------------------------------------Types of Parameter Inputs----------------------------------------------------------------------

#---------------Multivalue---------------

# The multivalue parameter type is used to allow the user to select multiple values for a parameter.
# The datatype attribute is set to a list of the data type.
# The parameterType attribute is set to Required or Optional.
# The direction attribute is set to Input or Output.
# The filter attribute is set to a list of values.
# The dependency attribute is set to a list of parameter names.
# The category attribute is set to a category name.
# The multiValue attribute of a prameter object found in getParameterInfo() can be used to handle multiple values; non-multivalue parameters can only handle one value.
# The multiValue attribute is a Boolean value that specifies whether the parameter is a multivalue parameter.
# The multiValue attribute is set to True to allow the user to select multiple values for the parameter.
# The multiValue attribute is set to False to allow the user to select only one value for the parameter.

def getParameterInfo(self):
    param0 = arcpy.Parameter(
        displayName="Building Number",
        name="buildingNumber",
        datatype="GPString",
        parameterType="Required",
        direction="Input",
        multiValue=True
    )

#---------------Filter---------------

# The filter attribute is used to restrict the values that the user can select for a parameter.
# The filter attribute is set to a list of values.
# The list of values can be a list of strings or a list of integers.

def getParameterInfo(self):
    param1 = arcpy.Parameter(
        displayName="Buffer radius",
        name="bufferRadius",
        datatype="GPDouble",
        parameterType="Required",
        direction="Input"
    )
    param1.filter.type = "Range"
    param1.filter.list = [10, 100]


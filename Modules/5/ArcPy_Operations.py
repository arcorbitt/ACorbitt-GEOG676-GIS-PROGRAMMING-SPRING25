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
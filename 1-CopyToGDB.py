import arcpy
from arcpy import env

env.overwriteOutput = True
env.workspace = 'C:/Users/MWright/Downloads/44'
outputEnv = 'C:/Users/MWright/Desktop/test/scratch012926.gdb/'

fclist = arcpy.ListFeatureClasses()
print(fclist)
print('\n')

for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    fcname = fcdesc.basename
    fcout = arcpy.ValidateTableName(fcname, outputEnv)
    arcpy.CopyFeatures_management(fc, outputEnv + fcout)

print('Feature class copy process complete.')

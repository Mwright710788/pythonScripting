import arcpy
from arcpy import env

env.overwriteOutput = True
env.workspace = 'C:/Users/MWright/Downloads/cl3/'
outputEnv = 'C:/Users/MWright/Desktop/ClevelandToOsageII/ClevelandToOsageII.gdb/'
x = 'lateral'
count = 1

fclist = arcpy.ListFeatureClasses()
print(fclist)
print('\n')

for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    fcname = fcdesc.basename
    if fcname == 'lateral':
        if arcpy.Exists(x):
            fcout = arcpy.ValidateTableName(fcname, outputEnv)
            arcpy.CopyFeatures_management(fc, outputEnv + fcout + str(x))
            print('\n' + fcname + ' has been copied to GDB.\n')
            x += 1
        else:
            fcout = arcpy.ValidateTableName(fcname, outputEnv)
#the str(count) part of the following line may be unnecessary! Look into later.
            arcpy.CopyFeatures_management(fc, outputEnv + fcout + str(count))
    else:
        print(fcname + " feature class does not need to be copied to geodatabase.")

print('\nBackbone feature class copy process complete.')

import arcpy
from arcpy import env

env.overwriteOutput = True
env.workspace = 'C:/Users/MWright/Desktop/ClevelandToOsageII/ClevelandToOsageII.gdb/'

fclist = arcpy.ListFeatureClasses()
x = 'global_iec_spans_clip'

print(fclist)
print('\n')

try:
    for fc in fclist:
        fcdesc = arcpy.Describe(fc)
        fcname = fcdesc.basename
        if fcname == x:
            arcpy.management.AddField(x, 'RT_NUM', 'TEXT')
            arcpy.management.CalculateField(x, 'RT_NUM', '!RT_NUM! == "00"')
            print('\n' + fcname + 'attribute table has been modified. \n')
        else:
            print(fcname + ' attribute table does not need modifications.')
    print('\n Attribute table successfully modified.')
except:
    print('\n An exception has occurred.')
    print(arcpy.GetMessages() + '\n')



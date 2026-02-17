import arcpy
from arcpy import env

env.overwriteOutput = True
x_path = 'C:/Users/MWright/Desktop/ClevelandToOsageII/ClevelandToOsageII.gdb'
env.workspace = x_path 

fclist = arcpy.ListFeatureClasses()
print(fclist)
print('\n')

arcpy.analysis.Buffer('backbone', 'backbone_clip', '2000 Feet')

for fc in fclist:
    if 'iec_poles' in fc:
        arcpy.analysis.Clip(fc, 'backbone_clip', fc + '_clip')
        arcpy.management.DeleteFeatures(fc)

    elif 'iec_spans' in fc:
        arcpy.analysis.Clip(fc, 'backbone_clip', fc + '_clip')
        arcpy.management.DeleteFeatures(fc)

    elif 'iec_serv' in fc:
        arcpy.analysis.Clip(fc, 'backbone_clip', fc + '_clip')
        arcpy.management.DeleteFeatures(fc)

    else:
        print('Clip function does not need to be performed on ' + str(fc) + ' feature class.')

for fc in fclist:
    result = arcpy.GetCount_management(fc)
    count = int(result.getOutput(0))
    if int(count) == 0:
        arcpy.Delete_management(fc)

arcpy.Delete_management('backbone_clip')
        
print('\n')
print('Clip process complete.')
    
    

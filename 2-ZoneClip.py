import arcpy
from arcpy import env

env.overwriteOutput = True
x_path = 'C:/Users/MWright/Desktop/Pawnee5/Pawnee5.gdb'
env.workspace = x_path 

fclist = arcpy.ListFeatureClasses()
print(fclist)
print('\n')

arcpy.analysis.Buffer('zone', 'zone_buffer', '2500 Feet')

for fc in fclist:
    if 'iec_poles' in fc:
        arcpy.analysis.Clip(fc, 'zone_buffer', fc + '_clip')
        arcpy.management.DeleteFeatures(fc)

    elif 'iec_spans' in fc:
        arcpy.analysis.Clip(fc, 'zone_buffer', fc + '_clip')
        arcpy.management.DeleteFeatures(fc)

    elif 'iec_serv' in fc:
        arcpy.analysis.Clip(fc, 'zone', fc + '_clip')
        arcpy.management.DeleteFeatures(fc)

    else:
        print('Intersect function does not need to be performed on ' + str(fc) + ' feature class.')

for fc in fclist:
    result = arcpy.GetCount_management(fc)
    count = int(result.getOutput(0))
    if int(count) == 0:
        arcpy.Delete_management(fc)

arcpy.Delete_management('zone_buffer')
        
print('\n')
print('Clip process complete.')
    
    

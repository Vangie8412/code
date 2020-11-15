# -*- encoding: utf-8 -*-
'''
@File    :   clip_raster.py
@Contact :   whut.hexin@foxmail.com
@License :   (C)Copyright 2017-2018, HeXin

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/1/2 0:59   xin      1.0         None
'''

import arcpy
import glob
import os

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")


def clip_raster( workspace, clip_shp, in_raster):
    arcpy.env.workspace = workspace
    if (os.path.exists(workspace)) == False:
        os.makedirs(workspace, 0o777)
    if not os.path.exists(workspace + "\\" + "raster_output_16"):
        os.mkdir(workspace + "\\" + "raster_output_16")
    if not os.path.exists(workspace + "\\" + "raster_output_8"):
        os.mkdir(workspace + "\\" + "raster_output_8")
    # desc = arcpy.Describe(shp_file_name)
    fields = ["SHAPE@"]

    fields.append("SHAPE@")
    for row in arcpy.SearchCursor(clip_shp):
        mask = row.getValue("Shape")
        # FID = int(row.getValue("FID"))
        FID= int(row.getValue("Id"))
        print FID
        # type=int(row.getValue("type"))
        # FID='1_'+str(type)+'_'+str(FID1)
        # arcpy.CopyFeatures_management(polygons, 'temp/temp_'+str(i)+'_'+str(j)+'.shp')
        mask_raster = arcpy.sa.ExtractByMask(in_raster, mask)

        mask_raster.save(workspace + '\\raster_output_16\\'+str(FID)+'.tif')
        arcpy.CopyRaster_management(workspace + '\\raster_output_16\\'+str(FID)+'.tif',
                                    workspace + '\\raster_output_8\\'+ str(FID) + '.tif', "DEFAULTS", "0", "9",
                                    "", "", "8_BIT_UNSIGNED")

        print (workspace +'/raster_output/' + str(FID) + '.tif is generated successfully!')
    print ('this project finished!!!')

if __name__ == "__main__":
   # clip_raster(r'F:\U_pan\three filed\clipresult\img', r'F:\U_pan\three filed\平田候选\贴标签结果\ptian_sample_kuang\ptian1_sample_kuang.shp', r'F:\U_pan\three filed\平田候选\2008.12.31平田候选影像\\新的平田候选1_206619_42816_18.tif')
   # clip_raster (r'F:\U_pan\three filed\clipresult\img', r'F:\U_pan\three filed\平田候选\贴标签结果\ptian_sample_kuang\ptian5_sample_kuang.shp',
   #              r'F:\U_pan\three filed\平田候选\2008.12.31平田候选影像\\平田候选5.tif')
   # clip_raster(r'F:\U_pan\three filed\clipresult\img', r'F:\U_pan\three filed\平田候选\贴标签结果\ptian_sample_kuang\ptian6_sample_kuang.shp', r'F:\U_pan\three filed\平田候选\2008.12.31平田候选影像\\2008平田候选6_206670_42466_18.tif')
  
   # clip_raster (r'F:\U_pan\three filed\clipresult\mask_1', r'F:\U_pan\分工任务\7人分工改634roi\kuang\samplekuang_1.shp',
   #              r'F:\U_pan\分工任务\7人分工改634roi\gt\\gt_1.tif')
   # clip_raster (r'F:\U_pan\three filed\clipresult\roi_1', r'F:\U_pan\分工任务\7人分工改634roi\kuang\samplekuang_1.shp',
   #              r'F:\U_pan\分工任务\7人分工改634roi\roi\\new_roi_1.tif')
   clip_raster(r'C:\Users\12991\Desktop\October\result_3\mask', r'C:\Users\12991\Desktop\September\5_week\roi_3\roi_3.shp', r'C:\Users\12991\Desktop\October\result_3\mask.tif')


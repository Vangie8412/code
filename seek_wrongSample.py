import json
from collections import Counter
import os
import tifffile as tif
import numpy as np
import openpyxl
import shutil
from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook

class_type={1:'平田',2:'滑坡',3:'草地',4:'水体',5:'村庄',6:'公路',7:'土路',8:'城镇',9:'梯田',10:'条田',11:'绿化草地',12:'疏林',13:'绿化疏林'}
def covert_GTvalue_to_CLSvalue(gt_value=''):    #将gt颜色转化为cls值
    clstype={'5': '[150   0 250]', '9':'[255   0   0]', '3':'[150 200 150]', '1':'[  0 200   0]', '4':'[200   0 200]', '6':'[150 150 250]', '10':'[255  20 147]','8': '[ 25  25 112]', '12':'[  0 134 139]','7':'[250 200   0]', '11':'[255 228 181]', '2':'[150 250   0]','13':'[0 0 0]'}
    for cls_ in clstype:
        if gt_value == str(clstype[cls_]):
            gt_value = cls_
            break
    return gt_value
def get_wrong_dapei(cells=[],one=[],other=[]):
	wrong_dapei=[]
	for i in one:
		for j in other:
			if (i in cells)&(j in cells):
				strvalue=i+'<>'+j
				wrong_dapei.append(strvalue)
	wrong_dapei=list(set(wrong_dapei))
	return wrong_dapei
	
	
	
def seek_wrong_sample(motherpath = r'F:\U_pan\dataset\new_dataset(967)0928\\'):
	# gt_path = motherpath + 'gt\\'
	gt_path = motherpath + 'mask\\raster_output_16\\'
	one_situation=['4','6','8','11','13']
	other_situation=['1','3','5','7','9','10','12']
	excel_path = motherpath + 'wrong_sample.xlsx'
	onlyfiles = [f for f in os.listdir (gt_path) if os.path.isfile (os.path.join (gt_path, f))]
	wb = Workbook ()
	sheets = wb.get_sheet_names ()
	# # 第一个表格的名称
	sheet_first = sheets[0]
	sheet = wb.get_sheet_by_name (sheet_first)
	numcount = 0
	for read_file in onlyfiles:
		if read_file[-4:]=='.tif':
			numcount = numcount + 1
			gt_file = gt_path + read_file
			gt = tif.imread (gt_file)
			# cells为单个样本中有那些类
			cells = []
			for i in range (224):
				for j in range (224):
					# value = covert_GTvalue_to_CLSvalue( str (gt[i][j]))
					value=str (gt[i][j])
					cells.append (value)
					cells = list (set (cells))
			cells = list (set (cells))
			wrong_dapei1=get_wrong_dapei(cells,one_situation,other_situation)
			wrong_dapei2=get_wrong_dapei(cells,other_situation,one_situation)
			wrong_dapei=wrong_dapei1
			sheet.cell (numcount, 1).value = read_file
			sheet.cell (numcount, 2).value = str (cells)
			if len(wrong_dapei)!=0:
				sheet_cell_value = str (wrong_dapei)
			else:
				sheet_cell_value  ='无排斥'
			sheet.cell (numcount, 3).value = sheet_cell_value
			print (read_file + '  ' + str (sheet_cell_value))
			print ('第 ' + str (numcount) + '个样本' + read_file + '统计完毕')
	wb.save (excel_path)
	
	

if __name__=='__main__':
	seek_wrong_sample(r'F:\U_pan\three filed\clipresult\ptian1021\\')
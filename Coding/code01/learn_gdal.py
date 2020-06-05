"""
用于学习 gdal库
"""
# !/usr/bin/python
import re
from osgeo import gdal, gdalconst
from osgeo import ogr

# 在打开GDAL所支持的光栅数据之前需要注册驱动。这里的驱动是针对GDAL支持的所有数据格式。
# 通常可以通过调用GDALAllRegister()函数来注册所有已知的驱动

# 单独注册
driver = gdal.GetDriverByName('HFA') #注册Erdas栅格数据类型
driver.Register()

file_path = 'D:/yexinyu\yxy/testdata/GF1_PMS1_E103.8_N33.3_20170115_L1A0002122491/GF1_PMS1_E103.8_N33.3_20170115_L1A0002122491-MSS1.tiff'
dataset = gdal.Open(file_path)
if dataset is None:
    print("open failed")
    exit(1)

# 通过索引值获取驱动，打印名称
drv = gdal.GetDriver(1)
print("%10s: %s" % (drv.ShortName, drv.LongName))

'''
获取栅格文件的一些基本信息，读取栅格数据集的x方向像素数，y方向像素数，和波段数...
'''
# 后面没有括号，因为他们是属性，不是方法
cols = dataset.RasterXSize  # 读取x方向像素数
rows = dataset.RasterYSize  # 读取y方向像素数
bands = dataset.RasterCount  # 读取波段数
proj = dataset.GetProjection()
print("cols:%d  rows:%d  bands:%d" % (cols, rows, bands))
print('proj:', proj)


# 读取某一像素点的值
# ReadAsArray(<xoff>, <yoff>, <xsize>, <ysize>)
# 读出从(xoff,yoff)开始，大小为(xsize,ysize)的矩阵。如果将矩阵大小设为1X1，就是读取一个像素了
# band = dataset.GetRasterBand(1)
# data = band.ReadAsArray(0, 0, 1, 1)

# 二维数组的处理

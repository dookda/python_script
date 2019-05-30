import arcpy
import os

inFiles = "c://workspace/py_spectro/out_veg/"
outFiles = "c://workspace/py_spectro/out_veg_ras/"
rasType = "FLOAT"

for f in os.listdir(inFiles):
    fname = f[:-4]
    ascii = inFiles + "/" + f
    outRas = outFiles + "/" + fname + ".tif"
    arcpy.ASCIIToRaster_conversion(ascii, outRas,rasType)
    print f + " ok!!"

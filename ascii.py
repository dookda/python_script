# from pandas import read_excel
import pandas as pd
import os

rd41 = 'RD41-Rep Phase'
rd31 = 'RD31-Rep Phase'
pt1 = 'PT1-Rep Phase'

# file_name = '_10_Veg-Phase_3_ricevarities.xlsx'
file_name = '_11_Rep-Phase_3_ricevarities.xlsx'
# file_name = '_12_Rip-Phase_3_ricevarities.xlsx'

d_rd41 = pd.read_excel(file_name, sheet_name=rd41)
d_rd31 = pd.read_excel(file_name, sheet_name=rd31)
d_pt1 = pd.read_excel(file_name, sheet_name=pt1)

# n 350-2500 = 2150
n = 2150
i = 0
while i <= n:
    r = 90  # rows
    j = 0
    fname = 'out_rep/_' + str(350 + i) + '.txt'
    f = open(fname, 'w')
    f.write('ncols 3\nnrows 90\nxllcorner 0.0\nyllcorner 0.0\ncellsize 50.0\nNODATA_value  -9999\n')
    i += 1
    while j < r:
        arr_rd41 = d_rd41.iloc[j, i]
        arr_rd31 = d_rd31.iloc[j, i]
        arr_pt1 = d_pt1.iloc[j, i]
        f.write(str(arr_rd41) + ' ' + str(arr_rd31) +
                ' ' + str(arr_pt1) + '\n')
        j += 1
    f.close()
    print('ok '+str(i))

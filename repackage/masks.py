import numpy as np

def Ni_10mN():
    mask = np.zeros((2048,2048), dtype='bool')
    mask[68:200,380:543] = 1
    mask[100:400,1100:1300] = 1
    mask[625:750,243:395] = 1
    mask[650:850,415:770] = 1
    mask[800:960,1300:1550] = 1
    mask[1166:1280,50:184] = 1
    mask[1275:1369,800:950] = 1
    mask[1370:1500,700:875] = 1
    mask[1383:1436,1740:1853] = 1
    mask[1460:1600,1787:1980] = 1
    mask[1501:1700,533:733] = 1
    mask[1863:1993,310:455] = 1
    mask[1925:2022,1236:1376] = 1

    return mask
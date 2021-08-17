# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:11:50 2020

@author: 12036
"""

from numpy import load
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

dict_data = load('/Users/apple/Desktop/graduate/Machine_Learning_Theory/MRI/npz/OAS1_0019_MR.npz')
data = dict_data['arr_0']

dict_data = load('/Users/apple/Desktop/graduate/Machine_Learning_Theory/MRI/npz/OAS1_0019_MRseg.npz')
data2 = dict_data['arr_0']


dict1_data = load('/Users/apple/Desktop/graduate/Machine_Learning_Theory/MRI/npz/OAS1_0019_MR_skullseg.npz')
data3 = dict1_data['arr_0']

dict2_data = load('/Users/apple/Desktop/graduate/Machine_Learning_Theory/MRI/OAS1_0019_MRobs_seg.npz')
data4 = dict2_data['arr_0']

segment_ven = []               
segment_skull = []                
segment_ob = []
segment_ven = np.matrix(np.nonzero(data2 > 0))
segment_skull = np.matrix(np.nonzero(data3 > 0))
segment_ven = segment_ven.T
segment_skull = segment_skull.T
segment_ob = np.matrix(np.nonzero(data4 > 0))
segment_ob = segment_ob.T


fig = plt.figure()
ax = Axes3D(fig)
x = segment_ven[:, 0]
y = segment_ven[:, 1]
z = segment_ven[:, 2]

ax.scatter(x,y,z)
plt.show()
        
print(segment_ob)    


#%%

from gen_needle_path import gen_needle_path


line_arr = gen_needle_path(segment_skull, segment_ven)

fig = plt.figure()
ax = Axes3D(fig)
x = segment_skull[:, 0]
y = segment_skull[:, 1]
z = segment_skull[:, 2]

xv = segment_ven[:, 0]
yv = segment_ven[:, 1]
zv = segment_ven[:, 2]

xo = segment_ob[:, 0]
yo = segment_ob[:,1]
zo = segment_ob[:,2] 
xpt = line_arr[:, 0]
ypt = line_arr[:, 1]
zpt = line_arr[:, 2]

ax.scatter(xo,yo,zo)
ax.scatter(xv,yv,zv, color = 'green')
ax.plot(xpt, ypt, zpt, color = 'red')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


o = list(segment_ob)



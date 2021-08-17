# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:32:45 2020

@author: 12036
"""

from numpy import load
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

dict_data = load(r'C:\Users\12036\Documents\Machine Learning 1\MRI Project\Linhui Code\OAS1_0019_MR.npz')
data = dict_data['arr_0']

dict_data1 = load(r'C:\Users\12036\Documents\Machine Learning 1\MRI Project\Linhui Code\OAS1_0019_MRseg.npz')
data2 = dict_data1['arr_0']


dict2_data =  load(r'C:\Users\12036\Documents\Machine Learning 1\MRI Project\Linhui Code\OAS1_0019_MR_skullseg.npz')
data3 = dict2_data['arr_0']

dict3_data = load(r'C:\Users\12036\Documents\Machine Learning 1\MRI Project\Linhui Code\npzOAS1_0019_MRobstruct_seg.npz')
data4 = dict3_data['arr_0']

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
x = segment_ob[:, 0]
y = segment_ob[:, 1]
z = segment_ob[:, 2]

ax.scatter(x,y,z)
plt.show()
        
print(segment_ob)    


#%%
from ob_optimize import find_optimal_path

[shortest_path_data, safest_path_data] = find_optimal_path(segment_ob, segment_skull, segment_ven,3)
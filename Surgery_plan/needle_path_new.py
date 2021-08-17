# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:59:42 2020

@author: 12036
"""



def rand_pt(arr):
    
    """This function picks a random element of an array"""
    
    from random import randrange
    
    pt_arg = randrange(len(arr))
    pt = arr[pt_arg]
    
    return pt


###########################################################################################


def skull_point(skull_seg):
    
    """This function selects a random point from the appropriate region of the skull"""
    
    import numpy as np
   
    skull_filtered = skull_seg
    skull_filtered = [pt for pt in skull_filtered if ((pt[0,0] > 50) & (pt[0,1] > 0) & (pt[0,2] > 50))]
    skull_filtered = np.array(skull_filtered)
    
    
    skull_pt = rand_pt(skull_filtered)
    print(skull_pt)
    return skull_pt
    

###########################################################################################################

def vent_point(skull_pt, vent_seg):
    
    """This function uses monte carlo methods to find the nearest point in the ventrical to a given skull point"""
    
    import numpy as np
    
    v_distances = []
    pts = []
    for i in range(1000):
        rand_vent_pt = rand_pt(vent_seg)
        dist = np.linalg.norm(skull_pt - rand_vent_pt)
        v_distances.append(dist)
        pts.append(rand_vent_pt)
        
    vent_pt = pts[np.argmin(v_distances)]
    
    return vent_pt

############################################################################################################

def rand_needle_path(skull_seg, vent_seg):
    
    """This function generates a random needle path given a skull segment and ventrical segment"""
    
    import numpy as np
    
    skull_pt = skull_point(skull_seg)
    vent_pt = vent_point(skull_pt, vent_seg)
    
    m_arr = vent_pt - skull_pt
    line_pt_lst = []

    for t in range(-100,100):
        t = t/m_arr[0,0]
        px = vent_pt[0,0] + t*m_arr[0,0]
        py = vent_pt[0,1] + t*m_arr[0,1]
        pz = vent_pt[0,2] + t*m_arr[0,2]
        pnt = [px, py, pz]
        line_pt_lst.append(pnt)
    

    line_arr = np.array(line_pt_lst)
    
    return line_arr,skull_pt,vent_pt
        
    
    
    
    
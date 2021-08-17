#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_obs(segment_ob,line_arr,skull_point,ven_point):
    """This function filters the obstacle points between the ventricle and skull"""
    import numpy as np
    sp = skull_point
    vp = ven_point
    
    xmin = min(sp[0,0],vp[0,0])
    xmax = max(sp[0,0],vp[0,0])
    xc = (xmin + xmax)/2
    ymin = min(sp[0,1],vp[0,1])
    ymax = max(sp[0,1],vp[0,1])
    yc = (ymin + ymax)/2
    zmin = min(sp[0,2],vp[0,2])
    zmax = max(sp[0,2],vp[0,2])
    zc = (zmin + zmax)/2
    radius = np.sqrt(np.sum(np.square(sp-vp))) /2 
    x_range = range(int(xc - radius), int(xc + radius + 1) )
    y_range = range(int(yc - radius), int(yc + radius + 1) )
    z_range = range(int(zc - radius), int(zc + radius + 1) )


    ob_filtered = [pt for pt in segment_ob if (pt[0,0] in x_range) 
                   & (pt[0,1] in y_range) &(pt[0,2] in z_range)]
                                             
    return ob_filtered   
    
    
############################################################################################################


def ob_distance(obst,line_arr):
    """This function calculates the random distance and its average value """
    import random
    import numpy as np
    
    ob_points = random.sample(list(obst),1000)
    sum_d = []
    
    for x0 in ob_points:
        
        x1 = line_arr[0]
        x2 = line_arr[-1]
        
        num_cross = np.cross((x2-x1), (x1-x0))
        num = np.linalg.norm(num_cross)
        
        denom = np.linalg.norm(x2-x1)
        d = num/denom
        sum_d.append(d)
        
    d_mean = np.mean(sum_d)
    tot_d = sum(sum_d)
    
    return tot_d, d_mean


# In[ ]:

def find_optimal_path(segment_ob, segment_skull, segment_vent,n):
    from needle_path import rand_needle_path
    import numpy as np
    
    surgery_paths = []
    tot_ds = []
    mean_ds = []
    skull_pts = []
    vent_pts = []
    dists = []
    
    for i in range(n):
        
        [line_arr, skull_pt, vent_pt, dist] = rand_needle_path(segment_skull, segment_vent)
        ob_filtered = find_obs(segment_ob, line_arr, skull_pt, vent_pt)
        
        [tot_d, d_mean] = ob_distance(ob_filtered, line_arr)
        
        tot_ds.append(tot_d)
        mean_ds.append(d_mean)
        skull_pts.append(skull_pt)
        vent_pts.append(vent_pt)
        dists.append(dist)
        surgery_paths.append(line_arr)
        
    
    shortest_path_data = [surgery_paths[np.argmin(dists)], dists[np.argmin(dists)], mean_ds[np.argmin(dists)], skull_pts[np.argmin(dists)], vent_pts[np.argmin(dists)]]
    safest_path_data = [surgery_paths[np.argmin(mean_ds)], dists[np.argmin(mean_ds)], mean_ds[np.argmin(mean_ds)], skull_pts[np.argmin(mean_ds)], vent_pts[np.argmin(mean_ds)]]
    
    return shortest_path_data, safest_path_data
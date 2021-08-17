#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def find_obs(segment_ob,line_arr,skull_point,ven_point):
    """This function filters the obstacle points between the ventricle and skull"""
    
    xmin = min(sp[0,0],vp[0,0])
    xmax = max(sp[0,0],vp[0,0])
    xc = (xmin + xmax)/2
    ymin = min(sp[0,1],vp[0,1])
    ymax = max(sp[0,1],vp[0,1])
    yc = (ymin + ymax)/2
    zmin = min(sp[0,2],vp[0,2])
    zmax = max(sp[0,2],vp[0,2])
    zc = (zmin + zmax)/2
    path_len = np.sqrt(np.sum(np.square(sp-vp)))
    radius = np.sqrt(np.sum(np.square(sp-vp))) /2 
    x_range = range(int(xc - radius), int(xc + radius + 1) )
    y_range = range(int(yc - radius), int(yc + radius + 1) )
    z_range = range(int(zc - radius), int(zc + radius + 1) )


    ob_filtered = [pt for pt in segment_ob if (pt[0,0] in x_range) 
                   & (pt[0,1] in y_range) &(pt[0,2] in z_range)]
    
                                             
    return ob_filtered, path_len  
    
    
############################################################################################################


def ob_distance(obst,line_arr):
    """This function calculates the random distance and its average value """
    
    import random
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
        
    
    return sum_d, d_mean

############################################################################################################

def evaluate_function(path_len,d_mean):
    
    score = d_mean-0.01*(path_len)**2
    
    return score




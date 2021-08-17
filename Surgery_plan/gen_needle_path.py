def gen_needle_path(segment_skull, segment_ven):
    from random import randrange
    import numpy as np
    
    rand_vent_arg = randrange(len(segment_ven))
    vent_point = segment_ven[rand_vent_arg]
    
    
    top_skull_arr = segment_skull
    top_skull_arr = [pt for pt in top_skull_arr if ((pt[0,0] > 0) & (pt[0,1] > 0) & (pt[0,2] > 0) & (pt[0,2] > vent_point[0,2]))]
    top_skull_arr = np.array(top_skull_arr)
    
    rand_skull_arg = randrange(len(top_skull_arr))
    
    
    
    skull_point = top_skull_arr[rand_skull_arg]
    
    m_arr = vent_point - skull_point
    line_pt_lst = []

    for t in range(-100,100):
        t = t/m_arr[0,0]
        px = vent_point[0,0] + t*m_arr[0,0]
        py = vent_point[0,1] + t*m_arr[0,1]
        pz = vent_point[0,2] + t*m_arr[0,2]
        pnt = [px, py, pz]
        line_pt_lst.append(pnt)
    

    line_arr = np.array(line_pt_lst)
    return line_arr
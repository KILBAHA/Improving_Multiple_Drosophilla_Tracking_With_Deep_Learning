import numpy as np
import cv2
from math import sqrt # need for euclidian distance
import pandas as pd
import time

coords = np.load('Coords.npz') #index using coords['arr_x']


def find_unpaired (a,b): #Finds unpaired indexes in two sets of coords
    global dists, j_list, best_match, bi_bm, add
    a_dist = [] #a/b dist is list containing x and y coords
    for rw in a:
        x = rw[0]
        y = rw[1]
        a_dist.append((x,y))
    
    b_dist = []
    for rw in b:
        x = rw[0]
        y = rw[1]
        b_dist.append((x,y))
    
    
    if len(a_dist) == len(b_dist): #if you have equal sizes, do not run
        return()
    
    if len(a_dist) > len(b_dist): #order a_list and b_list with biggest size at index 0
        order = [a_dist, b_dist]
        abig = True
    elif len(a_dist) < len(b_dist):
        order = [b_dist, a_dist]
        abig = False
    j_list = []    
    
    #find best match of entries in smaller list to bigger list
    for i in range(0,len(order[0])): #big list = i
        dists = []
        for j in range(0,len(order[1])): #smaller list = j
           dists.append(sqrt((order[0][i][0] - order[1][j][0])**2 + (order[0][i][1] - order[1][j][1])**2))         
        j_list.append([i, dists.index(min(dists)), min(dists)])
    
    j_list = pd.DataFrame(j_list, columns = ['Big_ind', 'Small_ind', 'Dist']) #convert j_list to dataframe
        
    bi_bm = [] #stores best matching small index with big index
    
    for uni in j_list['Small_ind'].unique():
        sel = j_list.loc[j_list['Small_ind'] == uni]
        add = sel.loc[sel['Dist'] == min(sel['Dist'])]
        bi_bm.append(int(add['Big_ind'].values[0]))
    
    ret = [abig] #return[0] gives boolean to dictate weather a or b requires cropping 
    for index in [x for x in range(0,len(order[0])) if x not in bi_bm]: #return all unmatched coordinates
        ret.append(order[0][index])
    
    return(ret)

k_list = []
for k in coords.keys():
    k_list.append(k)


enrich_coord = []
enrich_frame = []

for i in range(0,len(k_list)-1):
    unp = find_unpaired(coords[k_list[i]], coords[k_list[i+1]])
    
    if len(unp) > 1:
        enrich_coord.append(unp[1:])
        if unp[0] == True:
            enrich_frame.append(i)
        else:
            enrich_frame.append(i+1)


cap = cv2.VideoCapture("/home/yusuf/Documents/GitHub/Tracking_Project/Haar/Enrichment/test.mp4")

print('got coords')

h = 25
w = 25
count = 0
#itterate through specific frames, get crop and save as .png files in enrich folder

for ind, frm in enumerate(enrich_frame):
    count += 1
    cap.get(frm)
    
    ret, frame = cap.read()


    if ret==True:
        # Croping the frame
        for coord in enrich_coord[ind]:
            crop_frame = frame[coord[1]:coord[1]+h, coord[0]:coord[0]+w]
    
    
            # cv2.imshow('croped',crop_frame)
            # time.sleep(0.25)
            
            path = 'enrich/e'+ str(count) +'.png'
            cv2.imwrite(path,crop_frame)             
            
            

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break



    
    # enrich_coord.append(find_unpaired(coords[k_list[i]], coords[k_list[i+1]]))
    # enrich_frame.append(i) # I don't think this is the correct index




# for rw in a:
#     x = rw[0]
#     y = rw[1]


# #some input parameters
# show_window = False
# cap = cv2.VideoCapture("/home/yusuf/Documents/VJ_Ethoscope/output.avi") #dl a test vid, replace filename

# while(True): #open video
#     ret, frame = cap.read()
#     # Our operations on the frame come here
#     gray = frame#cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break






# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
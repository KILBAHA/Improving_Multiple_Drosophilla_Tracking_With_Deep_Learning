import numpy as np
import cv2
import matplotlib.pyplot as plt

#some input parameters
show_window = False
fly_cascade = cv2.CascadeClassifier('cascade_combined.xml') #potentially need to make coppy of xml and replace
cap = cv2.VideoCapture("/home/yusuf/Documents/VJ_Ethoscope/test.mp4") #dl a test vid, replace filename
known_flies = 32 # Number of flies present in test video (manually counted)



#save to video
ret, img = cap.read()
x,y,c = img.shape
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fileout = cv2.VideoWriter('/home/yusuf/Documents/VJ_Ethoscope/output_combined.avi', fourcc, 25.0, (y,x))

#process through

fly_list = []
fly_count = []
while 1:
    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        flies = fly_cascade.detectMultiScale(img, scaleFactor= 1.1,
                                                  minNeighbors= 3, 
                                                  flags= 0,
                                                  minSize= (15, 15),
                                                  maxSize= (20, 20) )
        
        fly_list.append(flies) #stores all coords of flies
        fly_count.append(len(flies))
    
        for (x,y,w,h) in flies:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

        #write frame to video
        fileout.write(img)

        #and show if asked
        if show_window:
            cv2.imshow('img',img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
    else:
        break

# Release everything if job is finished
cap.release()
fileout.release()
cv2.destroyAllWindows()

np.savez('Coords', *fly_list[:])

corrected_count = []


for count in fly_count:
    corrected_count.append(count - known_flies)
    
    
plt.bar(range(0,len(corrected_count)),corrected_count)

plt.xlabel('Frame')
plt.ylabel('Count deviation')

abs_deviation = []
for count in corrected_count:
    abs_deviation.append(abs(count))
    
print('Absolute Deviation: ', sum(abs_deviation))

print('Mean Fly count:', sum(fly_count)/len(fly_count))






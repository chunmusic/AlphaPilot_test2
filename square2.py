import cv2
import numpy as np
from random import randint

img = cv2.imread('testing/images/IMG_2235.JPG')
#img = cv2.resize(img,(500,500))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


pts1 = np.float32([[100,100],[1196,100],[100,764],[1196,764]])
pts2 = np.float32([[0,0],[1196,0],[0,764],[1196,764]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(gray,M,(1196,764))

# top = int(0.05 * dst.shape[0])  # shape[0] = rows
# bottom = top
# left = int(0.05 * dst.shape[1])  # shape[1] = cols
# right = left
# value = [randint(0, 255), randint(0, 255), randint(0, 255)]
# borderType = cv2.BORDER_CONSTANT
# dst = cv2.copyMakeBorder(dst, top, bottom, left, right, borderType, None, value)


ret,thresh = cv2.threshold(dst,127,255,0)

_, contours,hier = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)


for i in range(len(contours)):
        for j in range(len(contours[i])):
                contours[i][j][0][0] = contours[i][j][0][0]*0.92283950617
                contours[i][j][0][1] = contours[i][j][0][1]*0.88425925925


for i in range(len(contours)):
        for j in range(len(contours[i])):

                contours[i][j][0][0] = contours[i][j][0][0] + 100
                contours[i][j][0][1] = contours[i][j][0][1] + 100

Area = []
hull_list = []
dummy = [[[667,578]],[[305,539]],[[307,198]],[[624,224]]]

for cnt in contours:
        
        if cv2.contourArea(cnt)>10000:  # remove small areas like noise etc
                hull = cv2.convexHull(cnt)    # find the convex hull of contour
                hull = cv2.approxPolyDP(hull,0.1*cv2.arcLength(hull,True),True)

                if len(hull) == 4:
                        Area.append(cv2.contourArea(cnt))  #append all square area
                        hull_list.append(hull)          #append hull square
                        # print (hull_list)
                else:
                        Area.append(100)
                        hull_list.append(dummy)
                        # print(hull_list)

print(len(hull_list))
result = hull_list[Area.index(max(Area))]
list_result = [[]]
print(result)

for cnt2 in contours:
        if cv2.contourArea(cnt2)>10000:  # remove small areas like noise etc
                hull = cv2.convexHull(cnt2)    # find the convex hull of contour
                hull = cv2.approxPolyDP(hull,0.1*cv2.arcLength(hull,True),True)
           
                if len(hull) == 4:
                        
                        if (len(Area)>0):
                                #print(hull_list[Area.index(max(Area))])
                                cv2.drawContours(img,[hull_list[Area.index(max(Area))]],0,(0,255,0),2)

                        elif (len(Area) == 0):
                                #print(hull_list[0])
                                cv2.drawContours(img,[hull_list[0]],0,(0,255,0),2)
        

for i in range(len(result)):

        list_result[0].append(result[i][0][0])
        list_result[0].append(result[i][0][1])

# print(list_result)     

# for cnt in contours:
        
#     if cv2.contourArea(cnt)>10000:  # remove small areas like noise etc
#         hull = cv2.convexHull(cnt)    # find the convex hull of contour
#         hull = cv2.approxPolyDP(hull,0.1*cv2.arcLength(hull,True),True)

#         if len(hull)==4:
#             cv2.drawContours(img,[hull],0,(0,255,0),2)
        

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
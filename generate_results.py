# This script is to be filled by the team members. 
# Import necessary libraries
# Load libraries
import json
import cv2
import numpy as np

# Implement a function that takes an image as an input, performs any preprocessing steps and outputs a list of bounding box detections and assosciated confidence score. 


class GenerateFinalDetections():
    def __init__(self):
         self.seed = 2018

        
    
    def predict(self,img):

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


        pts1 = np.float32([[100,100],[1196,100],[100,764],[1196,764]])
        pts2 = np.float32([[0,0],[1196,0],[0,764],[1196,764]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(gray,M,(1196,764))

        ret,thresh = cv2.threshold(dst,127,255,0)

        contours,hier = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)


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

        if len(hull_list)==0:
                result = dummy
        else:
                result = hull_list[Area.index(max(Area))]

        list_result = [[]]


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

        

        list_result[0].append(0.5)
        test2_result = np.array(list_result)

        
        return test2_result.tolist()
        

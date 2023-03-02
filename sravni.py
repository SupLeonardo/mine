import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
cap = cv.VideoCapture(0)
img1 = cv.imread('/home/it-7/Levchill/ironman.jpg',cv.IMREAD_GRAYSCALE) # trainImage
sift = cv.SIFT_create()
bf = cv.BFMatcher()
kp1, des1 = sift.detectAndCompute(img1,None)
while True:
    ret, frame = cap.read() # queryImage
    # Initiate SIFT detector
    # find the keypoints and descriptors with SIFT
    kp2, des2 = sift.detectAndCompute(frame,None)
    # BFMatcher with default params
    matches = bf.knnMatch(des1,des2,k=2)
    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
    # cv.drawMatchesKnn expects list of lists as matches.
    img3 = cv.drawMatchesKnn(img1,kp1,frame,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv.imshow('aa', cv.resize(img3, (1000,650)))
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
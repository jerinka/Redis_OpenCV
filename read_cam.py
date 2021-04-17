#!/usr/bin/env python3

import cv2
import struct
import redis
import numpy as np

def toRedis(r,a,n):
   """Store given Numpy array 'a' in Redis under key 'n'"""
   h, w = a.shape[:2]
   shape = struct.pack('>II',h,w)
   encoded = shape + a.tobytes()

   # Store encoded data in Redis
   r.set(n,encoded)
   return

if __name__ == '__main__':
    
    # Redis connection
    r = redis.Redis(host='localhost', port=6379, db=0)
    
    cam = cv2.VideoCapture(0)
    key = 0
    while key != 27:
        ret, img = cam.read()
        cv2.imshow('img', img)

        key = cv2.waitKey(1) & 0xFF
        toRedis(r, img, 'image')

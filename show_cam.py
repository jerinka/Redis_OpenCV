#!/usr/bin/env python3

import cv2
from time import sleep
import struct
import redis
import numpy as np

def fromRedis(r,n):
   """Retrieve Numpy array from Redis key 'n'"""
   encoded = r.get(n)
   h, w = struct.unpack('>II',encoded[:8])
   a = np.frombuffer(encoded, dtype=np.uint8, offset=8).reshape(h,w,3)
   return a

if __name__ == '__main__':
    # Redis connection
    r = redis.Redis(host='localhost', port=6379, db=0)

    key = 0
    while key != 27:
        img = fromRedis(r,'image')

        print(f"read image with shape {img.shape}")
        cv2.imshow('image out', img)
        key = cv2.waitKey(1) & 0xFF

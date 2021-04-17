import redis
import cv2
import numpy as np
import time
import io
from PIL import Image

r = redis.StrictRedis.from_url('redis://')

img_path ="redis.png"
img1_bytes = open(img_path,"rb").read()

# Write into redis server
r.set(img_path, img1_bytes)

# Reading Redis
img1_bytes_ = r.get(img_path)

# Decoding CV2+Redis
decoded = cv2.imdecode(np.frombuffer(img1_bytes_, np.uint8), 1)
cv2.imwrite("cv2_redis.png", decoded)





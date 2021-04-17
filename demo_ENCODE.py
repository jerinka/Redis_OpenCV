import redis
import cv2
import numpy as np
import time
import io
from PIL import Image

r = redis.StrictRedis.from_url('redis://')
img_path ="redis.png"

img1 = cv2.imread(img_path, 1)
retval, buffer = cv2.imencode('.png', img1)
img1_bytes = np.array(buffer).tostring()

# Write into redis server
r.set(img_path, img1_bytes)

# Reading Redis
img1_bytes_ = r.get(img_path)

# Decoding CV2+Redis
decoded = cv2.imdecode(np.frombuffer(img1_bytes_, np.uint8), 1)
cv2.imwrite("cv2_redis.png", decoded)



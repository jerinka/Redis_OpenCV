import redis
import cv2
import numpy as np
import time
import io
import uuid

r = redis.StrictRedis.from_url('redis://')
img_path ="redis.png"
uid = str(uuid.uuid1())

img1 = cv2.imread(img_path, 1)

retval, buffer = cv2.imencode('.png', img1,[cv2.IMWRITE_PNG_COMPRESSION, 0])
img1_bytes = np.array(buffer).tostring()

# Write into redis server
r.set(uid, img1_bytes)

# Reading Redis
img1_bytes_ = r.get(uid)

# Decoding CV2+Redis
decoded = cv2.imdecode(np.frombuffer(img1_bytes_, np.uint8), 1)
cv2.imwrite("cv2_redis.png", decoded)



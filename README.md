# Redis and Opencv

Eg: OpenCV based camera reading and pushing frames to Redis, another application fetching frames from Redis and showing in screen.

![redis](redis.png)

## Redis Docker

```docker run -d -p 6379:6379 redis```

## Read Write image array

```python3 demo_ENCODE.py```

## Read Write file

```python3 demo_FILE.py```

## Read Cam

```python3 read_cam.py```

## Show Cam

```python3 show_cam.py```



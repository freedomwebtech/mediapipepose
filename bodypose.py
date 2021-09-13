import cv2
from vidgear.gears import PiGear


options = {
#    "vflip": True,
    "exposure_mode": "auto",
    "iso": 800,
    "exposure_compensation": 15,
    "awb_mode": "horizon",
    "sensor_mode": 0,
}

# open pi video stream with defined parameters
stream = PiGear(resolution=(640, 480), framerate=60, logging=True, **options).start()
while True:
     frame = stream.read()
     frame1 = cv2.flip(frame, flipCode = -1)
    
     cv2.imshow("Frame", frame1);
     key = cv2.waitKey(1) & 0xFF
     if key == ord("q"):
        break
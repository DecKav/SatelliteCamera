from time import sleep
import picamera
import numpy as np
import serial
from PIL import Image

port = serial.Serial("/dev/ttyS0", baudrate = 115200)
port.flush()
print("Serial Connected...")

with picamera.PiCamera() as camera:
    image_height = 240
    image_width = 320
    camera.resolution = (image_width,image_height)
    camera.framerate = 24
    output = np.empty((image_height, image_width, 3), dtype = np.uint8)

    sleep(1)
    camera.capture(output,'rgb')
    print("Photo Taken...")

    image = Image.fromarray(output, "RGB")
    L = image.convert("L")
    print("Greyscaled Image...")
    L.save("Sent_Image.png", "PNG")
    print("File Saved...")
    f = open("Sent_Image.png", "rb")        
    print('Sending Image...')
    port.write(f.read())
    print('Done!')



import cv2
import argparse
import time
from numpy import *
from PIL import ImageEnhance, ImageOps, Image
import pytesseract
import os


def getTextFromCaptureDevice(capture_device=None):
    try:
        os.system('wmctrl -c ImageMagick')
    except:
        pass
    if capture_device is None:
        capture_device = cv2.VideoCapture(2)
    ret, frame = capture_device.read()
    if not ret:
        print("error")
        return
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    # img = Image.fromarray(frame)
    dimg = ImageEnhance.Sharpness(img).enhance(1)
    cimg = ImageOps.grayscale(dimg)
    text = pytesseract.image_to_string(dimg)
    dimg.show()
    time.sleep(1)
    return text.strip()


def main():
    cap = cv2.VideoCapture(2)
    for i in range(0, 2):
        # while True:
        text = getTextFromCaptureDevice(cap)
        print(text)


if __name__ == "__main__":
    main()

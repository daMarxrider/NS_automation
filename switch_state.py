import cv2
import argparse
import time
from numpy import *
from PIL import ImageEnhance, ImageOps, Image
import pytesseract
import os


def getTextFromCaptureDevice(capture_device=None):
    if capture_device is None:
        capture_device = cv2.VideoCapture(2)
    ret, frame = capture_device.read()
    if not ret:
        print("error")
        return
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    # img = Image.fromarray(frame)
    img = ImageEnhance.Sharpness(img).enhance(1)
    img = ImageOps.grayscale(img)
    img = ImageOps.invert(img)
    width, height = img.size
    left = width/4*3
    top = height / 2
    right = width
    bottom = height/8*6
    img = img.crop((left, top, right, bottom))
    text = pytesseract.image_to_string(img)
    img.show()
    return text.strip()


def main():
    cap = cv2.VideoCapture(2)
    for i in range(0, 2):
        # while True:
        text = getTextFromCaptureDevice(cap)
        print(text)


if __name__ == "__main__":
    main()

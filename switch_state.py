import cv2
from PIL import ImageEnhance, ImageOps, Image
import pytesseract


def getTextFromCaptureDevice(capture_device=None):
    if capture_device is None:
        capture_device = cv2.VideoCapture(0)
    ret, frame = capture_device.read()
    cv2.imshow("video", frame)
    if not ret:
        print("error")
        return
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    # img = Image.fromarray(frame)
    img = ImageEnhance.Sharpness(img).enhance(1)
    img = ImageOps.grayscale(img)
    img = ImageOps.invert(img)
    width, height = img.size
    left = width/100*4
    top = height / 100*90
    right = width/100*6
    bottom = height/100*94
    img = img.crop((left, top, right, bottom))
    text = pytesseract.image_to_string(img, config='--psm 10')
    img.show()
    return text.strip()


def main():
    cap = cv2.VideoCapture(0)
    for i in range(0, 2):
        # while True:
        text = getTextFromCaptureDevice(cap)
        print(text)


if __name__ == "__main__":
    main()

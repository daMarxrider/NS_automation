import logging
import cv2
from JoycontrolPlugin import JoycontrolPlugin
from PIL import ImageEnhance, ImageOps, Image
import pytesseract

import inspect

logger = logging.getLogger(__name__)


def getTextFromCaptureDevice(inst=None, capture_device=None):
    if capture_device is None:
        capture_device = cv2.VideoCapture(0)
    ret, frame = capture_device.read()
    if not ret:
        print("error")
        return
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    # img = Image.fromarray(frame)
    dimg = ImageEnhance.Sharpness(img).enhance(1)
    cimg = ImageOps.grayscale(dimg)
    width, height = cimg.size

    left = 0
    top = height / 2
    right = width
    bottom = height
    text = pytesseract.image_to_string(dimg)
    print("text")
    print(text)
    grey_text = pytesseract.image_to_string(cimg)
    print("grey_text")
    print(grey_text)
    cimg = cimg.crop((left, top, right, bottom))
    grey_text = pytesseract.image_to_string(cimg)
    # print("cropped_grey_text")
    # print(grey_text)
    return text.strip()


def getOverworldYButton(inst=None, capture_device=None):
    if capture_device is None:
        capture_device = cv2.VideoCapture(0)
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
    left = width/100*4
    top = height / 100*90
    right = width/100*6
    bottom = height/100*94
    img = img.crop((left, top, right, bottom))
    text = pytesseract.image_to_string(img, config='--psm 10')
    print(text)
    return text.strip()


def getTextFromRaidStart(capture_device=None):
    if capture_device is None:
        capture_device = cv2.VideoCapture(0)
    ret, frame = capture_device.read()
    if not ret:
        print("error")
        return
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    # img = Image.fromarray(frame)
    img = ImageEnhance.Sharpness(img).enhance(1)
    img = ImageOps.grayscale(img)
    # img = ImageOps.invert(img)
    width, height = img.size
    left = width/2
    top = height / 2
    right = width
    bottom = height
    img = img.crop((left, top, right, bottom))
    text = pytesseract.image_to_string(img)
    print(inspect.currentframe().f_code.co_name)
    print(text)
    return text.strip()


def getTextFromTextBubbleOverworld(capture_device=None):
    if capture_device is None:
        capture_device = cv2.VideoCapture(0)
    ret, frame = capture_device.read()
    if not ret:
        print("error")
        return
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    # img = Image.fromarray(frame)
    img = ImageEnhance.Sharpness(img).enhance(1)
    img = ImageOps.grayscale(img)
    img = ImageOps.invert(img)
    text = pytesseract.image_to_string(img)
    print(inspect.currentframe().f_code.co_name)
    print(text)
    return text.strip()


def getTextFromInRaidMenu(capture_device=None):
    if capture_device is None:
        capture_device = cv2.VideoCapture(0)
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
    print(inspect.currentframe().f_code.co_name)
    print(text)
    return text.strip()


def getTextFromCatchPrompt(capture_device=None):
    if capture_device is None:
        capture_device = cv2.VideoCapture(0)
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
    left = width/2
    top = height/2
    right = width
    bottom = height
    img = img.crop((left, top, right, bottom))
    text = pytesseract.image_to_string(img)
    print(inspect.currentframe().f_code.co_name)
    print(text)
    return text.strip()


def getRaidResult(capture_device=None):
    if capture_device is None:
        capture_device = cv2.VideoCapture(0)
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
    left = width/2
    top = 0
    right = width
    bottom = height/2
    img = img.crop((left, top, right, bottom))
    text = pytesseract.image_to_string(img)
    print(inspect.currentframe().f_code.co_name)
    print(text)
    return text.strip()


class PokemonRaidFight(JoycontrolPlugin):
    async def run(self):
        print("connected")
        await self.button_push('home')
        await self.wait(2)
        rounds = 0
        while True:
            while True:
                text_bubble = getTextFromTextBubbleOverworld()
                if getOverworldYButton() == 'Y':
                    print("starting before den")
                    await self.button_push('a')
                    await self.wait(2)
                elif text_bubble.__contains__("Want to throw in"):
                    await self.wait(1)
                    await self.button_push('a')
                elif text_bubble.__contains__("like to save"):
                    await self.wait(1)
                    await self.button_push('a')
                elif text_bubble.__contains__("saved"):
                    await self.wait(2)
                    await self.button_push('a')
                elif text_bubble.__contains__("into the den"):
                    await self.wait(1)
                    await self.button_push('a')
                    await self.wait(1)
                    await self.button_push('a')
                elif getTextFromRaidStart().__contains__('Don\'t Invite Others'):
                    await self.wait(1)
                    await self.button_push('down')
                    await self.wait(0.3)
                    await self.button_push('a')
                    await self.wait(1)
                    await self.button_push('a')
                elif getTextFromInRaidMenu().__contains__('Fight') or getTextFromInRaidMenu().__contains__('Cheer On'):
                    await self.button_push("a")
                    await self.wait(1)
                    await self.button_push("a")
                    await self.wait(1)
                    await self.button_push("a")
                elif getTextFromCatchPrompt().__contains__("Catch"):
                    print("dont catch")
                    await self.wait(1)
                    await self.button_push('down')
                    await self.wait(1)
                    await self.button_push('a')
                elif getRaidResult().__contains__("You defeated"):
                    await self.wait(1)
                    await self.button_push('a')
                    break
                else:
                    await self.wait(0.2)
            rounds += 1
            print(f'rounds: {rounds}')

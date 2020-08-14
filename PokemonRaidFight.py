import logging
import cv2
from JoycontrolPlugin import JoycontrolPlugin
from PIL import ImageEnhance, ImageOps, Image
import pytesseract

logger = logging.getLogger(__name__)


def getTextFromCaptureDevice(inst=None, capture_device=None):
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


def getTextFromRaidStart(capture_device=None):
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
    # img = ImageOps.invert(img)
    width, height = img.size
    left = width/2
    top = height / 2
    right = width
    bottom = height
    img = img.crop((left, top, right, bottom))
    text = pytesseract.image_to_string(img)
    print(text)
    return text.strip()


def getTextFromTextBubbleOverworld(capture_device=None):
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
    text = pytesseract.image_to_string(img)
    print(text)
    return text.strip()


def getTextFromInRaidMenu(capture_device=None):
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
    print(text)
    return text.strip()


def getTextFromCatchPrompt(capture_device=None):
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
    left = width/2
    top = height/2
    right = width
    bottom = height
    img = img.crop((left, top, right, bottom))
    text = pytesseract.image_to_string(img)
    print(text)
    return text.strip()


def getRaidResult(capture_device=None):
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
    left = width/2
    top = 0
    right = width
    bottom = height/2
    img = img.crop((left, top, right, bottom))
    text = pytesseract.image_to_string(img)
    print(text)
    return text.strip()


class PokemonRaidFight(JoycontrolPlugin):
    async def run(self):
        print("connected")
        await self.button_push('home')
        await self.wait(2)
        rounds = 0
        while True:
            print("starting before den")
            await self.button_push('a')
            await self.wait(2)
            while not getTextFromTextBubbleOverworld().__contains__("Want to throw in"):
                await self.wait(1)
                print("expecting want to throw in")
            await self.button_push('a')
            while not getTextFromTextBubbleOverworld().__contains__("like to save"):
                await self.wait(1)
                print("expected like to save")
            await self.button_push('a')
            while not getTextFromTextBubbleOverworld().__contains__("saved"):
                await self.wait(2)
                print("expected saved")
            await self.button_push('a')
            while not getTextFromTextBubbleOverworld().__contains__("into the den"):
                await self.wait(1)
                print("expected into the den")
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('a')
            while not getTextFromRaidStart().__contains__('Don\'t Invite Others'):
                await self.wait(1)
                print("expected dont invite others")
            await self.button_push('down')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(0.3)
            while not getTextFromInRaidMenu().__contains__('Fight'):
                await self.wait(1)
            # fight started
            print("fight started")
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('left')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(1)
            while True:
                if getTextFromInRaidMenu().__contains__('Fight'):
                    await self.button_push("a")
                    await self.wait(1)
                    await self.button_push("a")
                    await self.wait(1)
                    await self.button_push("a")
                    await self.wait(1)
                elif getTextFromCatchPrompt().__contains__("Catch"):
                    print("dont catch")
                    await self.wait(1)
                    await self.button_push('down')
                    await self.wait(1)
                    await self.button_push('a')
                    await self.wait(1)
                elif getRaidResult().__contains__("You defeated"):
                    await self.wait(1)
                    await self.button_push('a')
                    await self.wait(1)
                    break
                else:
                    await self.wait(1)
            rounds += 1
            print(f'rounds: {rounds}')
            await self.wait(8)

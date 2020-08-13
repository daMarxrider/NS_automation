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
    right = 0
    bottom = 0
    text = pytesseract.image_to_string(dimg)
    print("text")
    print(text)
    grey_text = pytesseract.image_to_string(cimg)
    print("grey_text")
    print(grey_text)
    # cimg = cimg.crop((left, top, right, bottom))
    # grey_text = pytesseract.image_to_string(cimg)
    # print("cropped_grey_text")
    # print(grey_text)
    return text.strip()


class PokemonRaidFight(JoycontrolPlugin):
    async def run(self):
        print("connected")
        await self.wait(5)
        await self.button_push('home')
        await self.wait(2)
        while True:
            print("starting before den")
            await self.button_push('a')
            await self.wait(5)
            await self.button_push('a')
            await self.wait(5)
            await self.button_push('a')
            await self.wait(5)
            print("saved")
            await self.button_push('a')
            await self.wait(3)
            await self.button_push('a')
            await self.wait(10)
            # den is placed
            print("den is placed")
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('down')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(50)
            # fight started
            print("fight started")
            print(getTextFromCaptureDevice())
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('left')
            await self.wait(1)
            fight_is_active = True
            while fight_is_active:
                if(("catch" in getTextFromCaptureDevice().lower()
                        and "catching"
                        not in getTextFromCaptureDevice().lower())
                   or "is weak" in getTextFromCaptureDevice().lower()):
                    print("dont catch")
                    await self.wait(1)
                    await self.button_push('down')
                    await self.wait(1)
                    await self.button_push('a')
                    await self.wait(1)
                    break
                elif "catching" in getTextFromCaptureDevice().lower():
                    print("aborting catch")
                    await self.button_push('b')
                    await self.wait(1)
                    await self.button_push('down')
                    await self.wait(1)
                    await self.button_push('a')
                    await self.wait(1)
                    break

                await self.button_push('a')
                await self.wait(1)
            # result screen
            print("result screen")
            text = getTextFromCaptureDevice()
            print(text)
            while "Exp." not in getTextFromCaptureDevice():
                print(getTextFromCaptureDevice())
            await self.button_push('a')
            await self.wait(10)

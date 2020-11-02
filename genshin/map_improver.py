from threading import Thread
import cv2
import time
import numpy as np
import mss
import imutils
import os

lower_blue = np.array([20, 40, 0], dtype=np.uint8)
upper_blue = np.array([50, 100, 120], dtype=np.uint8)

# lower_blue = np.array([0, 17, 0], dtype=np.uint8)
# upper_blue = np.array([44, 100, 160], dtype=np.uint8)


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


class VideoStreamWidget(object):
    def __init__(self, src=0):
        self.path = os.sep.join(os.path.abspath(__file__).split(os.sep)[0:-1])
        # self.capture = cv2.VideoCapture(src)
        # self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        # self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        self.img = None
        # self.capture.set(cv2.CAP_PROP_FPS,30)
        # cv2.setNumThreads = 6
        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()
        self.maxed = False
        self.updating_map = False
        self.map = None
        self.base_map = cv2.imread(self.path+os.sep+'map_icon.png')
        # self.base_map = cv2.resize(self.base_map, (960, 540))

        hsv = cv2.cvtColor(self.base_map, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        self.base_map_mask = mask

        self.star = cv2.imread(self.path+os.sep+'star.png')
        hsv = cv2.cvtColor(self.star, cv2.COLOR_BGR2HSV)
        star_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        self.star_mask = star_mask

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            with mss.mss() as sct:
                # Part of the screen to capture
                monitor = {"top": 50, "left": 150, "width": 360, "height": 410}
                while "Screen capturing":
                    last_time = time.time()
                    self.img = cv2.circle(
                        np.array(sct.grab(monitor)), (180, 180), 180, (0, 0, 0), 2)

                    # self.img = cv2.cvtColor(self.img, cv2.COLOR_HSV2BGR)


# Resizes a image and maintains aspect ratio


    def maintain_aspect_ratio_resize(self, image, width=None, height=None, inter=cv2.INTER_AREA):
        # Grab the image size and initialize dimensions
        dim = None
        (h, w) = image.shape[:2]

        # Return original image if no need to resize
        if width is None and height is None:
            return image

        # We are resizing height if width is none
        if width is None:
            # Calculate the ratio of the height and construct the dimensions
            r = height / float(h)
            dim = (int(w * r), height)
        # We are resizing width if height is none
        else:
            # Calculate the ratio of the 0idth and construct the dimensions
            r = width / float(w)
            dim = (width, int(h * r))

        # Return the resized image
        return cv2.resize(image, dim, interpolation=inter)

    def auto_canny(self, image, sigma=0.33):
        v = np.median(image)
        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edged = cv2.Canny(image, lower, upper)
        # return the edged image
        return edged

    def detect_shit(self):
        large_image = self.base_map_mask
        w, h = self.mask.shape[:]
        # idfk, maybe change method of matching

        # Dynamically rescale image for better template matching
        for x in range(1):
            scale = 0.85
        # for scale in np.linspace(0.825, 0.85, 10)[::-1]:

            print(scale)
            # Resize image to scale and keep track of ratio
            resized = self.maintain_aspect_ratio_resize(
                large_image, width=int(large_image.shape[1] * scale))
            r = large_image.shape[1] / float(resized.shape[1])

            # Stop if template image size is larger than resized image
            if resized.shape[0] < h or resized.shape[1] < w:
                break
            # All the 6 methods for comparison in a list
            methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                       'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
            for meth in methods:
                pos = cv2.matchTemplate(
                    resized, self.mask, eval(meth))
                print(cv2.minMaxLoc(pos))
                mn, _, mnLoc, _ = cv2.minMaxLoc(pos)

# Draw the rectangle:
# Extract the coordinates of our best match
                MPx, MPy = mnLoc
# Step 2: Get the size of the template. This is the same size as the match.
                trows, tcols = self.mask.shape[:2]

# Step 3: Draw the rectangle on slarge_image
                cv2.rectangle(large_image, (MPx, MPy),
                              (MPx+tcols, MPy+trows), (140, 140, 255), 2)
                # cv2.namedWindow('map', cv2.WINDOW_NORMAL)
                # cv2.imshow('map', large_image)

            cv2.namedWindow('map', cv2.WINDOW_NORMAL)
            cv2.imshow('map', large_image)

    def show_frame(self):
        # Display frames in main program
        while self.updating_map:
            # time.sleep(0.001)
            pass
        try:
            image = self.img
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (3, 3), 0)
            # apply Canny edge detection using a wide threshold, tight
            # threshold, and automatically determined threshold
            wide = cv2.Canny(blurred, 10, 200)
            tight = cv2.Canny(blurred, 225, 250)
            auto = self.auto_canny(blurred)
# show the images
            cv2.imshow("Original", image)
            cv2.imshow("Edges", np.hstack([wide, tight, auto]))

            hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

            hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            res = cv2.bitwise_and(self.img, self.img, mask=mask)

            self.mask = mask
            self.res = res
            cv2.imshow('frame', self.img)
            cv2.imshow('mask', mask)
            cv2.imshow('res', res)
            cv2.namedWindow('map_mask', cv2.WINDOW_NORMAL)
            cv2.imshow('map_mask', self.base_map_mask)
            # self.detect_shit()

            # cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
            #                         cv2.CHAIN_APPROX_SIMPLE)
            # cnts = imutils.grab_contours(cnts)
            # print("I found {} black shapes".format(len(cnts)))
            # cv2.imshow("Mask", shapeMask)

            # cv2.imshow('frame', self.img)
            if not self.maxed:
                cv2.setWindowProperty(
                    'frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                self.maxed = True
        except Exception as e:
            print(e)
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            cv2.destroyAllWindows()
            exit(1)


if __name__ == '__main__':
    video_stream_widget = VideoStreamWidget(2)
    while True:
        try:
            video_stream_widget.show_frame()
        except AttributeError:
            pass

from threading import Thread
import cv2
import time
import numpy as np


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


class VideoStreamWidget(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        # self.capture.set(cv2.CAP_PROP_FPS,30)
        # cv2.setNumThreads = 6
        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()
        self.maxed = False
        self.updating_map = False
        self.map = None

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            # print(type(self.frame))
            # self.frame = rescale_frame(self.frame,200)
            arr:np.ndarray = self.frame
            # print(arr.shape)
            # print(arr)
            h,w,c = arr.shape
            self.updating_map = True
            for x in range(h//6):
                for y in range(w//6):
                    for z in range(c):
                        self.frame[x][y][z] = arr[y][x][z]
                        # print(arr[x][y][z])
            self.updating_map = False
            time.sleep(0.001)

    def show_frame(self):
        # Display frames in main program
        while self.updating_map:
            # time.sleep(0.001)
            pass
        cv2.imshow('frame', self.frame)
        if not self.maxed:
            cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            self.maxed = True
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

import cv2
import numpy as np
from colour import Colour

#done

class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = np.zeros((height, width, 3), dtype = np.float32)

    def set_pixel(self, x, y, col):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y, x] = col.vector

    def to_uint8(self):
        return (np.clip(self.pixels * 255, 0, 255)).astype(np.uint8)


class Video:
    def __init__(self, width, height, frame_count):
        self.width = width
        self.height = height
        self.frames = [Image(width, height) for _ in range(frame_count)]

    def set_pixel(self, frame_idx, x, y, col):
        if 0 <= frame_idx < len(self.frames) and 0 <= x < self.width and 0 <= y < self.height:
            self.frames[frame_idx].set_pixel(x, y, col)

    def write_mp4(self, file_name, fps = 30):

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(file_name, fourcc, fps, (self.width, self.height))

        for frame in self.frames:
            rgb_array = frame.to_uint8()
            out.write(rgb_array)

        out.release()

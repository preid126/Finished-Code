from colour import Colour

class Image:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _  in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, col):
        self.pixels[y][x] = col

    def write_ppm(self, img_file):
        
        def to_byte(c):
            return round(max(min(c * 255, 255), 0))

        img_file.write(f"P3 \n{self.width} {self.height}\n255\n")
        for row in self.pixels:
            for colour in row:
                img_file.write(
                    "{} {} {}".format
                    (to_byte(colour.x), to_byte(colour.y), to_byte(colour.z)
                    )
                )
                img_file.write("\n")

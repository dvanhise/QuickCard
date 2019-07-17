
from PIL import Image, ImageDraw


class CardTemplate:
    font = '/Library/Fonts/Arial.ttf'

    def __init__(self, dimensions=(400, 300)):
        self.dimensions = dimensions
        self.canvas = None
        self.offset = 0

    def generate(self, context):
        img = Image.new('RGB', self.dimensions, color='#f5f5dc')
        self.offset = 0
        self.canvas = ImageDraw.Draw(img)

        # draw border
        self.canvas.rectangle(((5, 5), (self.dimensions[0] - 5, self.dimensions[1] - 5)), outline=(30, 30, 30), width=5)

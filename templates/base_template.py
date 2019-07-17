

class CardTemplate:
    font = '/Library/Fonts/Arial.ttf'

    def __init__(self):
        pass

    def generate(self, context, background=None):
        if background:
            img = Image.Image.open(background)
            img.resize((self.width, self.height))
        else:
            img = Image.new('RGB', (self.width, self.height), color='white')
        self.offset = 0
        self.canvas = ImageDraw.Draw(img)

        # draw border
        self.canvas.rectangle(((5, 5), (self.width - 5, self.height - 5)), outline=(30, 30, 30), width=5)
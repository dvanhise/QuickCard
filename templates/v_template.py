from PIL import Image, ImageDraw, ImageFont


class VehicleTemplate:
    name = 'vehicle'
    height = 150
    width = 300

    def generate(self, context):
        img = Image.new('RGB', (self.width, self.height), color='white')
        d = ImageDraw.Draw(img)

        # draw border
        d.rectangle(((5, 5), (self.width - 5, self.height - 5)), outline=(30, 30, 30), width=5)

        # draw title
        fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 17)
        d.text((10, 10), context.get('name', self.name), font=fnt, fill=(30, 30, 30))

        # draw other parts

        # draw notes
        d.text((10, 30), context.get('notes1', ''), font=fnt, fill=(30, 30, 30))
        d.text((10, 45), context.get('notes2', ''), font=fnt, fill=(30, 30, 30))
        d.text((10, 60), context.get('notes3', ''), font=fnt, fill=(30, 30, 30))

        return img

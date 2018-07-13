from PIL import Image, ImageDraw, ImageFont


class EnemyTemplate:
    name = 'enemy'

    def generate(self, context):
        img = Image.new('RGB', (400, 200), color='white')

        # draw border

        # draw title
        fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
        d = ImageDraw.Draw(img)
        d.text((10, 10), context.get('name'), font=fnt, fill=(20, 20, 20))

        # draw stats

        # draw behavior

        return img

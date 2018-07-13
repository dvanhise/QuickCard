from PIL import Image, ImageDraw, ImageFont


class WeaponTemplate:
    name = 'weapon'
    height = 200
    width = 400

    # context fields - name, damage, rof, ap, notes1, notes2, notes3
    def generate(self, context):
        img = Image.new('RGB', (self.width, self.height), color='white')
        d = ImageDraw.Draw(img)

        # draw border
        d.rectangle(((5, 5), (self.width - 5, self.height - 5)), outline=(30, 30, 30), width=5)

        # draw title
        fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 17)
        d.text((15, 10), context.get('name', self.name), font=fnt, fill=(30, 30, 30))

        # draw damage
        fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
        d.text((15, 30), 'Damage: ' + context.get('damage', ''), font=fnt, fill=(30, 30, 30))

        # draw RoF
        d.text((15, 50), 'RoF: ' + context.get('rof', ''), font=fnt, fill=(30, 30, 30))

        # draw AP
        d.text((15, 70), 'AP: ' + context.get('ap', ''), font=fnt, fill=(30, 30, 30))

        # draw notes
        d.text((15, 90), context.get('notes1', ''), font=fnt, fill=(30, 30, 30))
        d.text((15, 105), context.get('notes2', ''), font=fnt, fill=(30, 30, 30))
        d.text((15, 130), context.get('notes3', ''), font=fnt, fill=(30, 30, 30))

        return img

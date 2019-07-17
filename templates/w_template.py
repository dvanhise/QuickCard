from templates.base_template import CardTemplate
from PIL import Image, ImageDraw, ImageFont
from notes import DEFAULT_NOTES


class WeaponTemplate(CardTemplate):
    name = 'weapon'
    height = 200
    width = 400

    def __init__(self):
        self.offset = 0
        self.canvas = None

    # context fields - name, damage, rof, ap, notes1, notes2, notes3
    def generate(self, context, background=None):
        img = super.generate(context, background)

        # draw title
        self.text_line(context.get('name', self.name), 10, 17)

        # draw damage
        self.text_line('Damage: ' + context.get('damage', ''), 20, 15)

        # draw range
        if context.get('range'):
            self.text_line('Range: ' + context.get('range', ''), 20, 15)

        # draw RoF
        if context.get('rof'):
            self.text_line('RoF: ' + context.get('rof', ''), 20, 15)

        # draw AP
        if context.get('ap', 0):
            self.text_line('AP: ' + context.get('ap', ''), 20, 15)

        # draw notes
        for note in context.get('notes', []):
            if note in DEFAULT_NOTES:
                self.text_line('{name}: {description}'.format(**(DEFAULT_NOTES[note])), 20, 15)

        for note in context.get('extra_notes', []):
            self.text_line(note, 20, 15)

        return img

    def text_line(self, text, offset, size, fill=(30, 30, 30)):
        self.offset += offset
        fnt = ImageFont.truetype(self.font, size)
        self.canvas.text((15, self.offset), text, font=fnt, fill=fill)

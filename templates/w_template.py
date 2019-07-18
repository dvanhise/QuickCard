from templates.base_template import CardTemplate
from PIL import ImageFont
import yaml


class WeaponTemplate(CardTemplate):
    name = 'weapon'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.offset = 0
        self.canvas = None
        with open('default_weapons.yaml', 'r', newline='') as f:
            self.default_weapons = yaml.load(f)

    # context fields - name, damage, range, rof, ap, shots
    def generate(self, context):
        super().generate(context)

        # Find inherited weapon stats if applicable
        data = self.default_weapons.get(context.get('inherit', ''), {})
        data.update(context)

        # draw title
        self.text_line(data.get('name', ''), 10, 17)

        # draw damage
        self.text_line('Damage: ' + data.get('damage', ''), 20, 15)

        # draw range
        if data.get('range'):
            self.text_line('Range: ' + data.get('range', ''), 20, 15)

        # draw RoF
        rof = data.get('rof', 1)
        if rof > 1:
            self.text_line('RoF: %d' % rof, 20, 15)

        # draw AP
        ap = data.get('ap', 0)
        if ap > 0:
            self.text_line('AP: %d' % ap, 20, 15)

        # draw notes (additional rules for weapon e.g. fragile, high crit, shotgun)
        # draw abilities (additional things you can do with weapon e.g. 3RB, auto)

        return self.image

    def text_line(self, text, offset, size, fill=(30, 30, 30)):
        self.offset += offset
        fnt = ImageFont.truetype(self.font, size)
        self.canvas.text((15, self.offset), text, font=fnt, fill=fill)

from templates.base_template import CardTemplate
import yaml
from jinja2 import Environment, FileSystemLoader
import imgkit


class CharacterTemplate(CardTemplate):
    name = 'character'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.offset = 0
        self.canvas = None
        with open('data_files/default_characters.yaml', 'r') as f:
            self.default_characters = yaml.safe_load(f)
        with open('data_files/character_abilities.yaml', 'r', encoding='utf8') as f:
            self.character_abilites = yaml.safe_load(f)
        with open('data_files/default_weapons.yaml', 'r') as f:
            self.weapons = yaml.safe_load(f)

        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)

        self.template = env.get_template('html/character.html')

    # context fields - name, damage, range, rof, ap, shots
    def generate(self, data, outfile='output.png', height=300, width=400, bgcolor='#f5f5dc'):
        wkhtml_options = {
            'height': height,
            'width': width
        }

        context = {
            'card_height': height,
            'card_width': width,
            'bgcolor': bgcolor,
            'abilites': [],
            'additional_abilites': [],
            'gear': [],
            'additional_gear': []
        }

        # Find inherited character stats if applicable
        context.update(self.default_characters.get(data.get('inherit', ''), {}))
        context.update(data)

        # Look up abilites by reference
        for ndx, ability in enumerate(context.get('abilites', [])):
            if type(ability) is str:
                if ability in self.character_abilites:
                    context['abilites'][ndx] = self.character_abilites[ability]
                else:
                    print('Unknown note name: %s' % ability)

        for ndx, item in enumerate(context.get('gear', [])):
            if type(item) is str:
                if item in self.weapons:
                    context['gear'][ndx] = self.weapons[item]
                # if item in self.items:
                #     context['gear'][ndx] = self.character_abilites[item]
                else:
                    print('Unknown item name: %s' % item)

        imgkit.from_string(self.template.render(context), outfile, options=wkhtml_options)

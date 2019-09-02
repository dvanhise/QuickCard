from templates.base_template import CardTemplate
import yaml
from jinja2 import Environment, FileSystemLoader
import imgkit


class ArmorTemplate(CardTemplate):
    name = 'armor'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.offset = 0
        self.canvas = None
        with open('data_files/default_armor.yaml', 'r') as f:
            self.default_armor = yaml.safe_load(f)
        with open('data_files/armor_notes.yaml', 'r', encoding='utf8') as f:
            self.armor_notes = yaml.safe_load(f)

        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)

        self.template = env.get_template('html/armor.html')

    # context fields - name, armor, parry, notes
    def generate(self, data, outfile='output.png', height=300, width=400, bgcolor='#f5f5dc'):
        wkhtml_options = {
            'height': height,
            'width': width
        }

        # Set defaults
        context = {
            'card_height': height,
            'card_width': width,
            'bgcolor': bgcolor,
            'armor': 0,
            'parry': '',
            'notes': [],
            'additional_notes': []
        }

        # Find inherited weapon stats if applicable
        context.update(self.default_armor.get(data.get('inherit', ''), {}))
        context.update(data)

        # Look up notes by reference
        for ndx, note in enumerate(context.get('notes', [])):
            if type(note) is str:
                if note in self.armor_notes:
                    context['notes'][ndx] = self.armor_notes[note]
                else:
                    print('Unknown note name: %s' % note)

        imgkit.from_string(self.template.render(context), outfile, options=wkhtml_options)

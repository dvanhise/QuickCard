from templates.e_template import EnemyTemplate
from templates.w_template import WeaponTemplate
from templates.i_template import ItemTemplate
from templates.v_template import VehicleTemplate

import csv
import yaml
import sys
import os
from random import randint


OUTPUT_DIR = 'output'


def main():
    # Arguments are a list of yaml/json/csv to make cards from
    if len(sys.argv) < 2:
        sys.exit(1)

    # card files with fields: title, type(item, weapon, armor), inherit, [any replacement fields], description,
    # abilities, additional_abilites, count

    # TODO: 2.5" x 3.5" cards by default

    for input_file in sys.argv[1:]:
        if input_file.lower().endswith(('.yml', '.yaml')):
            with open(input_file, 'r', newline='') as f:
                reader = yaml.load(f)
        elif input_file.lower().endswith('.csv'):
            pass
        elif input_file.lower().endswith('.json'):
            pass
        else:
            raise ValueError('Unable to handle file extension of %s' % input_file)

    # map template names to instances
    templates = {cls.name: cls() for cls in [EnemyTemplate, WeaponTemplate, ItemTemplate, VehicleTemplate]}

    counter = 1
    for row in reader:
        if row.get('type') not in templates:
            continue

        template = templates[row['type']]
        image = template.generate(row)

        for _ in range(row.get('count', 1)):
            image.save(os.path.join(OUTPUT_DIR, '%s-%s.png' % (row['type'], counter)))
            counter += 1


if __name__ == '__main__':
    main()

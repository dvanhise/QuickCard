from templates.e_template import EnemyTemplate
from templates.w_template import WeaponTemplate
from templates.i_template import ItemTemplate
from templates.v_template import VehicleTemplate

import csv
import sys
import os
from random import randint


OUTPUT_DIR = 'output'


def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    # load templates
    template_classes = [EnemyTemplate, WeaponTemplate, ItemTemplate, VehicleTemplate]

    # map template names to instances
    tmpl = {cls.name: cls() for cls in template_classes}

    input_file = sys.argv[1]
    with open(input_file, 'r', newline='') as f:
        reader = csv.DictReader(f)

    for row in reader:
        if 'template' not in row or row['template'] not in tmpl:
            continue

        template = tmpl[row['template']]
        image = template.generate(row)
        image.save(os.path.join(OUTPUT_DIR, get_file_name(row)))


def get_file_name(row):
    return row.get('filename', row['template'] + str(randint(100, 10000))) + '.png'


if __name__ == '__main__':
    main()

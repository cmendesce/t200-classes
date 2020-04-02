#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
from glob import glob
import os

env = Environment(loader=FileSystemLoader('web/templates'))

files = glob('web/templates/aulas/*.html')
for f in files:
    temp_file = f'aulas/{os.path.basename(f)}'
    template = env.get_template(temp_file)
    output = template.render()
    with open(f'_site/{os.path.basename(f)}', 'w', encoding='ISO-8859-1') as file:
        file.write(output)
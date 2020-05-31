import re

import numpy as np
from wfdb.io import wrann


with open('test-dataset-annos.txt') as file_:
    anno_txt = file_.read()

init_match = re.findall(r'(?:([AN]*)|(x\d\d))', anno_txt.replace('\n', ''))
init_match = [k for k in init_match if k != ('', '')]
annos = {}
latest_file = None
for line in init_match:
    if line[1] != '':
        latest_file = line[1]
        annos[latest_file] = ''
    elif line[0] != '':
        annos[latest_file] = annos[latest_file] + line[0]

for file, ann in annos.items():
    symbols = np.array([char for char in ann])
    samps = np.array([i*6000 for i, c in enumerate(ann)])
    wrann(file, 'apn', sample=samps, symbol=symbols)

import argparse
import glob
import os
import numpy as np
import pickle

parser = argparse.ArgumentParser()
parser.add_argument(
    '--input-dir',
    type=str,
    default="stdin"
)
parser.add_argument(
    '--model',
    type=str,
    default=""
)
args = parser.parse_args()
text = ""
if args.input_dir != "stdin":
    for filename in glob.glob(os.path.join(args.input_dir, '*.txt')):
        with open(os.path.join(args.input_dir, filename), 'r') as f:
            text += ' ' + f.read()
else:
    text = input()  # add multiple input

for i in text:
    if not i.isalpha():
        text = text.replace(i, ' ')
text = text.lower().split()

model = dict()
for pref in range(len(text) - 1):
    if text[pref] not in model.keys():
        model[text[pref]] = []
    model[text[pref]].append(text[pref + 1])

for pref in model.keys():
    items, counts = np.unique(model[pref], return_counts=True)
    n = len(model[pref])
    counts = list(map(lambda x: x / n, counts))
    model[pref] = list(zip(items, counts))

# print(model)
with open(args.model, 'wb') as f:
    pickle.dump(model, f)

import argparse
import numpy as np
import pickle

parser = argparse.ArgumentParser()
parser.add_argument(
    '--prefix',
    type=str,
    default=""
)
parser.add_argument(
    '--model',
    type=str,
    default=""
)
parser.add_argument(
    '--length',
    type=int,
    default=5
)
args = parser.parse_args()

with open(args.model, 'rb') as f:
    my_model = pickle.load(f)
length = args.length
ans = args.prefix.split()
if ans == []:
    ans.append(np.random.choice(list(my_model.keys()), 1)[0])
for i in range(length - len(ans)):
    ans.append(np.random.choice(list(map(lambda x: x[0], my_model[ans[-1]])), 1,
                                p=list(map(lambda x: x[1], my_model[ans[-1]])))[0])
print(' '.join(ans))

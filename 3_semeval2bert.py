# -*- coding:utf-8 -*-
"""
Created on 18/12/5 下午5:02.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import io
import re
import numpy as np

raw_data_path = ""
test_data_path = ""
train_tsv_path = ""    # end with ".tsv"
dev_tsv_path = ""      # end with ".tsv"
test_tsv_path = ""     # end with ".tsv"

REPEATED_CHARS = ['.', '?', '!', ',']

def processor(line):
    for c in REPEATED_CHARS:
        lineSplit = line.split(c)
        while True:
            try:
                lineSplit.remove('')
            except:
                break
        cSpace = ' ' + c + ' '
        line = cSpace.join(lineSplit)

    return line

train_data = []
test_data = []

with io.open(raw_data_path, encoding='utf8') as fin:
    fin.readline()

    for line in fin:
        line = processor(line).strip().split('\t')
        # line -> [id, turn0, turn1, turn2, label]
        id = line[0]

        conv = ' <eos> '.join(line[1:4])
        duplicateSpacePattern = re.compile(r'\ +')
        conv = re.sub(duplicateSpacePattern, ' ', conv)

        label = line[4]

        train_data.append((id, conv, label))

with io.open(test_data_path, encoding='utf8') as fin:
    fin.readline()

    for line in fin:
        line = processor(line).strip().split('\t')

        # line -> [id, turn0, turn1, turn2]
        id = line[0]
        conv = ' <eos> '.join(line[1:])
        # Remove any duplicate spaces
        duplicateSpacePattern = re.compile(r'\ +')
        conv = re.sub(duplicateSpacePattern, ' ', conv)
        test_data.append((id, conv))

data_len = len(train_data)
dev_len = data_len // 10

np.random.shuffle(train_data)

with open(train_tsv_path, 'w') as f_train:
    for term in train_data[:-dev_len]:
        f_train.write(term[0])
        f_train.write('\t')
        f_train.write(term[1])
        f_train.write('\t')
        f_train.write(term[2])
        f_train.write('\n')

with open(dev_tsv_path, 'w') as f_dev:
    for term in train_data[-dev_len:]:
        f_dev.write(term[0])
        f_dev.write('\t')
        f_dev.write(term[1])
        f_dev.write('\t')
        f_dev.write(term[2])
        f_dev.write('\n')

with open(test_tsv_path, 'w') as f_test:
    for term in test_data:
        f_test.write(term[0])
        f_test.write('\t')
        f_test.write(term[1])
        f_test.write('\n')
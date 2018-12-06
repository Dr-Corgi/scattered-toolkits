# -*- coding:utf-8 -*-
"""
Created on 18/12/6 上午11:20.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import json
import codecs

idx2emo = {0: 'Other', 1: 'Like', 2: 'Sadness', 3: 'Disgust', 4: 'Anger', 5: 'Happiness'}

train_raw_path = ""
dev_raw_path = ""
test_raw_path = ""

train_tsv_path = ""
dev_tsv_path = ""
test_tsv_path = ""

def processor(raw_data):
    processed_data = []
    for data in raw_data:
        text, label = data
        text = "".join(text.strip().split())
        text = " ".join([t for t in text])
        label = idx2emo[int(label)]
        processed_data.append([text, label])

    return processed_data

train_data_raw = json.load(codecs.open(train_raw_path, 'r', 'utf8'))
train_data = processor(train_data_raw)

dev_data_raw = json.load(codecs.open(dev_raw_path, 'r', 'utf8'))
dev_data = processor(dev_data_raw)

test_data_raw = json.load(codecs.open(test_raw_path, 'r', 'utf8'))
test_data = processor(test_data_raw)

id = 0

with open(train_tsv_path, 'w') as f_train:
    for term in train_data:
        id += 1
        f_train.write(str(id))
        f_train.write('\t')
        f_train.write(term[0])
        f_train.write('\t')
        f_train.write(term[1])
        f_train.write('\n')

with open(dev_tsv_path, 'w') as f_dev:
    for term in dev_data:
        id += 1
        f_dev.write(str(id))
        f_dev.write('\t')
        f_dev.write(term[0])
        f_dev.write('\t')
        f_dev.write(term[1])
        f_dev.write('\n')

with open(test_tsv_path, 'w') as f_test:
    for term in test_data:
        id += 1
        f_test.write(str(id))
        f_test.write('\t')
        f_test.write(term[0])
        f_test.write('\t')
        f_test.write(term[1])
        f_test.write('\n')
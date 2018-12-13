# -*- coding:utf-8 -*-
"""
Created on 18/12/13 上午11:05.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import json
import codecs

source_path = ""
dump_path = ""

source_data = json.load(codecs.open(source_path, 'r', 'utf8'))
data = []

for (src, src_emo), (trg, trg_emo) in source_data:
    src = " ".join([word for word in "".join(src.strip().split())])
    trg = " ".join([word for word in "".join(trg.strip().split())])

    data.append(src + '\t' + str(src_emo))
    data.append(trg + '\t' + str(trg_emo))

with codecs.open(dump_path, 'w', 'utf8') as fout:
    for d in data:
        fout.write(d)
        fout.write('\n')
# -*- coding:utf-8 -*-
"""
Created on 18/12/4 下午10:29.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import json
import jieba
import codecs

post_file_path = ""
response_file_path = ""
dump_path = ""

def emotion_classifier(text):
    # implementation of emotion classifier
    return 0

data = []

with open(post_file_path) as fp, open(response_file_path) as fr:

    post, response = fp.readline(), fr.readline()

    while post and response:

        post = post.strip().split("\t")[-1]
        response = response.strip().split("\t")[-1]

        post = " ".join(list(jieba.cut(post)))
        response = " ".join(list(jieba.cut(response)))

        data.append([[post, emotion_classifier(post)], [response, emotion_classifier(response)]])

        post, response = fp.readline(), fr.readline()

with codecs.open(dump_path, 'w', 'utf8') as fout:
    json.dump(data, fout, ensure_ascii=False)
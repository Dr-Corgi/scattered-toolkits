# -*- coding:utf-8 -*-
"""
Created on 18/12/5 上午10:02.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import jieba
import codecs

post_file_path = ""
response_file_path = ""
dump_path = ""

data = []

with open(post_file_path) as fp, open(response_file_path) as fr:

    post, response = fp.readline(), fr.readline()

    count = 0

    while post and response:

        # if count >= 1000:
        #     break

        post = post.strip().split("\t")[-1]
        response = response.strip().split("\t")[-1]

        data.append(" ".join(list(jieba.cut(post))))
        data.append(" ".join(list(jieba.cut(response))))

        post, response = fp.readline(), fr.readline()
        count += 1

with codecs.open(dump_path, 'w', 'utf8') as fout:
    for d in data:
        fout.write(d)
        fout.write('\n')
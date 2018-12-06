# -*- coding:utf-8 -*-
"""
Created on 18/12/6 上午11:51.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""

class NLPCCProcessor(DataProcessor):
    """Processor for the SemEval data set."""

    def get_train_examples(self, data_dir):
        return self._create_examples(
            self._read_tsv(os.path.join(data_dir, 'train.tsv')), 'train')

    def get_dev_examples(self, data_dir):
        return self._create_examples(
            self._read_tsv(os.path.join(data_dir, 'dev.tsv')), 'dev')

    def get_test_examples(self, data_dir):
        return self._create_examples(
            self._read_tsv(os.path.join(data_dir, 'test.tsv')), 'test')

    def get_labels(self):
        return ["Other", "Like", "Sadness", "Disgust", "Anger", "Happiness"]

    def _create_examples(self, lines, set_type):
        examples = []
        for (i, line) in enumerate(lines):
            guid = line[0]
            text_a = tokenization.convert_to_unicode(line[1])
            text_b = None
            if set_type != 'test':
                label = tokenization.convert_to_unicode(line[2])
            else:
                label = "Other"
            examples.append(
                InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label))
        return examples

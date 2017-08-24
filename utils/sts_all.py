import os
import utils
import collections

import numpy as np


class STSAll(object):
    def __init__(self, train_validation_split=None, test_split=None,
                 vocab_min_frequency=None):
        if train_validation_split is None or test_split is None:
            raise NotImplementedError('This Dataset does not implement '
                  'train_validation_split or test_split as the dataset is big'
                  ' enough and uses dedicated splits from the original '
                  'datasets')
        self.dataset_name = 'Semantic Text Similarity - All'
        self.dataset_description = 'This dataset has been generated by ' \
               'merging MPD, SICK, Quora, StackExchange and and SemEval ' \
               'datasets. \n It has 258537 Training sentence pairs, 133102 ' \
               'Test sentence pairs and 59058 validation sentence pairs.'
        self.dataset_path = os.path.join(utils.data_root_directory, 'mpd')
        self.train_path = os.path.join(self.dataset_path, 'train', 'train.txt')
        self.validation_path = os.path.join(self.dataset_path, 'validation',
                                            'validation.txt')
        self.test_path = os.path.join(self.dataset_path, 'test', 'test.txt')
        self.vocab_path = os.path.join(self.dataset_path, 'vocab.txt')
        self.w2v_path = os.path.join(self.dataset_path, 'test', 'test.txt')

        if vocab_min_frequency is None:
            self.w2i, self.i2w = self.load_vocabulary()
            self.w2v = self.load_w2v()
        else:
            self.w2i, self.i2w = self.create_vocabulary(vocab_min_frequency)
            self.w2v = self.preload_w2v()

        self.train = DataSet()
        self.validation = None
        self.test = None

    def load_vocabulary(self):
        w2i = {}
        i2w = {}
        with open(self.vocab_path, 'r') as vf:
            wid = 0
            for line in vf:
                term = line.strip().split('\t')[0]
                w2i[term] = wid
                i2w[wid] = term
                wid += 1
        return w2i, i2w

    def create_vocabulary(self, min_frequency=5, tokenizer='spacy',
                          downcase=True, max_vocab_size=None):
        cnt = collections.Counter()

        for line in self.train_path:
            if args.downcase:
                line = line.lower()
            if args.delimiter == "":
                tokens = list(line.strip())
            else:
                tokens = line.strip().split(args.delimiter)
            tokens = [_ for _ in tokens if len(_) > 0]
            cnt.update(tokens)

        logging.info("Found %d unique tokens in the vocabulary.", len(cnt))

        # Filter tokens below the frequency threshold
        if args.min_frequency > 0:
            filtered_tokens = [(w, c) for w, c in cnt.most_common()
                               if c > args.min_frequency]
            cnt = collections.Counter(dict(filtered_tokens))

        logging.info("Found %d unique tokens with frequency > %d.",
                     len(cnt), args.min_frequency)

        # Sort tokens by 1. frequency 2. lexically to break ties
        word_with_counts = cnt.most_common()
        word_with_counts = sorted(
                word_with_counts, key=lambda x: (x[1], x[0]), reverse=True)

        # Take only max-vocab
        if args.max_vocab_size is not None:
            word_with_counts = word_with_counts[:args.max_vocab_size]

        for word, count in word_with_counts:
            print("{}\t{}".format(word, count))

    def preload_w2v(self, initialize='random'):
        '''
        initialize can be "random" or "zeros"
        '''
        if initialize == 'random':
            w2v = np.random.rand(len(self.w2i), 300)
        else:
            w2v = np.zeros((len(self.w2i), 300))
        for term in self.w2i:
            w2v[self.w2i[term]] = utils.spacy_nlp(term).vector

        return w2v

    def load_w2v(self):
        return np.load(self.w2v_path)


    def save_w2v(self, w2v):
        return np.save(self.w2v_path, w2v)



class DataSet(object):

    def __init__(self, path, vocab, pad=0):

        self.path = path
        self._epochs_completed = 0
        self._index_in_epoch = 0
        self.vocab_w2i = vocab[0]
        self.vocab_i2w = vocab[1]
        self.datafile = None
        self.pad = pad
        self.Batch = collections.namedtuple('Batch', ['s1', 's2', 'sim'])

    def open(self):
        self.datafile = open(self.path, 'r')

    def close(self):
        self.datafile.close()

    def next_batch(self, batch_size, balance=True, seq_begin=False,
                   seq_end=False):
        if not self.datafile:
            raise Exception('The dataset needs to be open before being used. '
                            'Please call dataset.open() before calling '
                            'dataset.next_batch()')

        s1s, s2s, sims = [], [], []

        while len(s1s) == batch_size:

            row = self.datafile.readline()
            cols = row.strip().split('\t')
            s1, s2, sim = cols[0], cols[1], float(cols[2])
            s1, s2 = s1.split(' '), s2.split(' ')
            s1s.append(s1)
            s2s.append(s2)
            sims.append(sim)

        batch = self.Batch(
            s1=utils.padseq(utils.seq2id(s1s[:batch_size],
                                         self.vocab_w2i)),
            s2=utils.padseq(utils.seq2id(s2s[:batch_size],
                                         self.vocab_i2w)),
            sim=sims[:batch_size])
        return batch
        self._epochs_completed += 1
        self.datafile.seek(0)

    @property
    def epochs_completed(self):
        return self._epochs_completed



def load_dataset(data_dir, dataset, pad=0):

    dataset_root = os.path.join(data_dir, 'datasets', dataset)
    train_path = os.path.join(dataset_root, 'train', 'train.tsv')
    dev_path = os.path.join(dataset_root, 'dev', 'dev.tsv')
    test_path = os.path.join(dataset_root, 'test', 'test.tsv')
    vocab_path = os.path.join(dataset_root, 'vocab.txt')

    w2i, i2w = make_vocabulary(vocab_path)

    train = DataSet(train_path, (w2i, i2w), pad=pad)
    dev = DataSet(dev_path, (w2i, i2w), pad=pad)
    test = DataSet(test_path, (w2i, i2w), pad=pad)

    return base.Datasets(train=train, validation=dev, test=test)


import tensorflow as tf

from datasets import STS
from datasets import Sick
from templates import sts_cnn_blstm

FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()

if __name__ == '__main__':
    sts = STS()
    sick = Sick()
    sick.train.set_vocab((sts.w2i, sts.i2w))
    sick.test.set_vocab((sts.w2i, sts.i2w))
    sick.validation.set_vocab((sts.w2i, sts.i2w))

    if FLAGS.mode == 'train':
        sts_cnn_blstm.train(sick, sts.metadata_path, sts.w2v)
    elif FLAGS.mode == 'test':
        sts_cnn_blstm.test(sick, sts.metadata_path, sts.w2v, rescale=[1.0, 5.0])
    elif FLAGS.mode == 'results':
        sts_cnn_blstm.results(sick, sts.metadata_path, sts.w2v, rescale=[1.0,
                                                                         5.0])
# Original script developed by Harshal Priyadarshi https://github.com/harpribot and from Tensorflow: https://github.com/tensorflow/models/tree/master/tutorials/rnn/ptb
# Edited for purpose of this project.
# Import required libraries
from tensorflow.python.framework import ops
import tensorflow as tf
import numpy as np
import pandas as pd
from abc import abstractmethod, ABCMeta


class NeuralNet(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        
        # Sequence-to-sequence Neural Network

        
        # parameters
        self.train_batch_size = None
        self.test_batch_size = None
        self.memory_dim = None
        self.learning_rate = None
        self.saver = None
        self.sess = None
        self.test_size = self.test_size
        self.checkpointSys = self.checkpointSys
        self.mapper_dict = self.mapper_dict
        self.test_review = self.test_review
        self.true_summary = self.true_summary
        self.predicted_test_summary = self.predicted_test_summary

        # Load all the parameters
        self._load_model_params()

    def set_parameters(self, train_batch_size, test_batch_size, memory_dim, learning_rate):
        
        #Set the parameters for the model and training.

        #parameter train_batch_size: The batch size of examples used for batch training
        #parameter test_batch_size: The batch size of test examples used for testing
        #parameter memory_dim: The length of the hidden vector produced by the encoder
        #parameter learning_rate: The learning rate for Stochastic Gradient Descent
        

        self.train_batch_size = train_batch_size
        self.test_batch_size = test_batch_size
        self.memory_dim = memory_dim
        self.learning_rate = learning_rate

    @abstractmethod
    def _load_data(self):
        pass

    @abstractmethod
    def _split_train_tst(self):
        pass

    def _load_model_params(self):

        #Load model parameters

        #self.seq_length -> The length of the input sequence (Length of input sentence fed to the encoder-decoder model)
        #self.vocab_size -> The size of the data vocabulary
        #self.momentum -> The momentum parameter in the update rule for SGD

        #:return: None
        # parameters

        self.seq_length = self.mapper_dict['seq_length']
        self.vocab_size = self.mapper_dict['vocab_size']
        self.momentum = 0.9

    def begin_session(self):

        #Begins the session
       
        # start the tensorflow session
        # start the tensorflow session
        ops.reset_default_graph()
        # initialize interactive session
        self.sess = tf.Session()

    def form_model_graph(self):

        #Creates the data graph, loads the model and optimizer and then starts the session.
        #:return: None

        self._load_data_graph()
        self._load_model()
        self._load_optimizer()
        self._start_session()

    @abstractmethod
    def _load_data_graph(self):
        pass

    @abstractmethod
    def _load_model(self):
        pass

    @abstractmethod
    def _load_optimizer(self):
        pass

    def _start_session(self):
        
        print("Starting tensorflow session...")
        self.sess.run(tf.global_variables_initializer())
        # initialize the saver node
        # print tf.GraphKeys.GLOBAL_VARIABLES
        self.saver = tf.train.Saver(tf.global_variables())
        # get the latest checkpoint
        last_checkpoint_path = self.checkpointSys.get_last_checkpoint()
        if last_checkpoint_path is not None:
            print 'Previous saved tensorflow objects found... Extracting...'
            # restore the tensorflow variables
            self.saver.restore(self.sess, last_checkpoint_path)
            print 'Extraction Complete. Moving Forward....'

    @abstractmethod
    def fit(self):
        pass

    def _index2sentence(self, list_):
        
        # Converts the indexed sentence to the actual sentence, return string

       
        rev_map = self.mapper_dict['rev_map']  # rev_map is reverse mapping from index in vocabulary to actual word
        sentence = ""
        for entry in list_:
            if entry != 0:
                sentence += (rev_map[entry] + " ")

        return sentence

    def store_test_predictions(self, prediction_id='_final'):
        
        # Stores the test predictions in a CSV file
        
        # param prediction_id: A simple id appended to the name of the summary for uniqueness
        
        
        # prediction id is usually the step count
        print 'Storing predictions on Test Data...'
        document = []
        true_summary = []
        generated_summary = []
        for i in range(self.test_size):
            if not self.checkpointSys.is_output_file_present():
                document.append(self._index2sentence(self.test_review[i]))
                true_summary.append(self._index2sentence(self.true_summary[i]))
            if i < (self.test_batch_size * (self.test_size // self.test_batch_size)):
                generated_summary.append(self._index2sentence(self.predicted_test_summary[i]))
            else:
                generated_summary.append('')

        prediction_nm = 'generated_summary' + prediction_id
        if self.checkpointSys.is_output_file_present():
            df = pd.read_csv(self.checkpointSys.get_result_location(), header=0)
            df[prediction_nm] = np.array(generated_summary)
        else:
            df = pd.DataFrame()
            df['document'] = np.array(document)
            df['true_summary'] = np.array(true_summary)
            df[prediction_nm] = np.array(generated_summary)
        df.to_csv(self.checkpointSys.get_result_location(), index=False)
        print 'Stored the predictions. Moving Forward'
        if prediction_id == '_final':
            print 'All done. Exiting..'
            print 'Exited'

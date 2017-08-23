# Original script developed by Harshal Priyadarshi https://github.com/harpribot and from Tensorflow: https://github.com/tensorflow/models/tree/master/tutorials/rnn/ptb
# Edited for purpose of this project.
# Import required libraries
import tensorflow as tf
from Models.simple import Simple

# Initial class which initiate class in Tensorflow to get LSTM cell
class LstmSimple(Simple):
    # This function runs as first, with parameters: docSum_file, checkpointSys and attention.
    def __init__(self, docSum_file, checkpointSys, attention=False):
       
        super(LstmSimple, self).__init__(docSum_file, checkpointSys, attention)

    def get_cell(self):
        
        # Long short-term memory unit (LSTM) recurrent network cell.Long short-term memory unit (LSTM) recurrent network cell.
        # https://www.tensorflow.org/versions/r0.12/api_docs/python/rnn_cell/rnn_cells_for_use_with_tensorflow_s_core_rnn_methods#LSTMCell
 
        return tf.nn.rnn_cell.LSTMCell(self.memory_dim)

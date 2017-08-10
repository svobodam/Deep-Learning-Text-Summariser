import tensorflow as tf
from Models.simple import Simple


class LstmSimple(Simple):
    # This function runs as first, with parameters: docSum_file, checkpointSys and attention.
    def __init__(self, docSum_file, checkpointSys, attention=False):
       
        super(LstmSimple, self).__init__(docSum_file, checkpointSys, attention)

    def get_cell(self):
        
        #return: The atomic RNN Cell
 
        return tf.nn.rnn_cell.LSTMCell(self.memory_dim)

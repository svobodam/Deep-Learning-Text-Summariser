# Original script developed by Harshal Priyadarshi https://github.com/harpribot and from Tensorflow: # Original script developed by Harshal Priyadarshi https://github.com/harpribot
# Edited for purpose of this project.


#Script to initiate training process of the LSTM Bidirectional network with attention disabled.

# Import required libraries; Point system directory back to parent folder to allow import files below:
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from Models import lstmBidirectional
from PreProcessingScript import checkpoint


print("LSTM Bidirectional Network training process initiated with attention disabled...")


# Get the review summary file
try:
	docSum_file = 'Data/rewsum.csv'
	print("Source data loaded.")
except NameError:
	raise ValueError("No source data found. Please check if 'Data/rewsum.csv' exists!")

# Initialise Checkpointer to ensure checkpointing, No. of steps per checkpoint: 100
checkpointSys = checkpoint.checkpointSys('bidirectional', 'lstm', 'noAttention')
checkpointSys.steps_per_checkpoint(100)
checkpointSys.steps_per_prediction(100)


# Do using LSTM cell - with attention mechanism disabled
out_file = 'Results/Bidirectional-LSTM/NoAttention/no_attention.csv'
checkpointer.set_result_location(out_file)
lstm_net = lstm_bidirectional.LstmBidirectional(docSum_file, checkpointSys)
#Set the parameters for the model and training.
        #parameter train_batch_size: The batch size of examples used for batch training
        #parameter test_batch_size: The batch size of test examples used for testing
        #parameter memory_dim: The length of the hidden vector produced by the encoder
        #parameter learning_rate: The learning rate for Stochastic Gradient Descent
lstm_net.set_parameters(train_batch_size=128, test_batch_size=128, memory_dim=128, learning_rate=0.05)
lstm_net.begin_session()
lstm_net.form_model_graph()
lstm_net.fit()
lstm_net.predict()
lstm_net.store_test_predictions()



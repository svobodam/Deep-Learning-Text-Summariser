# Script to initiate training process of the GRU Cell Based network with attention disabled.


print("GRU Network training process initiated with attention disabled...")


# Import required libraries; Point system directory back to parent folder  to allow import files below:
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from Models import gruSimple
from PreProcessingScript import checkpoint

# Get the review summary file
try:
	docSum_file = 'Data/rewsum.csv'
	print("Source data loaded.")
except NameError:
	print("No source data found. Please check if 'Data/rewsum.csv' exists!")


# Initialize Checkpointer to ensure checkpointing
checkpointSys = checkpoint.checkpointSys('simple', 'gru', 'noAttention')
checkpointSys.steps_per_checkpoint(1000)
checkpointSys.steps_per_prediction(1000)


# Do using GRU cell - without attention mechanism
out_file = 'Results/gru/attention.csv'
checkpointSys.set_result_location(out_file)
gru_net = gruSimple.GruSimple(docSum_file, checkpointSys)
#Set the parameters for the model and training.
        #parameter train_batch_size: The batch size of examples used for batch training
        #parameter test_batch_size: The batch size of test examples used for testing
        #parameter memory_dim: The length of the hidden vector produced by the encoder
        #parameter learning_rate: The learning rate for Stochastic Gradient Descent
gru_net.set_parameters(train_batch_size=128, test_batch_size=128, memory_dim=128, learning_rate=0.05)
gru_net.begin_session()
gru_net.form_model_graph()
gru_net.fit()
gru_net.predict()
gru_net.store_test_predictions()

#!/bin/bash
# Startup script to run scripts in correct sequence

LSTMATTN=$HOME/deep-Learning-Text-Summariser/runScripts/trainLSTM-ATTN.py
LSTMNOATTN=$HOME/deep-Learning-Text-Summariser/runScripts/trainLSTM-noATTN.py
LSTMBIDATTN=$HOME/deep-Learning-Text-Summariser/runScripts/trainLSTM-Bidirectional-ATTN.py
LSTMBIDNOATTN=$HOME/deep-Learning-Text-Summariser/runScripts/trainLSTM-Bidirectional-noATTN.py

# Run Explorartion R Script
echo Starting Dataset Preprocessing...
echo Output from Dataset preprocessing...
#Rscript PreProcessingScript/source.r
echo Dataset preprocessing completed...
echo ...
echo Starting deep-learning process...
# Running deep-learning

echo Please select deep-learning model:
echo ...
echo [1] LSTM-Attention Enabled
echo [2] LSTM-Attention Disabled
echo [3] LSTM-Bidirectional-Attention Enabled
echo [4] LSTM-Bidirectional-Attention Disabled
echo Select your option:
read option

if [ $option ==  1 ]; then
	python $LSTMATTN
	exit 1
	elif [ $option == 2 ]; then
	python $LSTMNOATTN
	exit 1
	elif [ $option == 3 ]; then
	python $LSTMBIDATTN
	exit 1
	elif [ $option == 4 ]; then
	python $LSTMBIDNOATTN
	exit 1
else
	echo You have selected non-existing option...
	exit 1
	
fi



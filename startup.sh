#!/bin/bash
# Author: Matej Svoboda
# Startup script to run scripts in correct sequence

LSTM-ATTN = runScripts/trainLSTM-ATTN.py
LSTM-NO-ATTN = runScripts/trainLSTM-noATTN.py
GRU-ATTN = runScripts/trainGRU-ATTN.py
GRU-NO-ATTN = runScripts/trainGRU-noATTN.py

# Run Explorartion R Script
Rscript PreProcessingScript/source.r

# Running deep-learning

echo('Please select deep-learning model:')
echo('...')
echo('[1] LSTM-Attention Enabled')
echo('[2] LSTM-Attention Disabled')
echo('[3] GRU-Attention Enabled')
echo('[4] GRU-Attention Disabled')
echo('Select your option:')
read option

if [$option == 1]; then
	python $LSTM-ATTN
	exit 1
	elif [$option == 2]; then
	python $LSTM-NO-ATTN
	exit 1
	elif [$option == 3]; then
	python $GRU-ATTN
	exit 1
	elif [$option == 4]; then
	python $GRU-NO-ATTN
	exit 1
else
	echo('You have selected non-existing option...')
	exit 1
	
fi

